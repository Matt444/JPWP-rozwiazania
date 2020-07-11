import _pickle as pickle
from _thread import *
from socket import *

'''
W tym pliku należy uzupełnić wątek threaded_client
Należy również zmodyfikować adres IP w zmiennej 'HOST' na swój z sieci lokalnej
'''

HOST = "127.0.0.1"
PORT = 8999

connections = 0

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

try:
    s.bind((HOST, PORT))
except error as e:
    print(str(e))
try:
    s.listen(4)  # max. 4 users in queue
except error as e:
    print(str(e))
print("Waiting for a connection")


def threaded_client(connection, my_id):
    # W zmiennej connection znajduje się obiekt socket, pod zmienną my_id jest indywidualne id podłączonego clienta

    # W nieskończonej pętli należy odbierać wiadomości metodą connection.recv
    # Przesłaną wiadomość wyświetl na ekranie
    while True:
        try:
            data = connection.recv(2048)
            print(pickle.loads(data))
        except:
            break

    print("Connection lost", my_id)


my_id = 0
while True:
    # Serwer oczekuje na nowe połączenie od clienta
    # Analogicznie jak w zadaniu 2
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, my_id))
    my_id += 1