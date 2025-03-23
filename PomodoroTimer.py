import tkinter as tk
from tkinter import messagebox
import time
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Function to play a soothing tune
def play_tune():
    try:
        pygame.mixer.music.load("tune.wav")  # Replace with your audio file
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():  # Wait for the music to finish playing
            time.sleep(0.1)
    except Exception as e:
        print(f"Error playing tune: {e}")

# Function to show a creative popup
def show_creative_popup():
    popup = tk.Toplevel(root)
    popup.title("Time's Up! ⏰")
    popup.geometry("300x150")  # Set popup size
    popup.configure(bg="#FFD1DC")  # Light pink background

    # Add a colorful label with emojis
    label = tk.Label(
        popup,
        text="🎉 Time's Up! 🎉\nTake a break! ☕",
        font=("Helvetica", 16, "bold"),
        bg="#FFD1DC",  # Light pink background
        fg="#D32F2F",  # Dark red text color
    )
    label.pack(pady=20)

    # Add a close button
    close_button = tk.Button(
        popup,
        text="Close",
        command=popup.destroy,
        font=("Helvetica", 12, "bold"),
        bg="#FF5252",  # Red button color
        fg="#FFFFFF",  # White text color
        relief="flat",
        padx=10,
        pady=5,
    )
    close_button.pack(pady=10)

# Pomodoro timer function
def start_timer():
    try:
        # Get hours, minutes, and seconds from the input fields
        hours = int(hours_entry.get()) if hours_entry.get() else 0
        minutes = int(minutes_entry.get()) if minutes_entry.get() else 0
        seconds = int(seconds_entry.get()) if seconds_entry.get() else 0

        # Calculate total time in seconds
        total_seconds = (hours * 3600) + (minutes * 60) + seconds

        if total_seconds <= 0:
            messagebox.showerror("Error", "Please enter a valid time.")
            return

        # Start the countdown
        while total_seconds:
            hrs, remainder = divmod(total_seconds, 3600)
            mins, secs = divmod(remainder, 60)
            timer_label.config(text=f"{hrs:02d}:{mins:02d}:{secs:02d}")
            root.update()  # Update the GUI
            time.sleep(1)
            total_seconds -= 1

        timer_label.config(text="00:00:00")
        play_tune()  # Play a soothing tune
        show_creative_popup()  # Show a creative popup

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for hours, minutes, and seconds.")

# Create the main window
root = tk.Tk()
root.title("Pomodoro Timer")
root.geometry("400x350")  # Set window size
root.configure(bg="#FFE6EE")  # Light pink background color

# Custom fonts
label_font = ("Helvetica", 14, "bold")
entry_font = ("Helvetica", 12)
button_font = ("Helvetica", 14, "bold")
timer_font = ("Helvetica", 48, "bold")

# Create a frame for the timer display
timer_frame = tk.Frame(root, bg="#FFE6EE")
timer_frame.pack(pady=20)

# Timer display
timer_label = tk.Label(
    timer_frame,
    text="00:00:00",
    font=timer_font,
    bg="#FFE6EE",  # Light pink background
    fg="#880E4F",  # Dark pink text color
)
timer_label.pack()

# Create a frame for the input fields
input_frame = tk.Frame(root, bg="#FFE6EE")
input_frame.pack(pady=10)

# Hours input
tk.Label(
    input_frame,
    text="Hours:",
    font=label_font,
    bg="#FFE6EE",
    fg="#880E4F",
).grid(row=0, column=0, padx=5, pady=5)
hours_entry = tk.Entry(
    input_frame,
    font=entry_font,
    bg="#FFFFFF",  # White background for input field
    fg="#880E4F",  # Dark pink text color
    insertbackground="#880E4F",  # Cursor color
    relief="flat",
    width=5,
)
hours_entry.grid(row=0, column=1, padx=5, pady=5)

# Minutes input
tk.Label(
    input_frame,
    text="Minutes:",
    font=label_font,
    bg="#FFE6EE",
    fg="#880E4F",
).grid(row=1, column=0, padx=5, pady=5)
minutes_entry = tk.Entry(
    input_frame,
    font=entry_font,
    bg="#FFFFFF",
    fg="#880E4F",
    insertbackground="#880E4F",
    relief="flat",
    width=5,
)
minutes_entry.grid(row=1, column=1, padx=5, pady=5)

# Seconds input
tk.Label(
    input_frame,
    text="Seconds:",
    font=label_font,
    bg="#FFE6EE",
    fg="#880E4F",
).grid(row=2, column=0, padx=5, pady=5)
seconds_entry = tk.Entry(
    input_frame,
    font=entry_font,
    bg="#FFFFFF",
    fg="#880E4F",
    insertbackground="#880E4F",
    relief="flat",
    width=5,
)
seconds_entry.grid(row=2, column=1, padx=5, pady=5)

# Create a frame for the button
button_frame = tk.Frame(root, bg="#FFE6EE")
button_frame.pack(pady=20)

# Start button with rounded corners
start_button = tk.Button(
    button_frame,
    text="Start Timer",
    command=start_timer,
    font=button_font,
    bg="#F48FB1",  # Soft pink button color
    fg="#880E4F",  # Dark pink text color
    activebackground="#FF80AB",  # Brighter pink when clicked
    activeforeground="#880E4F",
    relief="flat",
    padx=20,
    pady=10,
    borderwidth=0,
    highlightthickness=0,
    bd=0,
)
start_button.pack()

# Run the application
root.mainloop()