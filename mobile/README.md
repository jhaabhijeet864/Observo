# React Native Mobile App for Observo

This directory contains the React Native mobile application for Observo Object Detection.

## Features

- Cross-platform (iOS and Android)
- Camera integration for capturing images
- Real-time object detection
- Display of detection results with bounding boxes and confidence scores
- Risk level visualization

## Setup Instructions

1. Install React Native CLI:
   ```bash
   npm install -g react-native-cli
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the app on Android:
   ```bash
   npx react-native run-android
   ```

4. Run the app on iOS:
   ```bash
   npx react-native run-ios
   ```

## Project Structure

- `/src` - Source code
  - `/components` - Reusable UI components
  - `/screens` - App screens
  - `/api` - API integration
  - `/utils` - Utility functions
  - `/assets` - Images and other assets

## Backend Configuration

Update the `API_URL` in `src/api/config.js` to point to your deployed backend server.

## Deployment

1. For Android:
   ```bash
   cd android && ./gradlew assembleRelease
   ```

2. For iOS, use Xcode to archive and distribute the app.
