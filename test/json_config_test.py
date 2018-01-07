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


def test_valid_js_config():
    config_file = "config_env/valid_json_1.conf"
    test_js_config = JsonConfig(config_file)
    if not test_js_config.read_from_config_file():
        return False

    if not test_js_config.is_config_good():
        return False

    return True


def test_valid_js_config_2():
    config_file = "config_env/valid_json_1.conf"
    test_js_config = JsonConfig(config_file)
    if not test_js_config.read_from_config_file():
        return False

    if not test_js_config.is_config_good():
        return False

    return True

def test_js_config_with_dir(dirname):
    test_js_config = JsonConfig(dirname)
    if test_js_config.read_from_config_file():
        return False

    if test_js_config.is_config_good():
        return False

    return True

def test_no_exist_config_file():
    test_js_config = JsonConfig("no_exist_file.conf")
    if test_js_config.read_from_config_file():
        return False

    if test_js_config.is_config_good():
        return False

    return True
