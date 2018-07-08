# Generated by Django 2.0.6 on 2018-07-08 06:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Peer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ip_address', models.GenericIPAddressField(protocol='IPv4')),
                ('port', models.IntegerField()),
                ('peer_id', models.CharField(max_length=60)),
                ('user_agent', models.TextField()),
                ('compact_representation', models.CharField(help_text='base64 encoded compact representation, sent as bytes to announcing torrent clients', max_length=10)),
                ('bytes_uploaded', models.BigIntegerField(default=0)),
                ('bytes_downloaded', models.BigIntegerField(default=0)),
                ('bytes_remaining', models.BigIntegerField()),
                ('complete', models.BooleanField(default=False)),
                ('first_announce', models.DateTimeField(auto_now_add=True)),
                ('last_announce', models.DateTimeField(auto_now=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='TorrentClient',
            fields=[
                ('peer_id_prefix', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('is_whitelisted', models.NullBooleanField(db_index=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
