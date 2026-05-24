# =========================================================
#                SCREEN AI PRO X - PREMIUM
# =========================================================
# Modern AI Screen Assistant
# Clean Human-like Answers
# Beautiful UI + Better Formatting
# =========================================================

import google.generativeai as genai
import mss
from PIL import Image
from pynput import keyboard
import tkinter as tk
from tkinter import scrolledtext
import threading
import time

# =========================================================
# GEMINI CONFIG
# =========================================================

API_KEY = ""

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(
    "gemini-3.1-flash-lite"
)

# =========================================================
# COLORS
# =========================================================

BG = "#0b1020"
CARD = "#121a2b"
INPUT = "#1b2538"

PRIMARY = "#7c4dff"
SECONDARY = "#00c2ff"

TEXT = "#f1f5f9"
SUBTEXT = "#94a3b8"

SUCCESS = "#22c55e"

# =========================================================
# RATE LIMIT PROTECTION
# =========================================================

last_request_time = 0

# =========================================================
# MAIN APP
# =========================================================

class ScreenAI:

    def __init__(self):
        self.window = None

    # =====================================================
    # SCREENSHOT
    # =====================================================

    def capture_screen(self):

        with mss.MSS() as sct:

            monitor = sct.monitors[0]

            screenshot = sct.grab(monitor)

            img = Image.frombytes(
                "RGB",
                screenshot.size,
                screenshot.rgb
            )

            # Compress image for speed
            img.thumbnail((1280, 720))

            return img

    # =====================================================
    # BEAUTIFUL TYPING EFFECT
    # =====================================================

    def type_text(self, widget, content):

        widget.config(state="normal")
        widget.delete("1.0", "end")

        for char in content:

            widget.insert("end", char)
            widget.see("end")
            widget.update()

            time.sleep(0.002)

        widget.config(state="disabled")

    # =====================================================
    # ASK AI
    # =====================================================

    def ask_ai(self):

        global last_request_time

        current = time.time()

        # Prevent request spam
        if current - last_request_time < 3:
            return

        last_request_time = current

        question = self.input_box.get().strip()

        if not question:
            return

        self.ask_btn.config(text="Thinking...")

        self.output.config(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("1.0", "Analyzing screen...")
        self.output.config(state="disabled")

        self.window.update()

        try:

            img = self.capture_screen()

            # =================================================
            # CLEAN HUMAN RESPONSE PROMPT
            # =================================================

            prompt = f"""
            You are a premium desktop AI assistant.

            Analyze the screenshot and answer ONLY the user's question.

            User Question:
            {question}

            STRICT RULES:
            - Give direct answer only
            - Keep response human-like
            - Keep formatting clean
            - No headings
            - No bullet points unless needed
            - No AI disclaimers
            - No "helpful insights"
            - No UI observations
            - No unnecessary explanation
            - Maximum 8-10 lines
            - Sound natural and smart
            - Make answer pleasant to read
            """

            response = model.generate_content([
                prompt,
                img
            ])

            answer = response.text.strip()

            self.type_text(
                self.output,
                answer
            )

        except Exception as e:

            self.output.config(state="normal")
            self.output.delete("1.0", "end")

            self.output.insert(
                "1.0",
                f"Error:\n\n{e}"
            )

            self.output.config(state="disabled")

        self.ask_btn.config(text="Ask AI")

    # =====================================================
    # CLEAR CHAT
    # =====================================================

    def clear_output(self):

        self.output.config(state="normal")
        self.output.delete("1.0", "end")
        self.output.config(state="disabled")

    # =====================================================
    # MAIN WINDOW
    # =====================================================

    def create_window(self):

        self.window = tk.Tk()

        self.window.title("Screen AI PRO X")

        self.window.geometry("1100x720+250+120")

        self.window.configure(bg=BG)

        self.window.attributes("-topmost", True)

        # =================================================
        # HEADER
        # =================================================

        header = tk.Frame(
            self.window,
            bg=CARD,
            height=80
        )

        header.pack(fill="x")

        title = tk.Label(
            header,
            text="SCREEN AI PRO X",
            bg=CARD,
            fg=TEXT,
            font=("Segoe UI Semibold", 24)
        )

        title.pack(
            side="left",
            padx=25,
            pady=18
        )

        status = tk.Label(
            header,
            text="● ONLINE",
            bg=CARD,
            fg=SUCCESS,
            font=("Segoe UI", 11, "bold")
        )

        status.pack(
            side="right",
            padx=25
        )

        # =================================================
        # BODY
        # =================================================

        body = tk.Frame(
            self.window,
            bg=BG
        )

        body.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        # =================================================
        # LEFT PANEL
        # =================================================

        left_panel = tk.Frame(
            body,
            bg=CARD,
            width=280
        )

        left_panel.pack(
            side="left",
            fill="y",
            padx=(0, 18)
        )

        left_panel.pack_propagate(False)

        left_title = tk.Label(
            left_panel,
            text="Features",
            bg=CARD,
            fg=TEXT,
            font=("Segoe UI Semibold", 20)
        )

        left_title.pack(
            anchor="w",
            padx=20,
            pady=(25, 20)
        )

        features = [
            "Live screen understanding",
            "Modern AI assistant",
            "Clean human responses",
            "Fast screenshot analysis",
            "Beautiful premium UI",
            "Smart coding help",
            "Dark mode experience",
            "Instant answers"
        ]

        for feature in features:

            item = tk.Label(
                left_panel,
                text=f"• {feature}",
                bg=CARD,
                fg=SUBTEXT,
                font=("Segoe UI", 11),
                anchor="w",
                justify="left"
            )

            item.pack(
                fill="x",
                padx=22,
                pady=8
            )

        # =================================================
        # RIGHT PANEL
        # =================================================

        right_panel = tk.Frame(
            body,
            bg=CARD
        )

        right_panel.pack(
            side="right",
            fill="both",
            expand=True
        )

        # =================================================
        # INPUT SECTION
        # =================================================

        top = tk.Frame(
            right_panel,
            bg=CARD
        )

        top.pack(
            fill="x",
            padx=20,
            pady=20
        )

        self.input_box = tk.Entry(
            top,
            bg=INPUT,
            fg=TEXT,
            relief="flat",
            insertbackground="white",
            font=("Segoe UI", 13)
        )

        self.input_box.pack(
            side="left",
            fill="x",
            expand=True,
            ipady=12
        )

        self.input_box.focus()

        # =================================================
        # ASK BUTTON
        # =================================================

        self.ask_btn = tk.Button(
            top,
            text="Ask AI",
            command=lambda: threading.Thread(
                target=self.ask_ai
            ).start(),
            bg=PRIMARY,
            fg="white",
            relief="flat",
            cursor="hand2",
            font=("Segoe UI Semibold", 11),
            padx=18,
            pady=10
        )

        self.ask_btn.pack(
            side="left",
            padx=10
        )

        # =================================================
        # CLEAR BUTTON
        # =================================================

        clear_btn = tk.Button(
            top,
            text="Clear",
            command=self.clear_output,
            bg=SECONDARY,
            fg="white",
            relief="flat",
            cursor="hand2",
            font=("Segoe UI Semibold", 11),
            padx=18,
            pady=10
        )

        clear_btn.pack(side="left")

        # =================================================
        # OUTPUT BOX
        # =================================================

        self.output = scrolledtext.ScrolledText(
            right_panel,
            wrap="word",
            bg="#0f172a",
            fg=TEXT,
            relief="flat",
            insertbackground="white",
            font=("Segoe UI", 14),
            padx=24,
            pady=24,
            spacing1=6,
            spacing2=4,
            spacing3=6
        )

        self.output.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        self.output.insert(
            "1.0",
            """
Welcome to Screen AI PRO X

Ask anything about your screen:
• Coding errors
• Websites
• UI designs
• Documents
• YouTube videos
• Wallpapers
• Apps
• Dashboards

Press Enter to ask AI
Press ESC to close
            """
        )

        self.output.config(state="disabled")

        # =================================================
        # FOOTER
        # =================================================

        footer = tk.Label(
            self.window,
            text="Powered by Gemini 3.1 Flash Lite",
            bg=BG,
            fg=SUBTEXT,
            font=("Segoe UI", 10)
        )

        footer.pack(
            pady=(0, 12)
        )

        # =================================================
        # KEYBINDS
        # =================================================

        self.window.bind(
            "<Return>",
            lambda e: threading.Thread(
                target=self.ask_ai
            ).start()
        )

        self.window.bind(
            "<Escape>",
            lambda e: self.window.destroy()
        )

        self.window.mainloop()

# =========================================================
# START HOTKEY
# =========================================================

app = ScreenAI()

hotkey = keyboard.GlobalHotKeys({

    '<ctrl>+<shift>+h':
        lambda: threading.Thread(
            target=app.create_window
        ).start()

})

print("""

=========================================
        SCREEN AI PRO X RUNNING
=========================================

HOTKEY:
CTRL + SHIFT + H

FEATURES:
✔ Premium UI
✔ Human-like AI answers
✔ Fast screen analysis
✔ Beautiful formatting
✔ Clean responses
✔ Gemini 3.1 Flash Lite

=========================================

""")

hotkey.start()
hotkey.join()