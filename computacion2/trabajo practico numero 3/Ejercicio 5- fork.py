import os
import sys

def child_process(child_pid, parent_pid):
    print("Soy el proceso", child_pid, ", The father one is", parent_pid)

def main(num_processes):
    parent_pid = os.getpid()

    for i in range(num_processes):
        child_pid = os.fork()
        if child_pid == 0:
            child_process(os.getpid(), parent_pid)
            sys.exit(0)

    for _ in range(num_processes):
        os.wait()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py -n <num_processes>")
        sys.exit(1)

    if sys.argv[1] != "-n":
        print("Usage: python script.py -n <num_processes>")
        sys.exit(1)

    num_processes = int(sys.argv[2])
    main(num_processes)
