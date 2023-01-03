from osint import Osint

steam = Osint()
total = 0
def percentage(value):
    return round((value / total) * 100)
print("""
:'######::'########:'########::::'###::::'##::::'##:
'##... ##:... ##..:: ##.....::::'## ##::: ###::'###:
 ##:::..::::: ##:::: ##::::::::'##:. ##:: ####'####:
. ######::::: ##:::: ######:::'##:::. ##: ## ### ##:
:..... ##:::: ##:::: ##...:::: #########: ##. #: ##:
'##::: ##:::: ##:::: ##::::::: ##.... ##: ##:.:: ##:
. ######::::: ##:::: ########: ##:::: ##: ##:::: ##:
:......::::::..:::::........::..:::::..::..:::::..::
:'#######:::'######::'####:'##::: ##:'########:
'##.... ##:'##... ##:. ##:: ###:: ##:... ##..::
 ##:::: ##: ##:::..::: ##:: ####: ##:::: ##::::
 ##:::: ##:. ######::: ##:: ## ## ##:::: ##::::
 ##:::: ##::..... ##:: ##:: ##. ####:::: ##::::
 ##:::: ##:'##::: ##:: ##:: ##:. ###:::: ##::::
. #######::. ######::'####: ##::. ##:::: ##::::
:.......::::......:::....::..::::..:::::..:::::
""")
print("paste the steamID of the user you want to attack")
print("\033[31mwarning: friend list must be public  \033[m \n")

token = str(input("TOKEN: "))
idProfile = str(input("STEAM ID: "))

while True:
    try:
        scan = steam.scanProfile(idProfile, token)
        for eachClose in steam.closeFriends():
            if eachClose["accuracy"] > total:
                total = eachClose["accuracy"]
        for each in steam.closeFriends():
            if percentage(each["accuracy"]) >= 10 and percentage(each["accuracy"]) < 25:
                print(f'[+] \033[31m{each["profile"]}\n Accuracy: {percentage(each["accuracy"])}% \033[m \n')
            elif percentage(each["accuracy"]) >= 25 and percentage(each["accuracy"]) < 50:
                print(f'[+] \033[33m{each["profile"]}\n Accuracy: {percentage(each["accuracy"])}% \033[m \n')
            elif percentage(each["accuracy"])>= 50 and percentage(each["accuracy"]) <= 100:
                print(f'[+] \033[92m{each["profile"]}\n Accuracy: {percentage(each["accuracy"])}% \033[m \n')
    except:
        print("\033[31m check if friends list is public, steamID is valid  or Token \033[m \n")
    keeping = str(input("do you wish to STOP?: [Y] \n")).capitalize()
    if keeping == "Y":
        break;
    else:
        idProfile = str(input("STEAM ID: "))