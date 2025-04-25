from langdetect import detect
from googletrans import Translator

#create translator
translator = Translator()

language_names={"en":"English",
                    "es":"Spanish(Español)",
                    "zh-tw":"Chinese (Traditional)",
                    "zh-cn": "Chinese (Original)",
                    "tl":"Talalog (Filipinio)",
                    "vi":"(Vitenamese)"}

language_choices={"en":"English",
                    "es":"Spanish(Español)",
                    "zh-tw":"Chinese (Traditional)",
                    "zh-cn": "Chinese (Original)",
                    "tl":"Talalog (Filipinio)",
                    "vi":"(Vitenamese)"}

#greeting user
originaltext=input("hello, what would you like to translate? ")

#detecting language
#there is a try function where the program tries to detect, if it cannot it will tell the user to try again


