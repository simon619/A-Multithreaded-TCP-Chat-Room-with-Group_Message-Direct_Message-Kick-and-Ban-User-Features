import threading
import socket
import csv

host, port = '127.0.0.1', 55555
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients, names, emails= [], [], []
csv_path = 'Data\info.csv'
ban_path = 'Data\list_of_bans.csv'
online_dic = {}
ban_email_list = []

with open(csv_path, 'r') as file:
    lines = csv.reader(file)
    
    for line in lines:
        names.append(line[0])
        emails.append(line[1])

with open(ban_path, 'r') as file:
    lines = csv.reader(file)
    
    for line in lines:
        ban_email_list.append(line[0])

with open('Data/password.txt', 'r') as file:
    pw = file.read()

def broadcast(message):
    for client in clients:
        client.send(message)
        
def data_exchange(client):
    global online_dic
    global clients
    global emails
    global names
    global ban_email_list 
    while True:
        bool =  False
        try:
            if client in clients:
                message = client.recv(1024)
                de = message.decode("utf-8")
                last_person = de.split()[-1]
                last_person = last_person.replace('/', '')
                if last_person in online_dic:
                    list = online_dic[last_person]
                    client = list[0]
                    client.send(message)
                elif de.startswith('KICK'):
                    for name, info in online_dic.items():
                        if info[0] == client:
                            if name == 'Admin':
                                user = de[5:len(de) - 4]
                                kick_client = online_dic[user][0]
                                kick_client.send('Your Are Kicked Out By Admin'.encode('ascii'))
                                clients.remove(kick_client)
                                kick_client.close() 
                                client.send('Kicked Out Someone'.encode('ascii'))
                                del online_dic[user]
                                bool = True
                                client.send('WAIT'.encode('ascii'))
                                broadcast(f'=>{user} Has Been Kicked Out by Admin'.encode('ascii'))
                            else:
                                client.send('Action Can\'t be Done'.encode('ascii'))
                elif de.startswith('BAN'):
                    for name, info in online_dic.items():
                        if info[0] == client:
                            if name == 'Admin':
                                user = de[4:len(de) - 4]
                                ban_client = online_dic[user][0]
                                ban_client.send('Your Are Kicked Out By Admin'.encode('ascii'))
                                clients.remove(ban_client)
                                ban_client.close() 
                                client.send('Kicked Out Someone'.encode('ascii'))
                                list = [online_dic[user][1]] * 1
                                ban_email_list.append(online_dic[user][1])
                                del online_dic[user]
                                bool = True
                                client.send('WAIT'.encode('ascii'))
                                broadcast(f'=>{user} Has Been Kicked Out By Admin'.encode('ascii'))
                                with open(ban_path, 'a', newline='\n') as file:
                                    new_line = csv.writer(file)
                                    new_line.writerow(list)
                                    file.close()
                            else:
                                client.send('Action Can\'t be Done'.encode('ascii'))
                else:  
                    broadcast(message)
        except:           
            temp = ''
            if online_dic['Admin']:
                if online_dic['Admin'][0] == client and bool:
                    continue
            else:
                clients.remove(client)
                client.close()
                for name, info in online_dic.items():
                    if info[0] == client:
                        temp = name
                del online_dic[temp]
            print(f'Someone Has Left From Simon\'s Server')
            if not len(online_dic):
                broadcast(f'{temp} Left the Chat'.encode('ascii'))
            break

def receive():
    global clients
    global emails
    global names
    global ban_email_list
    global pw
    while True:
        print(f'ban: {ban_email_list}')
        client, address = server.accept()
        client.send('NAME'.encode('ascii'))
        name = client.recv(1024).decode('ascii')
        client.send('EMAIL'.encode('ascii'))
        email = client.recv(1024).decode('ascii')
        if email in ban_email_list:
            client.send('BAN'.encode('ascii'))
            client.close()
            continue
        elif name == 'Admin':
            client.send('PASS'.encode('ascii'))
            password = client.recv(1024).decode('ascii')
            if password != pw:
                client.send('REFUSE'.encode('ascii'))
                client.close()
                continue
            else:
                online_dic[name] = [client, email]
                clients.append(client)
                broadcast(f'{name} Has Joined the Chat'.encode('ascii'))
                client.send(f'Welcome Back {name}'.encode('ascii'))
        elif str(email) not in emails:          
            names.append(name)
            emails.append(email)
            clients.append(client)
            online_dic[name] = [client, email]
            broadcast(f'{name} Has Joined the Server'.encode('ascii'))
            client.send(f'{name} Welcome to Simon\'s Server'.encode('ascii'))
            info_list = [name, email]

            with open(csv_path, 'a', newline='\n') as file:
                new_line = csv.writer(file)
                new_line.writerow(info_list)
                file.close() 
        else:
            online_dic[name] = [client, email]
            clients.append(client)
            broadcast(f'{name} Has Joined the Chat'.encode('ascii'))
            client.send(f'Welcome Back {name}'.encode('ascii'))
        print(f'Currently Online: {online_dic}')
        thread = threading.Timer(1, data_exchange, args=(client,))
        thread.start()
print('Server is Listening')
receive()