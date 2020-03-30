import os
import time
import sys
def banner():
 os.system("apt install toilet")
 os.system("clear")
 os.system("toilet -fmono12 -F gay MailDiya")
 print("    \033[1;36;40m Code made by: \033[1;32;40m Tuhin Bose")
 print("    \033[1;36;40m Inspired by : \033[1;32;40m Charlie:The Hacker")
 print("    \033[1;36;40m Instagram id: \033[1;32;40m www.instagram.com/tuhin1729")
 print("    \033[1;36;40m Github      : \033[1;32;40m www.github.com/tuhin1729")
 print("    \033[1;36;40m YouTube     : \033[1;32;40m https://bit.ly/TuhinTheHacker")
 print("    \033[1;36;40m Dedicated to: \033[1;34;40m Diya Saha")
 print("    \033[1;31;40m    Use a VPN before running it.Otherwise it won't work")
 print("\n\n")
banner()
print("          \033[1;32;40m[1] \033[1;36;40mAnonymous Mail")
print("          \033[1;32;40m[2] \033[1;36;40mMail Bombing")
op=input("\033[1;32;40mDiya>>>")
if(op=="1"):
 os.system("python3 anonmail.py")
elif(op=="2"):
 os.system("python3 bombmail.py")
else:
 print("\033[1;31;40mInvalid option.Quiting...")
 time.sleep(1.5)
 sys.exit()

 
 
