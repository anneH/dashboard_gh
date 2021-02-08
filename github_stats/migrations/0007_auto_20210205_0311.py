# Generated by Django 3.1.4 on 2021-02-05 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('github_stats', '0006_auto_20210205_0304'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DashboardPanel',
        ),
        migrations.AddField(
            model_name='projectdescription',
            name='panel_type',
            field=models.CharField(choices=[('piechart', 'Pie-chart of languages used'), ('barchart', 'Bar-chart of language sizes')], default=1, max_length=127),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectdescription',
            name='title',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]