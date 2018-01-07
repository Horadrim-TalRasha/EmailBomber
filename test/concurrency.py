from multiprocessing import Queue


global_test_case_info_queue = Queue()
global_test_result_queue = Queue()

def thread_pool_func(test_target_func, *arguments):
    current_test_case_info = global_test_case_info_queue.get()
    current_test_case_info["test_cases_count"] += 1
    if test_target_func(*arguments):
        current_test_case_info["success_cases_count"] += 1
    else:
        current_test_case_info["failed_cases_count"] += 1
    
    global_test_case_info_queue.put(current_test_case_info)
    global_test_result_queue.put(current_test_case_info)
