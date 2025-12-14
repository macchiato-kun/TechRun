"""
TECH RUN - Audio Manager
Handles background music and sound effects with volume control.
"""
import os
import config

# --- SETUP ---
AUDIO_ENABLED = False
try:
    import pygame
    pygame.mixer.init()
    AUDIO_ENABLED = True
except ImportError:
    pass

# --- PLAYBACK ---
def play_bgm():
    """Start menu background music with multi-format support."""
    if not AUDIO_ENABLED or not config.SOUND_ENABLED:
        return
    try:
        possible_paths = [
            os.path.join(config.SOUND_DIR, "menu_music.mp3"),
            os.path.join(config.SOUND_DIR, "menu_music.wav"),
            os.path.join(config.SOUND_DIR, "menu_music.ogg")
        ]
        
        path = None
        for p in possible_paths:
            if os.path.exists(p):
                path = p
                break
        
        if not path:
            return
            
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(path)
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.7 if config.SOUND_ENABLED else 0.0)
    except:
        pass

def play_gameplay_bgm():
    """Switch to gameplay music when game starts."""
    if not AUDIO_ENABLED or not config.SOUND_ENABLED:
        return
    try:
        possible_paths = [
            os.path.join(config.SOUND_DIR, "gameplay_music.mp3"),
            os.path.join(config.SOUND_DIR, "gameplay_music.wav"),
            os.path.join(config.SOUND_DIR, "gameplay_music.ogg")
        ]
        
        path = None
        for p in possible_paths:
            if os.path.exists(p):
                path = p
                break
        
        if not path:
            return
            
        pygame.mixer.music.stop()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.7 if config.SOUND_ENABLED else 0.0)
    except:
        pass

def play_sfx(sound_name):
    """Play sound effect with volume boosts for feedback."""
    if not AUDIO_ENABLED or not config.SOUND_ENABLED:
        return
    try:
        wav_path = os.path.join(config.SOUND_DIR, f"{sound_name}.wav")
        mp3_path = os.path.join(config.SOUND_DIR, f"{sound_name}.mp3")
        
        path = None
        if os.path.exists(wav_path):
            path = wav_path
        elif os.path.exists(mp3_path):
            path = mp3_path
        
        if not path:
            return
            
        sound = pygame.mixer.Sound(path)
        
        volume_boost = {
            "wrong": 2.0,
            "correct": 1.2,
            "click": 1.5,
            "hint": 1.0,
            "start": 1.0,
            "end": 1.0
        }
        
        volume = volume_boost.get(sound_name, 1.0)
        sound.set_volume(volume)
        sound.play()
    except:
        pass

def stop_bgm():
    """Stop background music completely."""
    if AUDIO_ENABLED:
        try:
            pygame.mixer.music.stop()
        except:
            pass

def switch_to_menu_music():
    """Force switch back to menu music with clean reset."""
    if not AUDIO_ENABLED:
        return
    try:
        stop_bgm()
        if config.SOUND_ENABLED:
            play_bgm()
    except:
        pass

def update_music_volume():
    """Update music volume based on current mute status."""
    if not AUDIO_ENABLED:
        return
    try:
        if pygame.mixer.music.get_busy():
            if config.SOUND_ENABLED:
                current_vol = pygame.mixer.music.get_volume()
                if current_vol > 0:
                    new_vol = 0.8 if current_vol >= 0.8 else 0.7
                    pygame.mixer.music.set_volume(new_vol)
                else:
                    pygame.mixer.music.set_volume(0.7)
            else:
                pygame.mixer.music.set_volume(0.0)
    except:
        pass