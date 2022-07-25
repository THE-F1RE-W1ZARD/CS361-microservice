import socket

host = "127.0.0.1"
port = 3000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    
    #values the API returns
    message = b"""{
        "0": "Day 1",
        "1": [
            "Rain",
            "High of 95 F",
            "Low of 80 F"
        ]
    }"""

    s.sendall(message)

    #get data and print
    data = s.recv(1024)
    print (data.decode())
