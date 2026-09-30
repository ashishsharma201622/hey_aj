import re
import subprocess


# ============================================================
# WAKE WORDS
# ============================================================

WAKE_WORDS = [
    "hey aj",
    "hey a j",
    "hey h j",
    "hey ahan",
    "hey a han",

    "aj",
    "a j",
    "a.j.",

    "ahan",
]


# ============================================================
# TEXT NORMALIZATION
# ============================================================

def normalize_text(text):
    """
    Normalize speech-to-text output so that different
    pronunciations/transcriptions can be compared reliably.
    """

    text = text.lower().strip()

    # Replace punctuation with spaces
    text = re.sub(r"[.,!?;:'\"()\[\]{}\-_/]", " ", text)

    # Remove extra whitespace
    text = " ".join(text.split())

    return text


# ============================================================
# WAKE WORD DETECTION
# ============================================================

def is_wake_word(text):
    """
    Check whether the recognized speech contains
    one of our wake words.
    """

    normalized = normalize_text(text)

    # Convert the recognized text into individual words
    words = normalized.split()

    # Check multi-word wake phrases first
    if "hey aj" in normalized:
        return True

    if "hey a j" in normalized:
        return True

    if "hey h j" in normalized:
        return True

    if "hey ahan" in normalized:
        return True

    if "hey a han" in normalized:
        return True

    # Check single-word wake words using exact words.
    # This prevents something like "project" accidentally
    # matching "aj".
    if "aj" in words:
        return True

    if "ahan" in words:
        return True

    # "a j" as two separate words
    for i in range(len(words) - 1):
        if words[i] == "a" and words[i + 1] == "j":
            return True

    return False


# ============================================================
# LISTEN
# ============================================================

def listen():
    """
    Ask Android/Termux speech recognition to listen once
    and return the recognized text.
    """

    result = subprocess.run(
        ["termux-speech-to-text"],
        capture_output=True,
        text=True
    )

    # If the command failed, show the error
    if result.returncode != 0:
        error = result.stderr.strip()

        if error:
            print(f"❌ Speech recognition error: {error}")

        return ""

    return result.stdout.strip()


# ============================================================
# SPEAK
# ============================================================

def speak(text):
    """
    Make AJ speak using Termux TTS.
    """

    print(f"🔊 AJ: {text}")

    subprocess.run([
        "termux-tts-speak",
        text
    ])


# ============================================================
# MAIN
# ============================================================

def main():

    print()
    print("================================")
    print("        🤖 HEY_AJ")
    print("================================")
    print()
    print("🎙️  Wake words:")
    print("   • Hey AJ")
    print("   • AJ")
    print("   • Ahan")
    print("   • Hey Ahan")
    print()
    print("👂 Listening...")
    print()

    while True:

        try:

            # ------------------------------------------------
            # LISTEN
            # ------------------------------------------------

            text = listen()

            if not text:
                continue

            # ------------------------------------------------
            # DISPLAY WHAT ANDROID HEARD
            # ------------------------------------------------

            print(f"👂 Heard: {text}")

            # ------------------------------------------------
            # WAKE WORD CHECK
            # ------------------------------------------------

            if is_wake_word(text):

                print("⚡ Wake word detected!")

                # ------------------------------------------------
                # RESPONSE
                # ------------------------------------------------

                speak("Hajur papa")

                print("👂 Listening...")
                print()

        except KeyboardInterrupt:

            print()
            print("👋 hey_aj stopped.")
            break

        except Exception as e:

            print(f"❌ Error: {e}")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
