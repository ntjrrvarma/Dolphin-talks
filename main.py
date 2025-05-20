import asyncio
from ollama import AsyncClient
import speech_recognition as sr
import pyttsx3
import run

def get_input():
    """
    Gets user input either from text or voice.

    Returns:
        str: The user's input as text.
    """
    while True:
        source = input("Enter 'text' for text input, 'voice' for voice input, or 'exit' to quit: ").lower()
        if source == 'text':
            return input("Enter your text prompt: ")
        elif source == 'voice':
            recognizer = sr.Recognizer()
            microphone = sr.Microphone()
            with microphone:
                print("Speak now...")
                audio = recognizer.listen(microphone)
            try:
                text = recognizer.recognize_google(audio)  # type: ignore[attr-defined]  # You can change the recognizer
                print(f"You said: {text}")
                return text
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
        elif source == 'exit':
            return None  # Signal to exit the main loop
        else:
            print("Invalid input. Please enter 'text' or 'voice'.")

def speak_response(text):
    """
    Converts the given text to speech using pyttsx3.

    Args:
        text (str): The text to be spoken.
    """
    engine = pyttsx3.init()
    # Change the voice here
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # You can change the index (0, 1, etc.) to select a different voice
    engine.say(text)
    engine.runAndWait()

async def chat_with_dolphin(prompt):
    """
    Sends a prompt to the Dolphin language model using Ollama and prints the response.

    Args:
        prompt (str): The user's input prompt.
    """
    try:
        message = {"role": "user", "content": prompt}
        response = ""
        async for part in await AsyncClient().chat(model="dolphin-mistral:7b", messages=[message], stream=True):
            chunk = part['message']['content']
            response += chunk
        speak_response(response) # Convert the LLM response to speech
    except Exception as e:
        print(f"An error occurred: {e}")

async def main():
    """
    Main function to run the chat interaction with the Dolphin model.
    """
    while True:
        user_input = get_input()
        if user_input is None:
            break
        await chat_with_dolphin(user_input)

if __name__ == "__main__":
    asyncio.run(main())