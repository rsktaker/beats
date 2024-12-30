# Bummy Beat Machine

The Bummy Beat Machine (BBM) was created because I love to tap my fingers against things in a rhythm. Unfortunately, I failed to foresee that the BBM would produce TWO sounds (one keyboard click and the other computer-generated), throwing me off my flow.

Looks like we'll have to procure better hardware to create a true, rsk-approved beat machine.

*Only Supports MacOS

## Demo

[![Watch the video](https://img.youtube.com/vi/jssngNc-K-A/hqdefault.jpg)](https://www.youtube.com/watch?v=jssngNc-K-A)

## Origins

It started with a few .wav files from [FreeWaveSamples](https://freewavesamples.com/) (also where I got the beats for Beats) and this addition to .bashrc:
```bash
function beats {
  local beat3="beat3.wav"
  local beat5="beat5.wav"
  local beat6="beat6.wav"

  while true; do
    read -n 1 -s key
    if [[ "$key" == "l" || "$key" == "s" ]]; then
      (afplay "$beat3" &)
    elif [[ "$key" == "p" || "$key" == "q" ]]; then
      (afplay "$beat5" &)
    elif [[ "$key" == "m" || "$key" == "x" ]]; then
      (afplay "$beat6" &)
    elif [[ "$key" == "0" ]]; then
      echo "Exiting..."
      break
    fi
  done

}
```
I was happy enough, but then I wanted a piano. And I couldn't find a 20s sample of each note! So I created my own piano notes with some sine waves and used threading to add some concurrency, and I needed Python for that.

## How to Use

First get the directory on your mac - you might need to install some stuff (like the keyboard module for python) and approve terminal to take control of your keyboard.

Then run ```sudo python3 beats.py``` and enjoy!

