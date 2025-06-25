import axios from 'axios';
import { API_URL } from './config';

// Create axios instance with base URL
const apiClient = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'multipart/form-data',
    'Accept': 'application/json',
  },
  timeout: 30000, // 30 seconds timeout
});

// Upload image and get detection results
export const detectObjects = async (imageUri) => {
  try {
    // Create form data for image upload
    const formData = new FormData();
    formData.append('image', {
      uri: imageUri,
      type: 'image/jpeg',
      name: 'upload.jpg',
    });

    // Make the API call
    const response = await apiClient.post('/detect', formData);
    return response.data;
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
};

// Check API health
export const checkHealth = async () => {
  try {
    const response = await apiClient.get('/health');
    return response.data;
  } catch (error) {
    console.error('Health check failed:', error);
    throw error;
  }
};
