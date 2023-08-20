import argparse
import subprocess
import datetime

def execute_command(command, output_file, log_file):
    
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    try:
        
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        
        with open(output_file, 'a') as f_out:
            f_out.write(stdout.decode('utf-8'))


        with open(log_file, 'a') as f_log:
            if process.returncode == 0:
                f_log.write(f"{formatted_time}: Comand \"{command}\" It was excuted correcty.\n")
            else:
                f_log.write(f"{formatted_time}: {stderr.decode('utf-8')}\n")
    except Exception as e:
        with open(log_file, 'a') as f_log:
            f_log.write(f"{formatted_time}: Error: {str(e)}\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Command executor with check-out or check-in ')
    parser.add_argument('-c', dest='command', required=True, help='The comand to execute.')
    parser.add_argument('-f', dest='output_file', required=True, help='output file for the command output.')
    parser.add_argument('-l', dest='log_file', required=True, help='log file for success messages or error messages.')

    args = parser.parse_args()

    execute_command(args.command, args.output_file, args.log_file)
