import os
import random

import requests.utils

__version__ = "2021.04.10"

UA_PLATFORM = os.getenv('UA_PLATFORM')

USER_AGENTS_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'useragents.txt')
with open(USER_AGENTS_FILE) as fh:
    USER_AGENTS = fh.read().splitlines()

ANDROID_USER_AGENTS_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'android_useragents.txt')
with open(ANDROID_USER_AGENTS_FILE) as fh:
    AND_USER_AGENTS = fh.read().splitlines()

requests.utils.default_user_agent = lambda: random.choice(USER_AGENTS)

if UA_PLATFORM == "android":
    requests.utils.default_user_agent = lambda: random.choice(AND_USER_AGENTS)
