import os
import sys

def reverse_line(line):
    return line[::-1]

def child_process(pipe_read, pipe_write):
    pipe_read.close()  
    line = pipe_write.recv()  
    inverted_line = reverse_line(line)  
    pipe_write.send(inverted_line)  
    pipe_write.close()  
    sys.exit(0)  

def main():
    if len(sys.argv) != 3 or sys.argv[1] != "-f":
        print("Uso: python3 inversor.py -f <archivo>")
        sys.exit(1)

    file_path = sys.argv[2]
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"No se pudo abrir el archivo: {file_path}")
        sys.exit(1)

    num_lines = len(lines)
    child_pids = []

    
    pipes = [os.pipe() for _ in range(num_lines)]

    
    for i in range(num_lines):
        child_pid = os.fork()
        if child_pid == 0:  
            pipe_read, pipe_write = pipes[i]
            child_process(pipe_read, pipe_write)
        else:
            child_pids.append(child_pid)

    
    for pipe_read, pipe_write in pipes:
        os.close(pipe_write)

    
    for i in range(num_lines):
        pipe_read, pipe_write = pipes[i]
        line = lines[i].strip()
        os.write(pipe_read, line.encode())
        os.close(pipe_read)

    
    for child_pid in child_pids:
        os.waitpid(child_pid, 0)
        pipe_read, pipe_write = pipes[child_pid - child_pids[0]]
        inverted_line = pipe_write.recv()
        print(inverted_line.decode())

if __name__ == "__main__":
    main()
