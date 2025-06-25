// React Native initialization script

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

console.log('Initializing React Native project...');

// Check if we're in the mobile directory
if (!fs.existsSync(path.join(process.cwd(), 'package.json'))) {
  console.error('Please run this script from the mobile directory');
  process.exit(1);
}

try {
  // Install dependencies
  console.log('Installing dependencies...');
  execSync('npm install', { stdio: 'inherit' });

  // Initialize React Native project files
  console.log('Setting up React Native project files...');
  
  // Create metro.config.js if it doesn't exist
  if (!fs.existsSync(path.join(process.cwd(), 'metro.config.js'))) {
    fs.writeFileSync(
      path.join(process.cwd(), 'metro.config.js'),
      `/**
 * Metro configuration for React Native
 * https://github.com/facebook/react-native
 *
 * @format
 */

module.exports = {
  transformer: {
    getTransformOptions: async () => ({
      transform: {
        experimentalImportSupport: false,
        inlineRequires: true,
      },
    }),
  },
};`
    );
    console.log('Created metro.config.js');
  }

  // Create babel.config.js if it doesn't exist
  if (!fs.existsSync(path.join(process.cwd(), 'babel.config.js'))) {
    fs.writeFileSync(
      path.join(process.cwd(), 'babel.config.js'),
      `module.exports = {
  presets: ['module:metro-react-native-babel-preset'],
  plugins: [
    'react-native-reanimated/plugin',
  ],
};`
    );
    console.log('Created babel.config.js');
  }

  console.log('\nProject setup complete!');
  console.log('\nNext steps:');
  console.log('1. Start the Metro bundler: npx react-native start');
  console.log('2. Run the app: npx react-native run-android (or run-ios on Mac)');
  console.log('3. Update the API URL in src/api/config.js to point to your backend server');

} catch (error) {
  console.error('Error during initialization:', error);
}
