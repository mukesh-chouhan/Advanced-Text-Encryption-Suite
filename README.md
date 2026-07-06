<<<<<<< HEAD
# Advanced-Text-Encryption-Suite
=======
# Advanced Text Encryption Suite

A professional-grade desktop application for text and file encryption using multiple industry-standard encryption algorithms. Built with Python and CustomTkinter, featuring a modern, cybersecurity-themed GUI.

## Features

### 🔐 Core Encryption Features
- **Multiple Encryption Algorithms**
  - AES-256 CBC Mode
  - DES CBC Mode
  - Triple DES (3DES)
  - RSA-2048 Asymmetric Encryption
  - Fernet (Symmetric Encryption)

- **Text Encryption & Decryption**
  - Large text input areas
  - Automatic key generation
  - Custom key support
  - Real-time encryption/decryption
  - Copy to clipboard functionality
  - Save encrypted text to files

- **File Encryption & Decryption**
  - Encrypt text files securely
  - Decrypt encrypted files
  - Progress indicators
  - Support for any file size
  - Preserves file integrity

- **RSA Key Management**
  - Generate 2048-bit RSA key pairs
  - Load and save keys from files
  - Display key information
  - Extract public key from private key
  - Secure key storage

### 📊 Advanced Features

- **Password-Based Encryption**
  - PBKDF2 key derivation
  - Secure random salt generation
  - SHA-256 hashing
  - Use passwords instead of keys

- **Encryption History**
  - Automatic operation logging
  - Date and time tracking
  - Algorithm and operation type recording
  - History export to JSON
  - Clear history option

- **User Interface**
  - Modern dark mode with blue/green accents
  - Responsive layout (1400x850)
  - Professional typography
  - Smooth animations
  - Rounded buttons and modern cards
  - Status bar with real-time updates
  - Left sidebar navigation

### ⚙️ Settings & Customization
- Dark/Light mode toggle
- Font size adjustment (Small, Medium, Large)
- Theme color customization
- Persistent settings

## Technical Specifications

### Security Features
- ✓ AES-256 with CBC mode and PKCS7 padding
- ✓ Secure random IV generation
- ✓ PBKDF2 for password-based key derivation
- ✓ SHA-256 for hashing operations
- ✓ RSA-2048 with OAEP padding
- ✓ Never hardcoded keys
- ✓ Secure random key generation

### Architecture
- **Modular Design**: Separation of concerns with dedicated modules for encryption, UI, utilities, and history
- **Object-Oriented Programming**: Clean class-based architecture
- **PEP 8 Compliant**: Follows Python best practices
- **Well-Documented**: Comprehensive docstrings and comments
- **Error Handling**: Graceful exception handling throughout

## Project Structure

```
AdvancedTextEncryption/
│
├── main.py                  # Main application entry point
├── requirements.txt         # Python dependencies
├── README.md               # This file
│
├── encryption/             # Encryption algorithms
│   ├── __init__.py
│   ├── aes_encryption.py   # AES-256 CBC implementation
│   ├── des_encryption.py   # DES CBC implementation
│   ├── triple_des_encryption.py  # 3DES implementation
│   ├── rsa_encryption.py   # RSA-2048 implementation
│   └── fernet_encryption.py # Fernet implementation
│
├── ui/                     # User interface components
│   ├── __init__.py
│   ├── components.py       # Reusable UI components
│   ├── dashboard.py        # Dashboard home page
│   ├── encryption.py       # Text encryption page
│   ├── decryption.py       # Text decryption page
│   ├── rsa_keys.py         # RSA key management page
│   ├── file_encryption.py  # File encryption page
│   ├── history.py          # History tracking page
│   └── settings.py         # Settings page
│
├── utils/                  # Utility functions
│   ├── __init__.py
│   ├── config.py           # Configuration and constants
│   ├── key_manager.py      # Key storage and retrieval
│   └── utilities.py        # Helper functions
│
├── history/                # History management
│   └── history_manager.py  # History tracking and export
│
├── keys/                   # RSA key storage (generated)
│
├── assets/                 # Application assets
│
└── screenshots/            # Application screenshots
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone or Download the Project**
```bash
cd AdvancedTextEncryption
```

2. **Create a Virtual Environment (Recommended)**
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. **Install Required Libraries**
```bash
pip install -r requirements.txt
```

## Usage

### Running the Application

```bash
python main.py
```

The application will launch with a modern GUI featuring a left sidebar for navigation and a main content area.

### Basic Workflows

#### Encrypting Text
1. Navigate to **Encrypt** from the sidebar
2. Select an encryption algorithm (AES, DES, 3DES, or Fernet)
3. Click **Generate New Key** to create a key
4. Enter text to encrypt
5. Click **🔐 Encrypt**
6. Copy or save the encrypted output

#### Decrypting Text
1. Navigate to **Decrypt** from the sidebar
2. Select the same algorithm used for encryption
3. Paste the encrypted text
4. Enter the decryption key
5. Click **🔓 Decrypt**

#### Encrypting Files
1. Navigate to **File Encryption**
2. Click **📂 Select File** to choose a text file
3. Generate or paste an encryption key
4. Click **🔐 Encrypt File**
5. Save the encrypted file

#### Managing RSA Keys
1. Navigate to **RSA Keys**
2. Click **Generate Key Pair** to create 2048-bit keys
3. Copy, save, or load keys as needed
4. Use public key for encryption, private key for decryption

#### Viewing History
1. Navigate to **History**
2. View all encryption operations with timestamps
3. Export history to JSON file
4. Clear history if needed

## Algorithm Details

### AES-256 CBC
- Key Size: 256 bits (32 bytes)
- Block Size: 128 bits (16 bytes)
- Mode: Cipher Block Chaining (CBC)
- Padding: PKCS7
- IV: Random, prepended to ciphertext

### DES CBC
- Key Size: 64 bits (8 bytes)
- Block Size: 64 bits
- Mode: Cipher Block Chaining (CBC)
- Padding: PKCS7
- IV: Random, prepended to ciphertext

### Triple DES (3DES)
- Key Size: 192 bits (24 bytes)
- Block Size: 64 bits
- Mode: Cipher Block Chaining (CBC)
- Padding: PKCS7
- IV: Random, prepended to ciphertext

### RSA-2048
- Key Size: 2048 bits
- Padding: OAEP with SHA-256
- Format: PEM (Privacy Enhanced Mail)
- Operations: Encryption with public key, decryption with private key

### Fernet
- Key Size: 256 bits
- Algorithm: AES-128 in CBC mode
- Authenticity: HMAC using SHA256
- Timestamp: Automatic

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| customtkinter | 5.2.0 | Modern GUI framework |
| cryptography | 41.0.7 | Encryption algorithms |
| Pillow | 10.1.0 | Image processing |

## Security Considerations

⚠️ **Important Security Notes:**

1. **Key Storage**: Store encryption keys in a secure location. Do not share unencrypted keys.
2. **Passwords**: Use strong, unique passwords for password-based encryption.
3. **Key Backup**: Back up important RSA private keys in a secure location.
4. **Data Integrity**: Always keep encrypted data in a safe location.
5. **Verification**: Test decryption with known encrypted data before relying on keys for important data.

## Code Quality

- **PEP 8 Compliant**: Follows Python style guidelines
- **Type Hints**: Clear type annotations where applicable
- **Documentation**: Comprehensive docstrings for all functions
- **Error Handling**: Proper exception handling throughout
- **DRY Principle**: No code duplication, reusable components
- **Modularity**: Separation of concerns across modules

## Future Improvements

- [ ] Support for more encryption algorithms (ChaCha20, AES-GCM)
- [ ] Drag-and-drop file encryption
- [ ] Batch file encryption/decryption
- [ ] Cloud backup integration
- [ ] Key password protection
- [ ] Enhanced UI with more animations
- [ ] Multi-language support
- [ ] Command-line interface (CLI)
- [ ] Configuration profiles
- [ ] Encryption strength indicators

## Troubleshooting

### Issue: Import errors when running main.py
**Solution**: Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Issue: CustomTkinter not found
**Solution**: Install CustomTkinter specifically:
```bash
pip install customtkinter
```

### Issue: Decryption failing with "ValueError"
**Solution**: 
- Verify you're using the correct algorithm
- Ensure the key is correct and wasn't modified
- Check that the encrypted text wasn't corrupted

### Issue: Application window too small or misaligned
**Solution**: The application requires minimum 1200x700 resolution. Adjust your display settings or window size.

## Performance

- Encryption/Decryption: < 1 second for typical text (< 1MB)
- RSA Key Generation: ~2-5 seconds (2048-bit)
- Key Derivation (PBKDF2): ~1 second

## License

This project is provided as-is for educational and professional use. Ensure compliance with local laws regarding encryption software.

## Contributing

Contributions are welcome! Please ensure:
- Code follows PEP 8 style guide
- All functions have docstrings
- Error handling is comprehensive
- Changes are well-tested

## Author

Created as a professional encryption suite demonstrating modern Python GUI development with security best practices.

## Support

For issues, questions, or suggestions, please review the code documentation and inline comments for detailed implementation information.

---

**Version**: 1.0.0  
**Last Updated**: 2024  
**Status**: Production Ready
>>>>>>> 7271e62 (initial commit)
