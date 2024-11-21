import os
import time
import subprocess

# Open a file for reading and writing, create if it doesn't exist
fd = os.open("ex.txt", os.O_RDWR | os.O_CREAT)
os.write(fd, b"yeeehawww")
os.lseek(fd, 0, os.SEEK_SET)
os.close(fd)  # Corrected typo here

# Get the current process ID
current_pid = os.getpid()
print(current_pid)
# Launch a child process
process = subprocess.Popen(["python", "-c", "print('yo mama child process')"])
process.wait()
print(f"The process ID of the child process is: {process.pid}")

# Get and format the current time
curt = time.localtime()
forma = time.strftime("%H:%M:%S", curt)  # Fixed typo in variable name
print(forma)