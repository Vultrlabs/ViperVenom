import os
from colorama import Fore, Back, Style
import random
import time
import glob
def Banner():
    print(f"""{Fore.RED}   
      (`-')  _      _  (`-') (`-')  _   (`-')       (`-') (`-')  _<-. (`-')_            <-. (`-')  
     _(OO ) (_)     \-.(OO ) ( OO).-/<-.(OO )      _(OO ) ( OO).-/   \( OO) )     .->      \(OO )_ 
,--.(_/,-.\ ,-(`-') _.'    \(,------.,------,),--.(_/,-.\(,------.,--./ ,--/ (`-')----. ,--./  ,-.)
\   \ / (_/ | ( OO)(_...--'' |  .---'|   /`. '\   \ / (_/ |  .---'|   \ |  | ( OO).-.  '|   `.'   |
 \   /   /  |  |  )|  |_.' |(|  '--. |  |_.' | \   /   / (|  '--. |  . '|  |)( _) | |  ||  |'.'|  |
_ \     /_)(|  |_/ |  .___.' |  .--' |  .   .'_ \     /_) |  .--' |  |\    |  \|  |)|  ||  |   |  |
\-'\   /    |  |'->|  |      |  `---.|  |\  \ \-'\   /    |  `---.|  | \   |   '  '-'  '|  |   |  |
    `-'     `--'   `--'      `------'`--' '--'    `-'     `------'`--'  `--'    `-----' `--'   `--'
""")
    print(f"{Fore.BLUE}The quieter you become, the more you can hear, ViperVenom\n")
    print()
Banner()
time.sleep(2)
print(f"{Fore.BLUE}[*]{Fore.WHITE} Getting temp folder...")
tempfolder = os.getenv("TEMP")
time.sleep(1)
print(f"{Fore.GREEN}[+]{Fore.WHITE} Got temp folder path.")
time.sleep(1)
print(f"{Fore.BLUE}[*]{Fore.WHITE} Looking for ViperVenom screenshot evidences...")
os.chdir(tempfolder)
for file in glob.glob("xpvuNBYVvC.jpg"):
    print(f"{Fore.GREEN}[+]{Fore.WHITE} Found screenshot! Accuracy level: 99.9%")
    time.sleep(2)
    os.chdir(tempfolder)
    for file in glob.glob("*.jpg"):
        print(f"{Fore.GREEN}[+]{Fore.WHITE} Found screenshot! Accuracy level: 40%")
        print(f"{Fore.BLUE}[*]{Fore.WHITE} If you suspect that you're a victim ViperVenom malware, contact {Fore.CYAN}info@revise7.com{Fore.WHITE}")
    for file in glob.glob("*.png"):
        print(f"{Fore.GREEN}[+]{Fore.WHITE} Found screenshot! Accuracy level: 30%")
exit()
