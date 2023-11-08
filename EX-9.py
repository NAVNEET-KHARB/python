import win32com.client as wcl
l = ["Navneet", "Shivani", "Vani", "Manish"]
voice = wcl.Dispatch("SAPI.SpVoice")
for i in l:
    voice.Speak(f"Shoutout to {i}")
