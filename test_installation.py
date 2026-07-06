#!/usr/bin/env python3
"""Test and verification script for Advanced Text Encryption Suite."""

import sys
import importlib
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))


def test_imports():
    """Test all required imports."""
    print("=" * 60)
    print("Testing Module Imports...")
    print("=" * 60)
    
    modules_to_test = [
        ("customtkinter", "UI Framework"),
        ("cryptography", "Encryption Library"),
        ("Pillow", "Image Processing"),
    ]
    
    all_ok = True
    for module_name, description in modules_to_test:
        try:
            importlib.import_module(module_name)
            print(f"✓ {module_name:20} - {description}")
        except ImportError as e:
            print(f"✗ {module_name:20} - MISSING: {description}")
            all_ok = False
    
    print()
    return all_ok


def test_local_modules():
    """Test local module imports."""
    print("=" * 60)
    print("Testing Local Modules...")
    print("=" * 60)
    
    local_modules = [
        ("utils.config", "Configuration"),
        ("utils.key_manager", "Key Management"),
        ("utils.utilities", "Utilities"),
        ("encryption.aes_encryption", "AES Encryption"),
        ("encryption.des_encryption", "DES Encryption"),
        ("encryption.triple_des_encryption", "3DES Encryption"),
        ("encryption.rsa_encryption", "RSA Encryption"),
        ("encryption.fernet_encryption", "Fernet Encryption"),
        ("history.history_manager", "History Manager"),
        ("ui.components", "UI Components"),
        ("ui.dashboard", "Dashboard UI"),
        ("ui.encryption", "Encryption UI"),
        ("ui.decryption", "Decryption UI"),
        ("ui.rsa_keys", "RSA Keys UI"),
        ("ui.file_encryption", "File Encryption UI"),
        ("ui.history", "History UI"),
        ("ui.settings", "Settings UI"),
    ]
    
    all_ok = True
    for module_name, description in local_modules:
        try:
            importlib.import_module(module_name)
            print(f"✓ {module_name:40} - {description}")
        except Exception as e:
            print(f"✗ {module_name:40} - ERROR: {str(e)[:30]}")
            all_ok = False
    
    print()
    return all_ok


def test_encryption():
    """Test encryption functionality."""
    print("=" * 60)
    print("Testing Encryption Functions...")
    print("=" * 60)
    
    try:
        from encryption.aes_encryption import AESEncryption
        from encryption.fernet_encryption import FernetEncryption
        from encryption.rsa_encryption import RSAEncryption
        
        test_message = "Hello, World! This is a test message."
        
        # Test AES
        print("Testing AES-256...")
        key = AESEncryption.generate_key()
        encrypted = AESEncryption.encrypt(test_message, key)
        decrypted = AESEncryption.decrypt(encrypted, key)
        assert decrypted == test_message, "AES decryption mismatch"
        print("✓ AES encryption/decryption works correctly")
        
        # Test Fernet
        print("Testing Fernet...")
        key = FernetEncryption.generate_key()
        encrypted = FernetEncryption.encrypt(test_message, key)
        decrypted = FernetEncryption.decrypt(encrypted, key)
        assert decrypted == test_message, "Fernet decryption mismatch"
        print("✓ Fernet encryption/decryption works correctly")
        
        # Test RSA
        print("Testing RSA-2048...")
        private_key, public_key = RSAEncryption.generate_key_pair()
        encrypted = RSAEncryption.encrypt(test_message, public_key)
        decrypted = RSAEncryption.decrypt(encrypted, private_key)
        assert decrypted == test_message, "RSA decryption mismatch"
        print("✓ RSA encryption/decryption works correctly")
        
        print()
        return True
    
    except Exception as e:
        print(f"✗ Encryption test failed: {str(e)}")
        print()
        return False


def test_file_system():
    """Test file system operations."""
    print("=" * 60)
    print("Testing File System...")
    print("=" * 60)
    
    try:
        from utils.config import KEYS_DIR, HISTORY_DIR
        from pathlib import Path
        
        # Check directories exist
        assert KEYS_DIR.exists(), "Keys directory doesn't exist"
        print(f"✓ Keys directory: {KEYS_DIR}")
        
        assert HISTORY_DIR.exists(), "History directory doesn't exist"
        print(f"✓ History directory: {HISTORY_DIR}")
        
        # Check permissions
        test_file = KEYS_DIR / ".test"
        try:
            test_file.write_text("test")
            test_file.unlink()
            print("✓ Directory write permissions: OK")
        except PermissionError:
            print("✗ Directory write permissions: DENIED")
            return False
        
        print()
        return True
    
    except Exception as e:
        print(f"✗ File system test failed: {str(e)}")
        print()
        return False


def test_ui():
    """Test UI components."""
    print("=" * 60)
    print("Testing UI Components...")
    print("=" * 60)
    
    try:
        from ui.components import (
            CTkCard, CTkButton, CTkLabel, CTkEntry, CTkTextBox
        )
        print("✓ All UI components imported successfully")
        print()
        return True
    
    except Exception as e:
        print(f"✗ UI test failed: {str(e)}")
        print()
        return False


def main():
    """Run all tests."""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + "  Advanced Text Encryption Suite - Verification Test".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "=" * 58 + "╝")
    print("\n")
    
    results = {}
    
    # Run tests
    results['imports'] = test_imports()
    results['local_modules'] = test_local_modules()
    results['encryption'] = test_encryption()
    results['file_system'] = test_file_system()
    results['ui'] = test_ui()
    
    # Summary
    print("=" * 60)
    print("Test Summary")
    print("=" * 60)
    
    for test_name, result in results.items():
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"{test_name.replace('_', ' ').title():30} {status}")
    
    print("=" * 60)
    
    all_passed = all(results.values())
    
    if all_passed:
        print("\n✓ All tests PASSED! Application is ready to use.")
        print("\nRun the application with: python main.py\n")
        return 0
    else:
        print("\n✗ Some tests FAILED. Please review the errors above.")
        print("\nFor help, see SETUP.md or README.md\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
