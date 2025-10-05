#!/usr/bin/env python3
# Pure Python test - NO UI libraries
print("=== PURE PYTHON TEST START ===")

try:
    import sys
    print(f"Python version: {sys.version}")
    
    import os
    print(f"OS name: {os.name}")
    print(f"Working directory: {os.getcwd()}")
    
    # Test platform detection
    is_android = False
    try:
        from android.storage import primary_external_storage_path
        from android.permissions import request_permission, Permission
        is_android = True
        storage = primary_external_storage_path()
        print(f"Platform: Android")
        print(f"Storage path: {storage}")
        
        # Test storage permissions
        try:
            request_permission(Permission.WRITE_EXTERNAL_STORAGE)
            print("✓ Storage permission requested")
        except Exception as e:
            print(f"Permission warning: {e}")
            
    except ImportError:
        print("Platform: Desktop/PC")
        storage = os.getcwd()
    
    # Test SQLite
    print("\nTesting SQLite...")
    import sqlite3
    print("✓ SQLite imported")
    
    test_db = os.path.join(storage, "pure_test.db")
    conn = sqlite3.connect(test_db)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER, name TEXT)")
    cursor.execute("INSERT INTO test VALUES (1, 'Test Data')")
    conn.commit()
    
    cursor.execute("SELECT * FROM test")
    result = cursor.fetchall()
    print(f"✓ Database test: {result}")
    conn.close()
    
    # Test file operations
    print("\nTesting file operations...")
    test_file = os.path.join(storage, "pure_test.txt")
    with open(test_file, 'w') as f:
        f.write("Pure Python test file")
    print(f"✓ File written to: {test_file}")
    
    with open(test_file, 'r') as f:
        content = f.read()
    print(f"✓ File read: {content}")
    
    # Test imports that should be available
    print("\nTesting standard library imports...")
    
    import json
    test_dict = {"test": "data", "number": 123}
    json_str = json.dumps(test_dict)
    print(f"✓ JSON: {json_str}")
    
    from datetime import datetime
    now = datetime.now()
    print(f"✓ DateTime: {now}")
    
    import math
    print(f"✓ Math: sqrt(16) = {math.sqrt(16)}")
    
    # Test if openpyxl works
    try:
        import openpyxl
        print("✓ OpenPyXL imported successfully")
        
        wb = openpyxl.Workbook()
        ws = wb.active
        ws['A1'] = 'Pure Python Excel Test'
        excel_file = os.path.join(storage, "pure_test.xlsx")
        wb.save(excel_file)
        print(f"✓ Excel file created: {excel_file}")
        
    except Exception as e:
        print(f"✗ OpenPyXL error: {e}")
    
    print("\n" + "="*50)
    print("PURE PYTHON TEST COMPLETED SUCCESSFULLY!")
    print("All basic Python functionality works.")
    print("The crash is likely in Kivy/UI components.")
    print("="*50)
    
except Exception as e:
    print(f"CRITICAL PYTHON ERROR: {e}")
    import traceback
    traceback.print_exc()
    
print("=== PURE PYTHON TEST END ===")