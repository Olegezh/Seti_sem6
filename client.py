import socket
import threading

# Choosing Nickname / Ввод псевдонима
nickname = input("Choose your nickname: ")
ip_address = "127.0.0.54"
# Connecting To Server / Подключение к серверу
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip_address, 1067))

# Listening to Server and Sending Nickname
# Прослушивение сервера и отправка псевдонима
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            # Получение сообщение от сервера 
            # Если человек отпаравил свой псевдоним
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            # Close Connection When Error
            # Закрытие подключения когда ошибка
            print("An error occured!")
            client.close()
            break

def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('utf-8'))

# Starting Threads For Listening And Writing
# Начало потока для прослушивание и записывания
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()