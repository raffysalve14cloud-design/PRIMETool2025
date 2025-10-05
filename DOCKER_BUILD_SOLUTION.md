# PRIME Tool - Docker Build Solution

Since buildozer has persistent issues on your Windows/WSL setup, here's a Docker approach that guarantees a working build environment:

## Step 1: Install Docker Desktop
Download and install Docker Desktop for Windows from https://www.docker.com/products/docker-desktop/

## Step 2: Use Kivy's Official Buildozer Docker Image

Open PowerShell in your project directory and run:

```powershell
# Pull the official buildozer Docker image
docker pull kivy/buildozer

# Build your APK using Docker
docker run --rm -v "${PWD}:/app" kivy/buildozer bash -c "cd /app && buildozer android debug"
```

## Step 3: Alternative - Use Docker with Custom Environment

Create a Dockerfile for more control:

```dockerfile
FROM ubuntu:22.04

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3.10 python3.10-venv python3.10-dev python3-pip \
    git zip unzip openjdk-11-jdk autoconf libtool pkg-config \
    zlib1g-dev libncurses5-dev libncursesw5-dev cmake \
    libffi-dev libssl-dev && \
    rm -rf /var/lib/apt/lists/*

# Install buildozer
RUN pip3 install buildozer cython==0.29.33

WORKDIR /app
CMD ["buildozer", "android", "debug"]
```

Then build and run:
```powershell
# Build the Docker image
docker build -t prime-builder .

# Run the build
docker run --rm -v "${PWD}:/app" prime-builder
```

## Step 3: Manual Alternative - Use Python-for-Android Directly

If Docker is not an option, you can bypass buildozer entirely:

```bash
# Install python-for-android directly
pip install python-for-android

# Build APK manually
p4a apk --private . --package=org.pagibig.primetool --name="PRIME Tool Test" --version=0.1 --bootstrap=sdl2 --requirements=python3,kivy==2.1.0
```

## Step 4: Use Online Build Services

### Replit (Free Option)
1. Go to https://replit.com
2. Create a new Python repl
3. Upload your project files
4. Install buildozer in the repl
5. Build your APK in the cloud environment

### GitHub Codespaces (If Available)
1. Open your repository in GitHub Codespaces
2. Use the Linux environment to build with buildozer
3. Download the generated APK

## Recommendation

**Try Docker first** - it's the most reliable solution that will work regardless of your local environment issues.

The command would be:
```powershell
docker run --rm -v "${PWD}:/app" kivy/buildozer bash -c "cd /app && buildozer android debug"
```

This eliminates all the Python version, WSL, and buildozer configuration issues we've been encountering.