# my_ui_module.py
import tkinter as tk
from tkinter import ttk

# Global variables for UI elements
_main_button = None
_my_label = None

def setup_and_run_ui(external_button_callbacks=None):
    """
    Sets up and runs the Tkinter UI.

    Args:
        external_button_callbacks (dict, optional): A dictionary where keys are
            button numbers (1, 2, 3) and values are the functions to call
            when those buttons are clicked. If None, default behavior is used.
    """
    global _main_button, _my_label # Access global variables

    root = tk.Tk()
    root.title("My Application UI")
    root.geometry("400x250")

    _my_label = ttk.Label(root, text="Click to reveal buttons!", font=("Arial", 14))
    _my_label.pack(pady=20)

    def on_reveal_buttons_click():
        """Handles the click of the initial 'Talk to Dolphin Mistral' button."""
        global _main_button
        if _main_button:
            _main_button.pack_forget()

        button_frame = ttk.Frame(root)
        button_frame.pack(pady=10)

        # Define a generic sub-button click handler if external callbacks aren't provided
        def default_sub_button_click(button_name): # Changed to button_name for clarity with new names
            _my_label.config(text=f"'{button_name}' was clicked! (Default UI behavior)") # type: ignore
            print(f"Default '{button_name}' clicked!")

        # Create and pack Button 1 - now "Text"
        btn1_command = external_button_callbacks.get(1) if external_button_callbacks else lambda: default_sub_button_click("Text")
        btn1 = ttk.Button(button_frame, text="Text", command=btn1_command)
        btn1.pack(side=tk.LEFT, padx=5, pady=5)

        # Create and pack Button 2 - now "Voice"
        btn2_command = external_button_callbacks.get(2) if external_button_callbacks else lambda: default_sub_button_click("Voice")
        btn2 = ttk.Button(button_frame, text="Voice", command=btn2_command)
        btn2.pack(side=tk.LEFT, padx=5, pady=5)

        # Create and pack Button 3 - now "Quit"
        btn3_command = external_button_callbacks.get(3) if external_button_callbacks else lambda: default_sub_button_click("Quit")
        btn3 = ttk.Button(button_frame, text="Quit", command=btn3_command)
        btn3.pack(side=tk.LEFT, padx=5, pady=5)

        _my_label.config(text="Options displayed!") # type: ignore

    # Initial "Reveal Buttons" button renamed to "Talk to Dolphin Mistral"
    _main_button = ttk.Button(root, text="Talk to Dolphin Mistral", command=on_reveal_buttons_click)
    _main_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    print("Running UI directly (for testing purposes).")
    setup_and_run_ui()