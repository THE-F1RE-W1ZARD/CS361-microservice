#code adapted from: https://realpython.com/python-sockets/
import socket
import json
from datetime import date, timedelta

#loopback interface adress
host = "127.0.0.1"
port = 3000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind((host, port))
    s.listen()

    conn, addr = s.accept()

    output = ""
    input = json.loads(conn.recv(1024).decode())

    #add day
    if input["0"] == "Day 1":
        output += "Today: \n"

    else:
        date_offset = (int(input["0"][4]) - 1)
        day = (date.today() + timedelta(days=date_offset))
        
        output += (day.strftime("%A") + ": \n")

    #add weather
    output += ("You will see " + input["1"][0].lower() + " outside\n")

    #add temp
    output += ("With a " + input["1"][1].lower() + " and a " + input["1"][2].lower())

    conn.sendall(bytes(output, 'utf-8'))

