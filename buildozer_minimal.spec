[app]
# Basic app info
title = MinimalTest
package.name = minimaltest  
package.domain = org.test.minimal
source.dir = .
version = 1.0

# Absolute minimal requirements
requirements = python3,kivy

# Basic files
source.include_exts = py
icon.filename = %(source.dir)s/data/icon.png
presplash.filename = %(source.dir)s/data/presplash.png

# Orientation
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[android]
# Use older, more stable versions
android.api = 28
android.minapi = 21
android.ndk = 19c
android.sdk = 28

# Simple architecture
android.archs = armeabi-v7a

# Basic bootstrap
android.bootstrap = sdl2

# Essential permissions only
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Simple settings
android.allow_backup = True
android.copy_libs = 1