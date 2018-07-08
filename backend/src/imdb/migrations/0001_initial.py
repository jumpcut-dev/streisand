# Generated by Django 2.0.6 on 2018-07-08 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FilmIMDb',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1024)),
                ('year', models.PositiveSmallIntegerField(null=True)),
                ('description', models.TextField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3, null=True)),
                ('rating_vote_count', models.PositiveIntegerField(null=True)),
                ('runtime_in_minutes', models.PositiveSmallIntegerField(null=True)),
                ('last_updated', models.DateTimeField(null=True)),
            ],
        ),
    ]
