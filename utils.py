import json
import requests
import properties
from datetime import datetime


def get_json_header():
    """ Function to return JSON Accepted header
    :return: JSON Header along with token
    """
    return {'Authorization': 'token ' + properties.GITTOKEN,
               'Accept': 'application/vnd.github.luke-cage-preview+json'}


def retrieve_data(url: str) -> list:
    """
    Function to retrieve data (all pages) from URL
    """

    data = []
    page = True
    page_number = 1
    while page:
        response = requests.get(url=url.format(page_number=page_number), headers=get_json_header())

        result = json.loads(response.text)

        for item in result['items']:
            data.append(item)

        if len(result) == 100:
            page_number += 1
        else:
            page = False

    return data

def get_date(time: str) -> datetime:
    return datetime.strptime(time, '%Y-%m-%dT%H:%M:%SZ')

def get_num_days(d1: datetime, d2: datetime) -> str:
    return (d2 - d1).days
