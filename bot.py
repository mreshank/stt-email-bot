import speech_recognition as sr
import smtplib
recognizer = sr.Recognizer()
text = ""
with sr.Microphone() as source:
    print("Clearing background noise")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Listening...")
    recordedAudio = recognizer.listen(source)
    print("Recording Done")
try:
    print("Recognizing...")
    text = recognizer.recognize_google(recordedAudio, language='en-US')
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, I could not understand your speech.")
except sr.RequestError as e:
    print("Sorry, an error occurred while processing your request:", str(e))
except Exception as e:
    print(e)

receiver = "mrpsiace@gmail.com"
message = text
sender = "contact.eshanktyagi@gmail.com"
subject = "Automated Test Email"
password = "ijljnfubflgsczfo"
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, message)