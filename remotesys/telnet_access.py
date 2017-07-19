import getpass
import sys
import telnetlib
import time

print()
print(" --> Remote access to Avaya switches <--")
print("  -> Developed by: Diego Chacón (dchacon@lynx.com.ec)")
print()
TEL_HOST = input("Enter the Avaya switch IP address: ")
TEL_USER = 'rwa'
TEL_PASS = getpass.getpass()

tn = telnetlib.Telnet(TEL_HOST)
time.sleep(4)
print("Reading login...")
tn.read_until("Login: ".encode())
time.sleep(1)
tn.write((TEL_USER + "\n").encode())
if TEL_PASS:
    print("Reading password...")
    tn.read_until("Password: ".encode())
    tn.write((TEL_PASS + "\n").encode())
print("Writting commands")
tn.write("show ip interface\n".encode())
time.sleep(1)
print("Printing all")
print(tn.read_very_eager())
print("Exiting shit")
tn.write("exit\n".encode())
time.sleep(2)
tn.close()