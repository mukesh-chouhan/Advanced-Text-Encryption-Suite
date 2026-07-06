"""DES Encryption module using DES in CBC mode."""

import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


class DESEncryption:
    """DES CBC Mode Encryption/Decryption."""
    
    KEY_SIZE = 8  # 64 bits
    BLOCK_SIZE = 8  # 64 bits
    
    @staticmethod
    def generate_key() -> str:
        """Generate a random DES key (8 bytes).
        
        Returns:
            str: Base64 encoded key.
        """
        key = os.urandom(DESEncryption.KEY_SIZE)
        return base64.b64encode(key).decode('utf-8')
    
    @staticmethod
    def generate_iv() -> str:
        """Generate a random IV for DES.
        
        Returns:
            str: Base64 encoded IV.
        """
        iv = os.urandom(DESEncryption.BLOCK_SIZE)
        return base64.b64encode(iv).decode('utf-8')
    
    @staticmethod
    def encrypt(plaintext: str, key: str, iv: str = None) -> str:
        """Encrypt plaintext using DES CBC.
        
        Args:
            plaintext: Text to encrypt.
            key: Base64 encoded DES key (8 bytes).
            iv: Base64 encoded IV. If None, a new one is generated.
        
        Returns:
            str: Base64 encoded encrypted text with IV prepended.
        
        Raises:
            ValueError: If key or plaintext is invalid.
        """
        if not plaintext:
            raise ValueError("Plaintext cannot be empty.")
        if not key:
            raise ValueError("Key cannot be empty.")
        
        try:
            key_bytes = base64.b64decode(key)
            if len(key_bytes) != DESEncryption.KEY_SIZE:
                raise ValueError(f"Key must be {DESEncryption.KEY_SIZE} bytes.")
            
            if iv is None:
                iv_bytes = os.urandom(DESEncryption.BLOCK_SIZE)
            else:
                iv_bytes = base64.b64decode(iv)
            
            # Pad plaintext using PKCS7
            padding_length = DESEncryption.BLOCK_SIZE - (len(plaintext.encode()) % DESEncryption.BLOCK_SIZE)
            padded_plaintext = plaintext.encode() + bytes([padding_length] * padding_length)
            
            cipher = Cipher(
                algorithms.TripleDES(key_bytes),  # Using TripleDES with single key for DES
                modes.CBC(iv_bytes),
                backend=default_backend()
            )
            encryptor = cipher.encryptor()
            ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
            
            # Prepend IV to ciphertext
            encrypted_data = iv_bytes + ciphertext
            return base64.b64encode(encrypted_data).decode('utf-8')
        
        except Exception as e:
            raise ValueError(f"Encryption failed: {str(e)}")
    
    @staticmethod
    def decrypt(encrypted_text: str, key: str) -> str:
        """Decrypt DES CBC encrypted text.
        
        Args:
            encrypted_text: Base64 encoded encrypted text (with IV prepended).
            key: Base64 encoded DES key (8 bytes).
        
        Returns:
            str: Decrypted plaintext.
        
        Raises:
            ValueError: If decryption fails.
        """
        if not encrypted_text or not key:
            raise ValueError("Encrypted text and key cannot be empty.")
        
        try:
            key_bytes = base64.b64decode(key)
            if len(key_bytes) != DESEncryption.KEY_SIZE:
                raise ValueError(f"Key must be {DESEncryption.KEY_SIZE} bytes.")
            
            encrypted_data = base64.b64decode(encrypted_text)
            iv_bytes = encrypted_data[:DESEncryption.BLOCK_SIZE]
            ciphertext = encrypted_data[DESEncryption.BLOCK_SIZE:]
            
            cipher = Cipher(
                algorithms.TripleDES(key_bytes),  # Using TripleDES with single key for DES
                modes.CBC(iv_bytes),
                backend=default_backend()
            )
            decryptor = cipher.decryptor()
            padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
            
            # Remove PKCS7 padding
            padding_length = padded_plaintext[-1]
            plaintext = padded_plaintext[:-padding_length].decode('utf-8')
            return plaintext
        
        except Exception as e:
            raise ValueError(f"Decryption failed: {str(e)}")
