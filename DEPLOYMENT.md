# Deployment Guide for Observo

This guide provides instructions on how to deploy both the backend API and mobile application for Observo.

## 1. Backend Deployment

### Option 1: Deploy to Heroku

1. Create a `Procfile` in the app directory:
   ```
   web: gunicorn app:app
   ```

2. Install the Heroku CLI and login:
   ```bash
   heroku login
   ```

3. Create a new Heroku app:
   ```bash
   heroku create observo-api
   ```

4. Deploy to Heroku:
   ```bash
   git push heroku main
   ```

### Option 2: Deploy to AWS EC2

1. Launch an EC2 instance with Ubuntu
2. Install required packages:
   ```bash
   sudo apt update
   sudo apt install -y python3-pip python3-dev nginx
   ```

3. Clone your repository:
   ```bash
   git clone <your-repo-url>
   cd Proto_Observo
   ```

4. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

5. Install requirements:
   ```bash
   pip install -r app/requirements.txt
   ```

6. Set up Gunicorn service:
   ```bash
   sudo nano /etc/systemd/system/observo.service
   ```
   
   Add the following:
   ```
   [Unit]
   Description=Gunicorn instance to serve Observo
   After=network.target

   [Service]
   User=ubuntu
   Group=www-data
   WorkingDirectory=/home/ubuntu/Proto_Observo/app
   Environment="PATH=/home/ubuntu/Proto_Observo/venv/bin"
   ExecStart=/home/ubuntu/Proto_Observo/venv/bin/gunicorn --workers 3 --bind unix:observo.sock -m 007 backend:app

   [Install]
   WantedBy=multi-user.target
   ```

7. Start and enable the service:
   ```bash
   sudo systemctl start observo
   sudo systemctl enable observo
   ```

8. Configure Nginx:
   ```bash
   sudo nano /etc/nginx/sites-available/observo
   ```
   
   Add the following:
   ```
   server {
       listen 80;
       server_name your_domain_or_ip;

       location / {
           include proxy_params;
           proxy_pass http://unix:/home/ubuntu/Proto_Observo/app/observo.sock;
       }
   }
   ```

9. Enable the site and restart Nginx:
   ```bash
   sudo ln -s /etc/nginx/sites-available/observo /etc/nginx/sites-enabled
   sudo systemctl restart nginx
   ```

## 2. Mobile App Deployment

### For Android:

1. Generate a signing key:
   ```bash
   keytool -genkeypair -v -storetype PKCS12 -keystore observo-key.keystore -alias observo-alias -keyalg RSA -keysize 2048 -validity 10000
   ```

2. Create `android/app/observo.keystore.properties`:
   ```
   keyAlias=observo-alias
   keyPassword=your_key_password
   storeFile=observo-key.keystore
   storePassword=your_store_password
   ```

3. Configure app/build.gradle to use the signing config

4. Build the release APK:
   ```bash
   cd android
   ./gradlew assembleRelease
   ```

5. The APK will be in `android/app/build/outputs/apk/release/app-release.apk`

### For iOS:

1. Open the project in Xcode:
   ```bash
   open ios/ObservoMobile.xcworkspace
   ```

2. Select your development team in the Signing & Capabilities tab

3. Archive the app:
   - Select "Product" > "Archive"
   - Follow the steps in the Organizer to distribute your app

## 3. Update the Mobile App Configuration

Don't forget to update the API URL in `mobile/src/api/config.js` to point to your deployed backend:

```javascript
export const API_URL = 'https://your-deployed-backend-url.com/api';
```

## 4. Continuous Integration/Deployment

Consider setting up GitHub Actions or another CI/CD tool to automate deployments when code is pushed to the main branch.

---

## ⚠️ Important: Do NOT Commit Sensitive or Large Files

- **Model weights, logs, uploads, and raw data are excluded from version control via `.gitignore`.**
- **Never commit files in `models/weights/`, `models/logs/`, `uploads/`, or `data/raw/` to GitHub.**
- **Notebooks and environment folders are also excluded.**

---
