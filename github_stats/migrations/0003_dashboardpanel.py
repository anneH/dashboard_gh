# Generated by Django 3.1.4 on 2021-02-04 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('github_stats', '0002_projectdescription_repo_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='DashboardPanel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('panel_type', models.CharField(choices=[('piechart', 'Pie-chart of languages used'), ('barchart', 'Bar-chart of language sizes')], max_length=127)),
            ],
        ),
    ]