import requests

def get_dom(url):
    """
    Return all HTML
    """
    response = requests.get(url)
    return response.text