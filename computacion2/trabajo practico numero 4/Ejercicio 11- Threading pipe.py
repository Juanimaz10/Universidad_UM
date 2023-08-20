import threading
import time

def child_thread(thread_number):
    thread_id = threading.get_ident()
    print(f"Hilo {thread_number}, ID de hilo: {thread_id}")
    time.sleep(thread_number)  

if __name__ == "__main__":
    num_threads = 10

    threads = []
    for i in range(1, num_threads + 1):
        thread = threading.Thread(target=child_thread, args=(i,))
        threads.append(thread)
        thread.start()

    
    for thread in threads:
        thread.join()

    print("All the threads are done.")
