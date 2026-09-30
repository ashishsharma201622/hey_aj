
import subprocess

print("🤖 hey_aj is listening...")

while True:
    try:
        result = subprocess.run(
            ["termux-speech-to-text"],
            capture_output=True,
            text=True
        )

        text = result.stdout.strip().lower()

        if text:
            print(f"👂 Heard: {text}")

        if "hey aj" in text or "hey h j" in text or "hey a j" in text:
            print("⚡ Wake word detected!")

            subprocess.run([
                "termux-tts-speak",
                "Hajur papa"
            ])

    except KeyboardInterrupt:
        print("\n👋 hey_aj stopped.")
        break

    except Exception as e:
        print(f"❌ Error: {e}")
