import random
import time

def animated_hello_world():
    messages = [
        "Initializing the world's greetings...",
        "Loading happiness protocol...",
        "Spreading joy worldwide...",
        "Saying 'Hello, World!' with enthusiasm!"
    ]

    for message in messages:
        print(message)
        time.sleep(1)

    print("\n🌍 Hello, World! 🎉")
    print("The world says hi back! 🌟")

if __name__ == "__main__":
    animated_hello_world()
