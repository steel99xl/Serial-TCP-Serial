import time
from serial import Serial
import socket
from threading import Thread
global connection 
connection = ""

def Server():
    global connection
    Server_Connector.listen(1)
	
    while True:
        connection, Client_Address = Server_Connector.accept()



def Send():
    while True:
        SEND = SER.readline()
        if(SEND != bytes("", "utf8")):
            connection.sendall(SEND)
        else:
            pass


def Receive():
    while True:
        if(connection != ""):
            DATA = connection.recv(BUFFER)
            SER.write(DATA)
            time.sleep(1)
        else:
            pass

#Serial Configuration

SER = Serial(
            port = '/dev/pts/8', #Replace with the serial port that you are using to read information
            baudrate = 9600, #Replace with baudrate that is used by the thing writing to serial
            timeout = 1,
            )


#Server Configureation

PORT = 1447
IP = "127.0.0.1"
BUFFER = 1024
ADDR = (IP, PORT)

Server_Connector = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Server_Connector.bind(ADDR)

Server_Thread = Thread(target = Server)
Server_Thread.start()

Receive_Thread = Thread(target = Receive)
Receive_Thread.start()

Send_Thread = Thread(target = Send)
Send_Thread.start()
