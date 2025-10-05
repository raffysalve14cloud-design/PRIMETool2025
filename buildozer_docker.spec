[app]
# (str) Title of your application
title = PRIME Test

# (str) Package name
package.name = primetest

# (str) Package domain
package.domain = org.pagibig.primetest

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (only essential files)
source.include_exts = py
source.exclude_exts = spec
source.exclude_dirs = tests,test*
source.exclude_patterns = test_*,*test*

# (str) Application versioning
version = 0.1

# (list) Application requirements - minimal for testing
requirements = python3,kivy==2.1.0

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

[android]
# (int) Target Android API
android.api = 30

# (int) Minimum API
android.minapi = 21

# (int) Android SDK version
android.sdk = 30

# (str) Android NDK version
android.ndk = 21b

# (list) Android application architectures
android.archs = arm64-v8a

# (str) Bootstrap to use for android builds
android.bootstrap = sdl2

# (bool) Enable debug mode
android.debug = 1

# (list) Android permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE