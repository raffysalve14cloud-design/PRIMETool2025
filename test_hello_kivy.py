#!/usr/bin/env python3
"""
Basic Hello World Kivy app - simplest possible UI
"""

print("Starting basic Kivy test...")

try:
    from kivy.app import App
    from kivy.uix.label import Label
    
    print("Kivy imports successful")
    
    class HelloApp(App):
        def build(self):
            print("Building app...")
            return Label(text='Hello World!\nKivy Works!')
    
    print("Running app...")
    HelloApp().run()
    
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()