
# 5 тестов
# Приведены тесты на HTTP-методы: GET, POST, DELETE.
# Указан базовый URI - browser.config.base_url в фикстуре в файле conftest.py.
# Все запросы выполняются через endpoint, без указания базового URI.
#   browser.open('/users')
# Созданы схемы для валидации API запросов как для request, так и для response.
# Подключено красивое логирование от Allure (allure.attach  как для  request, так и для response)
# Подключено логирование в консоль (уровень логирования, дата, время, код ответа, client url)
# В тестах присутствуют следующие проверки:
#   Status code
#   Значение response
#   Схема ответа

import requests

from config import web_config


NOTION_TOKEN = web_config.notion_api_key
DATABASE_ID = web_config.notion_database_id

headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
    # Check what is the latest version here: https://developers.notion.com/reference/changes-by-version
}

def test_get_pages():
    url = f"{web_config.notion_api_url}/v1/databases/{DATABASE_ID}/query"

def get_pages(num_pages=None):
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    get_all = num_pages is None
    page_size = 100 if get_all else num_pages
    payload = {"page_size": page_size}
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    results = data["results"]
    while data["has_more"] and get_all:
        payload = {"page_size": page_size, "start_cursor": data["next_cursor"]}
        url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        results.extend(data["results"])
    return results


def test_get_properties():
    pages = get_pages()
    for page in pages:
        page_id = page["id"]
        props = page["properties"]
        print(props)


# ___________________________

def create_page(data: dict):
    create_url = "https://api.notion.com/v1/pages"
    payload = {"parent": {"database_id": DATABASE_ID}, "properties": data}
    res = requests.post(create_url, headers=headers, json=payload)
    if res.status_code == 200:
        print(f"{res.status_code}: Page created successfully")
    else:
        print(f"{res.status_code}: Error during page creation")
    return res

def edit_page(page_block_id, data: dict):
    edit_url = f"https://api.notion.com/v1/blocks/{page_block_id}/children"
    payload = data
    res = requests.patch(edit_url, headers=headers, json=payload)
    if res.status_code == 200:
        print(f"{res.status_code}: Page edited successfully")
    else:
        print(f"{res.status_code}: Error during page editing")
    return res


def test_create_page():
    task_name = 'This is task name'
    due_date = '2024-12-01'
    summary = 'This is summary'
    properties = {
        'Task name': {
            'id': 'title',
            'type': 'title',
            'title': [{
                'type': 'text',
                'text': {
                    'content': task_name,
                    'link': None
                },
                'annotations': {
                    'bold': False,
                    'italic': False,
                    'strikethrough': False,
                    'underline': False,
                    'code': False,
                },
                'plain_text': task_name,
                'href': None
            }]
        },
        'Assignee': {
            'id': 'notion%3A%2F%2Ftasks%2Fassign_property',
            'type': 'people',
            'people': [{
                'object': 'user',
                'id': '5498b8ee-30c3-4a8a-940a-9948a7615dfd',
                'name': 'Sergey',
                'avatar_url': None,
                'type': 'person',
                'person': {
                    'email': '3tijplrlrs8k@mailslurp.net'
                }
            }]
        },
        'Status': {
            'id': 'notion%3A%2F%2Ftasks%2Fstatus_property',
            'type': 'status',
            'status': {
                'id': 'in-progress',
                'name': 'In progress',
            }
        },
        'Due': {
            'id': 'notion%3A%2F%2Ftasks%2Fdue_date_property',
            'type': 'date',
            'date': {
                'start': due_date,
                'end': None,
                'time_zone': None
            }
        },
        'Summary': {
            'id': 'notion%3A%2F%2Ftasks%2Fai_summary_property',
            'type': 'rich_text',
            'rich_text': [{
                'type': 'text',
                'text': {
                    'content': summary,
                    'link': None
                },
                'annotations': {
                    'bold': False,
                    'italic': False,
                    'strikethrough': False,
                    'underline': False,
                    'code': False,
                    'color': 'default'
                },
                'plain_text': summary,
                'href': None
            }]
        }
    }
    response = create_page(properties)
    page_block_id = response.json()["id"]
    print(page_block_id)


