# PRIME Tool - WSL Build Instructions

## Why WSL is Better for Android Builds

1. **Better buildozer compatibility** - Linux environment
2. **Stable Python versions** - Use Python 3.8-3.10 (tested with buildozer)
3. **Proper file permissions** - No Windows permission issues
4. **Better debugging tools** - Native ADB and logcat support

## Setup Instructions

### Step 1: Install Ubuntu on WSL
```bash
# Install Ubuntu (if not already done)
wsl --install -d Ubuntu

# Or update existing WSL
wsl --update
```

### Step 2: Setup Python Build Environment in WSL
```bash
# Enter WSL
wsl

# Update system
sudo apt update && sudo apt upgrade -y

# Install Python 3.10 (stable for buildozer)
sudo apt install python3.10 python3.10-venv python3.10-dev python3-pip -y

# Create virtual environment
python3.10 -m venv prime_env
source prime_env/bin/activate

# Install buildozer and dependencies
pip install buildozer cython==0.29.33

# Install Android build dependencies
sudo apt install -y git zip unzip openjdk-11-jdk autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
```

### Step 3: Copy Project to WSL
```bash
# From WSL, access Windows files
cd /mnt/c/PRIMETool2025

# Or copy to WSL filesystem (faster builds)
cp -r /mnt/c/PRIMETool2025 ~/prime_tool
cd ~/prime_tool
```

### Step 4: Build Android APK in WSL
```bash
# Activate environment
source ~/prime_env/bin/activate

# Build APK
buildozer android debug

# The APK will be in bin/ folder
ls -la bin/
```

### Step 5: Install APK to Android Device
```bash
# Install ADB in WSL
sudo apt install android-tools-adb -y

# Connect device and install
adb devices
adb install -r bin/*.apk
```

## Alternative: Docker Build (if WSL issues)

If WSL still has issues, we can use Docker:

```bash
# Create Dockerfile for consistent build environment
docker run -it --rm -v "C:\PRIMETool2025:/app" kivy/buildozer bash
cd /app
buildozer android debug
```

## Why This Will Work Better

1. **Linux environment** - buildozer is designed for Linux
2. **Stable Python version** - 3.10 is well-tested with buildozer
3. **Proper dependencies** - All Android build tools work correctly
4. **Better debugging** - ADB and logcat work natively
5. **No permission issues** - Linux file permissions

---

**Recommendation: Try WSL first. It's the most reliable way to build Android APKs from Windows.**