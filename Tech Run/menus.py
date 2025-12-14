"""
TECH RUN - Menu System
Handles custom modal windows (Settings, Leaderboard, Alerts, Instructions).
"""
import tkinter as tk
import config
import audio
from config import style_button, get_current_colors, get_theme, set_theme, get_hint_status, set_hint_status
from data_manager import get_high_scores, save_high_score

_settings_window = None  # Active settings window reference
_leaderboard_window = None  # Active leaderboard window reference

def create_modal(parent, title, message, buttons, sound=None, size="400x250"):
    """Create centered blocking popup window with styled buttons."""
    colors = get_current_colors()
    if sound: 
        audio.play_sfx(sound)

    popup = tk.Toplevel(parent)
    popup.title(f"Tech Run - {title}")
    popup.configure(bg=colors["panel_bg"])
    popup.resizable(False, False)
    
    # Center window on parent
    width, height = map(int, size.split('x'))
    x = parent.winfo_x() + (parent.winfo_width() // 2) - (width // 2)
    y = parent.winfo_y() + (parent.winfo_height() // 2) - (height // 2)
    popup.geometry(f"{width}x{height}+{x}+{y}")
    
    popup.transient(parent)
    popup.grab_set()
    
    def on_closing():
        popup.grab_release()
        popup.destroy()
    
    popup.protocol("WM_DELETE_WINDOW", on_closing)

    # Modal title
    tk.Label(popup, text=title, font=config.FONTS["btn"], 
             bg=colors["panel_bg"], fg=colors["accent"]).pack(pady=(20, 10))
    
    # Modal message
    tk.Label(popup, text=message, font=config.FONTS["body"], 
             bg=colors["panel_bg"], fg=colors["fg"], 
             wraplength=width-50, justify="left").pack(pady=10, expand=True)

    # Action buttons
    btn_frame = tk.Frame(popup, bg=colors["panel_bg"])
    btn_frame.pack(side="bottom", pady=20)

    for text, style, cmd in buttons:
        if cmd is None:
            action = on_closing
        else:
            action = cmd
        
        def make_action(func=action):
            def wrapper():
                popup.grab_release()
                popup.destroy()
                if func != on_closing:
                    func()
            return wrapper
        
        btn = tk.Button(btn_frame, text=text, width=12, command=make_action())
        style_button(btn, style)
        btn.bind("<Button-1>", lambda e: audio.play_sfx("click"), add="+")
        btn.pack(side="left", padx=5)

    parent.wait_window(popup)

def show_error(parent, title, msg):
    """Display error message with danger styling."""
    create_modal(parent, title, msg, [("OK", "danger", None)], sound=None, size="400x250")

def show_hint(parent, title, msg):
    """Display hint dialog with info styling and custom OK button."""
    colors = get_current_colors()
    
    def on_ok():
        popup.grab_release()
        popup.destroy()
    
    popup = tk.Toplevel(parent)
    popup.title(f"Tech Run - {title}")
    popup.configure(bg=colors["panel_bg"])
    popup.resizable(False, False)
    
    width, height = 400, 300
    x = parent.winfo_x() + (parent.winfo_width() // 2) - (width // 2)
    y = parent.winfo_y() + (parent.winfo_height() // 2) - (height // 2)
    popup.geometry(f"{width}x{height}+{x}+{y}")
    
    popup.transient(parent)
    popup.grab_set()
    
    # Hint title
    tk.Label(popup, text=title, font=config.FONTS["btn"], 
             bg=colors["panel_bg"], fg=colors["accent"]).pack(pady=(20, 10))
    
    # Hint content
    tk.Label(popup, text=msg, font=config.FONTS["hint"], 
             bg=colors["panel_bg"], fg=colors["fg"], 
             wraplength=width-50, justify="left").pack(pady=10, expand=True)

    # OK button
    ok_btn = tk.Button(popup, text="OK", width=12, command=on_ok)
    style_button(ok_btn, "info")
    ok_btn.bind("<Button-1>", lambda e: audio.play_sfx("click"), add="+")
    ok_btn.pack(side="bottom", pady=20)

    parent.wait_window(popup)

def show_game_over(parent, correct_ans, explanation, score, on_continue):
    """Compatibility wrapper for game over modal."""
    create_game_over_modal(parent, correct_ans, explanation, score, on_continue)

def create_game_over_modal(parent, correct_ans, explanation, score, on_continue):
    """Game over modal showing correct answer, explanation, and final score."""
    colors = get_current_colors()
    
    popup = tk.Toplevel(parent)
    popup.title("Tech Run - Game Over")
    popup.configure(bg=colors["panel_bg"])
    popup.resizable(False, False)
    
    width, height = 500, 500
    x = parent.winfo_x() + (parent.winfo_width() // 2) - (width // 2)
    y = parent.winfo_y() + (parent.winfo_height() // 2) - (height // 2)
    popup.geometry(f"{width}x{height}+{x}+{y}")
    
    popup.transient(parent)
    popup.grab_set()
    
    player_name = getattr(parent, 'player_name', 'Player')
    
    def close_modal():
        popup.grab_release()
        popup.destroy()
    
    popup.protocol("WM_DELETE_WINDOW", close_modal)
    
    def back_to_menu():
        close_modal()
        on_continue()
    
    # Header with game over text
    header_frame = tk.Frame(popup, bg=colors["panel_bg"], height=40)
    header_frame.pack(fill="x", pady=(15, 10))
    header_frame.pack_propagate(False)
    
    tk.Label(header_frame, text="YOUR RUN IS OVER", 
             font=config.FONTS["header"],
             bg=colors["panel_bg"], fg=colors["danger"]).pack(expand=True)
    
    main_container = tk.Frame(popup, bg=colors["panel_bg"])
    main_container.pack(fill="both", expand=True, padx=25, pady=5)
    
    # Correct answer section
    tk.Label(main_container, text="✅ CORRECT ANSWER:", 
             font=("Segoe UI", 11, "bold"),
             bg=colors["panel_bg"], fg=colors["success"], 
             anchor="w").pack(fill="x", pady=(0, 5), anchor="w")
    
    answer_frame = tk.Frame(main_container, bg=colors["btn_bg"], relief="flat", bd=1)
    answer_frame.pack(fill="x", pady=(0, 15))
    
    tk.Label(answer_frame, text=correct_ans, 
             font=("Segoe UI", 11),
             bg=colors["btn_bg"], fg=colors["fg"],
             wraplength=width-80,
             justify="left",
             padx=10, pady=8).pack(anchor="w")
    
    # Explanation section
    tk.Label(main_container, text="📚 EXPLANATION:", 
             font=("Segoe UI", 11, "bold"),
             bg=colors["panel_bg"], fg=colors["info"], 
             anchor="w").pack(fill="x", pady=(0, 5), anchor="w")
    
    explain_frame = tk.Frame(main_container, bg=colors["btn_bg"], relief="flat", bd=1, height=120)
    explain_frame.pack(fill="x", pady=(0, 15))
    explain_frame.pack_propagate(False)
    
    explain_text = tk.Label(explain_frame, text=explanation, 
             font=("Segoe UI", 10),
             bg=colors["btn_bg"], fg=colors["fg"],
             wraplength=width-90,
             justify="left",
             padx=10, pady=6)
    explain_text.pack(fill="both", expand=True, anchor="w")
    
    # Score display section
    score_section = tk.Frame(main_container, bg=colors["panel_bg"], height=60)
    score_section.pack(side="bottom", fill="x", pady=(20, 0))
    score_section.pack_propagate(False)
    
    score_display = tk.Frame(score_section, bg=colors["panel_bg"])
    score_display.pack(expand=True, pady=10)
    
    score_container = tk.Frame(score_display, bg=colors["panel_bg"])
    score_container.pack()
    
    tk.Label(score_container, text="SCORE: ", 
             font=("Segoe UI", 15, "bold"),
             bg=colors["panel_bg"], fg=colors["fg_secondary"]).pack(side="left")
    
    tk.Label(score_container, text=str(score), 
             font=("Segoe UI", 15, "bold"),
             bg=colors["panel_bg"], fg=colors["score"]).pack(side="left", padx=(0, 5))
    
    points_text = "point" if score == 1 else "points"
    tk.Label(score_container, text=points_text, 
             font=("Segoe UI", 15),
             bg=colors["panel_bg"], fg=colors["score"]).pack(side="left")
    
    # Back to menu button
    btn_frame = tk.Frame(popup, bg=colors["panel_bg"], height=50)
    btn_frame.pack(side="bottom", fill="x", pady=(0, 15))
    btn_frame.pack_propagate(False)
    
    back_btn = tk.Button(btn_frame, text="BACK TO MENU", 
                        font=config.FONTS["btn"],
                        width=20,
                        command=back_to_menu)
    style_button(back_btn, "info")
    back_btn.bind("<Button-1>", lambda e: audio.play_sfx("click"), add="+")
    back_btn.pack(expand=True)
    
    parent.wait_window(popup)

def ask_exit(parent, on_save, on_dont_save):
    """Exit confirmation with Save/Don't Save/Cancel options."""
    buttons = [
        ("SAVE & EXIT", "success", on_save),
        ("DON'T SAVE", "danger", on_dont_save),
        ("CANCEL", "subtle", None)
    ]
    create_modal(parent, "EXIT GAME", "Save progress?", buttons, sound=None, size="450x250")

def show_instructions(parent):
    """Tabbed instructions modal with gameplay, hints, and controls sections."""
    colors = get_current_colors()
    
    # Color tags for syntax highlighting in text widget
    color_tags = {
        "header": colors["accent"],
        "subheader": colors["info"], 
        "bullet": colors["fg"],
        "positive": colors["success"],
        "negative": colors["danger"],
        "warning": colors["warning"],
        "info": colors["info"], 
        "highlight": colors["score"],
        "secondary": colors["gold"],
        "code": colors["fg_secondary"]
    }
    
    popup = tk.Toplevel(parent)
    popup.title("Tech Run - How to Play")
    popup.configure(bg=colors["panel_bg"])
    popup.resizable(False, False)
    
    width, height = 520, 500
    x = parent.winfo_x() + (parent.winfo_width() // 2) - (width // 2)
    y = parent.winfo_y() + (parent.winfo_height() // 2) - (height // 2)
    popup.geometry(f"{width}x{height}+{x}+{y}")
    
    popup.transient(parent)
    popup.grab_set()
    
    def on_close():
        popup.grab_release()
        popup.destroy()
    
    popup.protocol("WM_DELETE_WINDOW", on_close)
    
    # Main title
    tk.Label(popup, text="📖 HOW TO PLAY TECH RUN", 
             font=("Segoe UI", 18, "bold"),
             bg=colors["panel_bg"], fg=colors["accent"]).pack(pady=(12, 8))
    
    # Tab buttons
    tab_frame = tk.Frame(popup, bg=colors["panel_bg"])
    tab_frame.pack(pady=(0, 6))
    
    # Content area
    content_frame = tk.Frame(popup, bg=colors["panel_bg"], height=300)
    content_frame.pack(fill="both", expand=True, padx=25, pady=(0, 5))
    content_frame.pack_propagate(False)
    
    # Text widget for color-coded instructions
    text_widget = tk.Text(content_frame, 
                         bg=colors["panel_bg"], 
                         font=("Segoe UI", 11),
                         wrap=tk.WORD,
                         padx=40, pady=6,
                         relief="flat",
                         height=14,
                         width=65,
                         state="disabled")
    text_widget.pack(fill="both", expand=True)
    
    # Configure text color tags
    text_widget.tag_config("header", foreground=color_tags["header"], 
                          font=("Segoe UI", 11, "bold"))
    text_widget.tag_config("subheader", foreground=color_tags["subheader"], 
                          font=("Segoe UI", 11, "bold"))
    text_widget.tag_config("bullet", foreground=color_tags["bullet"])
    text_widget.tag_config("positive", foreground=color_tags["positive"])
    text_widget.tag_config("negative", foreground=color_tags["negative"])
    text_widget.tag_config("warning", foreground=color_tags["warning"])
    text_widget.tag_config("info", foreground=color_tags["info"])
    text_widget.tag_config("highlight", foreground=color_tags["highlight"])
    text_widget.tag_config("secondary", foreground=color_tags["secondary"])
    text_widget.tag_config("code", foreground=color_tags["code"], 
                          font=config.FONTS["code"])
    
    # Tab content definitions
    tab_contents = {
        "gameplay": [
            ("🎮 ", "header"), ("GAMEPLAY BASICS\n\n", "header"),
            ("• Answer technology questions correctly\n", "bullet"),
            ("• Each correct answer = ", "bullet"), ("+1 point\n", "positive"),
            ("• Wrong answer ends your current run\n", "bullet"),
            ("• Score ", "bullet"), ("auto-saves to leaderboard\n\n", "highlight"),
            
            ("SCORING:\n", "subheader"),
            ("• Each correct answer = ", "bullet"), ("+1 point\n", "positive"),
            ("• Using a hint = ", "bullet"), ("-1 point\n", "negative"),
            ("• Score = ", "bullet"), ("points minus hint costs\n", "positive"),
            ("• Example: ", "bullet"), ("3 correct, 1 hint = 2 points\n", "highlight"),
            ("\n", "bullet"),
            
            ("LEADERBOARD:\n", "subheader"),
            ("• Top 5 scores saved\n", "bullet"),
            ("• Compare with friends!", "bullet")
        ],
        
        "hints": [
            ("💡 ", "header"), ("HINT SYSTEM\n\n", "header"),
            ("Hints cost ", "bullet"), ("1 point", "negative"), (" from your score.\n\n", "bullet"),
            ("TEXT MODE:\n", "subheader"),
            ("• Shows a helpful clue\n", "bullet"),
            ("• Learn technology concepts\n", "bullet"),
            ("• Example: ", "bullet"), ('"This protocol starts with HTTP"\n\n', "code"),
            ("50/50 MODE:\n", "subheader"),
            ("• Removes two wrong answers\n", "bullet"),
            ("• Improves your odds\n", "bullet"),
            ("• Pure game strategy", "bullet")
        ],
        
        "buttons": [
            ("🎯 ", "header"), ("CONTROLS & BUTTONS\n\n", "header"),
            ("MAIN MENU:\n", "subheader"),
            ("• ", "bullet"), ("Start Game", "positive"), (" - Begin quiz\n", "bullet"),
            ("• ", "bullet"), ("How to Play", "warning"), (" - This guide!\n", "bullet"),
            ("• ", "bullet"), ("Settings", "info"), (" - Customize game\n", "bullet"),
            ("• ", "bullet"), ("Leaderboard", "secondary"), (" - Top scores\n\n", "bullet"),
            ("IN-GAME (SIDEBAR):\n", "subheader"),
            ("• ", "bullet"), ("Use Hint (-1)", "warning"), (" - Buy clue\n", "bullet"),
            ("• ", "bullet"), ("Exit Game", "negative"), (" - Return to menu\n\n", "bullet"),
            ("ANSWER BUTTONS:\n", "subheader"),
            ("• Click to select answer\n", "bullet"),
            ("• ", "bullet"), ("Green", "positive"), (" = correct\n", "bullet"),
            ("• ", "bullet"), ("Red", "negative"), (" = wrong", "bullet")
        ]
    }
    
    def show_tab(tab_name, btn):
        """Display selected tab content with color coding."""
        # Update tab button states
        for b in [gameplay_btn, hints_btn, buttons_btn]:
            style_button(b, "toggle_inactive")
        
        style_button(btn, "toggle_active")
        
        # Update content
        text_widget.config(state="normal")
        text_widget.delete(1.0, tk.END)
        
        for text, tag in tab_contents[tab_name]:
            text_widget.insert(tk.END, text, tag)
        
        # Center-aligned with left margin
        text_widget.tag_add("centered_left", "1.0", "end")
        text_widget.tag_config("centered_left", justify="left", lmargin1=30, lmargin2=30)
    
        text_widget.config(state="disabled")
        text_widget.see(1.0)
    
    # Create tab buttons
    gameplay_btn = tk.Button(tab_frame, text="🎮 GAMEPLAY", width=14,
                           command=lambda: [audio.play_sfx("click"), show_tab("gameplay", gameplay_btn)])
    gameplay_btn.pack(side="left", padx=3)
    style_button(gameplay_btn, "toggle_inactive")
    
    hints_btn = tk.Button(tab_frame, text="💡 HINTS", width=14,
                        command=lambda: [audio.play_sfx("click"), show_tab("hints", hints_btn)])
    hints_btn.pack(side="left", padx=3)
    style_button(hints_btn, "toggle_inactive")
    
    buttons_btn = tk.Button(tab_frame, text="🎯 BUTTONS", width=14,
                          command=lambda: [audio.play_sfx("click"), show_tab("buttons", buttons_btn)])
    buttons_btn.pack(side="left", padx=3)
    style_button(buttons_btn, "toggle_inactive")
    
    # Close button section
    close_frame = tk.Frame(popup, bg=colors["panel_bg"], height=45)
    close_frame.pack(side="bottom", fill="x", pady=(0, 8))
    close_frame.pack_propagate(False)
    
    def on_close_click():
        audio.play_sfx("click")
        on_close()
    
    close_btn = tk.Button(close_frame, text="CLOSE", 
                         font=config.FONTS["btn"],
                         width=20,
                         command=on_close_click)
    style_button(close_btn, "danger")
    close_btn.pack(expand=True)
    
    # Show default tab
    show_tab("gameplay", gameplay_btn)
    
    parent.wait_window(popup)

def show_leaderboard(parent_window):
    """Display high score table with top 5 rankings."""
    global _leaderboard_window
    
    # Bring to front if already open
    if _leaderboard_window is not None and _leaderboard_window.winfo_exists():
        _leaderboard_window.lift()
        _leaderboard_window.focus_force()
        return
    
    colors = get_current_colors()
    lb_window = tk.Toplevel(parent_window)
    _leaderboard_window = lb_window
    lb_window.title("Tech Run - Leaderboard")
    lb_window.configure(bg=colors["bg"])
    lb_window.resizable(False, False)
    
    width, height = 400, 500
    x = parent_window.winfo_x() + (parent_window.winfo_width() // 2) - (width // 2)
    y = parent_window.winfo_y() + (parent_window.winfo_height() // 2) - (height // 2)
    lb_window.geometry(f"{width}x{height}+{x}+{y}")
    
    lb_window.transient(parent_window)
    lb_window.grab_set()
    
    def on_close():
        global _leaderboard_window
        lb_window.grab_release()
        _leaderboard_window = None
        lb_window.destroy()
    
    lb_window.protocol("WM_DELETE_WINDOW", on_close)
    
    # Title
    tk.Label(lb_window, text="🏆 TOP SCORES 🏆", font=config.FONTS["header"], 
             bg=colors["bg"], fg=colors["score"], pady=20).pack(side="top")

    # Scores table
    table_frame = tk.Frame(lb_window, bg=colors["bg"])
    table_frame.pack(side="top", padx=20, pady=10, fill="both", expand=True)
    
    try:
        top_scores = get_high_scores()
    except Exception as e:
        print(f"ERROR loading high scores: {e}")
        top_scores = []
    
    if not top_scores:
        tk.Label(table_frame, text="No records found.", font=config.FONTS["body"], 
                 bg=colors["bg"], fg=colors["fg"]).pack(pady=50)
    else:
        for idx, (name, score) in enumerate(top_scores):
            row_frame = tk.Frame(table_frame, bg=colors["bg"])
            row_frame.pack(fill="x", pady=5)
            
            # Gold for 1st place, accent for others
            rank_color = colors["score"] if idx == 0 else colors["accent"]
            tk.Label(row_frame, text=f"{idx+1}.", font=config.FONTS["body"], 
                     bg=colors["bg"], fg=rank_color, width=4, anchor="w").pack(side="left")
            
            tk.Label(row_frame, text=name, font=config.FONTS["body"], 
                     bg=colors["bg"], fg=colors["fg"], anchor="w").pack(side="left", fill="x", expand=True)
            
            tk.Label(row_frame, text=f"{score} pts", font=config.FONTS["body"], 
                     bg=colors["bg"], fg=colors["success"], anchor="e").pack(side="right")
            
            # Separator between rows
            if idx < len(top_scores) - 1:
                tk.Frame(table_frame, height=1, bg=colors["btn_active"]).pack(fill="x", pady=2)

    # Close button
    close_btn = tk.Button(lb_window, text="CLOSE", font=config.FONTS["btn"], width=20, command=on_close)
    style_button(close_btn, "danger")
    close_btn.bind("<Button-1>", lambda e: audio.play_sfx("click"), add="+")
    close_btn.pack(side="bottom", pady=20)

def open_settings(parent_window, refresh_callback):
    """Display settings window with theme, hint mode, and sound toggles."""
    global _settings_window
    
    # Bring to front if already open
    if _settings_window is not None and _settings_window.winfo_exists():
        _settings_window.lift()
        _settings_window.focus_force()
        return
    
    sw = tk.Toplevel(parent_window)
    _settings_window = sw
    sw.title("Tech Run - Settings")
    sw.resizable(False, False)
    
    width, height = 350, 450
    x = parent_window.winfo_x() + (parent_window.winfo_width() // 2) - (width // 2)
    y = parent_window.winfo_y() + (parent_window.winfo_height() // 2) - (height // 2)
    sw.geometry(f"{width}x{height}+{x}+{y}")
    
    sw.transient(parent_window)
    sw.grab_set()
    
    def on_close():
        global _settings_window
        sw.grab_release()
        _settings_window = None
        sw.destroy()
    
    sw.protocol("WM_DELETE_WINDOW", on_close)
    
    def apply_theme_to_window():
        """Update window colors when theme changes."""
        colors = get_current_colors()
        sw.configure(bg=colors["panel_bg"])
        
        for widget in sw.winfo_children():
            if isinstance(widget, tk.Label):
                if widget["text"] == "⚙ SETTINGS":
                    widget.config(bg=colors["panel_bg"], fg=colors["accent"])
                else:
                    widget.config(bg=colors["panel_bg"], fg=colors["fg"])
            elif isinstance(widget, tk.Frame):
                widget.config(bg=colors["panel_bg"])
    
    # Settings title
    lbl_title = tk.Label(sw, text="⚙ SETTINGS", font=config.FONTS["btn"])
    lbl_title.pack(pady=20)
    
    # Theme selection
    tk.Label(sw, text="VISUAL THEME", font=config.FONTS["body"]).pack(pady=5)
    frame_theme = tk.Frame(sw)
    frame_theme.pack(pady=5)
    
    btn_dark = tk.Button(frame_theme, text="DARK", width=15)
    btn_dark.pack(side="left", padx=5)
    
    btn_light = tk.Button(frame_theme, text="LIGHT", width=15)
    btn_light.pack(side="left", padx=5)
    
    # Hint mode selection
    tk.Label(sw, text="HINT MODE", font=config.FONTS["body"]).pack(pady=(20, 5))
    frame_hint = tk.Frame(sw)
    frame_hint.pack(pady=5)
    
    btn_text = tk.Button(frame_hint, text="TEXT", width=15)
    btn_text.pack(side="left", padx=5)
    
    btn_50 = tk.Button(frame_hint, text="50/50", width=15)
    btn_50.pack(side="left", padx=5)
    
    # Sound toggle
    tk.Label(sw, text="SOUND", font=config.FONTS["body"]).pack(pady=(20, 5))
    frame_sound = tk.Frame(sw)
    frame_sound.pack(pady=5)
    
    btn_sound_on = tk.Button(frame_sound, text="ON", width=15)
    btn_sound_on.pack(side="left", padx=5)
    
    btn_sound_off = tk.Button(frame_sound, text="OFF", width=15)
    btn_sound_off.pack(side="left", padx=5)
    
    # Close button
    btn_close = tk.Button(sw, text="CLOSE", width=15, command=on_close)
    style_button(btn_close, "danger")
    btn_close.bind("<Button-1>", lambda e: audio.play_sfx("click"), add="+")
    btn_close.pack(side="bottom", pady=20)
    
    # Add click sounds to all toggle buttons
    for btn in [btn_dark, btn_light, btn_text, btn_50, btn_sound_on, btn_sound_off]:
        btn.bind("<Button-1>", lambda e: audio.play_sfx("click"), add="+")
    
    def update_toggle_buttons():
        """Update toggle button states based on current settings."""
        # Theme buttons
        if get_theme() == "DARK":
            style_button(btn_dark, "toggle_active")
            style_button(btn_light, "toggle_inactive")
        else:
            style_button(btn_light, "toggle_active")
            style_button(btn_dark, "toggle_inactive")
        
        # Hint mode buttons
        if get_hint_status() == "50/50":
            style_button(btn_50, "toggle_active")
            style_button(btn_text, "toggle_inactive")
        else:
            style_button(btn_text, "toggle_active")
            style_button(btn_50, "toggle_inactive")
        
        # Sound buttons
        if config.get_sound_status():
            style_button(btn_sound_on, "toggle_active")
            style_button(btn_sound_off, "toggle_inactive")
        else:
            style_button(btn_sound_off, "toggle_active")
            style_button(btn_sound_on, "toggle_inactive")
        
        apply_theme_to_window()
    
    # Connect button actions
    btn_dark.config(command=lambda: [set_theme("DARK"), refresh_callback(), update_toggle_buttons()])
    btn_light.config(command=lambda: [set_theme("LIGHT"), refresh_callback(), update_toggle_buttons()])
    btn_text.config(command=lambda: [set_hint_status("TEXT"), update_toggle_buttons()])
    btn_50.config(command=lambda: [set_hint_status("50/50"), update_toggle_buttons()])
    btn_sound_on.config(command=lambda: [config.set_sound_status(True), update_toggle_buttons()])
    btn_sound_off.config(command=lambda: [config.set_sound_status(False), update_toggle_buttons()])
    
    update_toggle_buttons()