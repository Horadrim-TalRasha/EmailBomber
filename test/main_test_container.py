import sys

from multiprocessing import Queue

sys.path.append("..")

from concurrency import *
from test_cases import *

g_test_case_init_info = {
  "test_cases_count" : 0,
  "success_cases_count" : 0,
  "failed_cases_count" : 0 
}

def wait_test_cases():
    test_result = global_test_result_queue.get()
    success_cases_count = test_result["success_cases_count"]
    failed_cases_count = test_result["failed_cases_count"]
    test_cases_count = len(test_threads)
    while success_cases_count + failed_cases_count != test_cases_count:
        print "Current test process:"
        print "  All test cases: %s" % test_cases_count
        print "  Success test cases: %s" % success_cases_count
        print "  Failed test cases: %s" % failed_cases_count
        print ""


    print "Test(s) finished: %s" % test_cases_count
    print "  Success test cases: %s" % success_cases_count
    print "  Failed test cases: %s" % failed_cases_count
    print ""

def init_thread_pool(thread_num):
    if thread_num <= 0:
        raise Exception("thread pool number set error.")

    for i in range(0, thread_num):
        test_thread = test_threads[i]
        test_thread.start()

if __name__ == "__main__":
    global_test_case_info_queue.put(g_test_case_init_info)
    init_thread_pool(len(test_threads))
    wait_test_cases()
