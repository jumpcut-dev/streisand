# Generated by Django 2.0.6 on 2018-07-16 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0002_auto_20180708_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumpost',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='forumpost',
            name='modified_at',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='forumthread',
            name='created_at',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='forumthread',
            name='modified_at',
            field=models.DateTimeField(null=True),
        ),
    ]
