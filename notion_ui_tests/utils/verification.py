import re
import time

import mailslurp_client

from project import mail_config

configuration = mailslurp_client.Configuration()
configuration.api_key['x-api-key'] = mail_config.mail_slurp_api_key


def get_code_from_email():
    with mailslurp_client.ApiClient(configuration) as api_client:
        wait_for_controller = mailslurp_client.WaitForControllerApi(api_client)
        email = get_email_subject(wait_for_controller)
        pattern = re.compile(
            r"Your temporary Notion login code is ([A-Za-z0-9]+(-[A-Za-z0-9]+)+)"
        )
        matches = pattern.match(email.subject)
        code = matches.group(1)

    return code


def get_email_subject(wait_for_controller):
    email = get_email(wait_for_controller)
    if email.subject == 'A new device logged into your account':
        time.sleep(5)
        email = get_email(wait_for_controller)
    return email


def get_email(wait_for_controller):
    email = wait_for_controller.wait_for_latest_email(
        inbox_id=mail_config.mail_slurp_inbox_id,
        timeout=mail_config.mail_wait_timeout,
        unread_only=True,
    )
    return email
