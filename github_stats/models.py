from django.db import models

# Create your models here.
class ProjectDescription(models.Model):
    project_name = models.CharField(unique=False, max_length=30)
    project_description = models.TextField()
    repo_url = models.TextField()


class DashboardPanel(models.Model):
    title = models.CharField(max_length=30)
    panel_type = models.CharField(max_length=127, choices=[
       ("piechart", "Pie-chart of languages used"),
       ("barchart", "Bar-chart of language sizes"),
])

