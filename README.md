					 MY-SCREEN-APP





🧠 ScreenSense AI

&#x20;A Real-Time Screen-Aware AI Assistant



&#x20;📌 Project Overview



\*\*MY-SCREEN-APP (ScreenSense AI)\*\* is a real-time AI-powered desktop assistant designed to provide intelligent contextual help directly on the user's current screen without switching applications.



The application continuously works in the background and can instantly capture the current screen using a global hotkey. It then sends the screenshot along with the user's query to Google's Gemini Vision API, which analyzes the screen content and generates context-aware responses.



This project aims to reduce workflow interruption and improve productivity for developers, designers, editors, and power users.



\---



&#x20;🎯 Objectives



\* Develop a lightweight AI-powered desktop assistant.

\* Eliminate workflow disruption caused by application switching.

\* Use multimodal AI (Vision + Language) for contextual assistance.

\* Provide a floating always-on-top overlay interface.

\* Create an extensible architecture for future AI features.



\---



&#x20;⚙️ Working Flow



1\. Application runs silently in the background.

2\. User presses configurable hotkey (`Ctrl + Shift + H`).

3\. Current screen is captured instantly.

4\. Floating overlay window appears.

5\. User types a question.

6\. Screenshot + query are sent to Gemini Vision API.

7\. AI analyzes the screen and generates a response.

8\. Answer is displayed in the same overlay.



\---



&#x20;🏗️ System Architecture



| Module           | Library / Tool    | Function                            |

| ---------------- | ----------------- | ----------------------------------- |

| Hotkey Listener  | pynput            | Detects global keyboard shortcut    |

| Screen Capture   | mss               | Captures full screen image          |

| Image Processing | Pillow (PIL)      | Converts raw screen data            |

| AI Vision Engine | Google Gemini API | Analyzes screen and answers queries |

| Overlay UI       | tkinter           | Floating always-on-top interface    |

| Threading        | threading         | Keeps listener and UI independent   |



\---



✨ Key Features



🔹 Zero App Switching



Entire interaction happens inside a floating overlay.



&#x20;🔹 Context Awareness



Gemini Vision understands active applications and current screen state.



&#x20;🔹 Global Hotkey



Works from anywhere in the operating system.



&#x20;🔹 Lightweight Architecture



Minimal CPU and RAM usage.



🔹 Free AI Integration



Uses Google Gemini API free tier.



&#x20;🔹 Real-Time Assistance



Provides instant contextual guidance.



\---



&#x20;🚀 Tech Stack



&#x20;Frontend / UI



\* Python Tkinter



&#x20;AI \& Backend



\* Google Gemini Vision API



&#x20;Libraries Used



\* pynput

\* mss

\* Pillow

\* threading

\* tkinter

\* google-generativeai



\---



&#x20;📂 Recommended Project Structure



```bash

MY-SCREEN-APP/

│

├── src/

│   ├── pranjay.py

│

├── package.json

├── README.md

```



\---



🛠️ Installation Guide



1️⃣ Clone Repository



```bash

git clone https://github.com/pranjaysingh1001/MY-SCREEN-APP.git

```



\## 2️⃣ Move Into Project Folder



```bash

cd MY-SCREEN-APP

```



&#x20;3️⃣ Create Virtual Environment



```bash

python -m venv venv

```



&#x20;4️⃣ Activate Environment



&#x20;Windows



```bash

venv\\Scripts\\activate

```



&#x20;Linux / Mac



```bash

source venv/bin/activate

```



&#x20;5️⃣ Install Dependencies



```bash

pip install -r requirements.txt

```



\---



&#x20;▶️ Run Application



```bash

python src/pranjay.py

```



\---



&#x20;🔑 Environment Variables



Create a `.env` file:



```env

GEMINI\_API\_KEY=AIzaSyBjr\_C5pgOvfGExOnAMTsPymg8G1SJldEY

```



\---



📦 requirements.txt



```txt

pynput

mss

Pillow

google-generativeai

python-dotenv

```



\---



&#x20;📄 package.json



```json

{

&#x20; "name": "my-screen-app",

&#x20; "version": "1.0.0",

&#x20; "description": "AI-powered screen-aware desktop assistant using Gemini Vision API",

&#x20; "main": "src/main.py",

&#x20; "author": "Pranjay Singh",

&#x20; "license": "MIT",

&#x20; "scripts": {

&#x20;   "start": "python src/pranjay.py"

&#x20; },

&#x20; "keywords": \[

&#x20;   "AI",

&#x20;   "Gemini",

&#x20;   "Screen Assistant",

&#x20;   "Python",

&#x20;   "Desktop AI",

&#x20;   "Computer Vision",

&#x20;   "Automation"

&#x20; ]

}

```



\---



&#x20;📌 Future Scope



\* 🎤 Voice Input Integration

\* 🧠 App-Specific AI Prompts

\* 📜 Answer History Panel

\* ⚡ Quick Action Buttons

\* 🖱️ Cursor Guidance System

\* 📦 EXE Packaging with PyInstaller



\---



🧪 Example Use Cases



👨‍💻 Developers



Get coding help without leaving IDE.



&#x20;🎬 Video Editors



Understand complex editing tools instantly.



🎨 Designers



Receive contextual design assistance.



&#x20;📚 Students



Get explanations directly from study material.



\---



🔒 Security \& Privacy



\* Screenshots are processed only for generating contextual responses.

\* API keys should never be committed publicly.

\* Add `.env` to `.gitignore`.



\---

&#x20;📷 Suggested Screenshots Section



Add screenshots inside:



```bash

public/screenshots/

```



Example:



```md



\---



\# 👨‍💻 Author



&#x20;Pranjay Singh



\* GitHub: \[https://github.com/pranjaysingh1001](https://github.com/pranjaysingh1001)



\---



&#x20;⭐ Support



If you like this project:



\* Star the repository ⭐

\* Fork the project 🍴

\* Share with others 🚀



\---



&#x20;📜 License



This project is licensed under the MIT License.



