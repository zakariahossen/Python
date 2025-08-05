import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
from playsound import playsound
import asyncio

# Voice Input → Text
def listen(lang_code):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now...")
        audio = r.listen(source)

    input("📥 Press Enter to process...")

    try:
        text = r.recognize_google(audio, language=lang_code)
        print(f"✅ You said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Couldn't understand, please try again.")
        return None

# Text → Translated Text
async def translate_text(text, dest_lang):
    translator = Translator()
    result = await translator.translate(text, dest=dest_lang)
    print(f"🌐 Translation: {result.text}")
    return result.text

# Text → Voice Output
def speak(text, lang_code):
    tts = gTTS(text=text, lang=lang_code)
    filename = "output.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

# Language Maps
lang_map = {
    "bn": "en",
    "en": "bn"
}

speak_lang = {
    "bn": "bn",
    "en": "en"
}

# Main Program
async def main():
    while True:
        print("\n🌐 Select translation direction: ")
        print("1. Bangla → English")
        print("2. English → Bangla")
        choice = input("👉 Your choice (1/2): ")

        if choice == "1":
            input_lang = "bn"
        elif choice == "2":
            input_lang = "en"
        else:
            print("❗Invalid input")
            continue

        spoken_text = listen(input_lang)
        if spoken_text:
            translated = await translate_text(spoken_text, lang_map[input_lang])
            speak(translated, speak_lang[lang_map[input_lang]])

# Run it
if __name__ == "__main__":
    asyncio.run(main())
