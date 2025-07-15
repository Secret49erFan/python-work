import requests
from dotenv import load_dotenv
import os

# Make an API call and check the response.
load_dotenv()
token = os.getenv('GITHUB_TOKEN')
url = 'https://api.github.com/search/repositories'
url += '?q=language:javascript+sort:stars+stars:>10000'
headers = {"Accept":"application/vnd.github.v3+json",
           "Authorization": f"Bearer {token}"}
r = requests.get(url, headers=headers)

def get_status_code(response):
    '''Returns the status of the response.'''
    return response.status_code
print(f'Status code: {get_status_code(r)}')

# Convert the reponse object to a dictionary.
response_dict = r.json()
def get_total_count(dict):
    '''Returns the total repos in search'''
    return dict["total_count"]
print(f'Total repositories: {get_total_count(response_dict)}')
print(f'Complete results: {not response_dict["incomplete_results"]}')

# Explore information about the repositories.
repo_dicts = response_dict['items']
def get_returned_repos(dicts):
    return len(dicts)
print(f'Repositories returned: {get_returned_repos(repo_dicts)}')

# Examine the first repository.
#repo_dict = repo_dicts[0]
#print(f'\nKeys: {len(repo_dict)}')
#for key in sorted(repo_dict.keys()):
#    print(key)
print('\nSelected information about each repository.')
for repo_dict in repo_dicts:
    print(f'Name: {repo_dict["name"]}')
    print(f'Owner: {repo_dict["owner"]["login"]}')
    print(f'Stars: {repo_dict["stargazers_count"]}')
    print(f'Repository: {repo_dict["html_url"]}')
    print(f'Created: {repo_dict["created_at"]}')
    print(f'Updated: {repo_dict["updated_at"]}')
    print(f'Description: {repo_dict["description"]}')