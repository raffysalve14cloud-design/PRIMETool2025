import os
print("Starting UI component test...")

# Android graphics setup
try:
    os.environ['KIVY_GL_BACKEND'] = 'gl'
    os.environ['KIVY_WINDOW'] = 'sdl2'
    print("Graphics backend configured")
except:
    pass

# Platform detection
platform = "Unknown"
try:
    from android.storage import primary_external_storage_path
    platform = "Android"
    storage_path = primary_external_storage_path()
except ImportError:
    platform = "Windows" if os.name == 'nt' else "Linux"
    storage_path = os.getcwd()

print(f"Platform: {platform}")

# Import Kivy components one by one
try:
    print("Testing Kivy imports...")
    from kivymd.app import MDApp
    print("✓ MDApp imported")
    
    from kivymd.uix.screen import MDScreen
    print("✓ MDScreen imported")
    
    from kivymd.uix.label import MDLabel
    print("✓ MDLabel imported")
    
    from kivymd.uix.boxlayout import MDBoxLayout
    print("✓ MDBoxLayout imported")
    
    from kivymd.uix.button import MDRaisedButton, MDIconButton
    print("✓ Button widgets imported")
    
    from kivymd.uix.textfield import MDTextField
    print("✓ MDTextField imported")
    
    from kivymd.uix.card import MDCard
    print("✓ MDCard imported")
    
    from kivymd.uix.list import MDList, OneLineListItem
    print("✓ List widgets imported")
    
    from kivymd.uix.selectioncontrol import MDCheckbox
    print("✓ MDCheckbox imported")
    
    from kivy.uix.screenmanager import ScreenManager
    print("✓ ScreenManager imported")
    
    from kivy.lang import Builder
    print("✓ Builder imported")
    
except Exception as e:
    print(f"✗ Import failed: {e}")
    exit(1)

# Test KV string (simpler version of your main app)
kv_string = '''
<TestScreen>:
    name: 'test'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(10)
        
        MDLabel:
            text: "UI Component Test"
            theme_text_color: "Primary"
            halign: "center"
            size_hint_y: None
            height: dp(60)
            
        MDCard:
            orientation: "vertical"
            padding: dp(10)
            size_hint_y: None
            height: dp(200)
            elevation: 2
            
            MDLabel:
                text: "Test Card Component"
                theme_text_color: "Primary"
                halign: "center"
                
            MDTextField:
                id: test_field
                hint_text: "Test input field"
                helper_text: "Type something here"
                
            MDRaisedButton:
                text: "Test Button"
                size_hint_x: None
                width: dp(120)
                pos_hint: {"center_x": 0.5}
                on_release: app.test_button_click()
                
        MDLabel:
            text: "If you see this, UI components work!"
            theme_text_color: "Secondary"
            halign: "center"
'''

class TestScreen(MDScreen):
    pass

class UIComponentTestApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("App initialized")
        
    def build(self):
        print("Building app...")
        
        try:
            # Load KV string
            Builder.load_string(kv_string)
            print("✓ KV string loaded")
            
            # Create screen manager
            sm = ScreenManager()
            print("✓ ScreenManager created")
            
            # Create test screen
            test_screen = TestScreen()
            sm.add_widget(test_screen)
            print("✓ Test screen added")
            
            return sm
            
        except Exception as e:
            print(f"✗ Build error: {e}")
            import traceback
            traceback.print_exc()
            
            # Create minimal fallback
            layout = MDBoxLayout(orientation='vertical')
            layout.add_widget(MDLabel(text=f"Build Error: {str(e)[:100]}"))
            
            screen = MDScreen()
            screen.add_widget(layout)
            return screen
    
    def on_start(self):
        print("App started successfully!")
        
    def test_button_click(self):
        print("Test button clicked - UI interaction working!")

if __name__ == '__main__':
    print("Starting UI component test app...")
    try:
        app = UIComponentTestApp()
        app.run()
    except Exception as e:
        print(f"✗ App run error: {e}")
        import traceback
        traceback.print_exc()