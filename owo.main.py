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

print("owo battle ve hunt botuna hoş geldiniz.")
time.sleep(2)
print("")
print("NOT: Botu başlattıktan sonra discord kanalına tıklamanız için 3 saniyeniz var ve")
print("botu kullanırken başka bir yere tıklarsanız oraya yazacaktır dikkatli olun.")
time.sleep(2)
print("")
print("Botu başlatmak için 'scrlk'(scroll lock) tuşuna basınız.")
time.sleep(2)
print("Botu durdurmak için 'esc'(escape) tuşuna basınız.")
print("")
time.sleep(2)
print("")
print('\x1B[3m' + text + '\x1B[0m')

start = False
numbofloop = 1

try:
    while True:
        if keyboard.is_pressed('esc'):
            start = False
            print("")
            print("Durduruluyor...")
            print("")
            print("")
            print("")
            time.sleep(2)
            print(__header1__)
            print(__header2__)
            time.sleep(5)
            break
        if keyboard.is_pressed('scrlk'):
            start = True
            print("")
            print("Başlatılıyor...")
            print("")
            time.sleep(1)
            break

except KeyboardInterrupt:
    print("")
    print("Durduruluyor...")
    print("")
    print("")
    print("")
    time.sleep(2)
    print(__header1__)
    print(__header2__)
    time.sleep(5)
    sys.exit()

while start == True:
    time.sleep(3)
    print("Tekrar Sayısı:", numbofloop)
    pyautogui.typewrite('owo hunt')
    pyautogui.press('enter')
    pyautogui.typewrite('owo battle')
    pyautogui.press('enter')
    numbofloop = numbofloop + 1
    for _ in range(115):
        time.sleep(0.1)
        if keyboard.is_pressed("esc"):
            print("")
            print("Durduruluyor...")
            print("")
            print("")
            print("")
            time.sleep(2)
            print(__header1__)
            print(__header2__)
            time.sleep(5)
            sys.exit()

sys.exit()
