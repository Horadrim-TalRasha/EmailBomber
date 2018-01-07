from json_config_test import *
from threading import Thread
from concurrency import *

test_threads = [
  Thread(target=thread_pool_func, args=(test_invalid_js_config,)),
  Thread(target=thread_pool_func, args=(test_valid_js_config,)),
  Thread(target=thread_pool_func, args=(test_valid_js_config_2,)),
  Thread(target=thread_pool_func, args=(test_js_config_with_dir, "./config_env")),
  Thread(target=thread_pool_func, args=(test_no_exist_config_file,))
]
