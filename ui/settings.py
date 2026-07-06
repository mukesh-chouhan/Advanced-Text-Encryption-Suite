"""Settings page."""

import customtkinter as ctk
from ui.components import CTkCard, CTkLabel, CTkLabelSecondary, CTkButton
from utils.config import COLORS, FONTS


class SettingsPage(ctk.CTkFrame):
    """Settings page."""
    
    def __init__(self, master, on_theme_change=None, on_font_change=None, **kwargs):
        """Initialize the settings page.
        
        Args:
            master: Parent widget.
            on_theme_change: Callback for theme changes.
            on_font_change: Callback for font size changes.
            **kwargs: Additional arguments for CTkFrame.
        """
        super().__init__(master, fg_color=COLORS["dark_bg"], **kwargs)
        self.on_theme_change = on_theme_change
        self.on_font_change = on_font_change
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
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
            text="Settings",
            font=FONTS["heading"],
            text_color=COLORS["accent_secondary"],
        )
        title_label.pack(anchor="w", padx=30, pady=(30, 10))
        
        # Appearance Section
        appearance_card = CTkCard(main_frame)
        appearance_card.pack(fill="x", padx=30, pady=(0, 20))
        appearance_card.pack_propagate(False)
        appearance_card.configure(height=200)
        
        appearance_label = CTkLabel(
            appearance_card,
            text="🎨 Appearance",
            font=FONTS["subheading"],
        )
        appearance_label.pack(anchor="w", padx=15, pady=(15, 15))
        
        # Theme Mode
        theme_label = CTkLabel(
            appearance_card,
            text="Theme Mode",
            font=FONTS["regular"],
        )
        theme_label.pack(anchor="w", padx=15, pady=(0, 10))
        
        self.theme_var = ctk.StringVar(value="dark")
        theme_frame = ctk.CTkFrame(appearance_card, fg_color=COLORS["card_bg"])
        theme_frame.pack(fill="x", padx=15, pady=(0, 15))
        theme_frame.grid_columnconfigure((0, 1), weight=1)
        
        dark_radio = ctk.CTkRadioButton(
            theme_frame,
            text="🌙 Dark",
            variable=self.theme_var,
            value="dark",
            command=self._on_theme_change,
        )
        dark_radio.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        
        light_radio = ctk.CTkRadioButton(
            theme_frame,
            text="☀️ Light",
            variable=self.theme_var,
            value="light",
            command=self._on_theme_change,
        )
        light_radio.grid(row=0, column=1, sticky="w", padx=10, pady=10)
        
        # Font Size
        font_label = CTkLabel(
            appearance_card,
            text="Font Size",
            font=FONTS["regular"],
        )
        font_label.pack(anchor="w", padx=15, pady=(0, 10))
        
        self.font_var = ctk.StringVar(value="medium")
        font_frame = ctk.CTkFrame(appearance_card, fg_color=COLORS["card_bg"])
        font_frame.pack(fill="x", padx=15, pady=(0, 15))
        font_frame.grid_columnconfigure((0, 1, 2), weight=1)
        
        small_radio = ctk.CTkRadioButton(
            font_frame,
            text="Small",
            variable=self.font_var,
            value="small",
            command=self._on_font_change,
        )
        small_radio.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        
        medium_radio = ctk.CTkRadioButton(
            font_frame,
            text="Medium",
            variable=self.font_var,
            value="medium",
            command=self._on_font_change,
        )
        medium_radio.grid(row=0, column=1, sticky="w", padx=10, pady=10)
        
        large_radio = ctk.CTkRadioButton(
            font_frame,
            text="Large",
            variable=self.font_var,
            value="large",
            command=self._on_font_change,
        )
        large_radio.grid(row=0, column=2, sticky="w", padx=10, pady=10)
        
        # About Section
        about_card = CTkCard(main_frame)
        about_card.pack(fill="x", padx=30, pady=(0, 20))
        about_card.pack_propagate(False)
        about_card.configure(height=200)
        
        about_label = CTkLabel(
            about_card,
            text="ℹ️ About",
            font=FONTS["subheading"],
        )
        about_label.pack(anchor="w", padx=15, pady=(15, 15))
        
        app_name_label = CTkLabel(
            about_card,
            text="Application: Advanced Text Encryption Suite",
            text_color=COLORS["text_secondary"],
            font=FONTS["small"],
        )
        app_name_label.pack(anchor="w", padx=15, pady=(0, 5))
        
        version_label = CTkLabel(
            about_card,
            text="Version: 1.0.0",
            text_color=COLORS["text_secondary"],
            font=FONTS["small"],
        )
        version_label.pack(anchor="w", padx=15, pady=(0, 5))
        
        desc_label = CTkLabel(
            about_card,
            text="A professional-grade encryption tool supporting multiple algorithms\nincluding AES, DES, 3DES, RSA, and Fernet encryption.",
            text_color=COLORS["text_secondary"],
            font=FONTS["small"],
            wraplength=600,
            justify="left",
        )
        desc_label.pack(anchor="w", padx=15, pady=(10, 15))
        
        # Security Section
        security_card = CTkCard(main_frame)
        security_card.pack(fill="x", padx=30, pady=(0, 30))
        security_card.pack_propagate(False)
        security_card.configure(height=200)
        
        security_label = CTkLabel(
            security_card,
            text="🔒 Security",
            font=FONTS["subheading"],
        )
        security_label.pack(anchor="w", padx=15, pady=(15, 15))
        
        security_info = [
            "✓ Uses industry-standard cryptographic algorithms",
            "✓ All encryption keys are securely generated",
            "✓ No keys are hardcoded or logged",
            "✓ Secure random IV generation for CBC mode",
            "✓ PBKDF2 for password-based key derivation",
            "✓ SHA-256 for hashing operations",
        ]
        
        for info in security_info:
            info_label = CTkLabel(
                security_card,
                text=info,
                text_color=COLORS["success"],
                font=FONTS["small"],
            )
            info_label.pack(anchor="w", padx=15, pady=2)
        
        # Add padding
        padding = CTkLabel(security_card, text="", fg_color="transparent")
        padding.pack(pady=5)
    
    def _on_theme_change(self):
        """Handle theme change."""
        if self.on_theme_change:
            self.on_theme_change(self.theme_var.get())
    
    def _on_font_change(self):
        """Handle font size change."""
        if self.on_font_change:
            self.on_font_change(self.font_var.get())
    
    def refresh(self):
        """Refresh the page."""
        pass
