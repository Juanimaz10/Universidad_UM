import os
import sys
import argparse

def calculate_sum(start, end):
    return sum(range(start, end, 2))

def child_process(pid, ppid, verbose):
    if verbose:
        print(f"Starting process {pid}")
    result = calculate_sum(0, pid)
    if verbose:
        print(f"Ending process {pid}")
    return f"{pid} - {ppid}: {result}"

def main():
    parser = argparse.ArgumentParser(description="Calculates the sum of even integers from 0 to PID for each child process.")
    parser.add_argument("-n", type=int, required=True, help="Number of child processes to create")
    parser.add_argument("-v", action="store_true", help="Enable verbose mode")
    args = parser.parse_args()

    processes = []
    for i in range(args.n):
        pid = os.fork()
        if pid == 0:
            result = child_process(os.getpid(), os.getppid(), args.v)
            print(result)
            sys.exit(0)
        else:
            processes.append(pid)

 
    for pid in processes:
        os.waitpid(pid, 0)

if __name__ == "__main__":
    main()
