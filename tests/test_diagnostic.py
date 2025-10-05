#!/usr/bin/env python3
"""
Build Environment Diagnostic
"""

print("=== BUILD ENVIRONMENT DIAGNOSTIC ===")

import os
import sys

print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print(f"Current directory: {os.getcwd()}")
print(f"OS: {os.name}")

# Check if buildozer files exist
files_to_check = [
    'buildozer.spec',
    'main.py', 
    'data/icon.png',
    'data/presplash.png'
]

print("\nFile Check:")
for file in files_to_check:
    exists = "✓" if os.path.exists(file) else "✗"
    print(f"{exists} {file}")

# Check Python path
print(f"\nPython path:")
for path in sys.path:
    print(f"  {path}")

# Test basic imports that should always work
basic_imports = ['os', 'sys', 'sqlite3', 'json', 'datetime']
print(f"\nBasic imports:")
for module in basic_imports:
    try:
        __import__(module)
        print(f"✓ {module}")
    except Exception as e:
        print(f"✗ {module}: {e}")

# Check if we can detect Android
try:
    from android.storage import primary_external_storage_path
    print("\n✓ Android environment detected")
    storage = primary_external_storage_path()
    print(f"Storage path: {storage}")
except ImportError:
    print("\n• Desktop environment (expected)")

print("\n=== DIAGNOSTIC COMPLETE ===")

# Exit cleanly
sys.exit(0)