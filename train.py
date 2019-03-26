import os
import subprocess

# Train model on the server

command = "ssh -t boon@192.168.11.12 'python3 /home/boon/Desktop/2019-iot-ai-workshop/process.py'"
os.system(command)
result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
#returns result but must be read individualy via
#result.stdout.read()#returns output
#result.stderr.read()#returns error