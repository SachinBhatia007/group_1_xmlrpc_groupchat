## config.py
find an available port in local machine and input it in config.py for eg PORT = 5353 IP = "192.168.56.1" list of available ports can be seen using netstat -aon command in cmd

## running the server 
    python3 server.py
First need run the server, to receive the requests. 

## running the client 
    python3 client.py
And the client, to send the requests 
when u execute the client, will ask for a name (nick name), that name will show for all users are connected in the server when u send messages. Open this client in multiple terminals and you can see all messages sent by each client in all terminals
