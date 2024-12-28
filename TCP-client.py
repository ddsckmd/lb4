import socket
import os

# Налаштування клієнта
HOST = '127.0.0.1'  # Серверний хост (локальний)
PORT = 65433  # Порт на сервері = Порт клієнта

# Вказати шлях до файлу
file_path = input("Шлях до файлу для передачі його до сервера: ")

# Перевірка що файл є реально
if not os.path.isfile(file_path):
    print("Файл не знайдено! Спробуйте ще раз!")
else:
    # Отримання імені файла
    filename = os.path.basename(file_path)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))  # Підключаємося до серв
        client_socket.sendall(filename.encode())  # Надіслання імені файлу

        # Відкривається файл для читання та надсилається його вміст
        with open(file_path, "r") as f:
            while chunk := f.read(1024):
                client_socket.sendall(chunk.encode())

        print(f"Файл '{filename}' успішно надіслано")
