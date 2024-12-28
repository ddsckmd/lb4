import socket

# Створення серверного сокета
HOST = '127.0.0.1'  # Локальний хост
PORT = 65432        # Порт для з'єднання

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))  # Прив'язати сокет до адреси
    server_socket.listen()  # Прослуховування підключення
    print(f"Сервер запущено на {HOST}:{PORT}")

    conn, addr = server_socket.accept()  # Прийняли підключення
    with conn:
        print(f"Підключено клієнта: {addr}")
        while True:
            data = conn.recv(1024)  # Отримання даних
            if not data:
                break
            print(f"Отримано: {data.decode()}")
            conn.sendall(data)  # Назад клієнту щоб повреталось
