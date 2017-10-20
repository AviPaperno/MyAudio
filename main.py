import subprocess
import socket
from _thread import *

ADDRESS = ''

def play(name):
    print('File name: {}.mp3'.format(ADDRESS+name))
    try:
        player = subprocess.Popen(["omxplayer", ADDRESS+name+".mp3"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except:
        pass

HOST = ''
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

MP3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()


s.listen(10)
print ('Socket now listening')

def clientthread(conn):
    # Sending message to connected client
    conn.sendall(b'Welcome to the server. Type something and hit enter\n')  # send only takes string

    # infinite loop so that function do not terminate and thread do not end.
    while True:

        # Receiving from client
        try:
            data = conn.recv(1024)
            MyData = (data.decode("utf-8").strip())        
            if MyData in MP3:
                play(MyData)
            conn.sendall(data)
        except:
            pass
    conn.close()

while 1:
    # wait to accept a connection - blocking call
    conn, addr = s.accept()
    print ('Connected with ' + addr[0] + ':' + str(addr[1]))
    # start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread, (conn,))

s.close()
