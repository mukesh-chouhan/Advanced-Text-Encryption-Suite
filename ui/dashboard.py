"""Dashboard page."""

import customtkinter as ctk
from ui.components import CTkCard, CTkLabel, CTkLabelSecondary, CTkButton
from utils.config import COLORS, FONTS, APP_NAME, APP_VERSION, ALGORITHMS


class DashboardPage(ctk.CTkFrame):
    """Dashboard home page."""
    
    def __init__(self, master, **kwargs):
        """Initialize the dashboard page.
        
        Args:
            master: Parent widget.
            **kwargs: Additional arguments for CTkFrame.
        """
        super().__init__(master, fg_color=COLORS["dark_bg"], **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Create main scrollable container
        self.scrollable_frame = ctk.CTkScrollableFrame(
            self,
            fg_color=COLORS["dark_bg"],
            scrollbar_button_color=COLORS["card_bg"],
            scrollbar_button_hover_color=COLORS["border"],
        )
        self.scrollable_frame.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        
        # Header Section
        self._create_header()
        
        # Algorithm Cards Section
        self._create_algorithm_section()
        
        # Features Section
        self._create_features_section()
    
    def _create_header(self):
        """Create the header section."""
        header_frame = ctk.CTkFrame(self.scrollable_frame, fg_color=COLORS["dark_bg"])
        header_frame.grid(row=0, column=0, sticky="ew", padx=30, pady=(30, 20))
        header_frame.grid_columnconfigure(0, weight=1)
        
        # Title
        title_label = CTkLabel(
            header_frame,
            text=APP_NAME,
            font=FONTS["title"],
            text_color=COLORS["accent_secondary"],
        )
        title_label.grid(row=0, column=0, sticky="w")
        
        # Version
        version_label = CTkLabelSecondary(
            header_frame,
            text=f"Version {APP_VERSION} | Professional Encryption Suite",
        )
        version_label.grid(row=1, column=0, sticky="w", pady=(5, 0))
        
        # Description
        desc_label = CTkLabel(
            header_frame,
            text="Secure your sensitive data with industry-standard encryption algorithms",
            text_color=COLORS["text_secondary"],
            font=FONTS["regular"],
            wraplength=1000,
        )
        desc_label.grid(row=2, column=0, sticky="w", pady=(15, 0))
    
    def _create_algorithm_section(self):
        """Create algorithm information cards."""
        section_label = CTkLabel(
            self.scrollable_frame,
            text="Available Algorithms",
            font=FONTS["heading"],
            text_color=COLORS["accent_secondary"],
        )
        section_label.grid(row=1, column=0, sticky="w", padx=30, pady=(30, 20))
        
        # Cards container
        cards_frame = ctk.CTkFrame(self.scrollable_frame, fg_color=COLORS["dark_bg"])
        cards_frame.grid(row=2, column=0, sticky="ew", padx=30, pady=(0, 30))
        cards_frame.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        
        col = 0
        for algo_key, algo_info in ALGORITHMS.items():
            self._create_algo_card(cards_frame, algo_key, algo_info, col)
            col += 1
    
    def _create_algo_card(self, parent, algo_key: str, algo_info: dict, col: int):
        """Create an algorithm info card.
        
        Args:
            parent: Parent widget.
            algo_key: Algorithm key.
            algo_info: Algorithm information dictionary.
            col: Column position.
        """
        card = CTkCard(parent, fg_color=COLORS["card_bg"])
        card.grid(row=0, column=col, sticky="nsew", padx=5, pady=5)
        card.grid_columnconfigure(0, weight=1)
        
        # Algorithm name
        name_label = CTkLabel(
            card,
            text=algo_info["name"],
            font=FONTS["subheading"],
            text_color=COLORS["accent_secondary"],
        )
        name_label.pack(anchor="w", padx=15, pady=(15, 10))
        
        # Description
        desc_label = CTkLabel(
            card,
            text=algo_info["description"],
            text_color=COLORS["text_secondary"],
            font=FONTS["small"],
            wraplength=180,
            justify="left",
        )
        desc_label.pack(anchor="w", padx=15, pady=(0, 10))
        
        # Key size
        key_label = CTkLabelSecondary(
            card,
            text=f"Key Size: {algo_info['key_size']}",
        )
        key_label.pack(anchor="w", padx=15, pady=(0, 10))
        
        # Type
        algo_type = "Symmetric" if algo_info["is_symmetric"] else "Asymmetric"
        type_label = CTkLabelSecondary(
            card,
            text=f"Type: {algo_type}",
        )
        type_label.pack(anchor="w", padx=15, pady=(0, 15))
    
    def _create_features_section(self):
        """Create features section."""
        section_label = CTkLabel(
            self.scrollable_frame,
            text="Key Features",
            font=FONTS["heading"],
            text_color=COLORS["accent_secondary"],
        )
        section_label.grid(row=3, column=0, sticky="w", padx=30, pady=(30, 20))
        
        features = [
            ("🔐", "Multiple Encryption Algorithms", "Support for AES, DES, 3DES, RSA, and Fernet"),
            ("📁", "File Encryption", "Encrypt and decrypt text files securely"),
            ("🔑", "Key Management", "Generate, save, and manage encryption keys"),
            ("📊", "History Tracking", "Keep track of all encryption operations"),
            ("🎨", "Modern UI", "Responsive and intuitive user interface"),
            ("⚡", "Secure Algorithms", "Industry-standard encryption techniques"),
        ]
        
        features_frame = ctk.CTkFrame(self.scrollable_frame, fg_color=COLORS["dark_bg"])
        features_frame.grid(row=4, column=0, sticky="ew", padx=30, pady=(0, 30))
        features_frame.grid_columnconfigure((0, 1), weight=1)
        
        for idx, (icon, title, description) in enumerate(features):
            row = idx // 2
            col = idx % 2
            
            feature_card = CTkCard(features_frame)
            feature_card.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
            feature_card.grid_columnconfigure(1, weight=1)
            
            # Icon
            icon_label = CTkLabel(
                feature_card,
                text=icon,
                font=("Arial", 24),
                text_color=COLORS["accent_secondary"],
            )
            icon_label.grid(row=0, column=0, padx=15, pady=15, rowspan=2)
            
            # Title
            title_label = CTkLabel(
                feature_card,
                text=title,
                font=FONTS["subheading"],
            )
            title_label.grid(row=0, column=1, sticky="w", padx=(10, 15), pady=(15, 5))
            
            # Description
            desc_label = CTkLabel(
                feature_card,
                text=description,
                text_color=COLORS["text_secondary"],
                font=FONTS["small"],
                wraplength=300,
                justify="left",
            )
            desc_label.grid(row=1, column=1, sticky="w", padx=(10, 15), pady=(0, 15))
    
    def refresh(self):
        """Refresh the page."""
        pass
