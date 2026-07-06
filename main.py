"""Main Application - Advanced Text Encryption Suite."""

import customtkinter as ctk
from pathlib import Path
import sys

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from utils.config import (
    APP_NAME, APP_VERSION, WINDOW_WIDTH, WINDOW_HEIGHT, 
    COLORS, FONTS, KEYS_DIR, HISTORY_DIR
)
from ui import (
    DashboardPage,
    EncryptionPage,
    DecryptionPage,
    RSAKeyPage,
    FileEncryptionPage,
    HistoryPage,
    SettingsPage,
)


class MainApplication(ctk.CTk):
    """Main application window."""
    
    def __init__(self):
        """Initialize the main application."""
        super().__init__()
        
        # Window configuration
        self.title(f"{APP_NAME} v{APP_VERSION}")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.minsize(1200, 700)
        
        # Set appearance mode
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Configure grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Pages dictionary
        self.pages = {}
        self.current_page = None
        
        # Create UI
        self._create_sidebar()
        self._create_main_panel()
        self._create_status_bar()
        
        # Load dashboard by default
        self.show_page("Dashboard")
    
    def _create_sidebar(self):
        """Create the left sidebar."""
        self.sidebar = ctk.CTkFrame(
            self,
            fg_color=COLORS["card_bg"],
            border_width=1,
            border_color=COLORS["border"],
            corner_radius=0,
        )
        self.sidebar.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self.sidebar.grid_rowconfigure(8, weight=1)
        
        # Logo / Title
        logo_label = ctk.CTkLabel(
            self.sidebar,
            text="🔐",
            font=("Arial", 32),
            text_color=COLORS["accent_secondary"],
        )
        logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        app_title = ctk.CTkLabel(
            self.sidebar,
            text="ENCRYPTION",
            font=FONTS["heading"],
            text_color=COLORS["accent_secondary"],
        )
        app_title.grid(row=1, column=0, padx=20, pady=(0, 30))
        
        # Navigation buttons
        nav_items = [
            ("🏠 Dashboard", "Dashboard"),
            ("🔐 Encrypt", "Encryption"),
            ("🔓 Decrypt", "Decryption"),
            ("🔑 RSA Keys", "RSA Keys"),
            ("📁 File Encryption", "File Encryption"),
            ("📊 History", "History"),
            ("⚙️ Settings", "Settings"),
        ]
        
        self.nav_buttons = {}
        for idx, (label, page_name) in enumerate(nav_items):
            btn = ctk.CTkButton(
                self.sidebar,
                text=label,
                command=lambda pn=page_name: self.show_page(pn),
                fg_color=COLORS["card_bg"],
                hover_color=COLORS["border"],
                text_color=COLORS["text_primary"],
                font=FONTS["regular"],
                corner_radius=8,
                anchor="w",
                border_width=0,
            )
            btn.grid(row=2 + idx, column=0, sticky="ew", padx=15, pady=8)
            self.nav_buttons[page_name] = btn
        
        # Divider
        divider = ctk.CTkFrame(
            self.sidebar,
            height=1,
            fg_color=COLORS["border"],
        )
        divider.grid(row=9, column=0, sticky="ew", padx=15, pady=(20, 20))
        
        # About button
        about_btn = ctk.CTkButton(
            self.sidebar,
            text="ℹ️ About",
            command=self._show_about,
            fg_color=COLORS["border"],
            hover_color=COLORS["accent_secondary"],
            text_color=COLORS["text_primary"],
            font=FONTS["regular"],
            corner_radius=8,
            border_width=0,
        )
        about_btn.grid(row=10, column=0, sticky="ew", padx=15, pady=8)
    
    def _create_main_panel(self):
        """Create the main content panel."""
        self.main_panel = ctk.CTkFrame(
            self,
            fg_color=COLORS["dark_bg"],
            corner_radius=0,
        )
        self.main_panel.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)
        self.main_panel.grid_columnconfigure(0, weight=1)
        self.main_panel.grid_rowconfigure(0, weight=1)
        
        # Pages container
        self.pages_container = ctk.CTkFrame(
            self.main_panel,
            fg_color=COLORS["dark_bg"],
            corner_radius=0,
        )
        self.pages_container.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self.pages_container.grid_columnconfigure(0, weight=1)
        self.pages_container.grid_rowconfigure(0, weight=1)
        
        # Create all pages
        self._create_pages()
    
    def _create_pages(self):
        """Create all application pages."""
        # Dashboard
        self.pages["Dashboard"] = DashboardPage(self.pages_container)
        self.pages["Dashboard"].grid(row=0, column=0, sticky="nsew")
        
        # Encryption
        self.pages["Encryption"] = EncryptionPage(
            self.pages_container,
            on_status_change=self._update_status,
        )
        self.pages["Encryption"].grid(row=0, column=0, sticky="nsew")
        
        # Decryption
        self.pages["Decryption"] = DecryptionPage(
            self.pages_container,
            on_status_change=self._update_status,
        )
        self.pages["Decryption"].grid(row=0, column=0, sticky="nsew")
        
        # RSA Keys
        self.pages["RSA Keys"] = RSAKeyPage(
            self.pages_container,
            on_status_change=self._update_status,
        )
        self.pages["RSA Keys"].grid(row=0, column=0, sticky="nsew")
        
        # File Encryption
        self.pages["File Encryption"] = FileEncryptionPage(
            self.pages_container,
            on_status_change=self._update_status,
        )
        self.pages["File Encryption"].grid(row=0, column=0, sticky="nsew")
        
        # History
        self.pages["History"] = HistoryPage(self.pages_container)
        self.pages["History"].grid(row=0, column=0, sticky="nsew")
        
        # Settings
        self.pages["Settings"] = SettingsPage(
            self.pages_container,
            on_theme_change=self._on_theme_change,
            on_font_change=self._on_font_change,
        )
        self.pages["Settings"].grid(row=0, column=0, sticky="nsew")
    
    def _create_status_bar(self):
        """Create the status bar."""
        self.status_bar = ctk.CTkFrame(
            self,
            fg_color=COLORS["card_bg"],
            border_width=1,
            border_color=COLORS["border"],
            height=40,
        )
        self.status_bar.grid(row=1, column=0, columnspan=2, sticky="ew", padx=0, pady=0)
        self.status_bar.grid_columnconfigure(0, weight=1)
        self.status_bar.pack_propagate(False)
        
        self.status_label = ctk.CTkLabel(
            self.status_bar,
            text="Ready",
            text_color=COLORS["success"],
            font=FONTS["regular"],
            anchor="w",
        )
        self.status_label.pack(side="left", padx=15, pady=10)
    
    def show_page(self, page_name: str):
        """Show a specific page.
        
        Args:
            page_name: Name of the page to show.
        """
        if page_name not in self.pages:
            return
        
        # Hide all pages
        for page in self.pages.values():
            page.grid_remove()
        
        # Show selected page
        self.pages[page_name].grid()
        self.current_page = page_name
        
        # Update sidebar buttons
        for btn_name, btn in self.nav_buttons.items():
            if btn_name == page_name:
                btn.configure(
                    fg_color=COLORS["accent_primary"],
                    text_color=COLORS["dark_bg"],
                )
            else:
                btn.configure(
                    fg_color=COLORS["card_bg"],
                    text_color=COLORS["text_primary"],
                )
        
        # Refresh page if it has a refresh method
        if hasattr(self.pages[page_name], 'refresh'):
            self.pages[page_name].refresh()
        
        # Reset status
        self._update_status("Ready")
    
    def _update_status(self, message: str):
        """Update status bar message.
        
        Args:
            message: Status message.
        """
        # Determine color based on message
        if "Success" in message or "✓" in message:
            color = COLORS["success"]
        elif "Error" in message or "✗" in message:
            color = COLORS["error"]
        elif "..." in message:
            color = COLORS["accent_secondary"]
        else:
            color = COLORS["text_secondary"]
        
        self.status_label.configure(text=message, text_color=color)
    
    def _on_theme_change(self, theme: str):
        """Handle theme change.
        
        Args:
            theme: "dark" or "light".
        """
        if theme == "dark":
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")
        
        self._update_status(f"Theme changed to {theme.capitalize()} mode")
    
    def _on_font_change(self, size: str):
        """Handle font size change.
        
        Args:
            size: "small", "medium", or "large".
        """
        self._update_status(f"Font size changed to {size}")
    
    def _show_about(self):
        """Show about dialog."""
        import tkinter.messagebox as messagebox
        about_text = f"""{APP_NAME}
Version {APP_VERSION}

A professional-grade encryption tool supporting multiple algorithms:
• AES-256 CBC
• DES CBC
• Triple DES
• RSA-2048
• Fernet

Features:
✓ Text Encryption & Decryption
✓ File Encryption & Decryption
✓ RSA Key Management
✓ Encryption History
✓ Modern UI with Cybersecurity Theme

Built with Python and CustomTkinter
Using cryptography library for secure encryption
        """
        messagebox.showinfo("About", about_text)


def main():
    """Main entry point."""
    app = MainApplication()
    app.mainloop()


if __name__ == "__main__":
    main()
