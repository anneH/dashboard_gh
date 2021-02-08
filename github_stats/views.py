import requests
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
import pygal
from github_stats.models import ProjectDescription
from github_stats.models import DashboardPanel

headers = { 
"Authorization": "Basic YW5uZS5oZXNlbWFubkBnbWFpbC5jb206SWFYWXZmZWVoNHJ2VXJVSUdhQWI0MUM3", 
"Accept": "application/json" 
} 

repos = requests.get('https://api.github.com/users/anneH/repos').json()

# creates a dictionary of languages and count of repos that use the language
def get_languages(repos):
    repo_languages = {}
    for repo in repos:
        language = repo['language']
        if language not in repo_languages:
            repo_languages[language] = 1
        else:
           repo_languages[language] +=1
    return repo_languages


def get_kc_repos(repos):
    kc_repo_list = []
    project_list = ProjectDescription.objects.all()
    for repo_item in repos:
        for project in project_list:
            if repo_item['name'] == project.project_name:
                kc_repo_list.append(repo_item)
    return kc_repo_list


# renders a bar graph of repository sizes
def github_sizes(request):
    line_chart = pygal.HorizontalBar()
    line_chart.title = 'Repository Sizes'
    for repo in repos:
        line_chart.add(repo['name'],repo['size'])
    chart_svg_as_datauri = line_chart.render_data_uri()
    context = {
        'rendered_chart_svg_as_datauri' : chart_svg_as_datauri,
    }
    return render(request, 'github_sizes.html', context)


# renders data to the repository list on the index page
def index(request):
    context = {
        'github_repos': repos,
    }
    return render(request, 'index.html', context)


# Renders a pie chart representing languages on the Languages page
def github_languages (request):
    repo_languages = get_languages(repos)
    pie_chart = pygal.Pie()
    pie_chart.title = 'Repository Languages'
    pie_chart.force_uri_protocol = 'http'
    for language, count in repo_languages.items():
       pie_chart.add(language, count)
    chart_svg_as_datauri = pie_chart.render_data_uri()
    context = {
        'github_repos': repos,
        'language_used' : language,
         'rendered_chart_svg_as_datauri' : chart_svg_as_datauri,
    }
    return render(request, 'github_languages.html', context)

# Description of each repo
def project_descriptions(request):
    project_list = ProjectDescription.objects.all()
    panels_list = DashboardPanel.objects.all()
    
    context = {
        'project_list': project_list,
        'panels_list' : panels_list
    }
    return render(request, 'repo_descriptions.html', context)


# def panel_details(request, panel_id, name):
#     panel = DashboardPanel.objects.filter(name=name)

def panel_details(request, panel_id):
    panel = DashboardPanel.objects.get(id=panel_id)
    kc_repos = get_kc_repos(repos)
    repo_languages = get_languages(kc_repos)
    print(repo_languages)
    # repo_languages = get_languages(repos)
    if panel.panel_type == 'piechart':
        chart = pygal.Pie()
        for language, count in repo_languages.items():
            chart.add(language, count)
    if panel.panel_type == 'barchart':
        chart = pygal.HorizontalBar()
        for repo in kc_repos:
            chart.add(repo['name'],repo['size'])
    chart.title = panel.title
    chart_svg_as_datauri = chart.render_data_uri()
    context = {
        'rendered_chart_svg_as_datauri' : chart_svg_as_datauri,
    }
    return render(request, "panel_details.html", context)



# TODO: Make aspects of the chart (such as Pie vs Bar, styling, etc)
# customizable based on the data in the panel model
# TODO: Get data from API, file, DB, or somewhere else, possibly based on
# the panel model
    # for repo_dict in repo_list:
    #     value = 42 # TODO: Replace this...
    #     label = repo_dict["name"]
    #     chart.add(label, value)
    # context = {
    # "panel": panel,
    # "rendered_chart_svg": chart.render(),
    # }
    # return render(request, "panel_details.html", context)