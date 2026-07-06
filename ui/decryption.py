"""Decryption page."""

import customtkinter as ctk
from ui.components import CTkCard, CTkLabel, CTkLabelSecondary, CTkButton, CTkTextBox, CTkComboBox
from utils.config import COLORS, FONTS, ALGORITHMS
from encryption import AESEncryption, DESEncryption, TripleDESEncryption, FernetEncryption, RSAEncryption
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog


class DecryptionPage(ctk.CTkFrame):
    """Text decryption page."""
    
    def __init__(self, master, on_status_change=None, **kwargs):
        """Initialize the decryption page.
        
        Args:
            master: Parent widget.
            on_status_change: Callback for status changes.
            **kwargs: Additional arguments for CTkFrame.
        """
        super().__init__(master, fg_color=COLORS["dark_bg"], **kwargs)
        self.on_status_change = on_status_change
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
            text="Text Decryption",
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
            text="Select Decryption Algorithm",
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
        
        # Encrypted text input
        encrypted_label = CTkLabel(
            main_frame,
            text="Encrypted Text",
            font=FONTS["subheading"],
        )
        encrypted_label.pack(anchor="w", padx=30, pady=(20, 10))
        
        self.encrypted_textbox = CTkTextBox(main_frame)
        self.encrypted_textbox.pack(fill="both", expand=True, padx=30, pady=(0, 20), ipady=10)
        
        # Key input
        key_label = CTkLabel(
            main_frame,
            text="Decryption Key",
            font=FONTS["subheading"],
        )
        key_label.pack(anchor="w", padx=30, pady=(20, 10))
        
        self.key_textbox = CTkTextBox(main_frame, height=80)
        self.key_textbox.pack(fill="x", padx=30, pady=(0, 20), ipady=10)
        
        # Buttons
        buttons_frame = ctk.CTkFrame(main_frame, fg_color=COLORS["dark_bg"])
        buttons_frame.pack(fill="x", padx=30, pady=(0, 20))
        buttons_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        
        decrypt_btn = CTkButton(
            buttons_frame,
            text="🔓 Decrypt",
            command=self._decrypt,
            fg_color=COLORS["success"],
            hover_color=COLORS["accent_secondary"],
        )
        decrypt_btn.grid(row=0, column=0, sticky="ew", padx=(0, 5))
        
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
            text="Decrypted Output",
            font=FONTS["subheading"],
        )
        output_label.pack(anchor="w", padx=30, pady=(20, 10))
        
        self.output_textbox = CTkTextBox(main_frame)
        self.output_textbox.pack(fill="both", expand=True, padx=30, pady=(0, 30), ipady=10)
        self.output_textbox.configure(state="disabled")
    
    def _decrypt(self):
        """Decrypt the text."""
        try:
            encrypted_text = self.encrypted_textbox.get("1.0", "end-1c").strip()
            key = self.key_textbox.get("1.0", "end-1c").strip()
            algorithm = self.algorithm_var.get()
            
            if not encrypted_text:
                messagebox.showerror("Error", "Please enter encrypted text")
                return
            
            if not key:
                messagebox.showerror("Error", "Please enter decryption key")
                return
            
            if self.on_status_change:
                self.on_status_change("Decrypting...")
            
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
            
            self.output_textbox.configure(state="normal")
            self.output_textbox.delete("1.0", "end")
            self.output_textbox.insert("1.0", decrypted)
            self.output_textbox.configure(state="disabled")
            
            if self.on_status_change:
                self.on_status_change("Decryption Successful ✓")
        
        except Exception as e:
            messagebox.showerror("Decryption Error", f"Failed to decrypt: {str(e)}")
            if self.on_status_change:
                self.on_status_change("Decryption failed")
    
    def _copy_output(self):
        """Copy decrypted output to clipboard."""
        try:
            output = self.output_textbox.get("1.0", "end-1c").strip()
            if not output:
                messagebox.showwarning("Warning", "No decrypted text to copy")
                return
            
            self.master.clipboard_clear()
            self.master.clipboard_append(output)
            messagebox.showinfo("Success", "Decrypted text copied to clipboard")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to copy: {str(e)}")
    
    def _save_output(self):
        """Save decrypted output to file."""
        try:
            output = self.output_textbox.get("1.0", "end-1c").strip()
            if not output:
                messagebox.showwarning("Warning", "No decrypted text to save")
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
        self.encrypted_textbox.delete("1.0", "end")
        self.key_textbox.delete("1.0", "end")
        self.output_textbox.configure(state="normal")
        self.output_textbox.delete("1.0", "end")
        self.output_textbox.configure(state="disabled")
    
    def refresh(self):
        """Refresh the page."""
        pass
