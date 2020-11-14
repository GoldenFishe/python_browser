import requests


def get_url(url):
    response = requests.get(url)
    return response.text
