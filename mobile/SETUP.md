# React Native Mobile App Setup Guide

This guide will help you set up and run the React Native mobile app for Observo object detection.

## Prerequisites

Make sure you have the following installed:

1. Node.js (v14 or newer)
2. JDK (Java Development Kit, version 11 or newer)
3. Android Studio (for Android development)
4. Xcode (for iOS development, Mac only)
5. CocoaPods (for iOS dependencies, Mac only)

## Setup Steps

### 1. Install React Native CLI globally

```bash
npm install -g react-native-cli
```

### 2. Install project dependencies

```bash
cd mobile
npm install
```

### 3. Set up Android development environment

- Install Android Studio
- Install Android SDK
- Configure ANDROID_HOME environment variable
- Create an Android Virtual Device (AVD) for testing

### 4. Set up iOS development environment (Mac only)

```bash
cd ios
pod install
cd ..
```

## Running the Application

### Start Metro Bundler

```bash
npx react-native start
```

### Run on Android

Make sure you have an Android emulator running or a device connected:

```bash
npx react-native run-android
```

### Run on iOS (Mac only)

```bash
npx react-native run-ios
```

## Troubleshooting

### Metro Bundler Issues

If you encounter issues with Metro Bundler, try:

```bash
# Clear cache
npx react-native start --reset-cache

# or if that doesn't work
rm -rf node_modules
npm install
```

### Android Build Issues

If you encounter build issues with Android:

```bash
cd android
./gradlew clean
cd ..
npx react-native run-android
```

### iOS Build Issues (Mac only)

```bash
cd ios
pod deintegrate
pod install
cd ..
npx react-native run-ios
```

## Configuring the API URL

Before running the app, make sure to update the API URL in `src/api/config.js` to point to your backend server:

```javascript
// For development on emulator/simulator
export const API_URL = 'http://10.0.2.2:5000/api'; // For Android emulator
// export const API_URL = 'http://localhost:5000/api'; // For iOS simulator

// For production
// export const API_URL = 'https://your-production-server.com/api';
```

## Initializing a New React Native Project from Scratch

If you prefer to create a new React Native project from scratch instead of using the provided structure:

```bash
npx react-native init ObservoMobile
cd ObservoMobile
npm install --save axios react-native-camera react-native-image-picker react-native-vector-icons @react-navigation/native @react-navigation/native-stack react-native-screens react-native-safe-area-context
```

Then copy the source files from the `mobile/src` directory to your new project.
