Tracking valorant's player performance from the party screen (manually) since valtracker not allowing that so that I CAN NOT DODGE THESE BULLSHITSTUPIDASS PLAYERS!
--------------------------------------------------------------------
# Yue's ValTracker

A lightweight, high-performance **Valorant Overlay** tool built for players who want to check their teammates' stats (Rank, K/D, ACS) instantly without leaving the game or opening a browser.

### 🚀 Features
*   **Instant Stats:** Displays current Rank, Elo, K/D Ratio, and ACS (Average Combat Score) based on the last 5 competitive matches.
*   **Performance First:** Zero-overhead design, minimal RAM usage.
*   **PIP-like Experience:** Always-on-top overlay that stays visible during your match (requires "Windowed Fullscreen" game mode).
*   **Visual Feedback:** 
    *   🟢 **Green:** High performance (K/D >= 1.1) - Solid teammate.
    *   ⚪ **White:** Balanced performance (K/D 0.9 - 1.09).
    *   🔴 **Red:** Low performance (K/D < 0.9) - Potential "baiter" or bad form.
*   **Smart Hotkeys:** 
    *   `F6`: Toggle Overlay (Show/Hide).
    *   `F5`: Kill process and exit safely.

---

### 📋 Prerequisites
*   Python 3.x installed.
*   Required libraries: `pip install keyboard requests`

---

### 🛠️ How to Use

1.  **Get your API Key:**
    *   Visit [api.henrikdev.xyz/dashboard/api-keys](https://api.henrikdev.xyz/dashboard/api-keys) to generate your free API key.
2.  **Configuration:**
    *   Open `valtracker.py` with any text editor.
    *   Locate the line `API_KEY = "YOUR_HENRIKDEV_KEY"` and replace it with your actual key.
3.  **Run the tool:**
    *   Open your Terminal/Console.
    *   Navigate to the project folder:
        ```bash
        cd path/to/your/folder
        ```
    *   Run the script:
        ```bash
        python valtracker.py
        ```
4.  **In-Game:**
    *   Press `F6` to toggle the overlay.
    *   Paste the Riot ID (e.g., `Name#Tag`) and press `Enter`.
    *   Press `F5` when you want to terminate the application.

---

### ⚠️ Important Notes
*   **Game Settings:** For the overlay to appear over your game, please set your Valorant **Display Mode** to **"Windowed Fullscreen"**.
*   **Permissions:** Always run your terminal as **Administrator**, otherwise the global hotkeys (`F6`/`F5`) will not work while you are inside the game.

---
*Created for personal use. Use responsibly.*

---
