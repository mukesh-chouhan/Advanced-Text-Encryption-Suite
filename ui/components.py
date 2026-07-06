"""Base UI components and helpers."""

import customtkinter as ctk
from utils.config import COLORS, FONTS


class CTkCard(ctk.CTkFrame):
    """A modern card component."""
    
    def __init__(self, master, **kwargs):
        """Initialize the card.
        
        Args:
            master: Parent widget.
            **kwargs: Additional arguments for CTkFrame.
        """
        super().__init__(
            master,
            border_width=1,
            border_color=COLORS["border"],
            corner_radius=8,
            **kwargs
        )


class CTkButton(ctk.CTkButton):
    """A modern button component."""
    
    def __init__(self, master, **kwargs):
        """Initialize the button.
        
        Args:
            master: Parent widget.
            **kwargs: Additional arguments for CTkButton.
        """
        defaults = {
            "fg_color": COLORS["accent_primary"],
            "hover_color": COLORS["accent_secondary"],
            "text_color": COLORS["text_primary"],
            "border_width": 0,
            "corner_radius": 8,
            "font": FONTS["regular"],
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)


class CTkLabel(ctk.CTkLabel):
    """A modern label component."""
    
    def __init__(self, master, **kwargs):
        """Initialize the label.
        
        Args:
            master: Parent widget.
            **kwargs: Additional arguments for CTkLabel.
        """
        defaults = {
            "text_color": COLORS["text_primary"],
            "font": FONTS["regular"],
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)


class CTkLabelSecondary(ctk.CTkLabel):
    """A secondary label component."""
    
    def __init__(self, master, **kwargs):
        """Initialize the label.
        
        Args:
            master: Parent widget.
            **kwargs: Additional arguments for CTkLabel.
        """
        defaults = {
            "text_color": COLORS["text_secondary"],
            "font": FONTS["small"],
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)


class CTkEntry(ctk.CTkEntry):
    """A modern entry component."""
    
    def __init__(self, master, **kwargs):
        """Initialize the entry.
        
        Args:
            master: Parent widget.
            **kwargs: Additional arguments for CTkEntry.
        """
        defaults = {
            "fg_color": COLORS["card_bg"],
            "border_color": COLORS["border"],
            "border_width": 1,
            "text_color": COLORS["text_primary"],
            "font": FONTS["regular"],
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)


class CTkTextBox(ctk.CTkTextbox):
    """A modern textbox component."""
    
    def __init__(self, master, **kwargs):
        """Initialize the textbox.
        
        Args:
            master: Parent widget.
            **kwargs: Additional arguments for CTkTextbox.
        """
        defaults = {
            "fg_color": COLORS["card_bg"],
            "border_color": COLORS["border"],
            "border_width": 1,
            "text_color": COLORS["text_primary"],
            "font": FONTS["mono"],
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)


class CTkComboBox(ctk.CTkComboBox):
    """A modern combobox component."""
    
    def __init__(self, master, **kwargs):
        """Initialize the combobox.
        
        Args:
            master: Parent widget.
            **kwargs: Additional arguments for CTkComboBox.
        """
        defaults = {
            "fg_color": COLORS["card_bg"],
            "border_color": COLORS["border"],
            "border_width": 1,
            "text_color": COLORS["text_primary"],
            "font": FONTS["regular"],
            "dropdown_fg_color": COLORS["card_bg"],
            "dropdown_text_color": COLORS["text_primary"],
            "button_color": COLORS["accent_primary"],
        }
        defaults.update(kwargs)
        super().__init__(master, **defaults)
