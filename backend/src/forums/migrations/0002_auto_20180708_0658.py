# Generated by Django 2.0.6 on 2018-07-08 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
        ('forums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumtopic',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='topic_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='forumtopic',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='topics', to='forums.ForumGroup'),
        ),
        migrations.AddField(
            model_name='forumtopic',
            name='latest_post',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='topic_latest', to='forums.ForumPost'),
        ),
        migrations.AddField(
            model_name='forumtopic',
            name='minimum_user_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='unlocked_forum_topics', to='users.UserClass'),
        ),
        migrations.AddField(
            model_name='forumthreadsubscription',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='forums.ForumThread'),
        ),
        migrations.AddField(
            model_name='forumthreadsubscription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forum_thread_subscriptions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='forumthread',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='forum_threads_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='forumthread',
            name='latest_post',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='thread_latest', to='forums.ForumPost'),
        ),
        migrations.AddField(
            model_name='forumthread',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_threads', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='forumthread',
            name='subscribed_users',
            field=models.ManyToManyField(related_name='forum_threads_subscribed', through='forums.ForumThreadSubscription', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='forumthread',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='threads', to='forums.ForumTopic'),
        ),
        migrations.AddField(
            model_name='forumreport',
            name='post',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='forums.ForumPost'),
        ),
        migrations.AddField(
            model_name='forumreport',
            name='reporting_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='reports', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='forumreport',
            name='resolved_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='report_resolved', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='forumreport',
            name='thread',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='forums.ForumThread'),
        ),
        migrations.AddField(
            model_name='forumpost',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='forum_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='forumpost',
            name='modified_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='forumpost',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='forums.ForumThread'),
        ),
        migrations.AddField(
            model_name='forumgroup',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='forums.ForumGroup'),
        ),
    ]
