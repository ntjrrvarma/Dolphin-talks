# run.py (unchanged, but now works with new button names)
import ui
import time

def process_button_one_from_main():
    # This function is now called when the "Text" button is clicked
    print("Main App: Executing specific logic for Text (Button 1)!")
    time.sleep(0.5)
    print("Main App: Text logic complete.")

def handle_button_two_action_from_main(data):
    # This function is now called when the "Voice" button is clicked
    print(f"Main App: Handling Voice (Button 2) action with data: {data}")
    time.sleep(0.5)
    print("Main App: Voice action complete.")

def activate_button_three_feature_from_main():
    # This function is now called when the "Quit" button is clicked
    print("Main App: Activating Quit (Button 3) feature!")
    time.sleep(0.5)
    print("Main App: Quit feature activated.")

if __name__ == "__main__":
    print("Starting main application process...")

    button_callbacks = {
        1: process_button_one_from_main,
        2: lambda: handle_button_two_action_from_main("voice_input_data"),
        3: activate_button_three_feature_from_main
    }

    print("Launching UI...")
    ui.setup_and_run_ui(external_button_callbacks=button_callbacks)
    print("UI closed. Main application process finished.")