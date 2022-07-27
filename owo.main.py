import pyautogui
import time
import keyboard
import sys

__header1__ = r"""      ___          ___                       ___                  
     /\__\        /\  \        _____        /\__\        _____    
    /:/  /       /::\  \      /::\  \      /:/ _/_      /::\  \   
   /:/  /       /:/\:\  \    /:/\:\  \    /:/ /\__\    /:/\:\  \  
  /:/  /  ___  /:/  \:\  \  /:/  \:\__\  /:/ /:/ _/_  /:/  \:\__\ 
 /:/__/  /\__\/:/__/ \:\__\/:/__/ \:|__|/:/_/:/ /\__\/:/__/ \:|__|
 \:\  \ /:/  /\:\  \ /:/  /\:\  \ /:/  /\:\/:/ /:/  /\:\  \ /:/  /
  \:\  /:/  /  \:\  /:/  /  \:\  /:/  /  \::/_/:/  /  \:\  /:/  / 
   \:\/:/  /    \:\/:/  /    \:\/:/  /    \:\/:/  /    \:\/:/  /  
    \::/  /      \::/  /      \::/  /      \::/  /      \::/  /   
     \/__/        \/__/        \/__/        \/__/        \/__/    """

__header2__ = r"""                                      ___          ___          ___                 ___          ___          ___     
     _____                           /\  \        /\__\        /\  \               /\__\        /\  \        /\  \    
    /::\  \       ___               |::\  \      /:/ _/_      /::\  \       ___   /:/  /       /::\  \       \:\  \   
   /:/\:\  \     /|  |              |:|:\  \    /:/ /\__\    /:/\:\__\     /\__\ /:/  /       /:/\:\  \       \:\  \  
  /:/ /::\__\   |:|  |            __|:|\:\  \  /:/ /:/ _/_  /:/ /:/  /    /:/  //:/  /  ___  /:/ /::\  \  _____\:\  \ 
 /:/_/:/\:|__|  |:|  |           /::::|_\:\__\/:/_/:/ /\__\/:/_/:/__/___ /:/__//:/__/  /\__\/:/_/:/\:\__\/::::::::\__\
 \:\/:/ /:/  /__|:|__|           \:\~~\  \/__/\:\/:/ /:/  /\:\/:::::/  //::\  \\:\  \ /:/  /\:\/:/  \/__/\:\~~\~~\/__/
  \::/_/:/  //::::\  \            \:\  \       \::/_/:/  /  \::/~~/~~~~/:/\:\  \\:\  /:/  /  \::/__/      \:\  \      
   \:\/:/  / ~~~~\:\  \            \:\  \       \:\/:/  /    \:\~~\    \/__\:\  \\:\/:/  /    \:\  \       \:\  \     
    \::/  /       \:\__\            \:\__\       \::/  /      \:\__\        \:\__\\::/  /      \:\__\       \:\__\    
     \/__/         \/__/             \/__/        \/__/        \/__/         \/__/ \/__/        \/__/        \/__/    """

text = "GameChords'un isteği üzerine yapılmıştır."

print(__header1__)
print(__header2__)
print("")
print("")
print("")
print("")
print("")
time.sleep(1.5)
print("owoChords v2")
time.sleep(1.5)
print("")
print("NOT: Botu başlattıktan sonra discord kanalına tıklamanız için 3 saniyeniz var ve")
print("botu kullanırken başka bir yere tıklarsanız oraya yazacaktır dikkatli olun.")
time.sleep(1.5)
print("")
print("")
print("")
print("Battle / Hunt Botunu başlatmak için    'Scroll Lock'")
time.sleep(1.5)
print("")
print("Pray Botunu başlatmak için             'Home'")
time.sleep(1.5)
print("")
print("İki botu da başlatmak için             'Insert'")
time.sleep(1.5)
print("")
print("Botu Durdurmak için                    'Escape'")
time.sleep(1.5)
print("")
print("Programdan çıkmak için                 'CTRL+C'")
time.sleep(1.5)
print("")
print("")
print("")
print('\x1B[3m' + text + '\x1B[0m')

owobhstart = False
owopraystart = False
owoallstart = False

numberofbhloops = 0
numberofprayloops = 0

try:
    while True:
        if not owobhstart:
            if keyboard.is_pressed('scrlk'):
                owobhstart = True
                print("")
                print("B/H Başlatıldı.")
                print("")
                continue
            else:
                if keyboard.is_pressed('ctrl+c'):
                    owobhstart = False
                    print("")
                    print("Kapatılıyor...")
                    time.sleep(2)
                    print("")
                    print("")
                    print("")
                    print(__header1__)
                    print(__header2__)
                    time.sleep(5)
                    sys.exit()
        if not owopraystart:
            if keyboard.is_pressed('home'):
                owopraystart = True
                print("")
                print("Pray Başlatıldı.")
                print("")
                continue
            else:
                if keyboard.is_pressed('ctrl+c'):
                    owobhstart = False
                    print("")
                    print("Kapatılıyor...")
                    time.sleep(2)
                    print("")
                    print("")
                    print("")
                    print(__header1__)
                    print(__header2__)
                    time.sleep(5)
                    sys.exit()
        if not owoallstart:
            if keyboard.is_pressed("insert"):
                owoallstart = True
                print("")
                print("Bütün botlar başlatıldı.")
                print("")
                continue
            else:
                if keyboard.is_pressed('ctrl+c'):
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
                    sys.exit()
        while owoallstart:
            numberofbhloops = numberofbhloops + 1
            time.sleep(3)
            pyautogui.typewrite('owo hunt')
            pyautogui.press('enter')
            pyautogui.typewrite('owo battle')
            pyautogui.press('enter')
            print("owo B/H Tekrar Sayısı: ", numberofbhloops)
            if numberofbhloops % 25 == 0:
                numberofprayloops = numberofprayloops + 1
                pyautogui.typewrite('owo pray')
                pyautogui.press('enter')
                print("owo Pray Tekrar Sayısı: ", numberofprayloops)
            elif numberofbhloops == 1:
                numberofprayloops = numberofprayloops + 1
                pyautogui.typewrite('owo pray')
                pyautogui.press('enter')
                print("owo Pray Tekrar Sayısı: ", numberofprayloops)

            else:
                pass
            for _ in range(120):
                time.sleep(0.1)
                if keyboard.is_pressed('esc'):
                    owoallstart = False
                    print("")
                    print("Duraklatıldı.")
                    break
                elif keyboard.is_pressed('ctrl+c'):
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
                    sys.exit()
                else:
                    continue
        while owopraystart:
            numberofprayloops = numberofprayloops + 1
            time.sleep(3)
            pyautogui.typewrite('owo pray')
            pyautogui.press('enter')
            print("owo Pray Tekrar Sayısı: ", numberofprayloops)
            for _ in range(2970):
                time.sleep(0.1)
                if keyboard.is_pressed('esc'):
                    owopraystart = False
                    print("")
                    print("Duraklatıldı.")
                    break
                elif keyboard.is_pressed('ctrl+c'):
                    owobhstart = False
                    print("")
                    print("Kapatılıyor...")
                    time.sleep(2)
                    print("")
                    print("")
                    print("")
                    print(__header1__)
                    print(__header2__)
                    time.sleep(5)
                    sys.exit()
                else:
                    continue
        while owobhstart:
            numberofbhloops = numberofbhloops + 1
            time.sleep(3)
            pyautogui.typewrite('owo hunt')
            pyautogui.press('enter')
            pyautogui.typewrite('owo battle')
            pyautogui.press('enter')
            print("owo B/H Tekrar Sayısı: ", numberofbhloops)
            for _ in range(120):
                time.sleep(0.1)
                if keyboard.is_pressed('esc'):
                    owobhstart = False
                    print("")
                    print("Duraklatıldı.")
                    break
                elif keyboard.is_pressed('ctrl+c'):
                    owobhstart = False
                    print("")
                    print("Kapatılıyor...")
                    time.sleep(2)
                    print("")
                    print("")
                    print("")
                    print(__header1__)
                    print(__header2__)
                    time.sleep(5)
                    sys.exit()
                else:
                    continue
            continue
        continue
except KeyboardInterrupt:
    print("")
    print("Kapatılıyor...")
    time.sleep(2)
    print("")
    print("")
    print("")
    print(__header1__)
    print(__header2__)
    time.sleep(5)
    sys.exit()
