import sys
import os

from config import JsonConfig
from concurrency import *

def test_invalid_js_config():
    config_file = "config_env/invalid_json.conf"
    test_js_config = JsonConfig(config_file)
    if test_js_config.read_from_config_file():
        return False

    if test_js_config.is_config_good():
        return False

    return True
