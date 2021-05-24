
import pyautogui
import webbrowser as wb
import time
# To Make sure the program runs perfectly you need to:
# i) Have logged in to WhatsApp earlier on the same device through Chrome
# ii) Chrome is open in Background
# iii) As WhatsApp loads click on the profile you wish to send the message and wait 30 seconds
# iv) Make sure Caps Lock isn't ON
n = int(input("Enter the number of times you wish to print: "))
text = input("Enter the text you wish to send: ")
wb.open("https://web.whatsapp.com/")
time.sleep(30)
for j in range(n):
    for k in range(len(text)):
        pyautogui.press(text[k])
    pyautogui.press("enter")
