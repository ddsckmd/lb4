import socket

# Налаштування клієнта
HOST = '127.0.0.1'  # Серверний хост (локальний)
PORT = 65432        # Порт на сервері = Порт клієнта

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))  # Підключення до сервера
    while True:
        message = input("Пиши повідомлення: ")
        if message.lower() == 'exit':
            break
        client_socket.sendall(message.encode())  # Надсилається повідомлення
        data = client_socket.recv(1024)  # Відповідь
        print(f"Отримано від сервера: {data.decode()}")
