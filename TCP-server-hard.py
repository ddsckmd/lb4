import socket


HOST = '127.0.0.1'  # Локальний хост
PORT = 65433        # Порт для з'єднання

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))  # Прив'язання сокета до адреси
    server_socket.listen()
    print(f"Сервер запущено на {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()  # Підключення
        print(f"Підключено клієнта: {addr}")
        with conn:
            # Отримання імені файлу
            filename = conn.recv(1024).decode()
            print(f"Отримано ім'я файлу: {filename}")

            # Відкриття файла щоб записати його вміст
            with open(f"received_{filename}", "w") as f:
                while True:
                    data = conn.recv(1024).decode()  # Отримання самого вмісту
                    if not data:  # Якщо всі дані отримано
                        break
                    f.write(data)  # Записання в новий файл

            print(f"Файл '{filename}' успішно збережено як 'received_{filename}'")
