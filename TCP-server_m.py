import socket


HOST = '127.0.0.1'  # Локальний хост
PORT = 65432        # Порт для з'єднання

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))  # Прив'язати сокет до адреси
    server_socket.listen()  # Прослуховування підключення
    print(f"Сервер запущено на {HOST}:{PORT}")

    # Нескінченний цикл для обробки клієнтів
    while True:
        conn, addr = server_socket.accept()  # Щоб прийняти нове підключення
        print(f"Підключено клієнта: {addr}")
        with conn:  # Обробка конкретного клієнта
            while True:
                data = conn.recv(1024)  # Отримання повід від клієнта
                if not data:  # Якщо клієнт завершив з'єднання
                    print(f"Клієнт {addr} відключився")
                    break
                print(f"Отримано від {addr}: {data.decode()}")
                conn.sendall(data)  # Повернення отримани даних
