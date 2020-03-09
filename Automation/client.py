#This is a our client's code
#Import the required module
import socket

#Main function, connects to localhost:5000, get a message from user
def Main():
    host = "127.0.0.1"
    port = 5000
        
    mySocket = socket.socket()
    mySocket.connect((host, port))
        
    message = input(">")
        
    while message != 'q':
        mySocket.send(message.encode())
        data = mySocket.recv(1024).decode()
        print ('Server: '+ data)
        message = input(">")

    mySocket.close()

if __name__ == '__main__':
    Main()
#---------------------------------------------------------------------