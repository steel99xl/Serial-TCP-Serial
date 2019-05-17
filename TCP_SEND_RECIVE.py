import time
from serial import Serial
import socket
from threading import Thread

def Send():
    while True:
        SEND = SER.readline()
        client_connection.send(SEND)

def Receive():
    while True:
        RECV = client_connection.recv(BUFFER)
        if(RECV != ""):
            SER.write(RECV)
            time.sleep(1)
        else:
            pass

#Serial Connection
SER = Serial(
            port = '/dev/pts/23', #Replace with the serial port that you are using to read information
            baudrate = 9600, #Replace with baudrate that is used by the thing writing to serial
            timeout = 1,
            )

#Server Connection

PORT = 1447
IP = "127.0.0.1"
BUFFER = 1024

ADDR = (IP, PORT)

client_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_connection.connect(ADDR)

Receive_Thread = Thread(target = Receive)
Receive_Thread.start()

Send_Thread = Thread(target = Send)
Send_Thread.start()
