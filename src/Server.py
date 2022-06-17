try:
    import socket as skt
    from socket import socket
    from threading import Thread
    from dataclasses import dataclass
    from typing_extensions import Self
    
except ModuleNotFoundError.__doc__ as mnfe:
    raise AttributeError(args='Cannot Run Server') from None

finally:
    ...
    



@dataclass
class Users:
    clients = set()





def clientThread(clientSocket : socket , clientAddress) -> None:
    while True:
        msg = clientSocket.recv(1024).decode(encoding='utf-8')
        print(f'{clientAddress[0]} : {str(clientAddress[1])} says: {msg}')
        for client in Users.clients:
            if (client is not clientSocket):
                client.send((f'{clientAddress[0]} : {str(clientAddress[1])} says: {msg}').encode(encoding='utf-8'))
        if (not msg):
            Users.clients.remove(clientSocket)
            print((f'{clientAddress[0]} : {str(clientAddress[1])} says: {msg}').encode(encoding='utf-8'))
            break
    clientSocket.close()
    

hostSocket = socket(skt.AF_INET , skt.SOCK_STREAM)
hostSocket.setsockopt(skt.SOL_SOCKET , skt.SO_REUSEADDR , 1)


hostSocket.bind(('127.0.0.1' , 8000))
hostSocket.listen(1)
print('Waiting For Connection . . .')


if (__name__ == '__main__' and __package__ is None):
    while True:
        clientSocket , clientAddress = hostSocket.accept()
        Users.clients.add(clientSocket)
        print(f"Connection Stablished With: {clientAddress[0]} : {clientAddress[1]}")
        th = Thread(target=clientThread , args=(clientSocket , clientAddress , ))
        th.start()