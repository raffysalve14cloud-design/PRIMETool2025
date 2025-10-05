@echo off
echo ===============================================
echo PRIME Tool - Docker Android Build Script
echo ===============================================

REM Check if Docker is running
docker info >nul 2>&1
if errorlevel 1 (
    echo ERROR: Docker is not running!
    echo Please start Docker Desktop and try again.
    pause
    exit /b 1
)

echo Docker is running. Starting build...

REM Clean previous builds
if exist bin\ rmdir /s /q bin
if exist .buildozer\ rmdir /s /q .buildozer

echo Building APK with Docker...
docker run --rm -v "%CD%:/app" kivy/buildozer bash -c "cd /app && cp buildozer_docker.spec buildozer.spec && buildozer android debug"

if exist bin\*.apk (
    echo ===============================================
    echo SUCCESS! APK built successfully!
    echo Location: %CD%\bin\
    echo ===============================================
    dir bin\*.apk
) else (
    echo ===============================================
    echo BUILD FAILED! Check the output above for errors.
    echo ===============================================
)

pause