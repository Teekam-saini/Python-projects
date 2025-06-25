import webbrowser
import pyttsx3
import requests
import datetime

HF_API_KEY = "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"

engine =pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    print(f"{text}")
    engine.say(text)
    engine.runAndWait()

def search_google(querry):
    speak(f"searching for querry: {querry}")
    webbrowser.open(f"https://www.google.com/search?q={querry}")

def gettime():
    now = datetime.datetime.now().strftime("%H:%M")

    speak(f"the current time is {now}")

def ask_gpt(question):
    try:
        url = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
        headers = {
            "Authorization": f"Bearer {HF_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "inputs": f"[INST] {question} [/INST]"
        }
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

        # Extract and clean the reply
        generated = data[0]['generated_text']
        reply = generated.split('[/INST]')[-1].strip()

        speak(reply)

    except Exception as e:
        speak("Sorry, I couldn't fetch the answer.")
        print(f" Mistral Error: {e}")
def get_date():
    today = datetime.datetime.now().strftime("%A, %d %B %Y")
    speak(f"Today is {today}")

def play_song(song):
    query = song.replace(" ", "+")
    speak(f"Playing {song} on YouTube")
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")


def main():
    speak("Hello Teekam, I am Jarvis. How can I help you?")
    while True:
        command = input(">>> ").strip().lower()

        if command.startswith("ask "):
            ask_gpt(command.replace("ask ", ""))
        elif command == "date":
            get_date()
        elif command.startswith("play "):
            play_song(command.replace("play ", ""))
        elif command in ["exit", "quit"]:
            speak("by Teekam.")
            break
        else:
            speak("Sorry, I didn't understand that.")


if __name__ == "__main__":
    main()
