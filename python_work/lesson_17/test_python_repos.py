# Practice 7/13/2025.
# Chapter 17 - Testing python_repos.py
# test_python_repos.py
import requests
from dotenv import load_dotenv
import os
import pytest
from python_repos import get_status_code, get_total_count, get_returned_repos

load_dotenv()
token = os.getenv('GITHUB_TOKEN')
headers = {"Accept":"application/vnd.github.v3+json",
           "Authorization": f"Bearer {token}"}
url = 'https://api.github.com/search/repositories'
url += '?q=language:javascript+sort:stars+stars:>10000'

@pytest.fixture(scope='module')
def response_test():
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r

def test_status_code(response_test):
    status_code = get_status_code(response_test)
    assert status_code == 200

def test_total_repos(response_test):
    response_dict = response_test.json()
    total_count = get_total_count(response_dict)
    assert total_count > 0

def test_returned_repos(response_test):
    response_dict = response_test.json()
    repo_dicts = response_dict['items']
    returned_repos = get_returned_repos(repo_dicts)
    assert returned_repos == 30