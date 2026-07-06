# Quick Start Guide

## Running the Application

After installation (see SETUP.md), run the application with:

```bash
python main.py
```

Or from the project directory:
```bash
python /path/to/AdvancedTextEncryption/main.py
```

## Application Interface

The application has a professional layout with:
- **Left Sidebar**: Navigation menu
- **Main Content Area**: Current page content
- **Status Bar**: Shows current operation status

## Common Tasks

### 1. Encrypting Text (AES-256)

1. **Navigate to Encrypt**: Click "🔐 Encrypt" in the left sidebar
2. **Select Algorithm**: Dropdown shows "AES" (default, recommended)
3. **Generate Key**: Click "Generate New Key"
4. **Enter Text**: Paste or type text in "Text to Encrypt" area
5. **Encrypt**: Click "🔐 Encrypt" button
6. **Copy/Save**: 
   - Click "📋 Copy Output" to copy to clipboard
   - Click "💾 Save Output" to save as text file

### 2. Decrypting Text

1. **Navigate to Decrypt**: Click "🔓 Decrypt" in sidebar
2. **Select Algorithm**: Choose the same algorithm used for encryption
3. **Paste Encrypted Text**: Paste the encrypted message
4. **Enter Key**: Paste the decryption key
5. **Decrypt**: Click "🔓 Decrypt" button
6. **View Result**: Decrypted text appears below

### 3. Encrypting Files

1. **Go to File Encryption**: Click "📁 File Encryption"
2. **Select File**: Click "📂 Select File" and choose a text file
3. **Generate/Paste Key**: Create or paste encryption key
4. **Encrypt**: Click "🔐 Encrypt File"
5. **Save**: Choose save location (e.g., `filename.encrypted`)

### 4. Managing RSA Keys

1. **Go to RSA Keys**: Click "🔑 RSA Keys"
2. **Generate Pair**: Click "Generate Key Pair" (takes 2-5 seconds)
3. **Save Keys**: Click "💾 Save" for private and public keys
4. **Load Existing**: Click "📂 Load" to use previously saved keys

### 5. Viewing Operation History

1. **Go to History**: Click "📊 History"
2. **View Entries**: See all encryption/decryption operations
3. **Export**: Click "📤 Export" to save history as JSON
4. **Clear**: Click "🗑️ Clear History" if needed

### 6. Changing Settings

1. **Go to Settings**: Click "⚙️ Settings"
2. **Theme**: Choose "🌙 Dark" or "☀️ Light" mode
3. **Font Size**: Select "Small", "Medium", or "Large"
4. **About**: View application information

## Example Workflows

### Workflow 1: Simple Text Encryption for Email

```
1. Go to Encrypt
2. Select "AES" algorithm
3. Click "Generate New Key" → copy the key to safe location
4. Paste email text to encrypt
5. Click "Encrypt"
6. Copy encrypted text and send via email
7. Recipient uses Decrypt with same key to read it
```

### Workflow 2: Secure File Storage

```
1. Go to File Encryption
2. Select sensitive file
3. Generate and save encryption key in secure location
4. Click "Encrypt File"
5. Delete original file (optional)
6. To access later: Go to File Encryption
   → Select encrypted file
   → Paste saved key
   → Click "Decrypt File"
```

### Workflow 3: RSA Key-Pair Encryption

```
1. Go to RSA Keys
2. Generate and save key pair
3. Share only the PUBLIC KEY with others
4. Others encrypt messages to you with your public key
5. You decrypt with your private key
```

## Available Algorithms Comparison

| Algorithm | Type | Key Size | Speed | Security | Best For |
|-----------|------|----------|-------|----------|----------|
| **AES** | Symmetric | 256-bit | ⚡⚡⚡ | ★★★★★ | Most uses |
| **DES** | Symmetric | 64-bit | ⚡⚡⚡ | ★★☆☆☆ | Legacy/Demo |
| **3DES** | Symmetric | 192-bit | ⚡⚡ | ★★★★☆ | Compatibility |
| **Fernet** | Symmetric | 256-bit | ⚡⚡⚡ | ★★★★★ | Timestamps |
| **RSA** | Asymmetric | 2048-bit | ⚡ | ★★★★★ | Key exchange |

**Recommendation**: Use **AES** for most text encryption tasks.

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Generate Key | -none- (button click) |
| Encrypt/Decrypt | -none- (button click) |
| Copy to Clipboard | Button click |
| Clear All | Button click |

## Tips & Tricks

✅ **Do's:**
- Save encryption keys in a secure location
- Use AES for general-purpose encryption
- Export history for record-keeping
- Test decryption with a small message first
- Back up RSA private keys

❌ **Don'ts:**
- Don't lose your encryption keys
- Don't share private RSA keys
- Don't forget which algorithm you used for encryption
- Don't modify encrypted text
- Don't store keys with encrypted data

## Common Errors & Solutions

### Error: "Decryption failed"
- **Cause**: Wrong key or wrong algorithm
- **Fix**: Verify key matches encryption key and algorithm is correct

### Error: "Invalid base64"
- **Cause**: Encrypted text was corrupted or modified
- **Fix**: Ensure you have the exact encrypted text without changes

### Error: "Key must be X bytes"
- **Cause**: Key size doesn't match algorithm
- **Fix**: Generate a new key with "Generate Key" button

### Error: "No file selected"
- **Cause**: Tried to encrypt without selecting file
- **Fix**: Click "📂 Select File" first

### Application runs slowly
- **Cause**: RSA key generation or large file processing
- **Fix**: This is normal. RSA key generation takes 2-5 seconds.

## File Formats

### Encrypted Files
- Extension: `.encrypted` (recommended) or `.txt`
- Format: Base64-encoded ciphertext with IV prepended
- Human-readable: No (binary-safe format)

### Key Files
- Extension: `.pem` (RSA keys)
- Format: Plain text, base64-encoded for symmetric keys
- Shareable: Public keys only (mark as PUBLIC KEY)

## Performance Notes

| Operation | Time |
|-----------|------|
| Encrypt 1KB text (AES) | < 0.1 second |
| Decrypt 1KB text (AES) | < 0.1 second |
| Generate AES key | Instant |
| Generate RSA key pair | 2-5 seconds |
| Encrypt file (100MB) | 1-5 seconds |

## Data Safety

⚠️ **Important:**
- This application does NOT recover lost keys
- Lost encryption keys = lost data permanently
- Always maintain secure backups of keys
- Test your key recovery procedure

## Getting More Help

- See README.md for complete documentation
- See SETUP.md for installation help
- Check source code comments for implementation details
- Each module has comprehensive docstrings

## Next Steps

1. ✅ Successfully installed application
2. 📖 Read this Quick Start Guide
3. 🧪 Try encrypting a test message
4. 🔐 Encrypt your first important file
5. 📚 Explore all features systematically

---

**Happy Encrypting!** 🔐

For issues or questions, refer to the full documentation in README.md
