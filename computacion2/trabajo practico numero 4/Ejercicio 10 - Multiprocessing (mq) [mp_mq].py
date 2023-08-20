import multiprocessing
import time

def child_process(process_number, queue):
    pid = multiprocessing.current_process().pid
    print(f"Proceso {process_number}, PID: {pid}")
    time.sleep(process_number)  
    queue.put(pid)

if __name__ == "__main__":
    num_processes = 10
    queue = multiprocessing.Queue()

  
    processes = []
    for i in range(1, num_processes + 1):
        process = multiprocessing.Process(target=child_process, args=(i, queue))
        processes.append(process)
        process.start()

    
    for process in processes:
        process.join()

   
    print("Contenido de la cola de mensajes:")
    while not queue.empty():
        pid = queue.get()
        print(f"{pid}\t")
