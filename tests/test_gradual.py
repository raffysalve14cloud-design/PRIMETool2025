import os
print("Starting gradual test...")

# Add Android-specific OpenGL backend
if hasattr(os, 'environ'):
    platform = "Windows" if os.name == 'nt' else "Linux"
    try:
        from android.storage import primary_external_storage_path
        from android.permissions import request_permission, Permission
        platform = "Android"
        print(f"Platform: {platform}")
        
        # Try to set stable OpenGL backend for Android
        os.environ['KIVY_GL_BACKEND'] = 'gl'
        print("Set OpenGL backend to 'gl'")
    except ImportError:
        print(f"Platform: {platform}")
        print("Not Android - skipping Android-specific setup")

# Test 1: Basic imports
try:
    print("Testing imports...")
    from kivymd.app import MDApp
    from kivymd.uix.screen import MDScreen
    from kivymd.uix.label import MDLabel
    from kivymd.uix.boxlayout import MDBoxLayout
    print("✓ Basic KivyMD imports successful")
except Exception as e:
    print(f"✗ Import failed: {e}")
    exit(1)

# Test 2: Database imports
try:
    import sqlite3
    print("✓ SQLite import successful")
except Exception as e:
    print(f"✗ SQLite import failed: {e}")

# Test 3: Excel imports  
try:
    import openpyxl
    print("✓ OpenPyXL import successful")
except Exception as e:
    print(f"✗ OpenPyXL import failed: {e}")

class GradualTestApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("App __init__ called")
        
    def build(self):
        print("App build() called")
        
        try:
            # Create simple layout
            layout = MDBoxLayout(orientation='vertical', padding=20, spacing=10)
            
            # Add labels to test different aspects
            layout.add_widget(MDLabel(
                text="PRIME Tool - Gradual Test",
                theme_text_color="Primary",
                halign="center"
            ))
            
            layout.add_widget(MDLabel(
                text=f"Platform: {platform}",
                theme_text_color="Secondary",
                halign="center"
            ))
            
            if platform == "Android":
                try:
                    storage_path = primary_external_storage_path()
                    layout.add_widget(MDLabel(
                        text=f"Storage: {storage_path}",
                        theme_text_color="Secondary",
                        halign="center"
                    ))
                except Exception as e:
                    layout.add_widget(MDLabel(
                        text=f"Storage error: {e}",
                        theme_text_color="Error",
                        halign="center"
                    ))
            
            # Test database creation
            try:
                print("Testing database...")
                db_path = "test_db.db" if platform != "Android" else f"{storage_path}/test_db.db"
                conn = sqlite3.connect(db_path)
                conn.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT)")
                conn.close()
                layout.add_widget(MDLabel(
                    text="✓ Database test passed",
                    theme_text_color="Primary",
                    halign="center"
                ))
                print("✓ Database creation successful")
            except Exception as e:
                layout.add_widget(MDLabel(
                    text=f"✗ Database error: {str(e)[:50]}...",
                    theme_text_color="Error",
                    halign="center"
                ))
                print(f"✗ Database error: {e}")
            
            layout.add_widget(MDLabel(
                text="App running successfully!",
                theme_text_color="Primary", 
                halign="center"
            ))
            
            layout.add_widget(MDLabel(
                text="Tap anywhere to continue testing...",
                theme_text_color="Hint",
                halign="center"
            ))
            
            screen = MDScreen()
            screen.add_widget(layout)
            
            print("✓ UI creation successful")
            return screen
            
        except Exception as e:
            print(f"✗ Build error: {e}")
            # Create emergency fallback
            emergency_layout = MDBoxLayout(orientation='vertical')
            emergency_layout.add_widget(MDLabel(
                text=f"Build Error: {str(e)[:100]}",
                theme_text_color="Error"
            ))
            emergency_screen = MDScreen()
            emergency_screen.add_widget(emergency_layout)
            return emergency_screen
            
    def on_start(self):
        print("App on_start() called")
        print("App started successfully - waiting for interaction...")

if __name__ == '__main__':
    print("Creating app instance...")
    try:
        app = GradualTestApp()
        print("Running app...")
        app.run()
    except Exception as e:
        print(f"✗ App run error: {e}")
        import traceback
        traceback.print_exc()