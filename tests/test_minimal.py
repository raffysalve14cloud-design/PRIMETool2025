#!/usr/bin/env python3
# Absolute minimal test - just print and exit
print("=== MINIMAL TEST START ===")

try:
    import sys
    print(f"Python version: {sys.version}")
    
    import os
    print(f"OS: {os.name}")
    
    # Test if we're on Android
    try:
        from android.storage import primary_external_storage_path
        print("Platform: Android")
        storage = primary_external_storage_path()
        print(f"Storage: {storage}")
    except ImportError:
        print("Platform: Desktop")
    
    # Test basic imports one by one
    print("Testing imports...")
    
    try:
        import kivy
        print(f"✓ Kivy {kivy.__version__} imported")
    except Exception as e:
        print(f"✗ Kivy import failed: {e}")
        exit(1)
    
    try:
        from kivy.app import App
        print("✓ Kivy App imported")
    except Exception as e:
        print(f"✗ Kivy App import failed: {e}")
        exit(1)
        
    try:
        from kivy.uix.label import Label
        print("✓ Kivy Label imported")
    except Exception as e:
        print(f"✗ Kivy Label import failed: {e}")
        exit(1)
    
    # Create absolute minimal Kivy app
    class MinimalApp(App):
        def build(self):
            print("Building minimal app...")
            return Label(text='Minimal Test - Kivy Works!')
        
        def on_start(self):
            print("Minimal app started!")
            
        def on_stop(self):
            print("Minimal app stopped!")
    
    print("Creating app...")
    app = MinimalApp()
    
    print("Running app...")
    app.run()
    
    print("App finished successfully!")
    
except Exception as e:
    print(f"CRITICAL ERROR: {e}")
    import traceback
    traceback.print_exc()
    
print("=== MINIMAL TEST END ===")