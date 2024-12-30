import os
import subprocess
import keyboard
import threading
import time


# My big dict!
active_piano_notes = {}

def play_sound_piano(file_path, key):    
    process = subprocess.Popen(["afplay", file_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    with lock:
        active_piano_notes[key] = process
    try:
        while keyboard.is_pressed(key):
            time.sleep(0.1)
    finally:
        process.terminate()
        with lock:
            active_piano_notes.pop(key, None)


active_keys = set()
lock = threading.Lock()

def play_sound(file_path, key):
    global active_keys
    with lock:
        if key in active_keys:
            return  # Skip if the key is already playing
        active_keys.add(key)
    try:
        process = subprocess.Popen(["afplay", file_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(0.095)
    finally:
        with lock:
            active_keys.remove(key)
def beats():
    beats = {
        "l": "Beats/beat3.wav",
        "s": "Beats/beat3.wav",
        "p": "Beats/beat5.wav",
        "q": "Beats/beat5.wav",
        ",": "Beats/beat6.wav",
        "x": "Beats/beat6.wav",
    }

    piano_keys = {
        "1": "Notes/piano1.wav",
        "2": "Notes/piano2.wav",
        "3": "Notes/piano3.wav",
        "4": "Notes/piano4.wav",
        "5": "Notes/piano5.wav",
        "6": "Notes/piano6.wav",
        "7": "Notes/piano7.wav",
        "8": "Notes/piano8.wav",
        "9": "Notes/piano9.wav",
        "0": "Notes/piano10.wav",
    }


    print("Piano keys: 1-0 (Hold to play note).")
    print("Beat controls: 'l'/'s' (drum), 'p'/'q' (kick), ','/'x' (buzz beat).")
    print("Press 'b' to quit.")

    while True:
        try:
            # Check for beats
            for key, beat in beats.items():
                if keyboard.is_pressed(key):
                    threading.Thread(target=play_sound, args=(beat, key)).start()

            # Check for piano keys
            for key, note in piano_keys.items():
                if key not in active_piano_notes and keyboard.is_pressed(key):
                    # Start playing the note if pressed and not already active
                    threading.Thread(target=play_sound_piano, args=(note, key)).start()

            # Check for quit key
            if keyboard.is_pressed("b"):
                print("\nExiting...")
                break
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    beats()
