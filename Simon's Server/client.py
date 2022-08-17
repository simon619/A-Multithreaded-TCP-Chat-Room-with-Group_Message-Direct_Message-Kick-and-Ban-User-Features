import socket
import threading

name = input('Enter Your Name: ')
email = input('Enter Your Email: ')
if name == 'Admin':
    pw = input('Admin, Enter Your Password: ')

ip, port = '127.0.0.1', 55555
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))
thread_ter = False

def receive():
    while True:
        global thread_ter
        if thread_ter:
            break
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NAME':
                client.send(name.encode('ascii'))
            if message == 'EMAIL':
                client.send(email.encode('ascii'))
                next_message = client.recv(1024).decode('ascii')
                if next_message == 'PASS':
                    client.send(pw.encode('ascii'))
                    if client.recv(1024).decode('ascii') == 'REFUSE':
                        print('Connection is Terminated. Wrong Password!')
                        thread_ter = True
                if next_message == 'BAN':
                    print('You Are Bannised From the Simon\'s Server')
                    client.close()
                    thread_ter = True
                if next_message == 'WAIT':
                    thread_ter = True
            else:
                print(message)
        except:
            print('An ERROR Has Occured')
            client.close()
            break

def write_a_message():
    try:
        while True:
            if thread_ter:
                break
            message = f'{name}: {input("")}'
            if message[len(name) + 2:].startswith('/'):
                if name == 'Admin':
                    if message[len(name) + 2:].startswith('/kick'):
                        print(f'KICK {message[len(name) + 2 + 6:]}')
                        client.send(f'KICK {message[len(name) + 2 + 6:]} now'.encode('ascii'))
                    elif message[len(name) + 2 :].startswith('/ban'):
                        print(f'BAN {message[len(name) + 2 + 5:]}')
                        client.send(f'BAN {message[len(name) + 2 + 5:]} now'.encode('ascii'))
                else:
                    print('Your Are Not The Admin. You Don\'t Have The Power')
            else:
                client.send(message.encode('ascii'))
    except:
        print('Your Are Currently Not A Part of Simon\'s Server')    

receive_thread = threading.Timer(1, receive)
receive_thread.start()

write_thread = threading.Timer(1, write_a_message)
write_thread.start()




