# -*- coding: utf-8 -*-
"""
Author: new92
Github: @new92
InstaFollowV3: Script for increasing the followers of an Instagram account



*********IMPORTANT*********
User's login credentials (such as: username, password) will not be stored or saved !
Will be used only to increase the followers of the user's Instagram account
***************************
"""


try:
    import sys
    if sys.version_info[0] < 3:
        print("[!] Error ! This script requires Python version 3.X ! ")
        print("""[+] Instructions to download Python 3.x : 
        Linux: apt install python3
        Windows: https://www.python.org/downloads/
        MacOS: https://docs.python-guide.org/starting/install3/osx/""")
        print("[+] Please install the Python 3 and then use this script ✅")
        sleep(2)
        print("[+] Exiting...")
        sleep(1)
        quit(0)
    import platform
    from os import system
    from time import sleep
    import os
    import instagrapi
    import requests
    from datetime import date
    import instaloader
except ImportError as imp:
    print("[!] WARNING: Not all packages used in this script have been installed !")
    sleep(2)
    print("[+] Ignoring warning...")
    sleep(1)
    if sys.platform.startswith('linux'):
        if os.geteuid() != 0:
            print("[!] Root user not detected !")
            sleep(2)
            print("[+] Trying to enable root user...")
            sleep(1)
            system("sudo su")
            try:
                system("sudo pip install -r requirements.txt")
            except Exception as ex:
                print("[!] Cannot install the required modules !")
                sleep(2)
                print("[1] Uninstall script")
                print("[2] Exit")
                opt=int(input("[>] Please enter a number (from the above ones): "))
                while opt < 1 or opt > 2 or opt == None or type(opt) != int:
                    if opt == None:
                        print("[!] This field can't be blank !")
                    elif type(opt) != int:
                        print(f"[!] The number must be an integer ! Not {type(opt)}")
                    else:
                        print("[!] Invalid number !")
                        sleep(1)
                        print("[+] Acceptable numbers: [1,2]")
                    sleep(1)
                    print("[1] Uninstall script")
                    print("[2] Exit")
                    opt=int(input("[>] Please enter a number (from the above ones): "))
                if opt == 1:
                    def rmdir(dire):
                        DIRS = []
                        for root, dirs, files in os.walk(dire):
                            for file in files:
                                os.remove(os.path.join(root,file))
                            for dir in dirs:
                                DIRS.append(os.path.join(root,dir))
                        for i in range(len(DIRS)):
                            os.rmdir(DIRS[i])
                        os.rmdir(dire)
                    rmdir(os.path.abspath('IGFollowersIncreaser'))
                    print("[+] Files and dependencies uninstalled successfully !")
                else:
                    print("[+] Exiting...")
                    sleep(1)
                    print("[+] See you next time 👋")
                    quit(0)
        else:
            system("sudo pip install -r requirements.txt")
    elif sys.platform == 'darwin':
        system("python -m pip install requirements.txt")
    elif platform.system() == 'Windows':
        system("pip install -r requirements.txt")

def Info():
    author = 'new92'
    license1 = 'MIT'
    lang = 'es-US'
    email = 'new92github@gmail.com'
    language = 'Python'
    name = 'InstaFollowV3'
    api = None
    lines = 847
    f = '/IGFollowersIncreaser/InstagramFollowers/V3/mainV3.py'
    if os.path.exists(os.path.abspath(f)):
        fsize = (os.stat(f)).st_size
    else:
        fsize = 0
    stars = 17
    forks = 10
    print("[+] Author: "+str(author))
    print("[+] Github: @"+str(author))
    print("[+] License: "+str(license1))
    print("[+] Natural language: "+str(lang))
    print("[+] Programming language(s) used: "+str(language))
    print("[+] Number of lines: "+str(lines))
    print("[+] Script's name: "+str(name))
    print("[+] API(s) used: "+str(api))
    print("[+] File size: "+str(fsize)+" bytes")
    print("[+] Github repo stars: "+str(stars))
    print("[+] Github repo forks: "+str(forks))

def Uninstall() -> str:
    def rmdir(dire):
        DIRS = []
        for root, dirs, files in os.walk(dire):
            for file in files:
                os.remove(os.path.join(root,file))
            for dir in dirs:
                DIRS.append(os.path.join(root,dir))
        for i in range(len(DIRS)):
            os.rmdir(DIRS[i])
        os.rmdir(dire)
    rmdir(os.path.abspath('IGFollowersIncreaser'))
    return "[+] Files and dependencies uninstalled successfully !"

def banner() -> str:
    return """
██╗███╗░░██╗░██████╗████████╗░█████╗░███████╗░█████╗░██╗░░░░░██╗░░░░░░█████╗░░██╗░░░░░░░██╗      ██╗░░░██╗██████╗░
██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔══██╗██║░░░░░██║░░░░░██╔══██╗░██║░░██╗░░██║      ██║░░░██║╚════██╗
██║██╔██╗██║╚█████╗░░░░██║░░░███████║█████╗░░██║░░██║██║░░░░░██║░░░░░██║░░██║░╚██╗████╗██╔╝      ╚██╗░██╔╝░█████╔╝
██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║██╔══╝░░██║░░██║██║░░░░░██║░░░░░██║░░██║░░████╔═████║░      ░╚████╔╝░░╚═══██╗
██║██║░╚███║██████╔╝░░░██║░░░██║░░██║██║░░░░░╚█████╔╝███████╗███████╗╚█████╔╝░░╚██╔╝░╚██╔╝░      ░░╚██╔╝░░██████╔╝
╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░░╚════╝░╚══════╝╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░      ░░░╚═╝░░░╚═════╝░
"""
ANS = ["yes","YES","Yes","y","Y","YeS","yEs","YEs","yES","no","NO","No","n","N","nO"]

def nums():
    print("[1] Increase followers")
    print("[2] Show script's info and exit")
    print("[3] Keep log")
    print("[4] Clear log")
    print("[5] Uninstall script")
    print("[6] Exit")

def clear():
    if platform.system() == 'Windows':
        system("cls")
    else:
        system("clear")
        
def checkUser(username:str) -> bool:
    return username == None or len(username) > 30 or type(username) != str

def valUser(username:str) -> bool:
    L = [400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 421, 422, 423, 424, 425, 426, 429, 431, 451]
    return requests.get("https://www.instagram.com/"+username).status_code in L

def main():
    print(banner())
    print("\n")
    print("[+] Script for increasing the followers of an account on Instagram (works for both public and private accounts)")
    print("\n")
    print("[+] Author: new92")
    print("[+] Github: @new92")
    print("\n")
    nums()
    print("\n")
    num=int(input("[>] Please enter a number (from the above ones): "))
    while num < 1 or num > 6 or num == None or type(num) != int:
        if num == None:
            print("[!] This field can't be empty !")
        elif type(num) != int:
            print("[!] The number must be an integer ! Not "+str(type(num)))
        else:
            print("[!] Invalid number !")
            sleep(1)
            print("[+] Acceptable numbers: [1/2/3/4/5/6]")
        sleep(1)
        nums()
        sleep(1)
        num=int(input("[>] Please enter again a number (from the above ones): "))
    if num == 1:
        clear()
        NAMES = ['Cristiano Ronaldo','Cardi B','Kim Kardashian','Ariana Grande','Nicki Minaj','Beyonce','Katy Perry','Selena Gomez','Justin Bieber','Lionel Messi','Neymar Jr','Kylian Mbappe','Dua Lipa','Billie Eilish','Kylie Jenner','Khloe Kardashian','Kourtney Kardashian','Jennifer Lopez','Shakira','NBA','Instagram','National Geographic','FC Barcelona','Real Madrid','Champions League','Chris Brown','Taylor Swift','Kendall Jenner','Virat Kohli','Zendaya','Marvel','Tom Holland','Emma Watson','Millie Bobby Brown','Shawn Mendes','Camila Cabello','NASA','Nike']
        users = {
            'Cristiano Ronaldo' : '173560420',
            'Cardi B' : '1436859892',
            'Kim Kardashian': '18428658',
            'Ariana Grande' : '7719696',
            'Nicki Minaj' : '451573056',
            'Beyonce' : '247944034',
            'Katy Perry' : '407964088',
            'Selena Gomez' : '460563723',
            'Justin Bieber' : '6860189',
            'Lionel Messi' : '427553890',
            'Neymar Jr' : '26669533',
            'Kylian Mbappe' : '4213518589',
            'Dua Lipa' : '12331195',
            'Billie Eilish' : '28527810',
            'Kylie Jenner' : '12281817',
            'Khloe Kardashian' : '208560325',
            'Kourtney Kardashian' : '145821237',
            'Jennifer Lopez' : '305701719',
            'Shakira' : '217867189',
            'NBA' : '20824486',
            'Instagram' : '25025320',
            'National Geographic' : '787132',
            'FC Barcelona' : '260375673',
            'Real Madrid' : '290023231',
            'Champions League' : '1269788896',
            'Chris Brown' : '29394004',
            'Taylor Swift' : '11830955',
            'Kendall Jenner' : '6380930',
            'Virat Kohli' : '2094200507',
            'Zendaya' : '9777455',
            'Marvel' : '204633036',
            'Tom Holland' : '176618189',
            'Emma Watson' : '1418652011',
            'Millie Bobby Brown' : '3439002676',
            'Shawn Mendes' : '212742998',
            'Camila Cabello' : '19596899',
            'NASA' : '528817151',
            'Nike' : '13460080'
        }
        if os.path.exists("cons.txt"):
            con=str(input("[>] Do you consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given (Instagram) account ? [yes/no] "))
            if con in ANS[:9]:
                f = open("cons.txt","a")
                f.write("[=] Date: "+str(date.today())+"\n")
                f.write("[=] User: Yes I consent that the author of this script (new92) has no responsibility for any loss or damage may the script cause to the given Instagram account.\n")
                f.write("-"*40)
                f.close()
            else:
                print("[OK]")
                sleep(1)
                print("[1] Exit")
                print("[2] Uninstall script and exit")
                num=int(input("[>] Please enter a number (from the above ones): "))
                while num < 1 or num > 2 or num == None:
                    if num == None:
                        print("[!] This field can't be blank !")
                    else:
                        print("[!] Invalid number !")
                        sleep(1)
                        print("[+] Acceptable numbers: [1/2]")
                    sleep(1)
                    print("[1] Exit")
                    print("[2] Uninstall script and exit")
                    sleep(1)
                    num=int(input("[>] Please enter a number (from the above ones): "))
                if num == 1:
                    clear()
                    print("[+] Exiting...")
                    sleep(1)
                    print("[+] See you next time 👋")
                    sleep(1)
                    quit(0)
                else:
                    clear()
                    print(Uninstall())
                    sleep(1)
                    print("[+] Exiting...")
                    sleep(1)
                    print("[+] Thank you for choosing to use my script 😁")
                    sleep(2)
                    print("[+] If you have any suggestions or found a bug or need help feel free to contact me anytime, at this email address: new92github@gmail.com")
                    sleep(3)
                    print("[+] Exiting...")
                    sleep(1)
                    quit(0)
        else:
            f = open("cons.txt","w")
            f.write("[=] Date: "+str(date.today())+"\n")
            f.write("[=] User: Yes I consent that the author (new92) has no responsibility for any loss or damage may the script cause to the given Instagram account.\n")
            f.write("-"*40)
            f.close()
        sleep(1)
        print("[+] The login credentials will not be stored or saved")
        sleep(2)
        print("-"*20+"login".upper()+"-"*20)
        username=str(input("[>] Please enter your username: "))
        while checkUser(username):
            if username == None:
                print("[!] This field can't be blank !")
            elif type(username) != str:
                print("[!] Username must be a string !")
            else:
                print("[!] Invalid length !")
                sleep(1)
                print("[+] Acceptable length: 30 or less chacacters")
            sleep(1)
            username=str(input("[>] Please enter again your username: "))
        while valUser(username):
            print("[!] User not found !")
            sleep(1)
            print("[1] Try with another username")
            print("[2] Return to menu")
            print("[3] Exit")
            opt=int(input("[>] Please enter a number (from the above ones): "))
            while opt < 1 or opt > 3 or opt == None:
                print("[!] Invalid number !")
                sleep(1)
                print("[1] Try with another username")
                print("[2] Return to menu")
                print("[3] Exit")
                opt=int(input("[>] Please enter again a number (from the above ones): "))
            if opt == 1:
                username=str(input("[>] Please enter the username: "))
                while checkUser(username):
                    if username == None:
                        print("[!] This field can't be blank !")
                    elif type(username) != str:
                        print("[!] Username must be a string !")
                    else:
                        print("[!] Invalid length !")
                        sleep(1)
                        print("[+] Acceptable length: 30 or less chacacters")
                    sleep(1)
                    username=str(input("[>] Please enter again the username: "))
            elif opt == 2:
                clear()
                main()
            else:
                clear()
                print("[+] Exiting...")
                sleep(1)
                print("[+] See you next time 👋")
                sleep(2)
                quit(0)
        con=str(input(f"[?] The script will increase the followers for the user: {username} is that correct ? [yes/no] "))
        while con not in ANS or con == None or type(con) != str:
            if con == None:
                print("[!] This field can't be blank !")
            elif type(con) != str:
                print(f"[!] The answer [yes/no] must be a string ! Not {type(con)}")
            else:
                print("[!] Invalid answer !")
                sleep(1)
                print("[+] Acceptable answers: [yes/no]")
            sleep(1)
            con=str(input(f"[?] The script will increase the followers for the user: {username} is it correct ? [yes/no] "))
        if con in ANS[9:]:
            username=str(input("[>] Please enter another username: "))
            while checkUser(username):
                if username == None:
                    print("[!] This field can't be blank !")
                elif type(username) != str:
                    print("[!] Username must be a string ! Not "+str(type(username)))
                else:
                    print("[!] Invalid length !")
                    sleep(1)
                    print("[+] Acceptable length: less than or equal to 30")
                sleep(1)
                username=str(input("[>] Please enter again your username: "))
            while valUser(username):
                print("[!] User not found !")
                sleep(1)
                print("[1] Try with another username")
                print("[2] Return to menu")
                print("[3] Exit")
                opt=int(input("[>] Please enter a number (from the above ones): "))
                while opt < 1 or opt > 3 or opt == None or type(opt) != int:
                    if opt == None:
                        print("[!] This field can't be blank !")
                    elif type(opt) != int:
                        print("[!] The number must be an integer ! Not "+str(type(opt)))
                    else:
                        print("[!] Invalid number !")
                        sleep(1)
                        print("[+] Acceptable numbers: [1/2/3]")
                    sleep(1)
                    print("[1] Try with another username")
                    print("[2] Return to menu")
                    print("[3] Exit")
                    opt=int(input("[>] Please enter again a number (from the above ones): "))
                if opt == 1:
                    clear()
                    username=str(input("[>] Please enter the username: "))
                    while checkUser(username):
                        if username == None:
                            print("[!] This field can't be blank !")
                        else:
                            print("[!] Invalid length  !")
                            sleep(1)
                            print("[+] The length of the username must be less than or equal to 30 characters.")
                        sleep(1)
                        username=str(input("[>] Please enter again the username: "))
                elif opt == 2:
                    clear()
                    main()
                else:
                    clear()
                    print("[+] Exiting...")
                    sleep(1)
                    print("[+] See you next time 👋")
                    sleep(1)
                    quit(0)
        ga=str(input("[?] Do you want to grant access to the script to have access to the number of your followers in order to provide additional information ? [yes/no] "))
        while ga not in ANS or ga == None or type(ga) != str:
            if ga == None:
                print("[!] This field can't be blank !")
            elif type(ga) != str:
                print(f"[!] Your answer must be a string ! Not {type(ga)}")
            else:
                print("[!] Invalid answer !")
                sleep(1)
                print("[+] Valid answers: [yes/no]")
            sleep(1)
            ga=str(input("[?] Do you want to grant access to the script to have access to the number of your followers in order to provide additional information ? [yes/no] "))
        if ga in ANS[:9]:
            loader = instaloader.Instaloader()
            profile = instaloader.Profile.from_username(loader.context, username)
            followers_bef = profile.followers
        username=username.lower()
        username=username.strip()
        sleep(1)
        password=str(input("[>] Please enter your password: "))
        while password == None or type(password) != str:
            if password == None:
                print("[!] This field can't be blank !")
            else:
                print(f"[!] Password must be a string ! Not {type(password)}")
            sleep(1)
            password=str(input("[>] Please enter again your password: "))
        password=password.strip()
        sleep(1)
        client=instagrapi.Client()
        try:
            login = client.login(username,password)
            if login:
                print("[✓] Login successful !")
                sleep(1)
                print("[+] Please wait while the program is increasing your followers...")
                sleep(2)
            else:
                print("[!] Login unsuccessful !")
                sleep(1)
                print("[+] Please check the username and/or the password !")
                sleep(2)
                print("\n")
                print("[1] Return to menu")
                print("[2] Exit")
                num=int(input("[>] Please enter a number (from the above ones): "))
                while num < 1 or num > 2 or num == None or type(num) != int:
                    if num == None:
                        print("[!] This field can't be empty !")
                    elif type(num) != int:
                        print("[!] The number must be an integer ! Not "+str(type(num)))
                    else:
                        print("[!] Invalid number !")
                        sleep(1)
                        print("[+] Acceptable numbers: [1/2]")
                    sleep(1)
                    print("[1] Return to menu")
                    print("[2] Exit")
                    num=int(input("[>] Please enter again a number (from the above ones):"))
                if num == 1:
                    clear()
                    main()
                else:
                    print("[+] Exiting...")
                    sleep(1)
                    print("[+] See you next time 👋")
                    sleep(2)
                    quit(0)
        except Exception:
            if Exception == 'The password you entered is incorrect. Please try again.':
                print("[!] Incorrect password !")
                sleep(2)
                password=str(input("[>] Please enter again your password: "))
                while password == None or type(password) != str:
                    if password == None:
                        print("[!] This field can't be blank !")
                    else:
                        print("[!] Password must be a string !")
                    sleep(1)
                    password=str(input("[>] Please enter again your password: "))
                password=password.strip()
            else:
                print("[!] Error !")
                sleep(1)
                print("[+] Error message ==> "+str(Exception))
                sleep(2)
                print("[1] Return to menu")
                print("[2] Exit")
                num=int(input("[>] Please enter a number (from the above ones): "))
                while num < 1 or num > 2 or num == None or type(num) != int:
                    if num == None:
                        print("[!] This field can't be empty !")
                    elif type(num) != int:
                        print("[!] The number must be an integer ! Not "+str(type(num)))
                    else:
                        print("[!] Invalid number !")
                        sleep(1)
                        print("[+] Acceptable numbers: [1/2]")
                    sleep(1)
                    print("[1] Return to menu")
                    print("[2] Exit")
                    num=int(input("[>] Please enter again a number (from the above ones):"))
                if num == 1:
                    clear()
                    main()
                else:
                    print("[+] Exiting...")
                    sleep(1)
                    print("[+] See you next time 👋")
                    sleep(1)
                    quit(0)
        sleep(2)
        print("[+] To end the process enter Ctrl + C")
        sleep(2)
        f = 0
        x = 0
        for i in range(30):
            try:
                for j in range(len(NAMES)-1):
                    client.user_follow(users[NAMES[j]])
                    print(f"[+] Following {NAMES[j]}...")
                    sleep(3)
                    f += 1
                    print(f"[+] Next user to follow: {NAMES[j+1]}...")
                    sleep(3)
                for j in range(len(NAMES)-1):
                    client.user_unfollow(users[NAMES[j]])
                    print(f"[-] Unfollowing {NAMES[j]}...")
                    sleep(3)
                    x += 1
                    print(f"[-] Next user to unfollow: {NAMES[j+1]}...")
                    sleep(3)
            except KeyboardInterrupt:
                res = f - x
                if res != 0:
                    suc = f / float(len(NAMES))
                    fail = res / float(len(NAMES))
                    tot = f + x
                    print(f"[✕] Failed to unfollow {abs(res)} users !")
                    sleep(2)
                    print(f"[✓] Successfully followed/unfollowed a total of {tot} users")
                    sleep(1)
                    print(f"[+] Percentage of failure: "+str(fail))
                    sleep(1)
                    print(f"[+] Percentage of success: "+str(suc))
                    sleep(1)
                    if ga in ANS[:9]:
                        followers_af = profile.followers
                        if followers_bef - followers_af != 0:
                            followers_af = user.number_of_followers
                            print(f"[✓] Successfully added: {followers_af - followers_bef} followers.")
                            sleep(1)
                    print("[*] Users which the script failed to unfollow:")
                    sleep(3)
                    print('-'*15+"users".upper()+'-'*15)
                    print("\n")
                    for i in range(res,-1,-1):
                        print("[+] User: "+str(NAMES[i]))
                else:
                    print("[+] Success: 100%")
                    sleep(1)
                    print(f"[+] Fail: {res}%")
                    sleep(2)
                print("\n")
                print("[1] Return to menu")
                print("[2] Exit")
                opt=int(input("[>] Please enter a number (from the above ones): "))
                while opt < 1 or opt > 2 or opt == None or type(opt) != int:
                    if opt == None:
                        print("[!] This field can't be blank !")
                    elif type(opt) != int:
                        print(f"[!] The number must be an integer ! Not {type(opt)}")
                    else:
                        print("[!] Invalid number !")
                        sleep(1)
                        print("[+] Acceptable numbers: [1/2]")
                        sleep(1)
                        print("[1] Return to menu")
                        print("[2] Exit")
                        opt=int(input("[>] Please enter again a number (from the above ones): "))
                if opt == 1:
                    clear()
                    main()
                else:
                    clear()
                    print("[+] Thank you for using my script 😁")
                    sleep(2)
                    print("[+] See you next time 👋")
                    sleep(1)
                    quit(0)
        res = f - x
        if res != 0:
            suc = f / float(len(NAMES))
            fail = res / float(len(NAMES))
            tot = f + x
            print(f"[✕] Failed to unfollow {abs(res)} users !")
            sleep(2)
            print(f"[✓] Successfully followed/unfollowed a total of {tot} users")
            sleep(1)
            print(f"[+] Percentage of failure: "+str(fail))
            sleep(1)
            print(f"[+] Percentage of success: "+str(suc))
            sleep(1)
            if ga in ANS[:9]:
                followers_af = profile.followers
                if followers_bef - followers_af != 0:
                    followers_af = user.number_of_followers
                    print(f"[✓] Successfully added: {followers_af - followers_bef} followers.")
                    sleep(1)
            print("[*] Users which the script didn't unfollow:")
            sleep(3)
            print('-'*15+"users".upper()+'-'*15)
            for i in range(res,-1,-1):
                print("[+] User: "+str(NAMES[i]))
        else:
            print("[+] Success: 100%")
            sleep(1)
            print(f"[+] Fail: {res}%")
            sleep(2)
        print("[1] Return to menu")
        print("[2] Exit")
        opt=int(input("[>] Please enter a number (from the above ones): "))
        while opt < 1 or opt > 2 or opt == None or type(opt) != int:
            if opt == None:
                print("[!] This field can't be blank !")
            elif type(opt) != int:
                print(f"[!] The number must be an integer ! Not {type(opt)}")
            else:
                print("[!] Invalid number !")
                sleep(1)
                print("[+] Acceptable numbers: [1/2]")
                sleep(1)
                print("[1] Return to menu")
                print("[2] Exit")
                opt=int(input("[>] Please enter again a number (from the above ones): "))
        if opt == 1:
            clear()
            main()
        else:
            clear()
            print("[+] Thank you for using my script 😁")
            sleep(2)
            print("[+] See you next time 👋")
            sleep(1)
            quit(0)
    elif num == 2:
        clear()
        Info()
    elif num == 3:
        clear()
        name = "log.txt"
        if os.path.exists(os.path.abspath(name)):
            f = open(name,"a")
            f.write("\n"+"-"*40)
            f.write("[+] Date: "+str(date.today())+"\n")
            f.write("[+] Followed: "+str(f)+" users"+"\n")
            f.write("[+] Unfollowed: "+str(x)+" users"+"\n")
            if res != 0:
                f.write("[✕] Failed to unfollow: "+str(abs(res))+" users"+"\n")
            pers = tot / float(len(NAMES)*2)
            f.write("[+] Percentage of success: "+str(pers)+"%"+"\n")
            f.write("[+] Percentage of fail: "+str(float(100 - pers))+"%"+"\n")
            if ga in ANS[:9]:
                followers_af = user.number_of_followers
                f.write("[✓] Successfully added: "+str(followers_af - followers_bef)+" followers.")
            f.close()
            print("[✓] Successfully saved log !")
            sleep(2)
            print("[↪] Log file name: "+name)
            print("[↪] Path to log file: "+os.path.abspath(name))
            print("[↪] Log file size: "+str((os.stat(name)).st_size))
            sleep(4)
            print("[1] Return to menu")
            print("[2] Exit")
            opt=int(input("[>] Please enter a number (from the above ones): "))
            while opt < 1 or opt > 2 or opt == None or type(opt) != int:
                if opt == None:
                    print("[!] This field can't be blank !")
                elif type(opt) != int:
                    print(f"[!] The number must be an integer ! Not {type(opt)}")
                else:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[+] Acceptable numbers: [1/2]")
                sleep(1)
                print("[1] Return to menu")
                print("[2] Exit")
                opt=int(input("[>] Please enter again a number (from the above ones): "))
            if opt == 1:
                clear()
                main()
            else:
                clear()
                print("[+] Thank you for using my script 😁")
                sleep(2)
                print("[+] See you next time 👋")
                sleep(1)
                quit(0)
        else:
            f = open(name,"w")
            f.write("\n"+"-"*40)
            f.write("[+] Date: "+str(date.today())+"\n")
            f.write("[+] Followed: "+str(f)+" users"+"\n")
            f.write("[+] Unfollowed: "+str(x)+" users"+"\n")
            pers = tot / float(len(NAMES)*2)
            f.write("[+] Percentage of success: "+str(pers)+"%"+"\n")
            f.write("[+] Percentage of fail: "+str(float(100 - pers))+"%"+"\n")
            f.close()
            print("[✓] Successfully saved log !")
            sleep(2)
            print("[↪] Log file name: "+name)
            print("[↪] Path to log file: "+os.path.abspath(name))
            print("[↪] Log file size: "+str((os.stat(name)).st_size))
            sleep(4)
            print("[1] Return to menu")
            print("[2] Exit")
            opt=int(input("[>] Please enter a number (from the above ones): "))
            while opt < 1 or opt > 2 or opt == None or type(opt) != int:
                if opt == None:
                    print("[!] This field can't be blank !")
                elif type(opt) != int:
                    print(f"[!] The number must be an integer ! Not {type(opt)}")
                else:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[+] Acceptable numbers: [1/2]")
                sleep(1)
                print("[1] Return to menu")
                print("[2] Exit")
                opt=int(input("[>] Please enter again a number (from the above ones): "))
            if opt == 1:
                clear()
                main()
            else:
                clear()
                print("[+] Thank you for using my script 😁")
                sleep(2)
                print("[+] See you next time 👋")
                sleep(1)
                quit(0)
    elif num == 4:
        clear()
        name = "log.txt"
        if os.path.exists(os.path.abspath(name)):
            f = open(name,"w")
            f.close()
            print("[✓] Successfully cleared log !")
            sleep(1)
            print("[↪] Log file name: "+name)
            print("[↪] Path to log file: "+os.path.abspath(name))
            print("[↪] Log file size: "+str((os.stat(name)).st_size))
            sleep(4)
            print("[1] Return to menu")
            print("[2] Exit")
            opt=int(input("[>] Please enter a number (from the above ones): "))
            while opt < 1 or opt > 2 or opt == None or type(opt) != int:
                if opt == None:
                    print("[!] This field can't be blank !")
                elif type(opt) != int:
                    print(f"[!] The number must be an integer ! Not {type(opt)}")
                else:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[+] Acceptable numbers: [1/2]")
                sleep(1)
                print("[1] Return to menu")
                print("[2] Exit")
                opt=int(input("[>] Please enter again a number (from the above ones): "))
            if opt == 1:
                clear()
                main()
            else:
                clear()
                print("[+] Thank you for using my script 😁")
                sleep(2)
                print("[+] See you next time 👋")
                sleep(1)
                quit(0)
        else:
            clear()
            print("[!] Log file not found on this device !")
            sleep(2)
            print("[+] Searched log file using name: "+name)
            sleep(2)
            print("[*] Please first create the log file and then use this option 😀")
            sleep(2)
            print("""[+] Instructions: 
            1) Return to menu and enter the option number 3
            2) Wait for the script to end and return to menu (enter yes when the script ask you if you want to return to menu)
            3) From the menu enter the number 4.
            """)
            print("[1] Return to menu")
            print("[2] Exit")
            opt=int(input("[>] Please enter a number (from the above ones): "))
            while opt < 1 or opt > 2 or opt == None or type(opt) != int:
                if opt == None:
                    print("[!] This field can't be blank !")
                elif type(opt) != int:
                    print(f"[!] The number must be an integer ! Not {type(opt)}")
                else:
                    print("[!] Invalid number !")
                    sleep(1)
                    print("[+] Acceptable numbers: [1/2]")
                sleep(1)
                print("[1] Return to menu")
                print("[2] Exit")
                opt=int(input("[>] Please enter again a number (from the above ones): "))
            if opt == 1:
                clear()
                main()
            else:
                clear()
                print("[+] Thank you for using my script 😁")
                sleep(2)
                print("[+] See you next time 👋")
                sleep(1)
                quit(0)
    elif num == 5:
        print(Uninstall())
        sleep(2)
        print("[+] Thank you for choosing my script 😀😁")
        sleep(2)
        print("[+] Hope you enjoyed it 🤗")
        sleep(1)
        print("[+] If you have any suggestions or found a bug or need help feel free to contact me anytime, at this email address: new92github@gmail.com")
        sleep(3)
        print("[+] Until we meet again 🫡")
        sleep(1)
        quit(0)
    else:
        clear()
        print("[+] Thank you for using my script 😁")
        sleep(2)
        print("[+] See you next time 👋")
        sleep(1)
        quit(0)

if __name__ == '__main__':
    main()