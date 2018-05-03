# Generated by Django 2.0.4 on 2018-05-03 03:13

from django.db import migrations, models
import picklefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReseedRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('fulfilled_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Torrent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_id', models.PositiveIntegerField(db_index=True, null=True)),
                ('cut', models.CharField(default='Theatrical', max_length=128)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('is_approved', models.NullBooleanField(choices=[(None, 'Not Yet Moderated'), (True, 'Approved'), (False, 'Work In Progress')])),
                ('last_seeded', models.DateTimeField(null=True)),
                ('snatch_count', models.IntegerField(default=0)),
                ('release_name', models.CharField(max_length=1024)),
                ('release_group', models.CharField(max_length=32)),
                ('is_scene', models.NullBooleanField(default=False)),
                ('description', models.TextField()),
                ('nfo', models.TextField()),
                ('is_3d', models.BooleanField(default=False)),
                ('is_source', models.BooleanField(default=False)),
                ('file_list', picklefield.fields.PickledObjectField(editable=False)),
                ('size_in_bytes', models.BigIntegerField()),
            ],
            options={
                'permissions': (('can_upload', 'Can upload new torrents'), ('can_moderate', 'Can moderate torrents'), ('can_request_reseed', 'Can request a reseed')),
            },
        ),
        migrations.CreateModel(
            name='TorrentComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TorrentMetaInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dictionary', picklefield.fields.PickledObjectField(editable=False)),
            ],
        ),
    ]
