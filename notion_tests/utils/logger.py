import logging

import allure
import curlify
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType

from config import config


def get_notion(url, **kwargs):
    with step(f'POST {url}'):
        response = requests.get(config.notion_api_url + url, **kwargs)
        curl = curlify.to_curl(response.request)
        logging.info(curl)
        allure.attach(body=curl, name='curl', attachment_type=AttachmentType.TEXT, extension='txt')
    return response


def post_notion(url, **kwargs):
    with step(f'POST {url}'):
        response = requests.post(config.notion_api_url + url, **kwargs)
        curl = curlify.to_curl(response.request)
        logging.info(curl)
        allure.attach(body=curl, name='curl', attachment_type=AttachmentType.TEXT, extension='txt')
    return response
