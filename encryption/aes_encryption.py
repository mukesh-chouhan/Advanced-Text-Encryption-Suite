"""AES Encryption module using AES-256 in CBC mode."""

import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class AESEncryption:
    """AES-256 CBC Mode Encryption/Decryption."""
    
    KEY_SIZE = 32  # 256 bits
    BLOCK_SIZE = 16  # 128 bits
    SALT_SIZE = 16
    ITERATIONS = 100000
    
    @staticmethod
    def generate_key() -> str:
        """Generate a random AES-256 key.
        
        Returns:
            str: Base64 encoded key.
        """
        key = os.urandom(AESEncryption.KEY_SIZE)
        return base64.b64encode(key).decode('utf-8')
    
    @staticmethod
    def generate_iv() -> str:
        """Generate a random IV.
        
        Returns:
            str: Base64 encoded IV.
        """
        iv = os.urandom(AESEncryption.BLOCK_SIZE)
        return base64.b64encode(iv).decode('utf-8')
    
    @staticmethod
    def derive_key_from_password(password: str, salt: bytes = None) -> tuple:
        """Derive AES key from password using PBKDF2.
        
        Args:
            password: User password.
            salt: Optional salt bytes. If None, a new salt is generated.
        
        Returns:
            tuple: (key, salt) both as bytes.
        """
        if salt is None:
            salt = os.urandom(AESEncryption.SALT_SIZE)
        
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=AESEncryption.KEY_SIZE,
            salt=salt,
            iterations=AESEncryption.ITERATIONS,
            backend=default_backend()
        )
        key = kdf.derive(password.encode())
        return key, salt
    
    @staticmethod
    def encrypt(plaintext: str, key: str, iv: str = None) -> str:
        """Encrypt plaintext using AES-256 CBC.
        
        Args:
            plaintext: Text to encrypt.
            key: Base64 encoded AES-256 key.
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
            if len(key_bytes) != AESEncryption.KEY_SIZE:
                raise ValueError(f"Key must be {AESEncryption.KEY_SIZE} bytes.")
            
            if iv is None:
                iv_bytes = os.urandom(AESEncryption.BLOCK_SIZE)
            else:
                iv_bytes = base64.b64decode(iv)
            
            # Pad plaintext using PKCS7
            padding_length = AESEncryption.BLOCK_SIZE - (len(plaintext.encode()) % AESEncryption.BLOCK_SIZE)
            padded_plaintext = plaintext.encode() + bytes([padding_length] * padding_length)
            
            cipher = Cipher(
                algorithms.AES(key_bytes),
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
        """Decrypt AES-256 CBC encrypted text.
        
        Args:
            encrypted_text: Base64 encoded encrypted text (with IV prepended).
            key: Base64 encoded AES-256 key.
        
        Returns:
            str: Decrypted plaintext.
        
        Raises:
            ValueError: If decryption fails.
        """
        if not encrypted_text or not key:
            raise ValueError("Encrypted text and key cannot be empty.")
        
        try:
            key_bytes = base64.b64decode(key)
            if len(key_bytes) != AESEncryption.KEY_SIZE:
                raise ValueError(f"Key must be {AESEncryption.KEY_SIZE} bytes.")
            
            encrypted_data = base64.b64decode(encrypted_text)
            iv_bytes = encrypted_data[:AESEncryption.BLOCK_SIZE]
            ciphertext = encrypted_data[AESEncryption.BLOCK_SIZE:]
            
            cipher = Cipher(
                algorithms.AES(key_bytes),
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
