import hashlib
import base64
from hashlib import blake2b
import os
from termcolor import cprint
from time import sleep
from datetime import date , datetime
import platform
#------------------------#
os.system("clear")  # windows => os.system("cls")
#------------------------#
while True:
  today = date.today()
  d1 = today.strftime("%Y/%m/%d")
  now = datetime.now()
  dt_string = now.strftime(" %H:%M:%S")
  cprint("#" * 50, "green")
  cprint("#" + "                  Mr Hidden                     #", "green")
  cprint("#" + "                                                #", "yellow")
  cprint("#" + "               Hashing in Python                #", "green")
  cprint("#" + " ---------------------------------------------- #", "white")
  cprint("#" + " Help :                                         #", "yellow")
  cprint("#" + "       [1] Hash        #     [6] Sha224         #", "green")
  cprint("#" + "       [2] Encode      #     [7] Sha512         #", "yellow")
  cprint("#" + "       [3] Sha1        #     [8] Hex            #", "green")
  cprint("#" + "       [4] Sha384      #     [9] Blake2b        #", "yellow")
  cprint("#" + "       [5] Sha256      #     [10] Exit          #", "green")
  cprint("#" + " ---------------------------------------------- #", "white")
  cprint("#" + f" Time : {dt_string}  {today}                   #", "yellow")
  cprint("#" + f" System : {platform.system()}                                 #", "green")
  cprint("#" + f" User : {platform.node()}                          #", "yellow")
  cprint("#" * 50, "green")
  print()

  # ------------------------#
  try:
      ch = input("\nEnter Text => ")
  except KeyboardInterrupt as e:
    print(e)
    exit()
  sleep(3)
  # ------------------------#
  if ch == "1":
    cprint("=================================",'cyan')
    try:
      text = input("\nEnter The text for Hash = ")
    except:
      cprint("\nBay Bay :)\n", 'yellow')
      exit()
    f = hashlib.md5()
    f.update(text.encode('utf-8'))
    # ------------------------#
    sleep(1)
    print ("\nHash is = ",f.hexdigest(),"\n")
    cprint("=================================",'cyan')
    sleep(3)
 #==========================#
  elif ch == "2":
    cprint("=================================",'cyan')
    try:
      text = input("\nEnter The Text For Encode = ")
    except:
      cprint("\nBay Bay :)\n", 'yellow')
      exit()
    # ------------------------#
    sleep(1)
    print ("\nEncode is ", base64.b64encode(text.encode()),"\n")
    cprint("=================================",'cyan')
    sleep(3)
  #==========================#
  elif ch == "3":
    cprint("=================================",'cyan')
    try:
      text = input("\nEnter The Text For sha1 = ")
    except:
      cprint("\nBay Bay :)\n", 'yellow')
      exit()
    sha1 = hashlib.sha1()
    sha1.update(text.encode('utf-8'))
    # ------------------------#
    sleep(1)
    print("\nsha1 is ", sha1.hexdigest(), "\n")
    cprint("=================================",'cyan')
    sleep(3)

  #==========================#
  elif ch == "4":
    cprint("=================================",'cyan')
    try:
      text = input("\nEnter The Text For sha384 = ")
    except:
      cprint("\nBay Bay :)\n", 'yellow')
      exit()
    sha384 = hashlib.sha384()
    sha384.update(text.encode('utf-8'))
    #------------------------#
    sleep(1)
    print("\nsha384 is ", sha384.hexdigest(), "\n")
    cprint("=================================",'cyan')
    sleep(3)
  #==========================#
  elif ch == "5":
    cprint("=================================",'cyan')
    try:
      text = input("\nEnter The Text For sha256 = ")
    except:
      cprint("\nBay Bay :)\n", 'yellow')
      exit()
    sha256 = hashlib.sha256()
    sha256.update(text.encode('utf-8'))
    #------------------------#
    sleep(1)
    print("\nsha256 is ", sha256.hexdigest(), "\n")
    cprint("=================================",'cyan')
    sleep(3)
  #==========================#
  elif ch == "6":
    cprint("=================================",'cyan')
    try:
      text = input("\nEnter The Text For sha224 = ")
    except:
      cprint("\nBay Bay :)\n", 'yellow')
      exit()
    sha224 = hashlib.sha224()
    sha224.update(text.encode('utf-8'))
    # ------------------------#
    sleep(1)
    print("\nsha224 is ", sha224.hexdigest(), "\n")
    cprint("=================================",'cyan')
    sleep(3)
  #==========================#
  elif ch == "7":
    cprint("=================================",'cyan')
    try:
      text = input("\nEnter The Text For sha512 = ")
    except:
      cprint("\nBay Bay :)\n", 'yellow')
      exit()
    sha512 = hashlib.sha512()
    sha512.update(text.encode('utf-8'))
    # ------------------------#
    sleep(1)
    print("\nsha512 is ", sha512.hexdigest(), "\n")
    cprint("=================================",'cyan')
    sleep(3)
    # ==========================#
  elif ch == "8":
    cprint("=================================",'cyan')
    try:
      text = input("\nEnter The Text For Hex = ")
      dk = hashlib.pbkdf2_hmac(text, b'password', b'salt', 100000)
    except ValueError:
      sleep(.5)
      cprint("\nError !  unsupported hash type\n" , 'red')
      exit()
    except:
      cprint("\nBay Bay :)\n", 'yellow')
      exit()
    # ------------------------#
    sleep(1)
    print("\nHex is ", dk.hex(), "\n")
    cprint("=================================",'cyan')
    sleep(3)
   # ==========================#
  elif ch == "9":
    cprint("=================================",'cyan')
    try:
      text = input("\nEnter The Text For blake2b = ")
    except:
      cprint("\nBay Bay :)\n", 'yellow')
      exit()
    h = blake2b()
    h.update(text.encode('utf-8'))
    # ------------------------#
    sleep(1)
    print("\nblake2b is ", h.hexdigest(), "\n")
    cprint("=================================",'cyan')
    sleep(3)
  elif ch == "10":
    cprint("\nBay Bay :)\n" , 'yellow')
    exit()
  else:
    sleep(.5)
    os.system("clear")  # windows => os.system("cls")
    cprint ("\nPlease enter the correct option !\n" , 'red')
