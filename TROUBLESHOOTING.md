# PRIME Tool Android Crash Troubleshooting Guide

## Current Status
- ✗ All test apps crash (Python-only, minimal Kivy, gradual tests)
- ✗ Even absolute minimal tests crash
- ✗ Issue appears to be fundamental build/device compatibility

## Immediate Diagnostic Steps

### 1. Get Detailed Crash Information
```bash
# Clear logcat and get fresh crash log
adb logcat -c
adb logcat > crash_log.txt

# In another terminal, install and run test app
adb install -r bin/*.apk
adb shell am start -n org.test.minimal/.PythonActivity

# Wait for crash, then check crash_log.txt
```

### 2. Check Build Environment
```bash
# Check buildozer version
buildozer --version

# Check if buildozer can detect Android SDK
buildozer android list_targets

# Check Java version
java -version

# Check Android SDK path
echo $ANDROID_SDK_ROOT
echo $ANDROID_HOME
```

### 3. Device-Specific Checks (OPPO CPH1937)

**Known Issues with OPPO Devices:**
- Custom Android ROM with aggressive restrictions
- Modified security policies
- Non-standard OpenGL implementations
- Strict app execution policies

**Device Settings to Check:**
1. **Developer Options:**
   - USB Debugging: ON
   - Install via USB: ON
   - USB Debugging (Security Settings): ON
   - Verify apps over USB: OFF
   
2. **Security Settings:**
   - Unknown Sources: Allow for test apps
   - Install unknown apps: Allow for your test method
   
3. **Battery Optimization:**
   - Find your test app in battery settings
   - Set to "Don't optimize" or "No restrictions"
   
4. **App Permissions:**
   - Manually grant ALL permissions before running
   - Check "Special app access" permissions

### 4. Alternative Build Approaches

#### Option A: Try Different Architecture
```ini
# In buildozer.spec, try different arch
android.archs = armeabi-v7a
# OR
android.archs = arm64-v8a
# OR  
android.archs = armeabi-v7a, arm64-v8a
```

#### Option B: Try Older Android API
```ini
# In buildozer.spec
android.api = 27
android.minapi = 19
android.sdk = 27
android.ndk = 17c
```

#### Option C: Try Different Bootstrap
```ini
# In buildozer.spec
android.bootstrap = pygame
# OR
android.bootstrap = webview
```

### 5. Test on Different Device
If possible, test the same APK on:
- Different Android device (non-OPPO)
- Android emulator
- Different Android version

## Most Likely Causes (in order of probability)

### 1. OPPO-Specific Security Restrictions
**Solution:** Disable ColorOS security features:
- Settings > Security > Unknown Source Scanner: OFF
- Settings > Battery > Battery Optimization: Add app to whitelist
- Settings > Apps > Special Access > Install unknown apps: Allow

### 2. Incompatible Android Version/Architecture
**Your Device:** OPPO CPH1937, Android 11, ARM64
**Solution:** Try buildozer.spec with:
```ini
android.api = 30
android.minapi = 21  
android.archs = arm64-v8a
android.ndk = 21b
```

### 3. Build Environment Issues
**Solution:** 
```bash
# Completely clean and reinstall buildozer
pip uninstall buildozer
pip install buildozer==1.4.0

# Clean everything
rm -rf .buildozer/
rm -rf bin/
buildozer android clean
```

### 4. Corrupted APK Installation
**Solution:**
```bash
# Completely remove any existing installations
adb uninstall org.pagibig.primetool.primetool
adb uninstall org.test.minimal  
adb uninstall org.test.minimaltest

# Clear cache
adb shell pm clear org.pagibig.primetool.primetool
```

## Next Steps

1. **Get the exact crash logcat** - This is crucial
2. **Try the OPPO-specific settings** above
3. **Test different buildozer.spec configurations**
4. **If available, test on different device**

## Emergency Alternative: APK from Different Source

If all else fails, we can try building with:
- GitHub Actions (cloud build)
- Docker container
- Different build machine
- Python-for-android directly (bypassing buildozer)

---

**MOST IMPORTANT:** Get the detailed logcat crash log - this will tell us exactly what's failing.