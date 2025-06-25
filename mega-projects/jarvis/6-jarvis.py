import webbrowser
import pyttsx3
import datetime
import google.generativeai as genai
import time

genai.configure(api_key="AIzaSyCQBCSvYEc-INbWNGTqlB56W_INWA9YxyY")  # Replace with your key

model = genai.GenerativeModel(model_name="gemini-pro")


engine =pyttsx3.init()
engine = pyttsx3.init(driverName='espeak')
engine.setProperty('rate', 150)


def speak(text):
    print(f"jarvis: {text}")
    engine.say(text)
    engine.runAndWait()
    time.sleep(len(text) * 0.015) 

def search_google(querry):
    
    speak("understood")
    webbrowser.open(f"https://www.google.com/search?q={querry}")

def gettime():
    now = datetime.datetime.now().strftime("%H:%M")

    speak(f"the current time is {now}")

def ask_gpt(question):
    try:
        prompt = f"""Act like Jarvis. Keep answers short and helpful. Question: {question}"""
        response = model.generate_content(prompt)
        return speak(response.text.strip())
    except Exception as e:
        speak("Sorry, I couldn't fetch the answer.")
        print(f"error: {e}")
def get_date():
    today = datetime.datetime.now().strftime("%A, %d %B %Y")
    speak(f"Today is {today}")

def play_song(song):
    query = song.replace(" ", "+")
    speak(f"Playing {song} on YouTube")
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")


def main():
    speak("Hello Teekam, I am Jarvis. How can I help?")
    while True:
        command = input(">>> ").strip().lower()

        if command.startswith("chat "):
            ask_gpt(command.replace("chat ", ""))
        elif command == "date":
            get_date()
        elif command =="time":
            gettime()
        elif command.startswith("play "):
            play_song(command.replace("play ", ""))
        elif command.startswith("search "):
            search_google(command.replace("search ", ""))

        elif command in ["exit", "quit"]:
            speak("by Teekam.")
            break
        else:
            speak("Sorry, I didn't understand that.")


if __name__ == "__main__":
    main()
