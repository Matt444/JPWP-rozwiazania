import _pickle as pickle  # for faster serialization
import socket

'''
Należy zmodyfikować adres IP w zmiennej self.host w konstruktorze na swój z sieci lokalnej
'''

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "127.0.0.1" # To be changed to your local IP address
        self.port = 8999
        self.addr = (self.host, self.port)

    def connect(self):
        self.client.connect(self.addr)
        data = self.client.recv(2048 * 12)
        return pickle.loads(data)

    def disconnect(self):
        self.client.close()

    def send(self, data):

        try:

            self.client.send(pickle.dumps(data))

            reply = self.client.recv(2048 * 12)
            try:
                reply = pickle.loads(reply)
            except Exception as e:
                print(e)

            return reply
        except socket.error as e:
            print(e)