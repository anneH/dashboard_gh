"""dashboard_gh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from github_stats import views
from github_stats.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('details/<panel_id>/', views.panel_details),
    # path('details/<panel_id>/<search_term>', views.???),
    path('github-languages/', views.github_languages, name='languages'),
    path('github-sizes/', views.github_sizes, name='sizes'),
    path('', index),
    path('project-descriptions/', views.project_descriptions, name='descriptions'),
]
