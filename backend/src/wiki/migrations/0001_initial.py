# Generated by Django 2.0.6 on 2018-07-08 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WikiArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_id', models.PositiveIntegerField(db_index=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256)),
                ('body', models.TextField()),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_wiki_pages', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_wiki_pages', to=settings.AUTH_USER_MODEL)),
                ('read_access_minimum_user_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wiki_articles_with_read_access', to='users.UserClass')),
                ('write_access_minimum_user_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wiki_articles_with_write_access', to='users.UserClass')),
            ],
            options={
                'ordering': ['-created_at'],
                'get_latest_by': 'created_at',
            },
        ),
    ]
