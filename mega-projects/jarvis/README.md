#  CLI Jarvis – AI Assistant (Mistral-Powered)

A command-line virtual assistant that responds to typed commands with smart voice replies, using HuggingFace's Mistral LLM.

Created by **Teekam** as a smart, speech-enabled Python-based alternative to voice-only Jarvis systems.

---

## Features

| Command            | Description                                  |
|--------------------|----------------------------------------------|
| `ask <question>`   | Asks Mistral LLM (via HuggingFace)           |
| `date`             | Tells today’s full date                      |
| `time`             | Speaks current time                          |
| `play <song>`      | Opens YouTube to play your song              |
| `search <query>`   | Opens Google search for your query           |
| `exit` / `quit`    | Exits the assistant                          |

---

## Powered By

- [Mistral-8x7B via HuggingFace Inference API](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1)
- Python libraries:
  - `pyttsx3` for text-to-speech
  - `webbrowser` for URL opening
  - `requests` for API calls
  - `datetime` for time and date

---
