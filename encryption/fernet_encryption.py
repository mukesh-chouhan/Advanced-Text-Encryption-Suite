"""Fernet Encryption module using cryptography.fernet."""

import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os


class FernetEncryption:
    """Fernet Symmetric Encryption/Decryption."""
    
    SALT_SIZE = 16
    ITERATIONS = 100000
    
    @staticmethod
    def generate_key() -> str:
        """Generate a random Fernet key.
        
        Returns:
            str: Base64 encoded Fernet key.
        """
        key = Fernet.generate_key()
        return key.decode('utf-8')
    
    @staticmethod
    def derive_key_from_password(password: str, salt: bytes = None) -> tuple:
        """Derive Fernet key from password using PBKDF2HMAC.
        
        Args:
            password: User password.
            salt: Optional salt bytes. If None, a new salt is generated.
        
        Returns:
            tuple: (key, salt) where key is a string and salt is bytes.
        """
        if salt is None:
            salt = os.urandom(FernetEncryption.SALT_SIZE)
        
        kdf = PBKDF2(
            algorithm=hashes.SHA256(),
            length=32,  # Fernet requires 32 bytes for the key
            salt=salt,
            iterations=FernetEncryption.ITERATIONS,
            backend=default_backend()
        )
        key_bytes = kdf.derive(password.encode())
        key = base64.urlsafe_b64encode(key_bytes)
        return key.decode('utf-8'), salt
    
    @staticmethod
    def encrypt(plaintext: str, key: str) -> str:
        """Encrypt plaintext using Fernet.
        
        Args:
            plaintext: Text to encrypt.
            key: Fernet key (base64 encoded).
        
        Returns:
            str: Base64 encoded encrypted text.
        
        Raises:
            ValueError: If encryption fails.
        """
        if not plaintext:
            raise ValueError("Plaintext cannot be empty.")
        if not key:
            raise ValueError("Key cannot be empty.")
        
        try:
            fernet = Fernet(key.encode())
            encrypted = fernet.encrypt(plaintext.encode())
            return base64.b64encode(encrypted).decode('utf-8')
        except Exception as e:
            raise ValueError(f"Encryption failed: {str(e)}")
    
    @staticmethod
    def decrypt(encrypted_text: str, key: str) -> str:
        """Decrypt Fernet encrypted text.
        
        Args:
            encrypted_text: Base64 encoded encrypted text.
            key: Fernet key (base64 encoded).
        
        Returns:
            str: Decrypted plaintext.
        
        Raises:
            ValueError: If decryption fails.
        """
        if not encrypted_text or not key:
            raise ValueError("Encrypted text and key cannot be empty.")
        
        try:
            fernet = Fernet(key.encode())
            ciphertext = base64.b64decode(encrypted_text)
            decrypted = fernet.decrypt(ciphertext)
            return decrypted.decode('utf-8')
        except Exception as e:
            raise ValueError(f"Decryption failed: {str(e)}")
