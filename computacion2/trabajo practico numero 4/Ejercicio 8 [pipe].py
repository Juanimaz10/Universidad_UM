include <stdio.h>
include <stdlib.h>
include <unistd.h>
include <signal.h>

int pipe_fd[2];

void handler_usr1(int signum) {
    // Proceso B
    printf("B (PID=%d) escribiendo: Mensaje 1 (PID=%d)\n", getpid(), getpid());
    write(pipe_fd[1], "Mensaje 1 (PID=BBBB)\n", 22);
    // Enviar señal USR1 al proceso C
    kill(getpid() + 2, SIGUSR1);
}

void handler_usr2(int signum) {
    // Proceso A
    printf("A (PID=%d) leyendo:\n", getpid());
    char buffer[256];
    ssize_t n;
    while ((n = read(pipe_fd[0], buffer, sizeof(buffer))) > 0) {
        write(STDOUT_FILENO, buffer, n);
    }
}

void handler_usr1_C(int signum) {
    // Proceso C
    printf("C (PID=%d) escribiendo: Mensaje 2 (PID=%d)\n", getpid(), getpid());
    write(pipe_fd[1], "Mensaje 2 (PID=CCCC)\n", 21);
    // Enviar señal USR2 al proceso A
    kill(getppid(), SIGUSR2);
    exit(0);
}

int main() {
    // Crear el pipe
    if (pipe(pipe_fd) == -1) {
        perror("Error al crear el pipe");
        exit(1);
    }

    // Crear el proceso B
    pid_t pid_B = fork();
    if (pid_B == -1) {
        perror("Error al crear el proceso B");
        exit(1);
    } else if (pid_B == 0) {
        // Proceso B
        signal(SIGUSR1, handler_usr1);
        pause();  // Esperar la señal USR1 del proceso A
    } else {
        // Proceso A
        pid_t pid_C = fork();
        if (pid_C == -1) {
            perror("Error al crear el proceso C");
            exit(1);
        } else if (pid_C == 0) {
            // Proceso C
            signal(SIGUSR1, handler_usr1_C);
            pause();  // Esperar la señal USR1 del proceso B
        } else {
            // Proceso A
            signal(SIGUSR2, handler_usr2);
            // Enviar señal USR1 al proceso B para iniciar la secuencia
            kill(pid_B, SIGUSR1);
            // Esperar señal USR2 del proceso C para leer desde el pipe
            pause();
        }
    }

    return 0;
}

