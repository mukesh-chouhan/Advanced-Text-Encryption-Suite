"""History management for encryption operations."""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import List, Dict


class HistoryManager:
    """Manages encryption operation history."""
    
    def __init__(self, history_file: Path):
        """Initialize history manager.
        
        Args:
            history_file: Path to the history JSON file.
        """
        self.history_file = history_file
        self.history: List[Dict] = self._load_history()
    
    def _load_history(self) -> List[Dict]:
        """Load history from file.
        
        Returns:
            List of history entries.
        """
        if self.history_file.exists():
            try:
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                return []
        return []
    
    def add_entry(self, algorithm: str, operation: str, message_preview: str = "", 
                  key_preview: str = "", status: str = "success") -> None:
        """Add an entry to history.
        
        Args:
            algorithm: Encryption algorithm used.
            operation: "encrypt" or "decrypt".
            message_preview: First 50 characters of the message.
            key_preview: First 20 characters of the key.
            status: Operation status ("success", "failed").
        """
        entry = {
            "timestamp": datetime.now().isoformat(),
            "date": datetime.now().strftime("%Y-%m-%d"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "algorithm": algorithm,
            "operation": operation,
            "message_preview": message_preview[:50] if message_preview else "",
            "key_preview": key_preview[:20] if key_preview else "",
            "status": status,
        }
        self.history.append(entry)
        self._save_history()
    
    def get_history(self, limit: int = None) -> List[Dict]:
        """Get history entries.
        
        Args:
            limit: Maximum number of entries to return. None = all.
        
        Returns:
            List of history entries.
        """
        if limit:
            return self.history[-limit:]
        return self.history
    
    def clear_history(self) -> None:
        """Clear all history."""
        self.history = []
        self._save_history()
    
    def export_history(self, export_file: Path) -> None:
        """Export history to a file.
        
        Args:
            export_file: Path to export the history.
        """
        try:
            with open(export_file, 'w', encoding='utf-8') as f:
                json.dump(self.history, f, indent=2, ensure_ascii=False)
        except Exception as e:
            raise ValueError(f"Failed to export history: {str(e)}")
    
    def _save_history(self) -> None:
        """Save history to file."""
        try:
            self.history_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(self.history, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Warning: Could not save history: {str(e)}")
