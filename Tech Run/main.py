"""
TECH RUN - Main Game Script
Tech quiz game with audio, theming, and UI systems.
"""
import tkinter as tk
from tkinter import messagebox
import random
import copy
import os

# --- LOCAL IMPORTS ---
import config
from config import style_button, get_current_colors
import audio
import menus
from data_manager import save_high_score

# --- IMAGE SUPPORT ---
try:
    from PIL import Image, ImageTk
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False  # Logos disabled without Pillow

try:
    from questions import all_questions as questions
except ImportError:
    questions = [{"question": "Error: No questions found", "options": ["OK"], "answer": "OK", "hint": "Check questions.py"}]

# --- GLOBAL GAME STATE ---
current_index = 0      # Current question position
score = 0              # Player's current score
shuffled_questions = [] # Randomized question list
player_name = "Player" # Current player name
game_running = False   # Game session status
hint_used = False      # Hint usage tracker

def format_score(score_value):
    """Returns 'point' or 'points' based on score."""
    return "point" if score_value == 1 else "points"

def load_logo(path="assets/logo.png", size=(300, 200)):
    """Load and resize logo image from assets folder."""
    if not PIL_AVAILABLE:
        return None
    
    try:
        img = Image.open(path)
        img = img.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception:
        return None  # Silent fail if logo missing

def play_click_sound(e=None):
    """Play button click sound effect."""
    try:
        audio.play_sfx("click")
    except:
        pass

def set_button_sizes():
    """Dynamically adjust button font size based on answer text length."""
    if not option_buttons or not game_running:
        return
    
    try:
        current_q = shuffled_questions[current_index]
        options = current_q["options"]
        
        if not options:
            return
        
        longest_text = max(options, key=len)
        text_length = len(longest_text)
        font_family = config.FONTS["btn"][0]
        
        # Progressive sizing based on text length
        if text_length <= 30:
            font_size, wraplength = 12, 260
        elif text_length <= 50:
            font_size, wraplength = 11, 280
        elif text_length <= 80:
            font_size, wraplength = 10, 300
        elif text_length <= 120:
            font_size, wraplength = 9, 320
        else:
            font_size, wraplength = 8, 340
        
        for btn in option_buttons:
            btn.config(font=(font_family, font_size, "bold"), wraplength=wraplength)
            
    except Exception:
        font_family = config.FONTS["btn"][0]
        for btn in option_buttons:
            btn.config(font=(font_family, 10, "bold"), wraplength=300)

def apply_theme_refresh():
    """Apply current theme colors to all UI elements."""
    try:
        colors = get_current_colors()
        
        # Update container backgrounds
        window.configure(bg=colors["bg"])
        menu_frame.config(bg=colors["bg"])
        menu_card.config(bg=colors["bg"]) 
        game_container.config(bg=colors["bg"])
        sidebar.config(bg=colors["panel_bg"])
        main_area.config(bg=colors["bg"])
        btn_grid.config(bg=colors["bg"])
        
        # Update text elements
        subtitle_label.config(bg=colors["bg"], fg=colors["fg_secondary"], font=config.FONTS["body"])
        name_label.config(bg=colors["bg"], fg=colors["fg"], font=config.FONTS["small"])
        sidebar_name.config(bg=colors["panel_bg"], fg=colors["fg"], font=config.FONTS["body"])
        
        # Update logo backgrounds
        if hasattr(window, 'menu_logo_label'):
            window.menu_logo_label.config(bg=colors["bg"])
        if hasattr(window, 'sidebar_logo_label'):
            window.sidebar_logo_label.config(bg=colors["panel_bg"])
        
        # Update fallback text
        if hasattr(window, 'title_label_fallback'):
            window.title_label_fallback.config(bg=colors["bg"], fg=colors["accent"], font=config.FONTS["title"])
        if hasattr(window, 'sidebar_title_fallback'):
            window.sidebar_title_fallback.config(bg=colors["panel_bg"], fg=colors["accent"], font=config.FONTS["sidebar"])
        
        # Update score display
        if hasattr(window, 'score_title_label'):
            window.score_title_label.config(bg=colors["panel_bg"], fg=colors["fg_secondary"])
        if hasattr(window, 'sidebar_score'):
            window.sidebar_score.config(bg=colors["panel_bg"], fg=colors["score"])
        
        sidebar_status.config(bg=colors["panel_bg"], fg=colors["fg"], font=config.FONTS["small"])
        question_label.config(bg=colors["bg"], fg=colors["fg"], font=("Segoe UI", 18))
        
        # Update input and buttons
        name_entry.config(bg=colors["btn_bg"], fg=colors["fg"], 
                         insertbackground=colors["fg"], font=config.FONTS["input"])
        style_button(start_btn, "success")
        style_button(instructions_btn, "how_to_play")
        style_button(lb_btn, "info")
        style_button(settings_btn, "subtle") 
        style_button(hint_btn, "warning")
        style_button(quit_btn, "danger")
        
        # Update answer buttons
        font_family = config.FONTS["btn"][0]
        for btn in option_buttons:
            current_font = btn.cget("font")
            if isinstance(current_font, (list, tuple)) and len(current_font) >= 2:
                font_size = current_font[1]
            else:
                font_size = 11
            
            btn.config(font=(font_family, font_size, "bold"))
            style_button(btn, "default")
            
    except Exception as e:
        print(f"Theme refresh error: {e}")

def animate_running_text(dot_count=0):
    """Animate 'PLAYING...' status with pulsing dots during gameplay."""
    if not game_running: 
        if 'sidebar_status' in globals():
            sidebar_status.config(text="PLAYING")
        return
    
    dots = "." * (dot_count % 4)
    try:
        if 'sidebar_status' in globals():
            sidebar_status.config(text=f"PLAYING{dots}")
        if game_running:
            window.after(500, lambda: animate_running_text(dot_count + 1))
    except: 
        return

def start_game_sequence():
    """Transition from main menu to active gameplay."""
    raw_name = name_entry.get().strip()
    clean_name = raw_name.replace(",", "")
    
    if not clean_name:
        menus.show_error(window, "NAME REQUIRED", "Please enter your name to play!")
        return
        
    global player_name, game_running
    player_name = clean_name
    game_running = True
    
    menu_frame.pack_forget()
    game_container.pack(fill="both", expand=True)
    sidebar_name.config(text=f"PLAYER:\n{player_name}")
    
    audio.play_gameplay_bgm()
    init_game()
    animate_running_text()

def quit_game_sequence():
    """Handle exit confirmation with score saving option."""
    if game_running:
        menus.ask_exit(window, 
                      lambda: [save_high_score(player_name, score), return_to_menu()], 
                      return_to_menu)
    else:
        return_to_menu()

def return_to_menu():
    """Return to main menu with proper state cleanup."""
    global game_running
    game_running = False 
    
    audio.switch_to_menu_music()
    game_container.pack_forget()
    menu_frame.pack(fill="both", expand=True)
    apply_theme_refresh()

def init_game():
    """Initialize new game session with shuffled questions."""
    global shuffled_questions, current_index, score
    score = 0
    current_index = 0
    shuffled_questions = copy.deepcopy(questions)
    random.shuffle(shuffled_questions)
    for q in shuffled_questions: 
        random.shuffle(q["options"])
    load_question()

def load_question():
    """Load and display the next question."""
    global hint_used
    hint_used = False
    
    if not shuffled_questions or current_index >= len(shuffled_questions):
        init_game()
        return
    
    current_q = shuffled_questions[current_index]
    question_label.config(text=current_q["question"])
    sidebar_score.config(text=f"{score} {format_score(score)}")
    
    for btn in option_buttons:
        btn.config(state="normal", command=None)
        style_button(btn, "default") 
    
    for i, option in enumerate(current_q["options"]):
        if i < len(option_buttons):
            btn = option_buttons[i]
            btn.config(text=option, command=lambda b=btn, opt=option: check_answer(b, opt))
    
    window.update_idletasks()
    set_button_sizes()

def check_answer(btn, selected_option):
    """Validate player's answer and provide feedback."""
    global current_index, score
    current_q = shuffled_questions[current_index]
    correct = current_q["answer"]
    colors = get_current_colors()
    
    for b in option_buttons: 
        b.config(state="disabled")

    if selected_option == correct:
        btn.config(bg=colors["success"], fg="white")
        audio.play_sfx("correct")
        score += 1
        window.after(600, lambda: next_step(True))
    else:
        btn.config(bg=colors["danger"], fg="white")
        audio.play_sfx("wrong")
        for b in option_buttons:
            if b.cget("text") == correct:
                b.config(bg=colors["success"], fg="white")
        
        text = current_q.get("explanation", current_q.get("hint", "No details."))
        window.after(1500, lambda: next_step(False, correct, text))

def next_step(was_correct, correct_ans=None, explanation=None):
    """Advance game after answer feedback."""
    global current_index
    if was_correct:
        current_index += 1
        if current_index >= len(shuffled_questions):
            init_game()
        load_question()
    else:
        audio.stop_bgm()
        save_high_score(player_name, score)
        window.player_name = player_name
        
        def on_continue():
            return_to_menu()
            menus.show_leaderboard(window)
            
        menus.create_game_over_modal(window, correct_ans, explanation, score, on_continue)

def get_hint():
    """Handle hint purchase and application logic."""
    global score, hint_used
    colors = get_current_colors()
    current_q = shuffled_questions[current_index]
    
    if hint_used:
        if config.HINT_MODE == "TEXT":
            menus.show_hint(window, "HINT RECALL", current_q["hint"])
        else:
            menus.show_hint(window, "HINT ACTIVE", "You have already used the hint.")
        return 

    if score < 1:
        menus.show_error(window, "NO POINTS", f"Hints cost 1 point.")
        return
    
    score -= 1
    hint_used = True
    sidebar_score.config(text=f"{score} {format_score(score)}")
    
    if config.HINT_MODE == "TEXT":
        menus.show_hint(window, "HINT", current_q["hint"])
    else:
        wrong = [b for b in option_buttons if b.cget("text") != current_q["answer"]]
        if len(wrong) >= 2:
            for b in random.sample(wrong, 2):
                b.config(text="", state="disabled", bg=colors["bg"])

# --- MAIN WINDOW SETUP ---
window = tk.Tk()
window.title("Tech Run")
colors = get_current_colors()
window.configure(bg=colors["bg"])

# Center 900x600 window
width, height = 900, 600
x = (window.winfo_screenwidth() - width) // 2
y = (window.winfo_screenheight() - height) // 2
window.geometry(f"{width}x{height}+{x}+{y}")

# --- MAIN MENU INTERFACE ---
menu_frame = tk.Frame(window, bg=colors["bg"]) 
menu_frame.pack(fill="both", expand=True)

menu_card = tk.Frame(menu_frame, bg=colors["bg"], padx=40, pady=25)
menu_card.place(relx=0.5, rely=0.45, anchor="center")

# Main menu logo (replaces title text)
menu_logo = load_logo("assets/logo.png", size=(340, 200))
if menu_logo:
    window.menu_logo = menu_logo
    window.menu_logo_label = tk.Label(menu_card, image=menu_logo, bg=colors["bg"])
    window.menu_logo_label.pack(pady=(0, 0))
else:
    window.title_label_fallback = tk.Label(menu_card, text="TECH RUN",
                                          font=config.FONTS["title"],
                                          fg=colors["accent"], bg=colors["bg"])
    window.title_label_fallback.pack(pady=(0, 10))

subtitle_label = tk.Label(menu_card, text="Test Your Technology Knowledge",
                         font=config.FONTS["body"],
                         fg=colors["fg_secondary"], bg=colors["bg"])
subtitle_label.pack(pady=(0, 10))

name_label = tk.Label(menu_card, text="PLAYER NAME:", font=config.FONTS["small"])
name_label.pack(anchor="w", pady=(0, 5), fill="x")

name_entry = tk.Entry(menu_card, font=config.FONTS["input"], justify="center", relief="flat", width=25)
name_entry.pack(pady=(0, 20), ipady=5)

start_btn = tk.Button(menu_card, text="START GAME", font=config.FONTS["btn"], width=20, command=start_game_sequence)
start_btn.pack(pady=(0, 15), ipady=5)
style_button(start_btn, "success")
start_btn.bind("<Button-1>", play_click_sound, add="+")

instructions_btn = tk.Button(menu_card, text="HOW TO PLAY", font=config.FONTS["btn"], 
                            width=20, command=lambda: menus.show_instructions(window))
instructions_btn.pack(pady=(0, 15))
style_button(instructions_btn, "how_to_play")
instructions_btn.bind("<Button-1>", play_click_sound, add="+")

settings_btn = tk.Button(menu_card, text="SETTINGS", font=config.FONTS["btn"], width=20, command=lambda: menus.open_settings(window, apply_theme_refresh))
settings_btn.pack(pady=(0, 15))
style_button(settings_btn, "subtle") 
settings_btn.bind("<Button-1>", play_click_sound, add="+")

lb_btn = tk.Button(menu_card, text="LEADERBOARD", font=config.FONTS["btn"], width=20, command=lambda: menus.show_leaderboard(window))
lb_btn.pack(pady=(0, 0))
style_button(lb_btn, "info")
lb_btn.bind("<Button-1>", play_click_sound, add="+")

# --- GAMEPLAY INTERFACE ---
game_container = tk.Frame(window)

sidebar = tk.Frame(game_container, width=200, padx=20, pady=20)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

# Sidebar logo (replaces title text)
sidebar_logo = load_logo("assets/logo.png", size=(200, 120))
if sidebar_logo:
    window.sidebar_logo = sidebar_logo
    window.sidebar_logo_label = tk.Label(sidebar, image=sidebar_logo, bg=colors["panel_bg"])
    window.sidebar_logo_label.pack(pady=(0, 10))
else:
    window.sidebar_title_fallback = tk.Label(sidebar, text="TECH RUN", font=config.FONTS["sidebar"])
    window.sidebar_title_fallback.pack(pady=(0, 40))

sidebar_name = tk.Label(sidebar, text="PLAYER:\nPlayer", font=config.FONTS["body"], justify="center")
sidebar_name.pack(pady=20)

score_title_label = tk.Label(sidebar, text="SCORE", 
         font=config.FONTS["sidebar"],
         bg=colors["panel_bg"], fg=colors["fg_secondary"],
         justify="center")
score_title_label.pack(pady=(20, 0))
window.score_title_label = score_title_label

sidebar_score = tk.Label(sidebar, text="0 points", 
                        font=config.FONTS["score"],
                        bg=colors["panel_bg"], fg=colors["score"],
                        justify="center")
sidebar_score.pack(pady=(0, 20))
window.sidebar_score = sidebar_score

sidebar_status = tk.Label(sidebar, text="PLAYING", font=config.FONTS["small"])
sidebar_status.pack(pady=5)

quit_btn = tk.Button(sidebar, text="EXIT GAME", font=config.FONTS["btn"], command=quit_game_sequence)
style_button(quit_btn, "danger")
quit_btn.bind("<Button-1>", play_click_sound, add="+")
quit_btn.pack(side="bottom", fill="x", pady=(10, 5))

hint_btn = tk.Button(sidebar, text="USE HINT (-1)", font=config.FONTS["btn"], command=get_hint)
style_button(hint_btn, "warning")
hint_btn.bind("<Button-1>", play_click_sound, add="+")
hint_btn.pack(side="bottom", fill="x", pady=(20, 0))

main_area = tk.Frame(game_container, padx=40, pady=40)
main_area.pack(side="right", fill="both", expand=True)

question_label = tk.Label(main_area, text="Loading...", font=("Segoe UI", 18), wraplength=600, justify="center")
question_label.pack(expand=True)

btn_grid = tk.Frame(main_area)
btn_grid.pack(fill="both", expand=True, pady=20)

btn_grid.grid_columnconfigure(0, weight=1, minsize=300, uniform="equal_boxes")
btn_grid.grid_columnconfigure(1, weight=1, minsize=300, uniform="equal_boxes")
btn_grid.grid_rowconfigure(0, weight=1, minsize=120, uniform="equal_boxes")
btn_grid.grid_rowconfigure(1, weight=1, minsize=120, uniform="equal_boxes")

option_buttons = []

font_family = config.FONTS["btn"][0]
for i in range(4):
    r = i // 2
    c = i % 2
    
    btn = tk.Button(btn_grid, text="", 
                   font=(font_family, 11, "bold"),
                   justify="center",
                   anchor="center",
                   wraplength=280,
                   padx=15,
                   pady=8)
    
    btn.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")
    btn.bind("<Button-1>", play_click_sound, add="+")
    option_buttons.append(btn)

apply_theme_refresh()

if __name__ == "__main__":
    try:
        audio.play_bgm()
        window.mainloop()
    except Exception as e:
        print(f"Game startup error: {e}")
        messagebox.showerror("Startup Error", f"Failed to start game:\n{e}")