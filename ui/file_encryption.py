"""File Encryption page."""

import customtkinter as ctk
from ui.components import CTkCard, CTkLabel, CTkLabelSecondary, CTkButton, CTkComboBox
from utils.config import COLORS, FONTS, ALGORITHMS
from encryption import AESEncryption, DESEncryption, TripleDESEncryption, FernetEncryption
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog
import os


class FileEncryptionPage(ctk.CTkFrame):
    """File encryption and decryption page."""
    
    def __init__(self, master, on_status_change=None, **kwargs):
        """Initialize the file encryption page.
        
        Args:
            master: Parent widget.
            on_status_change: Callback for status changes.
            **kwargs: Additional arguments for CTkFrame.
        """
        super().__init__(master, fg_color=COLORS["dark_bg"], **kwargs)
        self.on_status_change = on_status_change
        self.selected_file = None
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
            text="File Encryption & Decryption",
            font=FONTS["heading"],
            text_color=COLORS["accent_secondary"],
        )
        title_label.pack(anchor="w", padx=30, pady=(30, 10))
        
        # File Selection Section
        file_section = CTkCard(main_frame)
        file_section.pack(fill="x", padx=30, pady=(0, 20))
        file_section.pack_propagate(False)
        file_section.configure(height=100)
        
        file_label = CTkLabel(
            file_section,
            text="Select File",
            font=FONTS["subheading"],
        )
        file_label.pack(anchor="w", padx=15, pady=(15, 10))
        
        file_btn_frame = ctk.CTkFrame(file_section, fg_color=COLORS["card_bg"])
        file_btn_frame.pack(fill="x", padx=15, pady=(0, 15))
        file_btn_frame.grid_columnconfigure((0, 1), weight=1)
        
        select_btn = CTkButton(
            file_btn_frame,
            text="📂 Select File",
            command=self._select_file,
        )
        select_btn.grid(row=0, column=0, sticky="ew", padx=(0, 5))
        
        self.file_label = CTkLabel(
            file_btn_frame,
            text="No file selected",
            text_color=COLORS["text_secondary"],
            font=FONTS["small"],
        )
        self.file_label.grid(row=0, column=1, sticky="ew", padx=(5, 0))
        
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
        # Only symmetric algorithms for files
        symmetric_algos = ["AES", "DES", "3DES", "Fernet"]
        algo_combo = CTkComboBox(
            algo_frame,
            values=symmetric_algos,
            variable=self.algorithm_var,
            state="readonly",
        )
        algo_combo.pack(fill="x", padx=15, pady=(0, 15))
        
        # Key section
        key_frame = CTkCard(main_frame)
        key_frame.pack(fill="x", padx=30, pady=(0, 20))
        key_frame.pack_propagate(False)
        key_frame.configure(height=150)
        
        key_label = CTkLabel(
            key_frame,
            text="Encryption Key",
            font=FONTS["subheading"],
        )
        key_label.pack(anchor="w", padx=15, pady=(15, 10))
        
        key_btn_frame = ctk.CTkFrame(key_frame, fg_color=COLORS["card_bg"])
        key_btn_frame.pack(fill="x", padx=15, pady=(0, 10))
        key_btn_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        
        gen_key_btn = CTkButton(
            key_btn_frame,
            text="Generate Key",
            command=self._generate_key,
        )
        gen_key_btn.grid(row=0, column=0, sticky="ew", padx=(0, 5))
        
        paste_key_btn = CTkButton(
            key_btn_frame,
            text="Paste from Clipboard",
            command=self._paste_key,
        )
        paste_key_btn.grid(row=0, column=1, sticky="ew", padx=5)
        
        copy_key_btn = CTkButton(
            key_btn_frame,
            text="Copy Key",
            command=self._copy_key,
        )
        copy_key_btn.grid(row=0, column=2, sticky="ew", padx=5)
        
        clear_key_btn = CTkButton(
            key_btn_frame,
            text="Clear Key",
            fg_color=COLORS["error"],
            hover_color="#c5353b",
            command=self._clear_key,
        )
        clear_key_btn.grid(row=0, column=3, sticky="ew", padx=(5, 0))
        
        # Key display with scrollbar
        from ui.components import CTkTextBox
        self.key_textbox = CTkTextBox(key_frame, height=60)
        self.key_textbox.pack(fill="x", padx=15, pady=(0, 15), ipady=10)
        
        # Encryption/Decryption Buttons
        action_frame = ctk.CTkFrame(main_frame, fg_color=COLORS["dark_bg"])
        action_frame.pack(fill="x", padx=30, pady=(0, 20))
        action_frame.grid_columnconfigure((0, 1, 2), weight=1)
        
        encrypt_btn = CTkButton(
            action_frame,
            text="🔐 Encrypt File",
            command=self._encrypt_file,
            fg_color=COLORS["success"],
            hover_color=COLORS["accent_secondary"],
        )
        encrypt_btn.grid(row=0, column=0, sticky="ew", padx=(0, 5))
        
        decrypt_btn = CTkButton(
            action_frame,
            text="🔓 Decrypt File",
            command=self._decrypt_file,
            fg_color=COLORS["success"],
            hover_color=COLORS["accent_secondary"],
        )
        decrypt_btn.grid(row=0, column=1, sticky="ew", padx=5)
        
        clear_all_btn = CTkButton(
            action_frame,
            text="🗑️ Clear All",
            fg_color=COLORS["error"],
            hover_color="#c5353b",
            command=self._clear_all,
        )
        clear_all_btn.grid(row=0, column=2, sticky="ew", padx=(5, 0))
        
        # Status section
        status_label = CTkLabel(
            main_frame,
            text="Status",
            font=FONTS["subheading"],
        )
        status_label.pack(anchor="w", padx=30, pady=(20, 10))
        
        self.status_textbox = ctk.CTkTextbox(
            main_frame,
            height=100,
            fg_color=COLORS["card_bg"],
            border_color=COLORS["border"],
            border_width=1,
            text_color=COLORS["text_secondary"],
            font=FONTS["mono"],
        )
        self.status_textbox.pack(fill="both", expand=True, padx=30, pady=(0, 30), ipady=10)
        self.status_textbox.configure(state="disabled")
    
    def _select_file(self):
        """Select a file for encryption/decryption."""
        filename = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if filename:
            self.selected_file = filename
            file_name = os.path.basename(filename)
            file_size = os.path.getsize(filename)
            self.file_label.configure(text=f"{file_name} ({file_size} bytes)")
    
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
            
            self.key_textbox.delete("1.0", "end")
            self.key_textbox.insert("1.0", key)
            
            self._add_status(f"✓ Key generated for {algorithm}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate key: {str(e)}")
    
    def _paste_key(self):
        """Paste key from clipboard."""
        try:
            key = self.master.clipboard_get()
            self.key_textbox.delete("1.0", "end")
            self.key_textbox.insert("1.0", key)
            self._add_status("✓ Key pasted from clipboard")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to paste key: {str(e)}")
    
    def _copy_key(self):
        """Copy key to clipboard."""
        try:
            key = self.key_textbox.get("1.0", "end-1c").strip()
            if key:
                self.master.clipboard_clear()
                self.master.clipboard_append(key)
                self._add_status("✓ Key copied to clipboard")
            else:
                messagebox.showwarning("Warning", "No key to copy")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to copy key: {str(e)}")
    
    def _clear_key(self):
        """Clear the key field."""
        self.key_textbox.delete("1.0", "end")
    
    def _encrypt_file(self):
        """Encrypt the selected file."""
        try:
            if not self.selected_file:
                messagebox.showerror("Error", "Please select a file first")
                return
            
            key = self.key_textbox.get("1.0", "end-1c").strip()
            if not key:
                messagebox.showerror("Error", "Please generate or enter an encryption key")
                return
            
            algorithm = self.algorithm_var.get()
            
            # Read file
            with open(self.selected_file, 'r', encoding='utf-8') as f:
                plaintext = f.read()
            
            self._add_status(f"Encrypting file with {algorithm}...")
            if self.on_status_change:
                self.on_status_change("Encrypting file...")
            
            # Encrypt
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
            
            # Save encrypted file
            output_filename = filedialog.asksaveasfilename(
                initialfile=os.path.basename(self.selected_file) + ".encrypted",
                filetypes=[("Encrypted files", "*.encrypted"), ("Text files", "*.txt"), ("All files", "*.*")]
            )
            
            if output_filename:
                with open(output_filename, 'w', encoding='utf-8') as f:
                    f.write(encrypted)
                
                self._add_status(f"✓ File encrypted and saved: {os.path.basename(output_filename)}")
                if self.on_status_change:
                    self.on_status_change("File encryption successful ✓")
                messagebox.showinfo("Success", f"File encrypted successfully:\n{output_filename}")
        
        except Exception as e:
            self._add_status(f"✗ Encryption error: {str(e)}")
            messagebox.showerror("Encryption Error", f"Failed to encrypt file: {str(e)}")
    
    def _decrypt_file(self):
        """Decrypt a file."""
        try:
            encrypted_file = filedialog.askopenfilename(
                filetypes=[("Encrypted files", "*.encrypted"), ("Text files", "*.txt"), ("All files", "*.*")]
            )
            
            if not encrypted_file:
                return
            
            key = self.key_textbox.get("1.0", "end-1c").strip()
            if not key:
                messagebox.showerror("Error", "Please enter decryption key")
                return
            
            algorithm = self.algorithm_var.get()
            
            # Read encrypted file
            with open(encrypted_file, 'r', encoding='utf-8') as f:
                encrypted_text = f.read()
            
            self._add_status(f"Decrypting file with {algorithm}...")
            if self.on_status_change:
                self.on_status_change("Decrypting file...")
            
            # Decrypt
            if algorithm == "AES":
                decrypted = AESEncryption.decrypt(encrypted_text, key)
            elif algorithm == "DES":
                decrypted = DESEncryption.decrypt(encrypted_text, key)
            elif algorithm == "3DES":
                decrypted = TripleDESEncryption.decrypt(encrypted_text, key)
            elif algorithm == "Fernet":
                decrypted = FernetEncryption.decrypt(encrypted_text, key)
            else:
                raise ValueError(f"Unsupported algorithm: {algorithm}")
            
            # Save decrypted file
            output_filename = filedialog.asksaveasfilename(
                initialfile=os.path.basename(encrypted_file).replace(".encrypted", ".decrypted.txt"),
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )
            
            if output_filename:
                with open(output_filename, 'w', encoding='utf-8') as f:
                    f.write(decrypted)
                
                self._add_status(f"✓ File decrypted and saved: {os.path.basename(output_filename)}")
                if self.on_status_change:
                    self.on_status_change("File decryption successful ✓")
                messagebox.showinfo("Success", f"File decrypted successfully:\n{output_filename}")
        
        except Exception as e:
            self._add_status(f"✗ Decryption error: {str(e)}")
            messagebox.showerror("Decryption Error", f"Failed to decrypt file: {str(e)}")
    
    def _clear_all(self):
        """Clear all fields."""
        self.selected_file = None
        self.file_label.configure(text="No file selected")
        self.key_textbox.delete("1.0", "end")
        self.status_textbox.configure(state="normal")
        self.status_textbox.delete("1.0", "end")
        self.status_textbox.configure(state="disabled")
    
    def _add_status(self, message: str):
        """Add a status message."""
        self.status_textbox.configure(state="normal")
        self.status_textbox.insert("end", f"{message}\n")
        self.status_textbox.see("end")
        self.status_textbox.configure(state="disabled")
    
    def refresh(self):
        """Refresh the page."""
        pass
