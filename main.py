import os

green="""\033[32m
    ________  ________  ________     
    |\   ____\|\   __  \|\   __  \    
     \ \  \___|\ \  \|\  \ \  \|\  \   
      \ \  \    \ \   _  _\ \  \\\  \  
       \ \  \____\ \  \\  \\ \  \\\  \ 
        \ \_______\ \__\\ _\\ \_______\\
         \|_______|\|__|\|__|\|_______|
    \033[0m"""
blue="\033[34m[?]: \033[0m"
def banner():
    print(f"""
          {green}
                                                                                                                
                Made by Anton Hrlić                                                                                                                                   
    """)

def functions():
    print("""
            1. Phishing tool             2. Gmail Bomber
            3. IP Tracker                4. DNS Spoofing
            5. Port Scanner              6. ls
            7. DDoS Attack                8. Keylogger
            9. Brute Force                10. Exit
        """)

def main():
    user=int(input(f"{blue} "))
    if user==1:
        os.system("git clone --depth=1 https://github.com/htr-tech/zphisher.git")
    elif user==2:
        os.system("git clone https://github.com/palahsu/MBomb.git")
    elif user==3:
        os.system("git clone https://github.com/rajkumardusad/IP-Tracer.git")
    elif user==4:
        os.system("git clone https://github.com/Trackbool/DerpNSpoof.git")
    elif user==5:
        os.system("git clone https://github.com/RustScan/RustScan.git")
    elif user==6:
        os.system("ls")
    elif user==7:
        os.system("git clone https://github.com/Anton-ai111/DDos-HAT.git")
    elif user==8:
        os.system("git clone https://github.com/De3vil/KLogger.git")
    elif user==9:
        os.system("git clone https://github.com/vanhauser-thc/thc-hydra.git")
    elif user==10:
        exit()

if __name__ == "__main__":
    banner()
    functions()
    main()