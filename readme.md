# Dolphin Chat Interface

## Overview

The Dolphin Chat Interface is a Python application that offers a simple graphical user interface (GUI) for interacting with the **Ollama language model**. It allows you to send prompts and receive responses, supporting both **text-based** and **voice-based** input.

## Features

* **Text Input:** Type your prompts directly using the keyboard.
* **Voice Input:** Speak your prompts into a microphone, and the application will transcribe them.
* **Ollama Integration:** Seamlessly communicates with the Ollama language model to generate responses.
* **Voice Output:** The LLM's responses are spoken aloud by the application.
* **Simple GUI:** An intuitive interface with clear buttons for selecting input mode and exiting.

---

## Requirements

* **Python 3.x**
* **Libraries:**
    * `aiohttp`
    * `asyncio`
    * `ollama`
    * `SpeechRecognition`
    * `pyttsx3`
    * `tkinter` (usually included with Python, but might require separate installation on some systems)
    * `Pillow`

---

## Installation

1.  **Install Python 3.x** on your system.
2.  **Clone this repository** (replace `<repository_url>` with your actual repository URL):

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

3.  **Create a virtual environment** (recommended for dependency isolation):

    ```bash
    python -m venv venv
    # Activate the virtual environment:
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows (Command Prompt)
    .\venv\Scripts\Activate.ps1 # On Windows (PowerShell)
    ```

4.  **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

    * **Note for `tkinter`:** While `tkinter` often comes with Python, some **Linux distributions** may require a separate system-level package installation. For example:
        * **Debian/Ubuntu:** `sudo apt-get install python3-tk`
        * **Fedora/CentOS/RHEL:** `sudo dnf install python3-tkinter` (or `python36-tkinter` for Python 3.6)
        * **Arch Linux:** `sudo pacman -S tk`

5.  **Set up Ollama:**
    * Ensure **Ollama is installed and running** on your system (download from [ollama.com](https://ollama.com/)).
    * **Pull the `dolphin-mistral:7b` model** (if you haven't already):

        ```bash
        ollama run dolphin-mistral:7b
        # You can type /bye to exit the chat session after the model is downloaded.
        ```

---

## Usage

1.  **Run the application:**

    ```bash
    python main.py
    ```

2.  The **Dolphin Chat Interface GUI window** will appear.

3.  **Interact using the buttons:**

    * **Text Input:** Click this button, then type your prompt in the terminal where you ran the script and press Enter. The application will speak the LLM's response.
    * **Voice Input:** Click this button, then speak into your microphone when prompted in the terminal. Your speech will be transcribed, sent to the LLM, and its response will be spoken aloud.
    * **Exit:** Click this button to close the application.

---

## Configuration

* Confirm your **Ollama server is running** and accessible (defaults to `http://localhost:11434`).
* A **microphone** is essential for voice input.
* **Speakers or headphones** are needed for voice output.

---

## Troubleshooting

* **No speech detected / Could not understand audio:**
    * Check your microphone connection and ensure it's not muted.
    * Verify your operating system's sound input settings.
    * Speak clearly and at a normal volume.
* **No voices available:**
    * `pyttsx3` relies on your OS's built-in text-to-speech engine. Ensure these features are installed and enabled in your system settings (e.g., Windows Speech settings, macOS Spoken Content).
    * On Linux, you might need to install a TTS engine like `espeak` (`sudo apt-get install espeak`).
* **Application freezes:**
    * Check the terminal for any error messages.
    * Confirm your Ollama server is still running and responsive.
    * Verify your internet connection if speech recognition or model downloads are active.
* **Error loading `microphone.png`:**
    * Make sure `microphone.png` is in the same directory as `main.py`, or update its path in the code.
    * Ensure the `Pillow` library is installed (`pip install Pillow`).
    * If you don't need the icon, you can remove the related image loading lines from `main.py`.
* **`tkinter` installation errors (e.g., "No matching distribution found for tkinter"):**
    * This typically means `tkinter` isn't properly installed or linked to your Python environment.
    * **Verify Python Installation:** Ensure you have a complete Python 3.x installation.
    * **Check in Python Shell:** Run `python3 -c "import tkinter; print('tkinter is installed')"` in your terminal. If it fails, `tkinter` is not found.
    * **Linux Specific:** As mentioned in the Installation section, `tkinter` is usually a system package. Use your distribution's package manager (e.g., `sudo apt-get install python3-tk`).
    * **Reinstall Python:** For Windows/macOS, a full Python reinstallation (ensuring `tk` support is selected during installation) can often fix this.
    * **Virtual Environment:** If using a virtual environment, try creating a new one.

---

## Dependencies

* `aiohttp`: For asynchronous HTTP communication with Ollama.
* `asyncio`: For handling asynchronous operations in Python.
* `ollama`: The Python client for the Ollama API.
* `SpeechRecognition`: To convert spoken words into text.
* `pyttsx3`: To convert text responses into spoken words.
* `tkinter`: Python's standard GUI (Graphical User Interface) toolkit.
* `Pillow`: For image manipulation (used for the microphone icon).

---

## License

This project is licensed under the \[License Name] License.

---

## Author

Rahul / @ntjrrvarma
