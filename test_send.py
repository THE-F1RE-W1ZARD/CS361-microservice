import socket

host = "127.0.0.1"
port = 3000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    
    #values the API returns
    message = b'{"0": "Day 1", "1": ["Clouds", "High of 77 F", "Low of 55 F"]}'

    s.sendall(message)

    #get data and print
    data = s.recv(1024)
    print (data.decode())