import socket 
import threading 


HOST = '127.0.0.1' # localhost
PORT = 5001


#create scoket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()

# List to hold all connected clients 
clients = []
nicknames = []

#broadcast function to send messages to all clients

def broadcast(message):
    for client in clients:
        client.send(message)
        
        
#handle client connection 
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[nicknames]
            broadcast(f'{nickname} left the chat!'.encode('utf-8'))
            nicknames.remove(nickname)
            break 
        
def receive():
    while True:
        client,address = server.accept()
        print(f'Connected with {str(address)}')
        
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)
        
        print(f'Nickname is {nickname}')
        broadcast(f'{nickname} joined the chat!'.encode('utf-8'))
        client.send('Connected to the server!'.encode('utf-8'))
        thread = threading.Thread(target=handle_client,args=(client,))
        thread.start()
    


print('Server is listening...')
receive()

        
        
    
        
            

            
            
            
            
            
    