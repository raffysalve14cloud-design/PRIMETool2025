[app]
# (str) Title of your application
title = PRIME Test

# (str) Package name
package.name = primetest

# (str) Package domain
package.domain = org.pagibig.primetest

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec
source.exclude_dirs = tests,.buildozer,bin,prime_env

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy==2.1.0

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

[android]
# (int) Target Android API, should be as high as possible.
android.api = 30

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 30

# (str) Android NDK version to use
android.ndk = 21b

# (list) Android application architectures to build for
android.archs = arm64-v8a

# (str) Bootstrap to use for android builds
android.bootstrap = sdl2

# (bool) Whether the build should use debug or release mode
android.debug = 1

# (list) List of permissions the android app needs
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE