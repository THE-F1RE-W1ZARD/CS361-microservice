# Requesting Data:
To request data you must use the socket library in python. <br />
The data must be sent as a byte string with the syntax:  <br />
> {"0": "Day 1", "1": ["Clouds", "High of 77 F", "Low of 55 F"]}

where "Day 1", "Clouds", "High of 77 F", and "Low of 55F" are gotten from the API call and may very.  <br />
You will use the sendall method to send the JSON object / string.  <br />

The host and port number will be given privatly to users since it is personal information.  <br />

Example code for sending data is stored in test_send.py.  <br />

# Receiving Data:
Data will be sent back using the sendall() method from socket.  <br />
It will be sent as a byte string, so use the decode() function to make the text seen as intended.  <br />
You will then see a string of the format:  <br />
> "day": <br />
> You will see "weather" outside  <br />
> With a high of "high temp" and a low of "low temp"  <br />
    
where all data inside "" was sent to the microservice in a JSON object.  <br />

It is intended to be inserted where the origianl JSON object was prior.  <br />

Example code for recieving data is stored in test_send.py. <br />

# UML Sequence Diagram:
![UML diagram](https://user-images.githubusercontent.com/92611933/180880964-db37d102-e6db-4236-91c9-d023f5fa23c4.png)
