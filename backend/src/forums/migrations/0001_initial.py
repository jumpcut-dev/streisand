# Generated by Django 2.0.6 on 2018-07-08 06:58

from django.db import migrations, models
import django_positions_2.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ForumGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_id', models.PositiveIntegerField(db_index=True, null=True)),
                ('sort_order', models.PositiveSmallIntegerField()),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='ForumPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_id', models.PositiveIntegerField(db_index=True, null=True)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified', models.BooleanField(default=False)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('modified_count', models.PositiveIntegerField(default=0, editable=False)),
                ('position', positions.fields.PositionField(default=-1, editable=False)),
            ],
            options={
                'ordering': ['created_at'],
                'get_latest_by': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='ForumReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reported_at', models.DateTimeField(auto_now_add=True)),
                ('reason', models.TextField(max_length=1024)),
                ('resolved', models.BooleanField(default=False)),
                ('date_resolved', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-reported_at',),
            },
        ),
        migrations.CreateModel(
            name='ForumThread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_id', models.PositiveIntegerField(db_index=True, null=True)),
                ('title', models.CharField(max_length=1024)),
                ('is_locked', models.BooleanField(default=False)),
                ('is_sticky', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified', models.BooleanField(default=False)),
                ('is_archived', models.BooleanField(default=False)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('modified_count', models.PositiveIntegerField(default=0, editable=False)),
                ('number_of_posts', models.PositiveIntegerField(default=0, editable=False)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ForumThreadSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ForumTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_id', models.PositiveIntegerField(db_index=True, null=True)),
                ('sort_order', models.PositiveSmallIntegerField()),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=1024)),
                ('staff_only_thread_creation', models.BooleanField(default=False)),
                ('number_of_threads', models.PositiveIntegerField(default=0)),
                ('number_of_posts', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['sort_order'],
            },
        ),
    ]
