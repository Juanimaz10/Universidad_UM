import os

def child_process():
    child_pid = os.getpid()
    print("I am the child one, PID", child_pid)
    for _ in range(5):
        print("I am the child one, PID", child_pid)
    print("PID", child_pid, "terminando")

def parent_process(child_pid):
    parent_pid = os.getpid()
    print("I am the father one, PID", parent_pid, ", My child is", child_pid)
    for _ in range(2):
        print("I am the father one, PID", parent_pid, ", My child is", child_pid)
    os.wait()
    print("My child process  , PID", child_pid, ", finish")

def main():
    child_pid = os.fork()

    if child_pid == 0:
        child_process()
    else:
        parent_process(child_pid)

if __name__ == "__main__":
    main()
