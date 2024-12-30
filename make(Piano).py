# If you run this file it's going to make you a piano...run all your files on terminal pls its so much cooler
import numpy as np
from scipy.io.wavfile import write

# I think this func speaks for itself
def generate_sine_wave(frequency, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = np.sin(2 * np.pi * frequency * t)
    # Convert sine wave to 16-bit PCM format
    wave = (wave * 32767).astype(np.int16)  
    return wave

# Big dict!
# C4 D4 E4 F4 G4 A4 B4 C5 D5 E5
digit_frequencies = {
    "1": 261.63,
    "2": 293.66,
    "3": 329.63,
    "4": 349.23,
    "5": 392.00,
    "6": 440.00,
    "7": 493.88,
    "8": 523.25,
    "9": 587.33,
    "0": 659.25,
}

duration = 20 # if you want to play a note for MORE than 20 seconds you're a bum anyway
sample_rate = 44100  # Pretty standard quality

# Generate WAV files for each digit
for digit, frequency in digit_frequencies.items():
    print(f"Generating {digit}: {frequency} Hz")
    sine_wave = generate_sine_wave(frequency, duration, sample_rate)
    filename = f"piano{digit}.wav"
    write(filename, sample_rate, sine_wave)
    print(f"Saved {filename}")

print("All good g")
