"""Utility functions for the application."""

import hashlib
import base64
from typing import Optional


def hash_password(password: str, salt: bytes = None) -> tuple:
    """Hash a password using SHA-256.
    
    Args:
        password: Password to hash.
        salt: Optional salt bytes.
    
    Returns:
        Tuple of (hashed_password, salt) as base64 encoded strings.
    """
    import os
    if salt is None:
        salt = os.urandom(16)
    
    hash_obj = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return base64.b64encode(hash_obj).decode('utf-8'), base64.b64encode(salt).decode('utf-8')


def verify_password(password: str, hashed_password: str, salt: str) -> bool:
    """Verify a password against its hash.
    
    Args:
        password: Password to verify.
        hashed_password: Base64 encoded hashed password.
        salt: Base64 encoded salt.
    
    Returns:
        True if password matches, False otherwise.
    """
    try:
        salt_bytes = base64.b64decode(salt)
        computed_hash, _ = hash_password(password, salt_bytes)
        return computed_hash == hashed_password
    except Exception:
        return False


def is_valid_base64(text: str) -> bool:
    """Check if a string is valid base64.
    
    Args:
        text: String to check.
    
    Returns:
        True if valid base64, False otherwise.
    """
    try:
        if isinstance(text, str):
            text_bytes = bytes(text, 'utf-8')
        elif isinstance(text, bytes):
            text_bytes = text
        else:
            return False
        return base64.b64encode(base64.b64decode(text_bytes)) == text_bytes
    except Exception:
        return False


def format_key_for_display(key: str, max_length: int = 50) -> str:
    """Format a key for display purposes.
    
    Args:
        key: Key to format.
        max_length: Maximum length to display.
    
    Returns:
        Formatted key string.
    """
    if len(key) > max_length:
        return key[:max_length // 2] + "..." + key[-max_length // 4:]
    return key


def truncate_text(text: str, max_length: int = 100) -> str:
    """Truncate text for display.
    
    Args:
        text: Text to truncate.
        max_length: Maximum length.
    
    Returns:
        Truncated text.
    """
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text


def format_file_size(size_bytes: int) -> str:
    """Format file size in human readable format.
    
    Args:
        size_bytes: Size in bytes.
    
    Returns:
        Formatted size string.
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"
