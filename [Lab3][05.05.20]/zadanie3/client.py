from network import Network

'''
W client.py wysyłamy wiadomość która zostanie odebrana przez server.
Tutaj nie trzeba nic modyfikować
'''

network = Network()
network.connect()

while True:
    message = input()
    network.send(message)
