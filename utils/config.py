"""Configuration and constants for the application."""

import os
from pathlib import Path

# Application Settings
APP_NAME = "Advanced Text Encryption Suite"
APP_VERSION = "1.0.0"
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 850

# Paths
BASE_DIR = Path(__file__).parent.parent
KEYS_DIR = BASE_DIR / "keys"
HISTORY_DIR = BASE_DIR / "history"
ASSETS_DIR = BASE_DIR / "assets"

# Create directories if they don't exist
KEYS_DIR.mkdir(exist_ok=True)
HISTORY_DIR.mkdir(exist_ok=True)
ASSETS_DIR.mkdir(exist_ok=True)

# Color Scheme (Cybersecurity Theme)
COLORS = {
    "dark_bg": "#0d1117",
    "darker_bg": "#010409",
    "card_bg": "#161b22",
    "border": "#30363d",
    "text_primary": "#c9d1d9",
    "text_secondary": "#8b949e",
    "accent_primary": "#1f6feb",  # Blue
    "accent_secondary": "#58a6ff",  # Light Blue
    "success": "#3fb950",  # Green
    "warning": "#d29922",  # Orange
    "error": "#f85149",  # Red
}

# Theme Settings
THEMES = {
    "dark": {
        "bg": COLORS["dark_bg"],
        "fg": COLORS["text_primary"],
        "accent": COLORS["accent_primary"],
    },
    "light": {
        "bg": "#ffffff",
        "fg": "#000000",
        "accent": "#0066cc",
    }
}

# Font Settings
FONTS = {
    "title": ("Segoe UI", 24, "bold"),
    "heading": ("Segoe UI", 18, "bold"),
    "subheading": ("Segoe UI", 14, "bold"),
    "regular": ("Segoe UI", 11),
    "small": ("Segoe UI", 9),
    "mono": ("Courier New", 10),
}

# Algorithm Configurations
ALGORITHMS = {
    "AES": {
        "name": "AES-256 CBC",
        "description": "Advanced Encryption Standard with 256-bit key in CBC mode",
        "key_size": "256 bits",
        "is_symmetric": True,
    },
    "DES": {
        "name": "DES CBC",
        "description": "Data Encryption Standard in CBC mode",
        "key_size": "64 bits",
        "is_symmetric": True,
    },
    "3DES": {
        "name": "Triple DES",
        "description": "Triple Data Encryption Standard",
        "key_size": "192 bits",
        "is_symmetric": True,
    },
    "RSA": {
        "name": "RSA-2048",
        "description": "Rivest-Shamir-Adleman with 2048-bit key",
        "key_size": "2048 bits",
        "is_symmetric": False,
    },
    "Fernet": {
        "name": "Fernet",
        "description": "Symmetric encryption with automatic timestamp",
        "key_size": "256 bits",
        "is_symmetric": True,
    },
}

# Status Messages
STATUS_MESSAGES = {
    "ready": "Ready",
    "encrypting": "Encrypting...",
    "encryption_success": "Encryption Successful ✓",
    "decrypting": "Decrypting...",
    "decryption_success": "Decryption Successful ✓",
    "error": "Error occurred",
    "file_processing": "Processing file...",
}

# RSA Key File Names
RSA_PUBLIC_KEY_FILE = "rsa_public_key.pem"
RSA_PRIVATE_KEY_FILE = "rsa_private_key.pem"

# History File Name
HISTORY_FILE = "encryption_history.json"
