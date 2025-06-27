// Frontend Integration Template for VISTA_S
// ==========================================
// Use this code in your frontend to connect to the VISTA_S backend

// Configuration
const API_CONFIG = {
  baseURL: 'https://vista-s.onrender.com',
  endpoints: {
    detect: '/api/detect',
    health: '/api/health',
    images: '/api/images'
  }
};

// Main API Class
class VISTA_API {
  constructor() {
    this.baseURL = API_CONFIG.baseURL;
  }

  // Health check
  async checkHealth() {
    try {
      const response = await fetch(`${this.baseURL}/api/health`);
      return await response.json();
    } catch (error) {
      console.error('Health check failed:', error);
      throw error;
    }
  }

  // Object detection
  async detectObjects(imageFile, options = {}) {
    try {
      const formData = new FormData();
      formData.append('image', imageFile);

      const response = await fetch(`${this.baseURL}/api/detect`, {
        method: 'POST',
        body: formData,
        // Don't set Content-Type header - let browser set it with boundary
      });

      if (!response.ok) {
        throw new Error(`Detection failed: ${response.status} ${response.statusText}`);
      }

      const result = await response.json();
      return result;
    } catch (error) {
      console.error('Object detection failed:', error);
      throw error;
    }
  }

  // Get processed image URL
  getImageURL(filename) {
    return `${this.baseURL}/api/images/${filename}`;
  }
}

// React Hook Example
const useVISTAAPI = () => {
  const [api] = useState(() => new VISTA_API());
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const detectObjects = async (imageFile) => {
    setLoading(true);
    setError(null);
    
    try {
      const result = await api.detectObjects(imageFile);
      setLoading(false);
      return result;
    } catch (err) {
      setError(err.message);
      setLoading(false);
      throw err;
    }
  };

  const checkHealth = async () => {
    try {
      const result = await api.checkHealth();
      return result;
    } catch (err) {
      setError(err.message);
      throw err;
    }
  };

  return {
    detectObjects,
    checkHealth,
    getImageURL: api.getImageURL.bind(api),
    loading,
    error
  };
};

// React Component Example
const ObjectDetectionComponent = () => {
  const { detectObjects, getImageURL, loading, error } = useVISTAAPI();
  const [detections, setDetections] = useState([]);
  const [processedImageUrl, setProcessedImageUrl] = useState(null);

  const handleImageUpload = async (event) => {
    const file = event.target.files[0];
    if (!file) return;

    try {
      const result = await detectObjects(file);
      
      if (result.success) {
        setDetections(result.detections);
        if (result.image_url) {
          setProcessedImageUrl(getImageURL(result.image_url.split('/').pop()));
        }
      }
    } catch (err) {
      console.error('Detection failed:', err);
    }
  };

  return (
    <div className="vista-detection">
      <h2>VISTA_S Object Detection</h2>
      
      <input
        type="file"
        accept="image/*"
        onChange={handleImageUpload}
        disabled={loading}
      />
      
      {loading && <p>Processing image...</p>}
      {error && <p className="error">Error: {error}</p>}
      
      {processedImageUrl && (
        <div className="processed-image">
          <h3>Processed Image</h3>
          <img src={processedImageUrl} alt="Processed" />
        </div>
      )}
      
      {detections.length > 0 && (
        <div className="detections">
          <h3>Detections ({detections.length})</h3>
          {detections.map((detection, index) => (
            <div key={detection.id || index} className={`detection ${detection.risk_level}`}>
              <h4>{detection.label}</h4>
              <p>Confidence: {(detection.confidence * 100).toFixed(1)}%</p>
              <p>Risk Level: {detection.risk_level}</p>
              <p>
                Position: ({detection.bbox.x.toFixed(0)}, {detection.bbox.y.toFixed(0)})
                Size: {detection.bbox.width.toFixed(0)} × {detection.bbox.height.toFixed(0)}
              </p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

// Vue.js Example
const VueDetectionComponent = {
  data() {
    return {
      api: new VISTA_API(),
      loading: false,
      error: null,
      detections: [],
      processedImageUrl: null
    };
  },
  methods: {
    async handleImageUpload(event) {
      const file = event.target.files[0];
      if (!file) return;

      this.loading = true;
      this.error = null;

      try {
        const result = await this.api.detectObjects(file);
        
        if (result.success) {
          this.detections = result.detections;
          if (result.image_url) {
            this.processedImageUrl = this.api.getImageURL(
              result.image_url.split('/').pop()
            );
          }
        }
      } catch (err) {
        this.error = err.message;
      } finally {
        this.loading = false;
      }
    }
  },
  template: `
    <div class="vista-detection">
      <h2>VISTA_S Object Detection</h2>
      
      <input
        type="file"
        accept="image/*"
        @change="handleImageUpload"
        :disabled="loading"
      />
      
      <p v-if="loading">Processing image...</p>
      <p v-if="error" class="error">Error: {{ error }}</p>
      
      <div v-if="processedImageUrl" class="processed-image">
        <h3>Processed Image</h3>
        <img :src="processedImageUrl" alt="Processed" />
      </div>
      
      <div v-if="detections.length > 0" class="detections">
        <h3>Detections ({{ detections.length }})</h3>
        <div
          v-for="(detection, index) in detections"
          :key="detection.id || index"
          :class="['detection', detection.risk_level]"
        >
          <h4>{{ detection.label }}</h4>
          <p>Confidence: {{ (detection.confidence * 100).toFixed(1) }}%</p>
          <p>Risk Level: {{ detection.risk_level }}</p>
          <p>
            Position: ({{ detection.bbox.x.toFixed(0) }}, {{ detection.bbox.y.toFixed(0) }})
            Size: {{ detection.bbox.width.toFixed(0) }} × {{ detection.bbox.height.toFixed(0) }}
          </p>
        </div>
      </div>
    </div>
  `
};

// Vanilla JavaScript Example
const initVISTADetection = () => {
  const api = new VISTA_API();
  const fileInput = document.getElementById('image-input');
  const resultsDiv = document.getElementById('results');

  fileInput.addEventListener('change', async (event) => {
    const file = event.target.files[0];
    if (!file) return;

    resultsDiv.innerHTML = '<p>Processing image...</p>';

    try {
      const result = await api.detectObjects(file);
      
      if (result.success) {
        displayResults(result);
      }
    } catch (error) {
      resultsDiv.innerHTML = `<p class="error">Error: ${error.message}</p>`;
    }
  });

  const displayResults = (result) => {
    let html = '<h3>Detection Results</h3>';
    
    if (result.image_url) {
      html += `<img src="${api.getImageURL(result.image_url.split('/').pop())}" alt="Processed" />`;
    }
    
    if (result.detections.length > 0) {
      html += '<div class="detections">';
      result.detections.forEach(detection => {
        html += `
          <div class="detection ${detection.risk_level}">
            <h4>${detection.label}</h4>
            <p>Confidence: ${(detection.confidence * 100).toFixed(1)}%</p>
            <p>Risk Level: ${detection.risk_level}</p>
          </div>
        `;
      });
      html += '</div>';
    } else {
      html += '<p>No objects detected</p>';
    }
    
    resultsDiv.innerHTML = html;
  };
};

// CSS Styles (add to your stylesheet)
const CSS_STYLES = `
.vista-detection {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.processed-image img {
  max-width: 100%;
  height: auto;
  border: 2px solid #ddd;
  border-radius: 8px;
}

.detections {
  margin-top: 20px;
}

.detection {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 15px;
  margin-bottom: 10px;
  background: #f9f9f9;
}

.detection.high {
  border-color: #e74c3c;
  background: #fdf2f2;
}

.detection.medium {
  border-color: #f39c12;
  background: #fef9e7;
}

.detection.low {
  border-color: #27ae60;
  background: #f0f8f0;
}

.error {
  color: #e74c3c;
  font-weight: bold;
}
`;

// Export for use in your frontend
export { VISTA_API, useVISTAAPI, ObjectDetectionComponent, VueDetectionComponent, initVISTADetection, CSS_STYLES };
