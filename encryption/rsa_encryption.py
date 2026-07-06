"""RSA Encryption module using 2048-bit RSA keys."""

import os
import base64
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend


class RSAEncryption:
    """RSA 2048-bit Encryption/Decryption."""
    
    KEY_SIZE = 2048
    PUBLIC_EXPONENT = 65537
    
    @staticmethod
    def generate_key_pair() -> tuple:
        """Generate RSA 2048-bit key pair.
        
        Returns:
            tuple: (private_key_pem, public_key_pem) as base64 encoded strings.
        """
        private_key = rsa.generate_private_key(
            public_exponent=RSAEncryption.PUBLIC_EXPONENT,
            key_size=RSAEncryption.KEY_SIZE,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        
        # Serialize to PEM format
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        
        return (
            (private_pem).decode('utf-8'),
            (public_pem).decode('utf-8')
        )
    
    @staticmethod
    def _normalize_pem(key_pem: str) -> bytes:
        """Normalize PEM input to bytes.

        Accepts either raw PEM text or base64-encoded PEM text.
        """
        if not key_pem:
            raise ValueError("Key PEM data cannot be empty.")

        pem_text = key_pem.strip()
        if pem_text.startswith("-----BEGIN ") and "-----END " in pem_text:
            return pem_text.encode("utf-8")

        try:
            decoded = base64.b64decode(pem_text, validate=True)
            if decoded.startswith(b"-----BEGIN ") and b"-----END " in decoded:
                return decoded
        except Exception:
            pass

        if "-----BEGIN " in pem_text and "-----END " in pem_text:
            return pem_text.encode("utf-8")

        raise ValueError("Invalid PEM format: key must be raw PEM text or base64-encoded PEM.")

    @staticmethod
    def get_public_key_from_private(private_key_pem: str) -> str:
        """Extract public key from private key.
        
        Args:
            private_key_pem: Private key in PEM format, raw text or base64 encoded.
        
        Returns:
            str: Public key in PEM format as raw text.
        
        Raises:
            ValueError: If private key is invalid.
        """
        try:
            private_pem = RSAEncryption._normalize_pem(private_key_pem)
            private_key = serialization.load_pem_private_key(
                private_pem,
                password=None,
                backend=default_backend()
            )
            public_key = private_key.public_key()
            
            public_pem = public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
            return public_pem.decode('utf-8')
        except Exception as e:
            raise ValueError(f"Failed to extract public key: {str(e)}")
    
    @staticmethod
    def encrypt(plaintext: str, public_key_pem: str) -> str:
        """Encrypt plaintext using RSA public key.
        
        Args:
            plaintext: Text to encrypt.
            public_key_pem: Base64 encoded RSA public key in PEM format.
        
        Returns:
            str: Base64 encoded encrypted text.
        
        Raises:
            ValueError: If encryption fails.
        """
        if not plaintext:
            raise ValueError("Plaintext cannot be empty.")
        if not public_key_pem:
            raise ValueError("Public key cannot be empty.")
        
        try:
            public_pem = RSAEncryption._normalize_pem(public_key_pem)
            public_key = serialization.load_pem_public_key(
                public_pem,
                backend=default_backend()
            )
            
            ciphertext = public_key.encrypt(
                plaintext.encode(),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            return base64.b64encode(ciphertext).decode('utf-8')
        except Exception as e:
            raise ValueError(f"Encryption failed: {str(e)}")
    
    @staticmethod
    def decrypt(encrypted_text: str, private_key_pem: str) -> str:
        """Decrypt RSA encrypted text using private key.
        
        Args:
            encrypted_text: Base64 encoded encrypted text.
            private_key_pem: Base64 encoded RSA private key in PEM format.
        
        Returns:
            str: Decrypted plaintext.
        
        Raises:
            ValueError: If decryption fails.
        """
        if not encrypted_text or not private_key_pem:
            raise ValueError("Encrypted text and private key cannot be empty.")
        
        try:
            private_pem = RSAEncryption._normalize_pem(private_key_pem)
            private_key = serialization.load_pem_private_key(
                private_pem,
                password=None,
                backend=default_backend()
            )
            
            ciphertext = base64.b64decode(encrypted_text)
            plaintext = private_key.decrypt(
                ciphertext,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            return plaintext.decode('utf-8')
        except Exception as e:
            raise ValueError(f"Decryption failed: {str(e)}")
    
    @staticmethod
    def get_key_info(key_pem: str, key_type: str = "public") -> dict:
        """Get information about an RSA key.
        
        Args:
            key_pem: Base64 encoded key in PEM format.
            key_type: Either "public" or "private".
        
        Returns:
            dict: Key information including size and algorithm.
        
        Raises:
            ValueError: If key is invalid.
        """
        try:
            key_bytes = RSAEncryption._normalize_pem(key_pem)
            
            if key_type == "private":
                key = serialization.load_pem_private_key(
                    key_bytes,
                    password=None,
                    backend=default_backend()
                )
            else:
                key = serialization.load_pem_public_key(
                    key_bytes,
                    backend=default_backend()
                )
            
            return {
                "algorithm": "RSA",
                "key_size": key.key_size,
                "key_type": key_type
            }
        except Exception as e:
            raise ValueError(f"Failed to get key info: {str(e)}")
