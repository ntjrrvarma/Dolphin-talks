import tkinter as tk
from tkinter import ttk
import subprocess

def main():
    """
    Main function to run the chat interaction with the Dolphin model.
    """

    def run_core_program():
        """
        Runs the main.py program in a separate process.
        """
        try:
            # Pass a parameter to main.py using an argument
            process = subprocess.Popen(["python", "main.py"])  # Changed to main.py and added argument
            print("Core program started with --from_ui argument.")

        except Exception as e:
            print(f"Error starting core program: {e}")

    root = tk.Tk()
    root.title("Dolphin Chat Interface")

    # Set a more modern theme
    ttk.Style(root).theme_use('clam')

    # Initial button to run the core program
    core_button = ttk.Button(root, text="Run Core Program", command=run_core_program, padding=10)
    core_button.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
    root.columnconfigure(0, weight=1)

    #  run the tkinter mainloop in the main thread
    root.mainloop()


if __name__ == "__main__":
    main()
