import os

import pytest
from dotenv import load_dotenv

load_dotenv()

ui_url = os.getenv('RC1_ORION')
auth_user = os.getenv('RC1_ORION_BASIC_USER')
auth_pass = os.getenv('RC1_ORION_BASIC_PASS')

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "http_credentials": {
            "username": auth_user,
            "password": auth_pass
        },
        'base_url': ui_url,
    }


