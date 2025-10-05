[app]

# (str) Title of your application
title = PRIME Tool

# (str) Package name
package.name = primetool

# (str) Package domain (needed for android/ios packaging)
package.domain = org.pagibig.primetool

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,db,xlsx,xls

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,data/*,exports/*,*.db

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements  
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.1.0,kivymd==1.1.1,pillow,plyer,android,pyjnius,sqlite3,openpyxl,et_xmlfile,jdcal

# (str) Presplash of the application
presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (landscape, sensorLandscape, portrait, all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# Debug mode settings
[buildozer:debug]
debug = 1

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

[android]

# (str) Android NDK version to use
android.ndk = 23b

# (str) Android SDK version to use
android.sdk = 33

# (str) Android API to use (auto = automatically detect, otherwise specify manually)
android.api = 31

# (str) Android minimum API to support
android.minapi = 21

# (str) Bootstrap to use for android builds
android.bootstrap = sdl2

# (str) Python bootstrap to use
p4a.bootstrap = sdl2

# (list) Gradle dependencies to add
android.gradle_dependencies = 

# (bool) Enable AndroidX support. Enable when 'android.gradle_dependencies'
android.enable_androidx = True

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = org.kivy.android.PythonActivity

# (list) Pattern to whitelist for the whole project
android.whitelist = 

# (str) Path to a custom whitelist file
# android.whitelist_src = 

# (str) Path to a custom blacklist file
# android.blacklist_src = 

# (list) Android application meta-data to set (key=value format)
android.meta_data = 

# (list) Android permissions
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,INTERNET,ACCESS_NETWORK_STATE,MANAGE_EXTERNAL_STORAGE

# (list) Android library project to add (will be added in the
# project.properties automatically.)
android.library_references = 

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D PythonActivity:D MainApp:D

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

# (bool) Add python activity in the main thread
android.add_python_to_android = True

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = False

# (bool) Enable hardware acceleration
android.hardwareAccelerated = True

# (bool) Use SDL2 for graphics (more stable)
android.use_sdl2 = True

# (str) OpenGL ES version to use
android.opengl_es2 = True

# (str) XML file for custom backup rules (see official auto backup documentation)
# android.backup_rules =

[buildozer:virtualenv]
# virtualenv used to run buildozer
# python = python3.8

# Python-for-Android specific settings
[app:p4a]
# (str) python-for-android fork to use, defaults to upstream (kivy)
p4a.fork = kivy

# (str) python-for-android branch to use, defaults to master
p4a.branch = master

# (str) Force the use of a specific revision
# p4a.rev = 

# (str) python-for-android git clone directory (if empty, it will be automatically cloned from github)
# p4a.source_dir =

# (str) The directory in which python-for-android should look for your own build recipes (if any)
# p4a.local_recipes =

# (str) Filename to the hook for p4a
# p4a.hook =

# PRIME Tool specific configurations