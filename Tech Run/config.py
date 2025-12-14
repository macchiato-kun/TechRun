"""
TECH RUN - Configuration & Style Manager
Centralized theming, fonts, and game settings.
"""
import os
import tkinter as tk

# --- PATHS ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOUND_DIR = os.path.join(BASE_DIR, "sounds")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
HIGH_SCORE_FILE = "highscores.txt"

# --- DEFAULTS ---
CURRENT_THEME = "DARK"
HINT_MODE = "TEXT"
SOUND_ENABLED = True

# --- THEME FUNCTIONS ---
def get_theme():
    return CURRENT_THEME

def set_theme(theme_name):
    global CURRENT_THEME
    if theme_name in THEMES:
        CURRENT_THEME = theme_name
        return True
    return False

def get_hint_status():
    return HINT_MODE

def set_hint_status(mode):
    global HINT_MODE
    HINT_MODE = mode

# --- SOUND FUNCTIONS ---
def toggle_sound():
    global SOUND_ENABLED
    SOUND_ENABLED = not SOUND_ENABLED
    
    import audio
    if audio.AUDIO_ENABLED:
        import pygame
        if SOUND_ENABLED:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.set_volume(0.7)
        else:
            pygame.mixer.music.set_volume(0.0)
    
    return SOUND_ENABLED

def set_sound_status(enabled):
    global SOUND_ENABLED
    new_status = bool(enabled)
    
    if SOUND_ENABLED != new_status:
        SOUND_ENABLED = new_status
        import audio
        if audio.AUDIO_ENABLED:
            import pygame
            if SOUND_ENABLED:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.set_volume(0.7)
            else:
                pygame.mixer.music.set_volume(0.0)
    
    return SOUND_ENABLED

def get_sound_status():
    return SOUND_ENABLED

# --- FONT SYSTEM ---
FONTS = {
    "header": ("Segoe UI", 28, "bold"),      # Modal headers
    "title": ("Orbitron", 36, "bold"),       # Main menu title
    "sidebar": ("Orbitron", 20, "bold"),     # Sidebar title
    
    "score": ("Segoe UI", 24, "bold"),       # Score numbers
    
    "btn": ("Segoe UI", 11, "bold"),         # All buttons
    "input": ("Segoe UI", 14),               # Text input fields
    
    "body": ("Segoe UI", 12),                # Regular paragraphs
    "hint": ("Segoe UI", 13),                # Hint/explanation text
    "code": ("Consolas", 11),                # Code/monospace text
    
    "small": ("Segoe UI", 10)                # Labels and captions
}

# --- COLOR SCHEMES ---
THEMES = {
    "DARK": {
        "bg": "#121212",
        "panel_bg": "#1E1E1E",
        
        "fg": "#FFFFFF",
        "fg_secondary": "#B0B0B0",
        "accent": "#64B5F6",
        
        "btn_bg": "#2D2D2D",
        "btn_fg": "#FFFFFF",
        "btn_subtle": "#424242",
        "btn_active": "#3D3D3D",
        
        "toggle_active": "#4CAF50",
        "toggle_inactive": "#2D2D2D",
        "toggle_text_active": "#FFFFFF",
        "toggle_text_inactive": "#B0B0B0",
        
        "success": "#4CAF50",
        "score": "#FFD700",
        "danger": "#F44336",
        "warning": "#FF9800",
        "info": "#2196F3",
        "gold": "#E6C300",
        
        "border": "#424242",
        "highlight": "#64B5F6",
        
        "how_to_play": "#D35400",
        "how_to_play_hover": "#E67E22"
    },
    "LIGHT": {
        "bg": "#F8F9FA",
        "panel_bg": "#FFFFFF",
        
        "fg": "#212121",
        "fg_secondary": "#666666",
        "accent": "#2196F3",
        
        "btn_bg": "#E0E0E0",
        "btn_fg": "#212121",
        "btn_subtle": "#B0BEC5",
        "btn_active": "#D5D5D5",
        
        "toggle_active": "#4CAF50",
        "toggle_inactive": "#E0E0E0",
        "toggle_text_active": "#FFFFFF",
        "toggle_text_inactive": "#666666",
        
        "success": "#4CAF50",
        "score": "#FFA000",
        "danger": "#F44336",
        "warning": "#FF9800",
        "info": "#2196F3",
        "gold": "#E69100",
        
        "border": "#E0E0E0",
        "highlight": "#2196F3",
        
        "how_to_play": "#E67E22",
        "how_to_play_hover": "#F39C12"
    }
}

def get_current_colors():
    return THEMES[CURRENT_THEME]

def style_button(btn, color_type="default"):
    """Apply consistent button styling with hover effects."""
    colors = get_current_colors()
    
    # Default styling
    base_bg = colors["btn_bg"]
    base_fg = colors["btn_fg"]
    active_bg = colors["btn_active"]
    active_fg = colors["accent"]
    
    # Color type overrides
    if color_type == "success":
        base_bg = colors["success"]
        base_fg = "#FFFFFF"
        active_bg = "#66BB6A" if CURRENT_THEME == "DARK" else "#81C784"
        active_fg = "#FFFFFF"
        
    elif color_type == "danger":
        base_bg = colors["danger"]
        base_fg = "#FFFFFF"
        active_bg = "#E53935" if CURRENT_THEME == "DARK" else "#EF5350"
        active_fg = "#FFFFFF"
        
    elif color_type == "info":
        base_bg = colors["info"]
        base_fg = "#FFFFFF"
        active_bg = "#1976D2" if CURRENT_THEME == "DARK" else "#42A5F5"
        active_fg = "#FFFFFF"
        
    elif color_type == "warning":
        base_bg = colors["warning"]
        base_fg = "#212121"
        active_bg = "#FB8C00" if CURRENT_THEME == "DARK" else "#FFB74D"
        active_fg = "#212121"
        
    elif color_type == "subtle":
        base_bg = colors["btn_subtle"]
        base_fg = colors["fg"]
        active_bg = colors["btn_active"]
        active_fg = colors["accent"]
        
    elif color_type == "toggle_active":
        base_bg = colors["toggle_active"]
        base_fg = colors["toggle_text_active"]
        active_bg = "#66BB6A" if CURRENT_THEME == "DARK" else "#81C784"
        active_fg = colors["toggle_text_active"]
        
    elif color_type == "toggle_inactive":
        base_bg = colors["toggle_inactive"]
        base_fg = colors["toggle_text_inactive"]
        active_bg = colors["btn_active"]
        active_fg = colors["accent"]
        
    elif color_type == "how_to_play":
        base_bg = colors["how_to_play"]
        base_fg = "#FFFFFF"
        active_bg = colors["how_to_play_hover"]
        active_fg = "#FFFFFF"

    # Apply base configuration
    btn.config(
        bg=base_bg, fg=base_fg,
        activebackground=active_bg, activeforeground=active_fg,
        relief="flat", bd=0, highlightthickness=0,
        font=FONTS["btn"], cursor="hand2"
    )
    
    # Hover effects
    def on_enter(e):
        if btn['state'] != 'disabled':
            btn.config(bg=active_bg)
            if color_type not in ["warning", "toggle_active", "toggle_inactive"]:
                btn.config(fg=active_fg)
            elif color_type == "toggle_inactive":
                btn.config(fg=colors["accent"])
    
    def on_leave(e):
        if btn['state'] != 'disabled':
            btn.config(bg=base_bg, fg=base_fg)

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)