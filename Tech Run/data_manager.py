"""
TECH RUN - Data Persistence Manager
Handles saving and loading high scores to a local text file.
"""

import os
import config

def save_high_score(name, score):
    """Append new score entry to CSV file (Name,Score format)."""
    try:
        with open(config.HIGH_SCORE_FILE, "a") as f: 
            f.write(f"{name},{score}\n")
    except: 
        pass  # Silent fail for read-only systems

def get_high_scores():
    """Read file and return top 5 unique high scores per player."""
    best_scores = {}
    
    if not os.path.exists(config.HIGH_SCORE_FILE): 
        return []
        
    try:
        with open(config.HIGH_SCORE_FILE, "r") as f:
            for line in f:
                if "," in line:
                    parts = line.strip().rsplit(",", 1)
                    if len(parts) == 2:
                        name, s = parts[0], int(parts[1])
                        # Keep highest score per player
                        if name not in best_scores or s > best_scores[name]:
                            best_scores[name] = s
    except: 
        pass
        
    # Sort descending and return top 5
    scores = list(best_scores.items())
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:5]