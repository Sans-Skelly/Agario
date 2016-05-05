#########################################
# Programmer: Alex Karner
# Date: 05.05.2016
# File Name: server_socket.py
# Description: This program opens a network socket and broadcasts a list. It will
#              then recieve replys from the client and print them on screen.
#########################################
from socket import *
import threading
import Queue
import time

PORT = 3000                             # arbitrary non-privileged port
BUFFER_SIZE = 1024                      # maximum amount of data that can be received at once

socket = socket(AF_INET, SOCK_DGRAM)
socket.bind(('', PORT))                 # sets "PORT" as the port that will be used for communication
socket.setsockopt(SOL_SOCKET, SO_BROADCAST,1)

class Recieve (threading.Thread):
    def __init__(self,q,socket,buffer_size):
        threading.Thread.__init__(self)
        self.q = q
        self.addr = False
        self.buffer_size = buffer_size
        self.socket = socket
        
    def run (self):
        while True:
            self.m, self.ip = self.socket.recvfrom(self.buffer_size)    #Recieves ip and data from client
            self.q.put([self.ip, self.m])                               #Puts data into queue
                
class Send (threading.Thread):
    def __init__(self,q,socket):
        threading.Thread.__init__(self)
        self.q = q
        self.socket = socket
        
    def run (self):
        while True:
            self.socket.sendto(sent_data,('<broadcast>', PORT))         #Brodcasts the sent_data variable
            print 'SERVER: Sent Data: '+sent_data                       #Prints sent data.
            time.sleep(0.1)                                             #Broadcasts every 100ms.

sent_data = '1,2,3,4,5,6,7,8'

print 'SERVER: Setting up Queues...'
recieving_q = Queue.Queue(10)
sending_q = Queue.Queue(10)
print 'SERVER: Queues setup.'

print 'SERVER: Starting sending thread...'
sending = Send(sending_q,socket)
sending.start()
print 'SERVER: Started sending thread.'

print 'SERVER: Starting recieving thread...'
recieving = Recieve(recieving_q,socket,BUFFER_SIZE)
recieving.start()
print 'SERVER: Started recieving thread.'


while True:
    if recieving.q.empty() == False:    
        client_ip, message = recieving.q.get()
        if client_ip != ('192.168.1.38',3000):
            print 'SERVER: Recieved '+str(message)+' from '+str(client_ip)

conn.close()                            # always close the connection socket; otherwise the process will stay active
