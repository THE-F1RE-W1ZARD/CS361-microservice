# CS361-microservice
# Requesting Data:
    To request data you must use the socket library in python.
    The data must be sent as a byte string with the syntax:
        {"0": "Day 1", "1": ["Clouds", "High of 77 F", "Low of 55 F"]}
    where "Day 1", "Clouds", "High of 77 F", and "Low of 55F" are gotten from the API call and may very.
    You will use the sendall method to send the JSON object / string.

    The host and port number will be given privatly to users since it is personal information.

    Example code for sending data is stored in test_send.py.

# Receiving Data:
    Data will be sent back using the sendall() method from socket.
    It will be sent as a byte string, so use the decode() function to make the text seen as intended.
    You will then see a string of the format:
        [day]:
        You will see [weather] outside
        With a high of [high temp] and a low of [low temp]
    where all data inside [] was sent to the microservice in a JSON object.

    It is intended to be inserted where the origianl JSON object was prior.

    Example code for recieving data is stored in test_send.py.

# UML Sequence Diagram: