from config_test import *
from threading import Thread
from concurrency import *

test_threads = [
  Thread(target=thread_pool_func, args=(test_invalid_js_config,))
]
