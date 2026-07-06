"""Key management utilities."""

import os
from pathlib import Path
from typing import Optional
from encryption.aes_encryption import AESEncryption
from encryption.des_encryption import DESEncryption
from encryption.triple_des_encryption import TripleDESEncryption
from encryption.rsa_encryption import RSAEncryption
from encryption.fernet_encryption import FernetEncryption


class KeyManager:
    """Manages encryption keys - generation, storage, and retrieval."""
    
    def __init__(self, keys_dir: Path):
        """Initialize key manager.
        
        Args:
            keys_dir: Directory to store keys.
        """
        self.keys_dir = Path(keys_dir)
        self.keys_dir.mkdir(parents=True, exist_ok=True)
    
    def generate_key(self, algorithm: str) -> str:
        """Generate a key for the specified algorithm.
        
        Args:
            algorithm: Name of the algorithm ("AES", "DES", "3DES", "Fernet").
        
        Returns:
            Base64 encoded key.
        
        Raises:
            ValueError: If algorithm is not supported.
        """
        if algorithm == "AES":
            return AESEncryption.generate_key()
        elif algorithm == "DES":
            return DESEncryption.generate_key()
        elif algorithm == "3DES":
            return TripleDESEncryption.generate_key()
        elif algorithm == "Fernet":
            return FernetEncryption.generate_key()
        else:
            raise ValueError(f"Unsupported algorithm: {algorithm}")
    
    def save_key(self, key: str, filename: str) -> Path:
        """Save a key to a file.
        
        Args:
            key: Key to save.
            filename: Name of the file.
        
        Returns:
            Path to the saved file.
        
        Raises:
            ValueError: If saving fails.
        """
        try:
            filepath = self.keys_dir / filename
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(key)
            return filepath
        except Exception as e:
            raise ValueError(f"Failed to save key: {str(e)}")
    
    def load_key(self, filename: str) -> Optional[str]:
        """Load a key from a file.
        
        Args:
            filename: Name of the file.
        
        Returns:
            The key if file exists, None otherwise.
        
        Raises:
            ValueError: If loading fails.
        """
        try:
            filepath = self.keys_dir / filename
            if filepath.exists():
                with open(filepath, 'r', encoding='utf-8') as f:
                    return f.read().strip()
            return None
        except Exception as e:
            raise ValueError(f"Failed to load key: {str(e)}")
    
    def save_rsa_keys(self, private_key: str, public_key: str, 
                      private_filename: str = "rsa_private_key.pem",
                      public_filename: str = "rsa_public_key.pem") -> tuple:
        """Save RSA key pair to files.
        
        Args:
            private_key: Private key.
            public_key: Public key.
            private_filename: Name for private key file.
            public_filename: Name for public key file.
        
        Returns:
            Tuple of (private_key_path, public_key_path).
        
        Raises:
            ValueError: If saving fails.
        """
        try:
            private_path = self.save_key(private_key, private_filename)
            public_path = self.save_key(public_key, public_filename)
            return private_path, public_path
        except Exception as e:
            raise ValueError(f"Failed to save RSA keys: {str(e)}")
    
    def load_rsa_keys(self, private_filename: str = "rsa_private_key.pem",
                      public_filename: str = "rsa_public_key.pem") -> tuple:
        """Load RSA key pair from files.
        
        Args:
            private_filename: Name of private key file.
            public_filename: Name of public key file.
        
        Returns:
            Tuple of (private_key, public_key) or (None, None) if not found.
        """
        private_key = self.load_key(private_filename)
        public_key = self.load_key(public_filename)
        return private_key, public_key
    
    def list_keys(self) -> list:
        """List all key files in the keys directory.
        
        Returns:
            List of filenames.
        """
        if not self.keys_dir.exists():
            return []
        return [f.name for f in self.keys_dir.glob("*.pem") if f.is_file()]
    
    def delete_key(self, filename: str) -> bool:
        """Delete a key file.
        
        Args:
            filename: Name of the file to delete.
        
        Returns:
            True if deleted, False if file doesn't exist.
        """
        try:
            filepath = self.keys_dir / filename
            if filepath.exists():
                filepath.unlink()
                return True
            return False
        except Exception as e:
            raise ValueError(f"Failed to delete key: {str(e)}")
