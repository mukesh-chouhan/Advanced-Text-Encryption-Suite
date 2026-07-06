"""RSA Key Management page."""
import base64
import customtkinter as ctk
from ui.components import CTkCard, CTkLabel, CTkLabelSecondary, CTkButton, CTkTextBox
from utils.config import COLORS, FONTS
from encryption import RSAEncryption
from utils.key_manager import KeyManager
from pathlib import Path
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog


class RSAKeyPage(ctk.CTkFrame):
    """RSA Key Management page."""
    
    def __init__(self, master, on_status_change=None, **kwargs):
        """Initialize the RSA key management page.
        
        Args:
            master: Parent widget.
            on_status_change: Callback for status changes.
            **kwargs: Additional arguments for CTkFrame.
        """
        super().__init__(master, fg_color=COLORS["dark_bg"], **kwargs)
        self.on_status_change = on_status_change
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Initialize key manager
        from utils.config import KEYS_DIR
        self.key_manager = KeyManager(KEYS_DIR)
        
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
            text="RSA Key Management",
            font=FONTS["heading"],
            text_color=COLORS["accent_secondary"],
        )
        title_label.pack(anchor="w", padx=30, pady=(30, 10))
        
        # Key Generation Section
        gen_section = CTkCard(main_frame)
        gen_section.pack(fill="x", padx=30, pady=(0, 20))
        gen_section.pack_propagate(False)
        gen_section.configure(height=80)
        
        gen_label = CTkLabel(
            gen_section,
            text="Generate New RSA Key Pair (2048-bit)",
            font=FONTS["subheading"],
        )
        gen_label.pack(anchor="w", padx=15, pady=(15, 10))
        
        gen_btn = CTkButton(
            gen_section,
            text="Generate Key Pair",
            command=self._generate_keys,
            fg_color=COLORS["success"],
            hover_color=COLORS["accent_secondary"],
        )
        gen_btn.pack(fill="x", padx=15, pady=(0, 15))
        
        # Private Key Section
        priv_label = CTkLabel(
            main_frame,
            text="Private Key",
            font=FONTS["subheading"],
        )
        priv_label.pack(anchor="w", padx=30, pady=(20, 10))
        
        self.private_key_textbox = CTkTextBox(main_frame, height=100)
        self.private_key_textbox.pack(fill="x", padx=30, pady=(0, 10), ipady=10)
        
        # Private Key Buttons
        priv_btn_frame = ctk.CTkFrame(main_frame, fg_color=COLORS["dark_bg"])
        priv_btn_frame.pack(fill="x", padx=30, pady=(0, 20))
        priv_btn_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        
        copy_priv_btn = CTkButton(
            priv_btn_frame,
            text="📋 Copy",
            command=lambda: self._copy_key(self.private_key_textbox),
        )
        copy_priv_btn.grid(row=0, column=0, sticky="ew", padx=(0, 5))
        
        save_priv_btn = CTkButton(
            priv_btn_frame,
            text="💾 Save",
            command=lambda: self._save_key(self.private_key_textbox, "rsa_private_key.pem"),
        )
        save_priv_btn.grid(row=0, column=1, sticky="ew", padx=5)
        
        load_priv_btn = CTkButton(
            priv_btn_frame,
            text="📂 Load",
            command=self._load_private_key,
        )
        load_priv_btn.grid(row=0, column=2, sticky="ew", padx=5)
        
        clear_priv_btn = CTkButton(
            priv_btn_frame,
            text="🗑️ Clear",
            fg_color=COLORS["error"],
            hover_color="#c5353b",
            command=lambda: self._clear_textbox(self.private_key_textbox),
        )
        clear_priv_btn.grid(row=0, column=3, sticky="ew", padx=(5, 0))
        
        # Public Key Section
        pub_label = CTkLabel(
            main_frame,
            text="Public Key",
            font=FONTS["subheading"],
        )
        pub_label.pack(anchor="w", padx=30, pady=(20, 10))
        
        self.public_key_textbox = CTkTextBox(main_frame, height=100)
        self.public_key_textbox.pack(fill="x", padx=30, pady=(0, 10), ipady=10)
        
        # Public Key Buttons
        pub_btn_frame = ctk.CTkFrame(main_frame, fg_color=COLORS["dark_bg"])
        pub_btn_frame.pack(fill="x", padx=30, pady=(0, 20))
        pub_btn_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        
        copy_pub_btn = CTkButton(
            pub_btn_frame,
            text="📋 Copy",
            command=lambda: self._copy_key(self.public_key_textbox),
        )
        copy_pub_btn.grid(row=0, column=0, sticky="ew", padx=(0, 5))
        
        save_pub_btn = CTkButton(
            pub_btn_frame,
            text="💾 Save",
            command=lambda: self._save_key(self.public_key_textbox, "rsa_public_key.pem"),
        )
        save_pub_btn.grid(row=0, column=1, sticky="ew", padx=5)
        
        load_pub_btn = CTkButton(
            pub_btn_frame,
            text="📂 Load",
            command=self._load_public_key,
        )
        load_pub_btn.grid(row=0, column=2, sticky="ew", padx=5)
        
        clear_pub_btn = CTkButton(
            pub_btn_frame,
            text="🗑️ Clear",
            fg_color=COLORS["error"],
            hover_color="#c5353b",
            command=lambda: self._clear_textbox(self.public_key_textbox),
        )
        clear_pub_btn.grid(row=0, column=3, sticky="ew", padx=(5, 0))
        
        # Key Info Section
        info_label = CTkLabel(
            main_frame,
            text="Key Information",
            font=FONTS["subheading"],
        )
        info_label.pack(anchor="w", padx=30, pady=(20, 10))
        
        self.info_textbox = CTkTextBox(main_frame, height=80)
        self.info_textbox.pack(fill="x", padx=30, pady=(0, 30), ipady=10)
        self.info_textbox.configure(state="disabled")
    
    def _generate_keys(self):
        """Generate RSA key pair."""
        try:
            if self.on_status_change:
                self.on_status_change("Generating RSA keys...")
            
            private_key, public_key = RSAEncryption.generate_key_pair()
            
            self.private_key_textbox.delete("1.0", "end")
            self.private_key_textbox.insert("1.0", private_key)
            
            self.public_key_textbox.delete("1.0", "end")
            self.public_key_textbox.insert("1.0", public_key)
            
            self._update_key_info(private_key)
            
            if self.on_status_change:
                self.on_status_change("RSA key pair generated ✓")
            
            messagebox.showinfo("Success", "RSA 2048-bit key pair generated successfully")
        
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate keys: {str(e)}")
    
    def _save_key(self, textbox: CTkTextBox, filename: str):
        """Save key to file."""
        try:
            key = textbox.get("1.0", "end-1c").strip()
            if not key:
                messagebox.showwarning("Warning", "No key to save")
                return
            
            self.key_manager.save_key(key, filename)
            messagebox.showinfo("Success", f"Key saved as {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save key: {str(e)}")
    
    def _load_private_key(self):
        """Load private key from file."""
        try:
            filename = filedialog.askopenfilename(
                filetypes=[("PEM files", "*.pem"), ("All files", "*.*")]
            )
            if filename:
                with open(filename, 'r', encoding='utf-8') as f:
                    key = f.read().strip()
                self.private_key_textbox.delete("1.0", "end")
                self.private_key_textbox.insert("1.0", key)
                self._update_key_info(key)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load key: {str(e)}")
    
    def _load_public_key(self):
        """Load public key from file."""
        try:
            filename = filedialog.askopenfilename(
                filetypes=[("PEM files", "*.pem"), ("All files", "*.*")]
            )
            if filename:
                with open(filename, 'rb') as f:
                    key = f.read().decode('utf-8').strip()
                self.public_key_textbox.delete("1.0", "end")
                self.public_key_textbox.insert("1.0", key)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load key: {str(e)}")
    
    def _copy_key(self, textbox: CTkTextBox):
        """Copy key to clipboard."""
        try:
            key = textbox.get("1.0", "end-1c").strip()
            if not key:
                messagebox.showwarning("Warning", "No key to copy")
                return
            self.master.clipboard_clear()
            self.master.clipboard_append(key)
            messagebox.showinfo("Success", "Key copied to clipboard")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to copy: {str(e)}")
    
    def _clear_textbox(self, textbox: CTkTextBox):
        """Clear a textbox."""
        textbox.delete("1.0", "end")
    
    def _update_key_info(self, key: str):
        """Update key information display."""
        try:
            info = RSAEncryption.get_key_info(key, "private" if "PRIVATE" in key else "public")
            
            self.info_textbox.configure(state="normal")
            self.info_textbox.delete("1.0", "end")
            
            info_text = f"Algorithm: {info['algorithm']}\n"
            info_text += f"Key Size: {info['key_size']} bits\n"
            info_text += f"Key Type: {info['key_type']}\n"
            
            self.info_textbox.insert("1.0", info_text)
            self.info_textbox.configure(state="disabled")
        except Exception as e:
            self.info_textbox.configure(state="normal")
            self.info_textbox.delete("1.0", "end")
            self.info_textbox.insert("1.0", f"Error: {str(e)}")
            self.info_textbox.configure(state="disabled")
    
    def refresh(self):
        """Refresh the page."""
        pass
