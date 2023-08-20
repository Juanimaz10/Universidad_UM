import multiprocessing
import os

def proceso_lectura(pipe):
    while True:
        linea = input("Write a line of the text (or 'exit' to finish): ")
        if linea == 'exit':
            break
        pipe.send(linea)

def proceso_mostrar(pipe):
    pid = os.getpid()
    while True:
        message = pipe.recv()
        print(f"Reading (pid: {pid}): {message}")

if __name__ == '__main__':
    father_pipe, son_pipe = multiprocessing.Pipe()

    
    process1 = multiprocessing.Process(target=proceso_lectura, args=(son_pipe,))
    process2 = multiprocessing.Process(target=proceso_mostrar, args=(father_pipe,))

   
    process1.start()
    process2.start()

    
    process1.join()
    process2.join()

    print("finished program")
