"""Encryption page."""

import customtkinter as ctk
from ui.components import CTkCard, CTkLabel, CTkLabelSecondary, CTkButton, CTkTextBox, CTkComboBox
from utils.config import COLORS, FONTS, ALGORITHMS
from encryption import AESEncryption, DESEncryption, TripleDESEncryption, FernetEncryption, RSAEncryption
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog


class EncryptionPage(ctk.CTkFrame):
    """Text encryption page."""
    
    def __init__(self, master, on_status_change=None, **kwargs):
        """Initialize the encryption page.
        
        Args:
            master: Parent widget.
            on_status_change: Callback for status changes.
            **kwargs: Additional arguments for CTkFrame.
        """
        super().__init__(master, fg_color=COLORS["dark_bg"], **kwargs)
        self.on_status_change = on_status_change
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Main content
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
            text="Text Encryption",
            font=FONTS["heading"],
            text_color=COLORS["accent_secondary"],
        )
        title_label.pack(anchor="w", padx=30, pady=(30, 10))
        
        # Algorithm selection
        algo_frame = CTkCard(main_frame)
        algo_frame.pack(fill="x", padx=30, pady=(0, 20))
        algo_frame.pack_propagate(False)
        algo_frame.configure(height=100)
        
        algo_label = CTkLabel(
            algo_frame,
            text="Select Encryption Algorithm",
            font=FONTS["subheading"],
        )
        algo_label.pack(anchor="w", padx=15, pady=(15, 10))
        
        self.algorithm_var = ctk.StringVar(value="AES")
        algo_combo = CTkComboBox(
            algo_frame,
            values=list(ALGORITHMS.keys()),
            variable=self.algorithm_var,
            state="readonly",
        )
        algo_combo.pack(fill="x", padx=15, pady=(0, 15))
        
        # Input text area
        input_label = CTkLabel(
            main_frame,
            text="Text to Encrypt",
            font=FONTS["subheading"],
        )
        input_label.pack(anchor="w", padx=30, pady=(20, 10))
        
        self.input_textbox = CTkTextBox(main_frame)
        self.input_textbox.pack(fill="both", expand=True, padx=30, pady=(0, 20), ipady=10)
        
        # Key management
        key_frame = CTkCard(main_frame)
        key_frame.pack(fill="x", padx=30, pady=(0, 20))
        key_frame.grid_columnconfigure((0, 1, 2), weight=1)
        
        key_label = CTkLabel(
            key_frame,
            text="Encryption Key Management",
            font=FONTS["subheading"],
        )
        key_label.grid(row=0, column=0, columnspan=3, sticky="w", padx=15, pady=(15, 10))
        
        # Generate key button
        gen_key_btn = CTkButton(
            key_frame,
            text="Generate New Key",
            command=self._generate_key,
        )
        gen_key_btn.grid(row=1, column=0, sticky="ew", padx=(15, 5), pady=(0, 15))
        
        # Key display
        self.key_display = CTkTextBox(key_frame, height=60)
        self.key_display.grid(row=1, column=1, columnspan=2, sticky="ew", padx=(5, 15), pady=(0, 15))
        
        # Buttons row
        buttons_frame = ctk.CTkFrame(main_frame, fg_color=COLORS["dark_bg"])
        buttons_frame.pack(fill="x", padx=30, pady=(0, 20))
        buttons_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        
        encrypt_btn = CTkButton(
            buttons_frame,
            text="🔐 Encrypt",
            command=self._encrypt,
            fg_color=COLORS["success"],
            hover_color=COLORS["accent_secondary"],
        )
        encrypt_btn.grid(row=0, column=0, sticky="ew", padx=(0, 5))
        
        copy_btn = CTkButton(
            buttons_frame,
            text="📋 Copy Output",
            command=self._copy_output,
        )
        copy_btn.grid(row=0, column=1, sticky="ew", padx=5)
        
        save_btn = CTkButton(
            buttons_frame,
            text="💾 Save Output",
            command=self._save_output,
        )
        save_btn.grid(row=0, column=2, sticky="ew", padx=5)
        
        clear_btn = CTkButton(
            buttons_frame,
            text="🗑️ Clear",
            command=self._clear,
            fg_color=COLORS["error"],
            hover_color="#c5353b",
        )
        clear_btn.grid(row=0, column=3, sticky="ew", padx=(5, 0))
        
        # Output
        output_label = CTkLabel(
            main_frame,
            text="Encrypted Output",
            font=FONTS["subheading"],
        )
        output_label.pack(anchor="w", padx=30, pady=(20, 10))
        
        self.output_textbox = CTkTextBox(main_frame)
        self.output_textbox.pack(fill="both", expand=True, padx=30, pady=(0, 30), ipady=10)
        self.output_textbox.configure(state="disabled")
    
    def _generate_key(self):
        """Generate a new encryption key."""
        try:
            algorithm = self.algorithm_var.get()
            
            if algorithm == "AES":
                key = AESEncryption.generate_key()
            elif algorithm == "DES":
                key = DESEncryption.generate_key()
            elif algorithm == "3DES":
                key = TripleDESEncryption.generate_key()
            elif algorithm == "Fernet":
                key = FernetEncryption.generate_key()
            else:
                messagebox.showerror("Error", "Algorithm not supported")
                return
            
            self.key_display.configure(state="normal")
            self.key_display.delete("1.0", "end")
            self.key_display.insert("1.0", key)
            self.key_display.configure(state="disabled")
            
            if self.on_status_change:
                self.on_status_change("Key generated successfully ✓")
        
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate key: {str(e)}")
    
    def _encrypt(self):
        """Encrypt the text."""
        try:
            plaintext = self.input_textbox.get("1.0", "end-1c").strip()
            key = self.key_display.get("1.0", "end-1c").strip()
            algorithm = self.algorithm_var.get()
            
            if not plaintext:
                messagebox.showerror("Error", "Please enter text to encrypt")
                return
            
            if not key:
                messagebox.showerror("Error", "Please generate or enter an encryption key")
                return
            
            if self.on_status_change:
                self.on_status_change("Encrypting...")
            
            if algorithm == "AES":
                encrypted = AESEncryption.encrypt(plaintext, key)
            elif algorithm == "DES":
                encrypted = DESEncryption.encrypt(plaintext, key)
            elif algorithm == "3DES":
                encrypted = TripleDESEncryption.encrypt(plaintext, key)
            elif algorithm == "Fernet":
                encrypted = FernetEncryption.encrypt(plaintext, key)
            else:
                raise ValueError(f"Unsupported algorithm: {algorithm}")
            
            self.output_textbox.configure(state="normal")
            self.output_textbox.delete("1.0", "end")
            self.output_textbox.insert("1.0", encrypted)
            self.output_textbox.configure(state="disabled")
            
            if self.on_status_change:
                self.on_status_change("Encryption Successful ✓")
        
        except Exception as e:
            messagebox.showerror("Encryption Error", f"Failed to encrypt: {str(e)}")
            if self.on_status_change:
                self.on_status_change("Encryption failed")
    
    def _copy_output(self):
        """Copy encrypted output to clipboard."""
        try:
            output = self.output_textbox.get("1.0", "end-1c").strip()
            if not output:
                messagebox.showwarning("Warning", "No encrypted text to copy")
                return
            
            self.master.clipboard_clear()
            self.master.clipboard_append(output)
            messagebox.showinfo("Success", "Encrypted text copied to clipboard")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to copy: {str(e)}")
    
    def _save_output(self):
        """Save encrypted output to file."""
        try:
            output = self.output_textbox.get("1.0", "end-1c").strip()
            if not output:
                messagebox.showwarning("Warning", "No encrypted text to save")
                return
            
            filename = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )
            
            if filename:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(output)
                messagebox.showinfo("Success", f"File saved to {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {str(e)}")
    
    def _clear(self):
        """Clear all fields."""
        self.input_textbox.delete("1.0", "end")
        self.output_textbox.configure(state="normal")
        self.output_textbox.delete("1.0", "end")
        self.output_textbox.configure(state="disabled")
        self.key_display.configure(state="normal")
        self.key_display.delete("1.0", "end")
        self.key_display.configure(state="disabled")
    
    def refresh(self):
        """Refresh the page."""
        pass
