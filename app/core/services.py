
# API von Drittanbieter einbinden

import requests

class ServiceException(Exception):
    pass

def call_external_api(url: str, query: str) -> list:
    """
    call_external_api(url="https://friendlybytes.net/api/blog/category/", id=1)
    """

    if not query:
        raise ServiceException("Der Parameter query darf nicht leer sein")

    url = f"{url}?query={query}"
    try:
        response = requests.get(url)
        data = response.json()  # String in Python Objekt (List of dict) umwandeln
    except Exception as e:
        raise ServiceException(str(e))
    
    return data


if __name__ == "__main__":
    response = call_external_api(url="https://friendlybytes.net/api/blog/category/", query="hallo welt ö")
    print(response.text)
