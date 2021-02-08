# Generated by Django 3.1.4 on 2021-02-05 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('github_stats', '0004_dashboardpanel_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboardpanel',
            name='project_description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dashboardpanel',
            name='project_name',
            field=models.CharField(default=1, max_length=30, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dashboardpanel',
            name='repo_url',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
