# VISTA_S Frontend Deployment Guide

## Current Status ✅
- **Backend**: Deployed on Render at https://vista-s.onrender.com/
- **Frontend**: Need to deploy (built by your friend)

## Available Backend API Endpoints

Your Flask backend provides these endpoints:

### 🔍 Object Detection API
- **POST** `/api/detect` - Upload image for object detection
- **GET** `/api/health` - Health check endpoint
- **GET** `/api/images/<filename>` - Get processed images
- **GET** `/uploads/<filename>` - Get uploaded files

### 📊 API Response Format
```json
{
  "success": true,
  "detections": [
    {
      "id": "0",
      "label": "FireExtinguisher",
      "confidence": 0.85,
      "bbox": {"x": 100, "y": 50, "width": 200, "height": 300},
      "risk_level": "low"
    }
  ],
  "image_url": "/api/images/processed_image.jpg"
}
```

## Frontend Deployment Steps

### Option 1: Deploy on Vercel (Recommended)

1. **Get Frontend Code**
   - Get access to your friend's GitHub repo
   - Fork or clone the repository

2. **Update API Configuration**
   - Update frontend to use your backend URL: `https://vista-s.onrender.com`
   - Configure CORS if needed

3. **Deploy on Vercel**
   ```bash
   # Install Vercel CLI
   npm install -g vercel
   
   # Login to Vercel
   vercel login
   
   # Deploy
   vercel --prod
   ```

4. **Set Environment Variables**
   - `REACT_APP_API_URL=https://vista-s.onrender.com`
   - Or `NEXT_PUBLIC_API_URL=https://vista-s.onrender.com` (for Next.js)

### Option 2: Deploy on Netlify

1. **Connect GitHub Repository**
   - Login to Netlify
   - Connect your friend's GitHub repo
   - Set build command and publish directory

2. **Environment Variables**
   - Add `REACT_APP_API_URL=https://vista-s.onrender.com`

## Frontend Integration Code Examples

### React Integration Example
```javascript
const API_BASE_URL = process.env.REACT_APP_API_URL || 'https://vista-s.onrender.com';

const detectObjects = async (imageFile) => {
  const formData = new FormData();
  formData.append('image', imageFile);
  
  try {
    const response = await fetch(`${API_BASE_URL}/api/detect`, {
      method: 'POST',
      body: formData,
    });
    
    const result = await response.json();
    return result;
  } catch (error) {
    console.error('Detection error:', error);
    throw error;
  }
};
```

### Vue.js Integration Example
```javascript
const API_BASE_URL = process.env.VUE_APP_API_URL || 'https://vista-s.onrender.com';

export const detectObjects = async (imageFile) => {
  const formData = new FormData();
  formData.append('image', imageFile);
  
  const response = await axios.post(`${API_BASE_URL}/api/detect`, formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
  
  return response.data;
};
```

## CORS Configuration (If Needed)

If you encounter CORS issues, update your Flask backend:

```python
# In backend.py
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=['https://your-frontend-domain.vercel.app'])
```

## Testing Integration

### 1. Test Backend API
```bash
# Test health endpoint
curl https://vista-s.onrender.com/api/health

# Test image detection
curl -X POST -F "image=@test_image.jpg" https://vista-s.onrender.com/api/detect
```

### 2. Test Frontend Integration
- Upload an image through frontend
- Verify API calls to backend
- Check detection results display

## Security Considerations

1. **API Rate Limiting** (if needed)
2. **File Upload Limits** (already configured)
3. **CORS Configuration** (restrict to your frontend domain)
4. **HTTPS Only** (both services support HTTPS)

## Monitoring and Analytics

1. **Backend Monitoring**: Render provides logs and metrics
2. **Frontend Analytics**: Vercel provides analytics
3. **Error Tracking**: Consider adding Sentry or similar

## Domain Configuration (Optional)

1. **Custom Domain for Frontend**: Configure in Vercel/Netlify
2. **Custom Domain for Backend**: Configure in Render
3. **SSL Certificates**: Automatically provided by both platforms

## Performance Optimization

1. **Image Optimization**: Compress images before upload
2. **Caching**: Implement appropriate caching strategies
3. **CDN**: Use built-in CDNs from Vercel/Netlify

## Troubleshooting Common Issues

1. **CORS Errors**: Update CORS configuration in Flask
2. **API Not Found**: Check API endpoint URLs
3. **Image Upload Fails**: Check file size limits and formats
4. **Slow Detection**: Consider model optimization

## Next Steps Summary

1. ✅ Backend deployed on Render
2. 🔄 Get frontend code from your friend
3. 🔄 Deploy frontend on Vercel/Netlify
4. 🔄 Update frontend API configuration
5. 🔄 Test full integration
6. 🔄 Configure custom domains (optional)
7. 🔄 Add monitoring and analytics
