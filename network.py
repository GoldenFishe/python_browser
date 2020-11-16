import requests


def get_html(url):
    response = None
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError as error:
        print(error)
    return response
