"""History page."""

import customtkinter as ctk
from ui.components import CTkCard, CTkLabel, CTkLabelSecondary, CTkButton
from utils.config import COLORS, FONTS, HISTORY_DIR, HISTORY_FILE
from history.history_manager import HistoryManager
from pathlib import Path
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog


class HistoryPage(ctk.CTkFrame):
    """Encryption history page."""
    
    def __init__(self, master, **kwargs):
        """Initialize the history page.
        
        Args:
            master: Parent widget.
            **kwargs: Additional arguments for CTkFrame.
        """
        super().__init__(master, fg_color=COLORS["dark_bg"], **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Initialize history manager
        self.history_manager = HistoryManager(HISTORY_DIR / HISTORY_FILE)
        
        self._create_ui()
    
    def _create_ui(self):
        """Create the UI elements."""
        main_frame = ctk.CTkScrollableFrame(
            self,
            fg_color=COLORS["dark_bg"],
            scrollbar_button_color=COLORS["card_bg"],
            scrollbar_button_hover_color=COLORS["border"],
        )
        main_frame.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        main_frame.grid_columnconfigure(0, weight=1)
        
        # Title
        title_label = CTkLabel(
            main_frame,
            text="Encryption History",
            font=FONTS["heading"],
            text_color=COLORS["accent_secondary"],
        )
        title_label.pack(anchor="w", padx=30, pady=(30, 10))
        
        # Control buttons
        control_frame = ctk.CTkFrame(main_frame, fg_color=COLORS["dark_bg"])
        control_frame.pack(fill="x", padx=30, pady=(0, 20))
        control_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        
        refresh_btn = CTkButton(
            control_frame,
            text="🔄 Refresh",
            command=self.refresh,
        )
        refresh_btn.grid(row=0, column=0, sticky="ew", padx=(0, 5))
        
        export_btn = CTkButton(
            control_frame,
            text="📤 Export",
            command=self._export_history,
        )
        export_btn.grid(row=0, column=1, sticky="ew", padx=5)
        
        clear_btn = CTkButton(
            control_frame,
            text="🗑️ Clear History",
            fg_color=COLORS["error"],
            hover_color="#c5353b",
            command=self._clear_history,
        )
        clear_btn.grid(row=0, column=2, sticky="ew", padx=5)
        
        # History count
        count_label = CTkLabelSecondary(
            control_frame,
            text="",
        )
        count_label.grid(row=0, column=3, sticky="e", padx=(5, 0))
        self.count_label = count_label
        
        # History items container
        self.history_container = ctk.CTkFrame(main_frame, fg_color=COLORS["dark_bg"])
        self.history_container.pack(fill="both", expand=True, padx=30, pady=(0, 30))
        self.history_container.grid_columnconfigure(0, weight=1)
        
        self._update_history()
    
    def _update_history(self):
        """Update history display."""
        # Clear existing items
        for widget in self.history_container.winfo_children():
            widget.destroy()
        
        history = self.history_manager.get_history()
        
        # Update count
        self.count_label.configure(text=f"Total: {len(history)} entries")
        
        if not history:
            no_history_label = CTkLabel(
                self.history_container,
                text="No encryption history yet",
                text_color=COLORS["text_secondary"],
                font=FONTS["regular"],
            )
            no_history_label.pack(anchor="center", pady=40)
            return
        
        # Display history items (most recent first)
        for idx, entry in enumerate(reversed(history)):
            self._create_history_item(entry, idx)
    
    def _create_history_item(self, entry: dict, idx: int):
        """Create a history item card.
        
        Args:
            entry: History entry dictionary.
            idx: Index for layout.
        """
        item_card = CTkCard(self.history_container)
        item_card.pack(fill="x", padx=0, pady=(0, 10))
        item_card.grid_columnconfigure(1, weight=1)
        
        # Left side - Status icon
        status_icon = "✓" if entry["status"] == "success" else "✗"
        status_color = COLORS["success"] if entry["status"] == "success" else COLORS["error"]
        
        icon_label = CTkLabel(
            item_card,
            text=status_icon,
            font=("Arial", 20),
            text_color=status_color,
        )
        icon_label.grid(row=0, column=0, padx=15, pady=15, rowspan=3)
        
        # Algorithm name
        algo_label = CTkLabel(
            item_card,
            text=f"{entry['algorithm']} - {entry['operation'].title()}",
            font=FONTS["subheading"],
            text_color=COLORS["accent_secondary"],
        )
        algo_label.grid(row=0, column=1, sticky="w", padx=(10, 15), pady=(15, 5))
        
        # Date and Time
        datetime_label = CTkLabelSecondary(
            item_card,
            text=f"{entry['date']} at {entry['time']}",
        )
        datetime_label.grid(row=1, column=1, sticky="w", padx=(10, 15), pady=2)
        
        # Message preview
        msg_preview = entry.get("message_preview", "")
        if msg_preview:
            msg_label = CTkLabelSecondary(
                item_card,
                text=f"Message: {msg_preview[:50]}{'...' if len(msg_preview) > 50 else ''}",
                font=FONTS["small"],
            )
            msg_label.grid(row=2, column=1, sticky="w", padx=(10, 15), pady=(2, 15))
        else:
            empty_label = CTkLabelSecondary(
                item_card,
                text="No message preview available",
                font=FONTS["small"],
            )
            empty_label.grid(row=2, column=1, sticky="w", padx=(10, 15), pady=(2, 15))
    
    def _export_history(self):
        """Export history to file."""
        try:
            filename = filedialog.asksaveasfilename(
                defaultextension=".json",
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
            )
            
            if filename:
                self.history_manager.export_history(Path(filename))
                messagebox.showinfo("Success", f"History exported to {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export history: {str(e)}")
    
    def _clear_history(self):
        """Clear all history."""
        result = messagebox.askyesno(
            "Confirm",
            "Are you sure you want to clear all history?\nThis action cannot be undone."
        )
        
        if result:
            try:
                self.history_manager.clear_history()
                self._update_history()
                messagebox.showinfo("Success", "History cleared")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to clear history: {str(e)}")
    
    def refresh(self):
        """Refresh the history display."""
        self._update_history()
    
    def add_entry(self, algorithm: str, operation: str, message: str = "", key: str = ""):
        """Add an entry to history.
        
        Args:
            algorithm: Algorithm name.
            operation: "encrypt" or "decrypt".
            message: Message used.
            key: Encryption key.
        """
        try:
            self.history_manager.add_entry(
                algorithm=algorithm,
                operation=operation,
                message_preview=message,
                key_preview=key,
                status="success"
            )
            self._update_history()
        except Exception as e:
            print(f"Failed to add history entry: {str(e)}")
