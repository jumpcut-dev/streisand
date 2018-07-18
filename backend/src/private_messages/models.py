from django.contrib.postgres.indexes import GinIndex
from django.core.validators import ValidationError
from django.db import models
from django.utils.timezone import now
from mptt.models import MPTTModel, TreeForeignKey

from users.models import User

from .managers import MessageManager


class Message(MPTTModel):
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='children',
        db_index=True
    )
    subject = models.CharField(max_length=200)
    body = models.TextField()
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.SET_NULL, null=True)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.SET_NULL, null=True)
    sent_at = models.DateTimeField(blank=True, null=True)
    replied_at = models.DateTimeField(auto_now_add=True)
    deleted_inbox = models.BooleanField(default=False)
    deleted_outbox = models.BooleanField(default=False)
    recipient_deleted_at = models.DateTimeField(null=True)
    sender_deleted_at = models.DateTimeField(null=True)

    objects = MessageManager()

    def replied(self):
        """returns whether the recipient has written a reply to this message"""
        if self.replied_at is not None:
            return True
        return False

    def __str__(self):
        return self.subject

    def save(self, **kwargs):
        if self.sender == self.recipient:
            raise ValidationError("You can't send messages to yourself")

        if not self.id:
            self.sent_at = now()
        if self.deleted_outbox is True:
            self.sender_deleted_at = now()
        if self.deleted_inbox is True:
            self.recipient_deleted_at = now()
        super(Message, self).save(**kwargs)

    class Meta:
        ordering = ['-sent_at']
        indexes = [GinIndex(fields=['id', 'parent'])]


def inbox_count(user):
    """
    Returns the number of unread messages for the given user but does not
    mark them as read
    """
    return Message.objects.filter(recipient=user, recipient_deleted_at__isnull=True).count()


def outbox_count(user):
    """
    Returns the number of unread sent messages for the given user but does not
    mark them as read
    """
    return Message.objects.filter(sender=user, sender_deleted_at__isnull=True).count()


def inbox(request):
    if request.user.is_authenticated:
        return {'messages_inbox_count': inbox_count(request.user)}
    else:
        return {}


def outbox(request):
    if request.user.is_authenticated:
        return {'messages_outbox_count': outbox_count(request.user)}
    else:
        return {}