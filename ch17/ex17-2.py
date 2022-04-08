from operator import itemgetter
from plotly.graph_objs import Bar
from plotly import offline

import requests
import json

url_s = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r_s = requests.get(url_s)
print(f"Status code: {r_s.status_code}")

submission_ids = r_s.json()

submission_dicts = []
for submission_id in submission_ids[:30]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f'https://news.ycombinator.com/item?id={submission_id}',
            'comments': response_dict['descendants'],
            'owner': response_dict['by'],
            'type': response_dict['type']
        }
    except KeyError:
        print(f"{submission_id} cannot find request word!")
        continue

    submission_dicts.append(submission_dict)
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

repo_links, stars, labels = [], [], []
for submission_dict in submission_dicts:
    repo_name = submission_dict['title']
    repo_url = submission_dict['hn_link']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"

    print(repo_url)
    repo_links.append(repo_link)
    stars.append(submission_dict['comments'])
    owner = submission_dict['owner']
    description = submission_dict['type']
    label = f"By: {owner}<br />Type: {description}"
    labels.append(label)

data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6
}]

my_layout = {
    'title': 'The most popular Python project on the GitHub',
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size', 20},
        'tickfont': {'size', 10}
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size', 24},
        'tickfont': {'size', 14}
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='17-2.html')
