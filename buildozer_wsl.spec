[app]
title = OPPO Test
package.name = oppotest
package.domain = com.test

source.dir = .
source.include_exts = py

version = 0.1
requirements = python3, kivy==2.1.0

[buildozer]
log_level = 2

[android]
# OPPO CPH1937 optimized settings
android.api = 30
android.minapi = 21
android.sdk = 30
android.ndk = 21b

# Single architecture for OPPO ARM64
android.archs = arm64-v8a

# OPPO-compatible bootstrap
android.bootstrap = sdl2

# Minimal permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE

# OPPO security compatibility
android.allow_backup = False
android.skip_update = False

# Graphics compatibility for OPPO
android.add_src = 

# Release optimization for OPPO
android.release_artifact = aab
android.debug = 0

# OPPO-specific gradle settings
android.gradle_dependencies = 

# Target newer OpenGL for OPPO devices
android.ndk_api = 21

[app:android.gradle_dependencies]

[app:android.gradle_repositories]

[app:android.add_src]

[app:android.add_libs_armeabi]

[app:android.add_libs_armeabi_v7a]

[app:android.add_libs_arm64_v8a]

[app:android.add_libs_x86]

[app:android.add_libs_mips]

[app:android.gradle_dependencies]

[app:android.java_options]

[app:android.aab_sign_key]

[app:android.loglevel]