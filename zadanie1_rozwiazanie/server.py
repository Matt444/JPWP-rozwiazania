import socket
from _thread import *
from player import Player
from ball import Ball
from game import Game, update_game_state
import pickle
import pygame

server = '127.0.0.1'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

w, h = 788,444
players = [Player(50, 414, 30, (255, 0, 0), 30, w/2-30, pygame.K_a, pygame.K_d, pygame.K_w),
           Player(w - 50, 414, 30, (0, 255, 0), w/2+30, w-30, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP)]
ball = Ball(200, 250, 0, 0, 20)
game = Game()

def threaded_client(conn, player):
    if player == 0:
        conn.send(pickle.dumps([players[0], players[1], ball, game]))
    else:
        conn.send(pickle.dumps([players[1], players[0], ball, game]))
    reply = ""

    while True:
        try:
            data = pickle.loads(conn.recv(2048))

            if not data:
                print("Disconnected")
                break
            else:
                players[player].x, players[player].y = data

                if player == 0:
                    reply = [players[1].x, players[1].y, ball, game]
                else:
                    reply = [players[0].x, players[0].y, ball, game]

                if player == 1:
                    ball.move(players[0], players[1], game, w)
                    update_game_state(ball, players[0], players[1], game, w)

            conn.send(pickle.dumps(reply))
        except:
            break

    print("Lost connection with player " + str(player))
    conn.close()


player = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, player))
    player += 1
