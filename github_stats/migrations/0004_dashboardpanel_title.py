# Generated by Django 3.1.4 on 2021-02-05 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('github_stats', '0003_dashboardpanel'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboardpanel',
            name='title',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
