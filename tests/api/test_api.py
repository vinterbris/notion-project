import json
import os
import requests
from pprint import pprint

from notion_client import Client

from config import web_config
from datetime import datetime, timezone
notion = Client(auth=web_config.notion_api_key)

# TODO CREATE 5 TESTS

NOTION_TOKEN = web_config.notion_api_key
DATABASE_ID = web_config.notion_database_id

headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

def get_pages(num_pages=None):
    """
    If num_pages is None, get all pages, otherwise just the defined number.
    """
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    get_all = num_pages is None
    page_size = 100 if get_all else num_pages

    payload = {"page_size": page_size}
    response = requests.post(url, json=payload, headers=headers)

    data = response.json()

    # Comment this out to dump all data to a file
    # import json
    # with open('db.json', 'w', encoding='utf8') as f:
    #    json.dump(data, f, ensure_ascii=False, indent=4)

    results = data["results"]
    while data["has_more"] and get_all:
        payload = {"page_size": page_size, "start_cursor": data["next_cursor"]}
        url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        results.extend(data["results"])

    return results

pages = get_pages()

def test_naked_api():
    title = "Test Title"
    description = "Test Description"
    published_date = datetime.now().astimezone(timezone.utc).isoformat()
    data = {
        "URL": {"rich_text": [{"text": {"content": description}}]},
        "Title": {"rich_text": [{"text": {"content": title}}]},
        "Published": {"date": {"start": published_date, "end": None}}
    }

    create_page(data)

def test_api():

    # get pages
    # pprint(pages[0])

    # for page in pages:
    #     pprint(page)
        # page_id = page["id"]
        # props = page["properties"]
        # published = props["Published"]["date"]["start"]
        # published = datetime.fromisoformat(published)
        # print(page_id, props, published)

    # update page

    page_id = pages[0]['id']

    new_date = datetime(2022, 1, 15).astimezone(timezone.utc).isoformat()
    update_data = {"Published": {"date": {"start": new_date, "end": None}}}

    update_page(page_id, update_data)

    # delete page
    delete_page(page_id)

def delete_page(page_id: str):
    url = f"https://api.notion.com/v1/pages/{page_id}"

    payload = {"archived": True}

    res = requests.patch(url, json=payload, headers=headers)
    return res

def update_page(page_id: str, data: dict):
    url = f"https://api.notion.com/v1/pages/{page_id}"

    payload = {"properties": data}

    res = requests.patch(url, json=payload, headers=headers)
    return res

def create_page(data: dict):
    create_url = "https://api.notion.com/v1/pages"

    payload = {"parent": {"database_id": DATABASE_ID}, "properties": data}

    res = requests.post(create_url, headers=headers, json=payload)
    pprint(res.json())
    pprint(res.status_code)
    return res


def createPage(databaseID, headers):
    createUrl = 'https://api.notion.com/v1/pages'
    newPageData = {
        "parent": { "database_id": databaseID },
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": "DONA"
                        }
                    }
                ]
            },
            "Text": {
                    "rich_text": [
                        {
                            "text": {
                                "content": "This is thienqc"
                            },
                        }
                    ]
                },
            "Checkbox": {
                    "checkbox": True
                },
            "Number": {
                    "number": 1999
            },
            "Select": {
                    "select": {
                        "name": "Mouse",
                    }
                },
            "Multi-select": {
                    "multi_select": [
                        {
                            "name": "Apple",
                        },
                        {
                            "name": "Banana",
                        }
                    ]
                },
            "Date": {
                    "date": {
                        "start": "2022-08-05",
                        "end": "2022-08-10",
                    }
                },
            "URL": {
                    "url": "google.com"
                },
            "Email": {
                    "email": "dolor@ipsum.com"
                },
            "Phone": {
                    "phone_number": "19191919"
                },
            "Person": {
                    "people": [
                        {
                            "id": "4af42d2d-a077-4808-b4f7-e960a93fd945",
                        }
                    ]
                },
            "Relation": {
                    "relation": [
                        {
                            "id": "fbb0a7f2-413e-4728-adbf-281ab14f0c33"
                        }
                    ]
                }
            }
        }
    data = json.dumps(newPageData)
    res = requests.request("POST", createUrl, headers=headers, data=data)
    print(res.status_code)

def test_sdk():
    list_users_response = notion.users.list()
    notion.pages.create()
    pprint(list_users_response)

    response = requests.get('https://cotton-sheet-6c9.notion.site/a8ba44cda9104725ae1dd4325f82de85?pvs=4')
    pprint(response)




