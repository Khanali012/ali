import os

R = "\033[1;91m"
G = "\033[1;92m"
Y = "\033[1;93m"
B = "\033[1;94m"
P = "\033[1;95m"
S = "\033[1;96m"
W = "\033[1;97m"


def clear():
   logo =(f'''    \033[1;97m##    ## ##     ##    ###    ##    ## \n    ##   ##  ##  {B}   ##   ## ##   ###   {W}## \n    ##  ##   ##     ##  ##   ##  ####  ## \n    #####    ######### ##     ## ## ## ## \n    ##  {S}##   ##     ## ######{W}### ##  #### \n    ##   ##  ##     ## ##     ## ##   ### \n    ##    ## ##     ## ##     ## ##    ## \n--------------{P}-------------------{W}---------------\n[✔] Owner   : Khan Ali\n[✔] Github  : https://github.com/Khanali012\n--------------{P}-------------------{W}---------------''')
   os.system("clear")
   print(logo) 
  
def linex():
    print("\033[1;97m-"*40)
    
clear()
print("[1] Method\n[2] Method")

chos=input("[!] Choose: ")

if chos=="1":
    os.system("chmod 777 KHANN;./KHANN")
else:
    os.system("chmod 777 KHAN60;./KHAN60")
    
    