from operator import itemgetter

import requests

import plotly.express as px

# Make an API call about each sumbmission.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f'Status Code: {r.status_code}')


# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    r = requests.get(url)
    print(f'id: {submission_id}\tstatus: {r.status_code}')
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {'title': response_dict['title'],
                       'hn_link': f'https://news.ycombinator.com/item?id={submission_id}',
                       'comments': response_dict.get('descendants', 0),}
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts,
                          key=itemgetter('comments'),
                          reverse=True)

# Extract information.
submission_links, submission_comments = [], []
for submission_dict in submission_dicts:
    submission_name = submission_dict['title']
    submission_url = submission_dict['hn_link']
    submission_comment = submission_dict["comments"]
    submission_link = f'<a href="{submission_url}">{submission_name}</a>'
    submission_links.append(submission_link)
    submission_comments.append(submission_comment)

# Make visualization.
title = 'Most Commented Submissions on Hacker News\' Top Stories'
labels = {'x': 'Story', 'y': 'Comments'}
fig = px.bar(x=submission_links,
             y=submission_comments,
             title=title,
             labels=labels)

fig.update_layout(title_font_size=28,
                  xaxis_title_font_size=20,
                  yaxis_title_font_size=20)

fig.update_traces(marker_color='GoldenRod', marker_opacity=0.6)

fig.show()