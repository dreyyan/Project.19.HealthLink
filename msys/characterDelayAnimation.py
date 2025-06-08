import time
# UTILITY: display text with a typing effect
def characterDelayAnimation(stringInput, seconds):
    for char in stringInput:
        print(char, end="", flush=True)
        time.sleep(seconds)
    print()