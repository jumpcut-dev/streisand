# Generated by Django 2.0.6 on 2018-07-08 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('torrents', '0001_initial'),
        ('torrent_stats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='torrentstats',
            name='torrent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='torrent_stats', to='torrents.TorrentFile', to_field='info_hash'),
        ),
    ]
