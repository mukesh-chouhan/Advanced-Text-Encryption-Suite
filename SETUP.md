# Setup Instructions

## Prerequisites

- **Python 3.8+** installed on your system
- **pip** (Python package manager)
- At least 100 MB of free disk space
- Administrator privileges (for some system setups)

## Installation Steps

### Step 1: Verify Python Installation

Open your terminal/command prompt and verify Python is installed:

```bash
python --version
```

Should output: Python 3.8.0 or higher

### Step 2: Navigate to Project Directory

```bash
cd path/to/AdvancedTextEncryption
```

### Step 3: Create Virtual Environment (Recommended)

Creating a virtual environment is highly recommended to avoid conflicts with other Python packages.

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

After activation, your terminal should show `(venv)` at the beginning of the line.

### Step 4: Upgrade pip (Optional but Recommended)

```bash
python -m pip install --upgrade pip
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- **customtkinter**: Modern GUI framework
- **cryptography**: Encryption algorithms
- **Pillow**: Image processing support

The installation should complete within 2-3 minutes depending on your internet speed.

### Step 6: Verify Installation

```bash
python -c "import customtkinter; import cryptography; print('✓ All dependencies installed successfully')"
```

If you see the success message, you're ready to go!

## Troubleshooting Installation

### Issue: "Python command not found"
**Solution**: 
- Ensure Python is installed from python.org
- Add Python to your system PATH
- Try using `python3` instead of `python`

### Issue: "Permission denied" when activating venv
**Solution**:
- On Windows, try running Command Prompt as Administrator
- On macOS/Linux, ensure file permissions are correct: `chmod +x venv/bin/activate`

### Issue: "pip command not found"
**Solution**:
- Ensure pip is installed: `python -m ensurepip`
- Or upgrade Python to the latest version

### Issue: Installation takes too long
**Solution**:
- Check your internet connection
- Try using a different PyPI mirror:
  ```bash
  pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
  ```

### Issue: Module not found errors
**Solution**:
- Ensure virtual environment is activated (should see `(venv)` prefix)
- Verify requirements are installed: `pip list`
- Reinstall requirements: `pip install -r requirements.txt --force-reinstall`

## Running the Application

### First Run

```bash
python main.py
```

The application window should open within 2-3 seconds.

### Running from Different Directory

If running from a different directory, use:

```bash
python /path/to/AdvancedTextEncryption/main.py
```

## Deactivating Virtual Environment

When you're done using the application:

```bash
deactivate
```

## System Requirements

| Component | Requirement |
|-----------|------------|
| OS | Windows 10+, macOS 10.12+, Linux (Ubuntu 18.04+) |
| Python | 3.8 - 3.11 |
| RAM | 512 MB minimum |
| Disk Space | 200 MB |
| Display Resolution | 1200 x 700 minimum |

## Installing on Different Platforms

### Windows

1. Download Python from python.org
2. Run the installer with "Add Python to PATH" checked
3. Open Command Prompt and follow steps above

### macOS

```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python3

# Follow installation steps above
```

### Linux (Ubuntu/Debian)

```bash
# Update package manager
sudo apt-get update

# Install Python and pip
sudo apt-get install python3 python3-pip python3-venv

# Follow installation steps above
```

### Linux (Fedora/RHEL)

```bash
# Install Python and pip
sudo dnf install python3 python3-pip

# Follow installation steps above
```

## Post-Installation Configuration

### Optional: Create Desktop Shortcut (Windows)

1. Create a new file named `run_encryption.bat`
2. Add the following content:
   ```batch
   @echo off
   cd /d "%~dp0"
   venv\Scripts\python.exe main.py
   pause
   ```
3. Save and double-click to run

### Optional: Create Shell Alias (macOS/Linux)

Add to your `.bashrc` or `.zshrc`:
```bash
alias encryption="cd ~/path/to/AdvancedTextEncryption && source venv/bin/activate && python main.py"
```

Then use: `encryption` to launch the app

## Updating Dependencies

To update all dependencies to their latest versions:

```bash
pip install -r requirements.txt --upgrade
```

## Uninstalling

To remove the application:

1. Deactivate virtual environment: `deactivate`
2. Delete the project folder
3. Delete the virtual environment folder (if applicable)

## Getting Help

- Check the README.md for feature documentation
- Review the QUICKSTART.md for common use cases
- Check inline code comments for implementation details
- See individual module docstrings for API documentation

## Next Steps

After successful installation, proceed to [QUICKSTART.md](QUICKSTART.md) for usage instructions.
