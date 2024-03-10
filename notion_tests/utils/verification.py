import re

import mailslurp_client
import time

from config import mail_config

configuration = mailslurp_client.Configuration()
configuration.api_key['x-api-key'] = mail_config.mail_api_key


def get_code_from_email():
    with mailslurp_client.ApiClient(configuration) as api_client:
        waitfor_controller = mailslurp_client.WaitForControllerApi(api_client)
        email = get_email_subject(waitfor_controller)
        pattern = re.compile(r"Your temporary Notion login code is ([A-Za-z0-9]+(-[A-Za-z0-9]+)+)")
        matches = pattern.match(email.subject)
        code = matches.group(1)

    return code


def get_email_subject(waitfor_controller):
    email = get_email(waitfor_controller)
    print(email.subject)
    if email.subject == 'A new device logged into your account':
        time.sleep(2)
        email = get_email(waitfor_controller)
        print(email.subject)
    return email


def get_email(waitfor_controller):
    email = waitfor_controller.wait_for_latest_email(
        inbox_id=mail_config.mail_inbox_id,
        timeout=mail_config.mail_wait_timeout,
        unread_only=True
    )
    return email
