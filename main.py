"""
OPPO Device Test - Ultra Minimal
This is the absolute simplest test for OPPO devices
"""

import sys
import os

def main():
    print("=== OPPO DEVICE TEST ===")
    print(f"Python version: {sys.version}")
    print(f"Platform: {sys.platform}")
    
    # Test basic file operations
    try:
        test_file = "/storage/emulated/0/oppo_test.txt"
        with open(test_file, 'w') as f:
            f.write("OPPO test successful")
        print(f"File write test: SUCCESS")
        
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)
            print(f"File cleanup: SUCCESS")
            
    except Exception as e:
        print(f"File test failed: {e}")
    
    print("=== TEST COMPLETE ===")
    print("App will exit in 5 seconds...")
    
    # Keep app alive for 5 seconds so you can see output
    import time
    time.sleep(5)
    
    print("Exiting now...")
    sys.exit(0)

if __name__ == "__main__":
    main()