import subprocess


WAKE_WORDS = [
    "hey aj",
    "hey a j",
    "hey h j",
    "hey h. j.",
    "aj",
    "a j",
    "a.j.",
    "ahan",
    "hey ahan",
    "hey a han",
]




def listen():
    """Listen once and return recognized speech."""
    result = subprocess.run(
        ["termux-speech-to-text"],
        capture_output=True,
        text=True
    )

    return result.stdout.strip().lower()



def is_wake_word(text):
    """Check whether the user said a wake word."""

    # Normalize punctuation
    normalized = (
        text.lower()
        .replace(".", " ")
        .replace(",", " ")
        .replace("-", " ")
    )

    # Remove extra spaces
    normalized = " ".join(normalized.split())

    for word in WAKE_WORDS:
        word = word.lower().replace(".", " ")
        word = " ".join(word.split())

        if word in normalized:
            return True

    return False
    

def speak(text):
    """Make AJ speak."""
    subprocess.run([
        "termux-tts-speak",
        text
    ])


def main():
    print("🤖 hey_aj is listening...")

    while True:
        try:
            text = listen()

            if text:
                print(f"👂 Heard: {text}")

            if is_wake_word(text):
                print("⚡ Wake word detected!")

                speak("Hajur papa")

        except KeyboardInterrupt:
            print("\n👋 hey_aj stopped.")
            break

        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
