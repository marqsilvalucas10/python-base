#!/usr/bin python3
""" Hello world """
import os 

current_language = os.getenv("LANG")[:5]
msg = "Debuqi zon de taibou"
if current_language == 'pt_BR':
    msg = "Damiao"
elif current_language == "it_IT":
    msg = "mama mia"

print(msg)
