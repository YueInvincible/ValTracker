import tkinter as tk
import keyboard
import requests
import threading
import ctypes
import os
import urllib.parse

HOTKEY_TOGGLE = "F6"
HOTKEY_EXIT = "F5"
API_KEY = "C'on, your api key goes here!"  # <--- api.henrikdev.xyz/dashboard/api-keys

root = tk.Tk()
root.title("Yue's Valorant Overlay") #MAKE SURE VALORANT VIDEO SETTING = WINDOWED FULLSCREEN
root.geometry("350x260")
root.configure(bg="#18181c")
root.attributes("-topmost", True)

HWND_TOPMOST = -1
ctypes.windll.user32.SetWindowPos(root.winfo_id(), HWND_TOPMOST, 0, 0, 0, 0, 3)

lbl = tk.Label(root, text="Riot ID (Name#Tag):", bg="#18181c", fg="#ece8e1", font=("Arial", 11, "bold"))
lbl.pack(pady=8)
entry = tk.Entry(root, width=24, font=("Arial", 12), bg="#2f3136", fg="white", insertbackground="white", bd=0, justify="center")
entry.pack(pady=5)
lbl_res = tk.Label(root, text="F6: Hide/Show | F5: Kill the process.", bg="#18181c", fg="#00ffcc", font=("Arial", 10, "bold"))
lbl_res.pack(pady=10)

def fetch_stats(riot_id):
    if not API_KEY or API_KEY == "YOUR_HENRIKDEV_KEY":
        lbl_res.config(text="NO API KEY PROVIDED!", fg="#ff4655")
        return
    if "#" not in riot_id:
        lbl_res.config(text="Invalid Name#Tag", fg="#ff4655")
        return
    
    name, tag = riot_id.split("#", 1)
    name_enc, tag_enc = urllib.parse.quote(name), urllib.parse.quote(tag)
    headers = {"Authorization": API_KEY}
    
    try:
        lbl_res.config(text="Yue is finding...", fg="#ece8e1")
        res_acc = requests.get(f"https://api.henrikdev.xyz/valorant/v1/account/{name_enc}/{tag_enc}", headers=headers, timeout=5)
        if res_acc.status_code != 200:
            lbl_res.config(text=f"Contact discord (yueinv) with error code: {res_acc.status_code}", fg="#ff4655")
            return
        
        puuid = res_acc.json().get("data", {}).get("puuid")
        region = res_acc.json().get("data", {}).get("region")

        lbl_res.config(text="Yue is receiving rank information...", fg="#ece8e1")
        res_mmr = requests.get(f"https://api.henrikdev.xyz/valorant/v2/by-puuid/mmr/{region}/{puuid}", headers=headers, timeout=5)
        rank_text = "Unranked"
        if res_mmr.status_code == 200:
            mmr_data = res_mmr.json().get("data", {}).get("current_data", {})
            rank = mmr_data.get("currenttierpatched", "Unranked")
            elo = mmr_data.get("elo", 0)
            rank_text = f"Rank: {rank} (Elo: {elo})"

        lbl_res.config(text="Yue is examing player's last 5 matches...", fg="#ece8e1")
        res_matches = requests.get(f"https://api.henrikdev.xyz/valorant/v3/by-puuid/matches/{region}/{puuid}?mode=competitive&size=5", headers=headers, timeout=8)
        
        kd_text = "No ranked games found!"
        kd_color = "#ece8e1"
        
        if res_matches.status_code == 200:
            matches = res_matches.json().get("data", [])
            if matches:
                kills, deaths, wins, total_score, total_rounds = 0, 0, 0, 0, 0
                for m in matches:
                    for p in m.get("players", {}).get("all_players", []):
                        if p.get("puuid") == puuid:
                            stats = p.get("stats", {})
                            kills += stats.get("kills", 0)
                            deaths += stats.get("deaths", 0)
                            total_score += stats.get("score", 0)
                            total_rounds += m.get("metadata", {}).get("rounds_played", 1)
                            if m.get("teams", {}).get(p.get("team", "").lower(), {}).get("has_won"):
                                wins += 1
                            break
                            
                kd = round(kills / deaths, 2) if deaths > 0 else kills
                acs = round(total_score / total_rounds) if total_rounds > 0 else 0
                losses = len(matches) - wins
                
                kd_color = "#00ffcc" if kd >= 1.1 else ("#ece8e1" if kd >= 0.9 else "#ff4655")
                kd_text = f"Match history (5 matches): {wins}W - {losses}L\nK/D: {kd}  |  ACS: {acs}"

        lbl_res.config(text=f"{rank_text}\n\n{kd_text}", fg=kd_color)

    except Exception:
        lbl_res.config(text="Connection error / Timeout!", fg="#ff4655")

entry.bind("<Return>", lambda e: threading.Thread(target=fetch_stats, args=(entry.get().strip(),), daemon=True).start())

is_visible = False
def toggle_window():
    global is_visible
    if is_visible:
        root.withdraw()
    else:
        entry.delete(0, tk.END)
        lbl_res.config(text="Yue's here! Paste ID & Enter.\nF6: Hide/Show | F5: Kill the process", fg="#ece8e1")
        root.deiconify()
        ctypes.windll.user32.SetWindowPos(root.winfo_id(), HWND_TOPMOST, 0, 0, 0, 0, 3)
        entry.focus_force()
    is_visible = not is_visible

keyboard.add_hotkey(HOTKEY_TOGGLE, lambda: root.after(0, toggle_window))
keyboard.add_hotkey(HOTKEY_EXIT, lambda: os._exit(0))

root.withdraw()
root.mainloop()