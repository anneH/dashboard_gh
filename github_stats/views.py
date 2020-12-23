import requests
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
import pygal

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