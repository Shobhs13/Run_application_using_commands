# coding: utf-8


import pyttsx3
import os


pyttsx3.speak("Welcome to Run Command")


print("\n")
print("Chat with me for you requirements: ", end='')
print("\n")

print("Enter the choice: ")
p = input()
#print(p)
#os.system(p)

if ("run" in p) or ("execute" in p) and ("chrome" in p):
    os.system("chrome")
    
elif (("run" in p) or ("execute" in p)) and (("notepad" in p) or ("editor" in p)):
    os.system("notepad")
    
elif ("run" in p) or ("execute" in p) and ("brave" in p):
    os.system("brave")
    
else:
    print("Don't support")
    




