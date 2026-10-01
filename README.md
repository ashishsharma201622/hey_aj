# 🤖 hey_AJ

> **A lightweight, voice-activated personal AI assistant for Android — built from the ground up with Python and Termux.**

**hey_AJ** is an experimental personal voice assistant designed to turn an Android phone into a hands-free AI interface.

The project starts with a simple idea:

> **Say “Hey AJ” — and AJ wakes up.**

Instead of continuously processing everything the microphone hears, `hey_AJ` listens for specific wake words and activates only when one is detected.

---

## ✨ Current Features

### 🎙️ Voice Wake-Word Detection

The assistant continuously listens using Android's speech-to-text capability through Termux.

Supported wake words currently include:

* **Hey AJ**
* **AJ**
* **Ahan**

The wake-word system is designed to tolerate natural variations in speech rather than requiring one exact phrase.

Example:

```text
👂 Heard: hey
👂 Heard: aj
⚡ Wake word detected!
```

---

### 📱 Built for Android + Termux

The project runs directly on an Android phone using:

* Python
* Termux
* Termux:API
* Android speech recognition

No dedicated server or powerful computer is required for the basic listener.

---

### 🧠 Designed as the Foundation of a Personal AI

`hey_AJ` is not intended to remain just a wake-word detector.

The long-term goal is to build a personal AI system that can:

```text
🎙️ Voice
   ↓
👂 Wake-word detection
   ↓
🧠 AI reasoning
   ↓
🔧 Tools / actions
   ↓
💬 Voice response
```

Eventually, AJ should be able to understand natural requests, use external tools, interact with computers, retrieve information, automate tasks, and respond conversationally.

---

## 🏗️ Current Architecture

```text
                    📱 Android Phone
                           │
                           ▼
                    ┌─────────────┐
                    │   Termux    │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   Python    │
                    │   Listener  │
                    └──────┬──────┘
                           │
                           ▼
                 🎙️ Android Speech-to-Text
                           │
                           ▼
                    ┌─────────────┐
                    │ Wake Word   │
                    │ Detection   │
                    └──────┬──────┘
                           │
                    Wake word found
                           │
                           ▼
                    ⚡ AJ ACTIVATED
                           │
                           ▼
                 Future AI / Tool Layer
```

---

## 📂 Project Structure

```text
hey_aj/
│
├── app/
│   └── main.py
│
├── scripts/
│   └── ...
│
├── tests/
│   └── ...
│
├── requirements.txt
├── README.md
└── .gitignore
```

### `app/`

Core application code.

### `scripts/`

Helper and setup scripts.

### `tests/`

Testing and experimentation.

### `requirements.txt`

Python dependencies used by the project.

---

## 🚀 Getting Started

### 1. Install Termux

Install Termux from a trusted source such as F-Droid or the official Termux project.

Then update packages:

```bash
pkg update && pkg upgrade
```

---

### 2. Install Python

```bash
pkg install python
```

Check:

```bash
python --version
```

---

### 3. Install Termux:API

Install the **Termux:API** Android application and the Termux API package:

```bash
pkg install termux-api
```

The Android Termux:API application must also be installed and granted the required permissions.

---

### 4. Clone the repository

```bash
git clone https://github.com/ashishsharma201622/hey_aj.git
```

Enter the project:

```bash
cd hey_aj
```

---

### 5. Install Python dependencies

```bash
pip install -r requirements.txt
```

---

### 6. Run AJ

```bash
python app/main.py
```

You should see:

```text
🤖 hey_AJ is listening...
```

Speak naturally.

For example:

```text
Hey AJ
```

or:

```text
AJ
```

or:

```text
Ahan
```

When detected:

```text
⚡ Wake word detected!
```

---

## 🎯 Roadmap

`hey_AJ` is intentionally being developed in stages.

### ✅ Phase 1 — Voice Listener

* [x] Python listener
* [x] Termux integration
* [x] Android speech-to-text
* [x] Wake-word detection
* [x] Multiple wake words
* [x] Basic project structure
* [x] GitHub repository

### 🚧 Phase 2 — Conversation

* [ ] Capture the user's complete command after wake-up
* [ ] Natural-language command detection
* [ ] AI model integration
* [ ] Conversation context
* [ ] Voice responses
* [ ] Better speech recognition handling

### 🔜 Phase 3 — Personal AI

* [ ] Personal memory
* [ ] Tool calling
* [ ] Web research
* [ ] File access
* [ ] Computer control
* [ ] Android automation
* [ ] Personal dashboard
* [ ] Background operation

### 🚀 Phase 4 — Autonomous AJ

The long-term experiment:

```text
        "Hey AJ..."
              │
              ▼
       🎙️ Understand me
              │
              ▼
       🧠 Think / Reason
              │
              ▼
       🔧 Choose a tool
              │
       ┌──────┼──────┐
       ▼      ▼      ▼
     Phone   PC     Web
       │      │      │
       └──────┼──────┘
              ▼
        ⚙️ Do the task
              │
              ▼
        🔊 Tell me
```

The goal is to move from a **voice-triggered program** toward a **personal AI agent**.

---

## 🧪 Why Build This?

Most voice assistants are designed as finished products.

`hey_AJ` is different.

It is an experiment in building a personal assistant **from the lowest practical layer upward**.

Instead of starting with:

> “What can an existing assistant do?”

the project starts with:

> **“What would my own AI assistant look like if I built it myself?”**

The phone becomes the interface.

The AI becomes the brain.

Tools become the hands.

And the wake word becomes the doorway.

---

## 🔐 Privacy

The project is designed with privacy and local control in mind.

The basic wake-word listener runs locally on the Android device.

AI/cloud services may be introduced in later stages when required for advanced capabilities.

---

## 🛠️ Technology

| Technology      | Purpose                          |
| --------------- | -------------------------------- |
| 🐍 Python       | Core application                 |
| 📱 Android      | Primary device                   |
| 💻 Termux       | Linux-like execution environment |
| 🎙️ Termux:API  | Android speech integration       |
| 🧠 AI Models    | Planned reasoning layer          |
| 🔧 Python Tools | Planned automation layer         |
| 🌐 APIs         | Planned external integrations    |

---

## 📌 Project Status

**Experimental / actively developing**

This project is intentionally evolving.

The current implementation is small, but the architecture is being developed toward a much larger personal AI system.

---

## 👨‍💻 Author

**Ashish Sharma**

Built as a personal AI experiment.

---

## ⭐ Vision

```text
A phone that doesn't just listen.

A phone that understands.

An AI that doesn't just answer.

An AI that acts.

        ┌───────────────┐
        │    hey_AJ     │
        └───────┬───────┘
                │
         "Hey AJ..."
                │
                ▼
        ┌───────────────┐
        │     LISTEN    │
        └───────┬───────┘
                │
                ▼
        ┌───────────────┐
        │   UNDERSTAND  │
        └───────┬───────┘
                │
                ▼
        ┌───────────────┐
        │     THINK     │
        └───────┬───────┘
                │
                ▼
        ┌───────────────┐
        │      ACT      │
        └───────┬───────┘
                │
                ▼
        ┌───────────────┐
        │      AJ       │
        └───────────────┘
```

**This is only the beginning.**
