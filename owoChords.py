import pyautogui
import time
import keyboard
import sys

__header1__ = r"""
______________________________________________________/\\\\\\\\\__/\\\________/\\\_______/\\\\\_________/\\\\\\\\\______/\\\\\\\\\\\\________/\\\\\\\\\\\___        
 ___________________________________________________/\\\////////__\/\\\_______\/\\\_____/\\\///\\\_____/\\\///////\\\___\/\\\////////\\\____/\\\/////////\\\_       
  _________________________________________________/\\\/___________\/\\\_______\/\\\___/\\\/__\///\\\__\/\\\_____\/\\\___\/\\\______\//\\\__\//\\\______\///__      
   _____/\\\\\_____/\\____/\\___/\\_____/\\\\\_____/\\\_____________\/\\\\\\\\\\\\\\\__/\\\______\//\\\_\/\\\\\\\\\\\/____\/\\\_______\/\\\___\////\\\_________     
    ___/\\\///\\\__\/\\\__/\\\\_/\\\___/\\\///\\\__\/\\\_____________\/\\\/////////\\\_\/\\\_______\/\\\_\/\\\//////\\\____\/\\\_______\/\\\______\////\\\______    
     __/\\\__\//\\\_\//\\\/\\\\\/\\\___/\\\__\//\\\_\//\\\____________\/\\\_______\/\\\_\//\\\______/\\\__\/\\\____\//\\\___\/\\\_______\/\\\_________\////\\\___   
      _\//\\\__/\\\___\//\\\\\/\\\\\___\//\\\__/\\\___\///\\\__________\/\\\_______\/\\\__\///\\\__/\\\____\/\\\_____\//\\\__\/\\\_______/\\\___/\\\______\//\\\__  
       __\///\\\\\/_____\//\\\\//\\\_____\///\\\\\/______\////\\\\\\\\\_\/\\\_______\/\\\____\///\\\\\/_____\/\\\______\//\\\_\/\\\\\\\\\\\\/___\///\\\\\\\\\\\/___ 
        ____\/////________\///__\///________\/////___________\/////////__\///________\///_______\/////_______\///________\///__\////////////_______\///////////_____"""

__header2__ = r"""         ____________________________________________________________________________________________________________________________________________________________
          ______/\\\________/\\\______________/\\\\\\\\\_____________/\\\\\\\\\\\\\\\_________________________________________________________________________________           
           _____\/\\\_______\/\\\____________/\\\///////\\\__________\/\\\///////////__________________________________________________________________________________          
            _____\//\\\______/\\\____________\///______\//\\\_________\/\\\_____________________________________________________________________________________________         
             ______\//\\\____/\\\_______________________/\\\/__________\/\\\\\\\\\\\\____________________________________________________________________________________        
              _______\//\\\__/\\\_____________________/\\\//____________\////////////\\\__________________________________________________________________________________       
               ________\//\\\/\\\___________________/\\\//__________________________\//\\\_________________________________________________________________________________      
                _________\//\\\\\__________________/\\\/__________________/\\\________\/\\\_________________________________________________________________________________     
                 __________\//\\\__________________/\\\\\\\\\\\\\\\__/\\\_\//\\\\\\\\\\\\\/__________________________________________________________________________________    
                  ___________\///__________________\///////////////__\///___\/////////////____________________________________________________________________________________   """

# noinspection SpellCheckingInspection
text = "GameChords'un isteği üzerine yapılmıştır."

print(__header1__)
print(__header2__)
print("")
print("")
print("")
print("")
print("")
time.sleep(1.5)
print("owoChords v2.5")
time.sleep(1.5)
print("")
# noinspection SpellCheckingInspection
print("NOT: Botu başlattıktan sonra discord kanalına tıklamanız için 3 saniyeniz var ve")
# noinspection SpellCheckingInspection
print("botu kullanırken başka bir yere tıklarsanız oraya yazacaktır dikkatli olun.")
time.sleep(1.5)
print("")
print("")
# noinspection SpellCheckingInspection
print("Battle / Hunt Botunu başlatmak için    'Scroll Lock'")
time.sleep(1.5)
print("")
# noinspection SpellCheckingInspection
print("Pray Botunu başlatmak için             'Home'")
time.sleep(1.5)
print("")
# noinspection SpellCheckingInspection
print("İki botu da başlatmak için             'Insert'")
time.sleep(1.5)
print("")
# noinspection SpellCheckingInspection
print("Botu Durdurmak için                    'Escape'")
time.sleep(1.5)
print("")
# noinspection SpellCheckingInspection
print("Programdan çıkmak için                 'CTRL+C'")
time.sleep(1.5)
print("")
print("")
print('\x1B[3m' + text + '\x1B[0m')

owobhstart = False
owopraystart = False
owoallstart = False

numberofbhloops = 0
numberofprayloops = 0


def pauseall():
    global owobhstart
    global owopraystart
    global owoallstart
    owobhstart = False
    owopraystart = False
    owoallstart = False
    print("")
    print("Duraklatıldı.")
    print("Devam etmek için isteğiniz botu tekrar başlatınız, kaldığınız yerden devam edeceksiniz.")
    print("")


def closeall():
    global owobhstart
    global owopraystart
    global owoallstart
    owobhstart = False
    owopraystart = False
    owoallstart = False
    print("")
    print("Kapatılıyor...")
    time.sleep(2)
    print("")
    print("")
    print("")
    print(__header1__)
    print(__header2__)
    time.sleep(5)
    print("")
    input("Kapatmak için Enter'a basın...")
    sys.exit()


def owopray():
    global numberofprayloops
    numberofprayloops = numberofprayloops + 1
    pyautogui.typewrite('owo pray')
    pyautogui.press('enter')
    print("owo Pray Tekrar Sayısı: ", numberofprayloops)


def owobh():
    global numberofbhloops
    numberofbhloops = numberofbhloops + 1
    time.sleep(3)
    pyautogui.typewrite('owo hunt')
    pyautogui.press('enter')
    pyautogui.typewrite('owo battle')
    pyautogui.press('enter')
    print("owo B/H Tekrar Sayısı: ", numberofbhloops)


try:
    while True:
        while not owobhstart and not owopraystart and not owoallstart:
            if keyboard.is_pressed('scrlk'):
                owobhstart = True
                print("")
                print("B/H Başlatıldı.")
                print("")
                break
            elif keyboard.is_pressed('home'):
                owopraystart = True
                print("")
                print("Pray Başlatıldı.")
                print("")
                break
            elif keyboard.is_pressed("insert"):
                owoallstart = True
                print("")
                print("Bütün botlar başlatıldı.")
                print("")
                break
            elif keyboard.is_pressed('ctrl+c'):
                closeall()
                break
            else:
                continue
        while owoallstart:
            owobh()
            if numberofbhloops % 25 == 0 or numberofbhloops == 1:
                owopray()
            else:
                pass
            for _ in range(120):
                time.sleep(0.1)
                if keyboard.is_pressed('esc'):
                    pauseall()
                    break
                elif keyboard.is_pressed('ctrl+c'):
                    closeall()
                    break
                else:
                    continue
        while owopraystart:
            time.sleep(3)
            owopray()
            for _ in range(2970):
                time.sleep(0.1)
                if keyboard.is_pressed('esc'):
                    pauseall()
                    break
                elif keyboard.is_pressed('ctrl+c'):
                    closeall()
                    break
                else:
                    continue
        while owobhstart:
            owobh()
            for _ in range(120):
                time.sleep(0.1)
                if keyboard.is_pressed('esc'):
                    pauseall()
                    break
                elif keyboard.is_pressed('ctrl+c'):
                    closeall()
                    break
                else:
                    continue
except KeyboardInterrupt:
    closeall()
