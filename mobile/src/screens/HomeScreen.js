import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  Image,
  ScrollView,
  ActivityIndicator,
  SafeAreaView,
  StatusBar,
  Alert,
  Dimensions,
} from 'react-native';
import { launchCamera, launchImageLibrary } from 'react-native-image-picker';
import Icon from 'react-native-vector-icons/MaterialCommunityIcons';
import { detectObjects, checkHealth } from '../api/detectApi';

const { width } = Dimensions.get('window');

const HomeScreen = ({ navigation }) => {
  const [image, setImage] = useState(null);
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState(null);
  const [serverStatus, setServerStatus] = useState('checking');

  // Check server health on component mount
  useEffect(() => {
    const checkServerHealth = async () => {
      try {
        const health = await checkHealth();
        setServerStatus(health.status === 'healthy' ? 'online' : 'offline');
      } catch (error) {
        setServerStatus('offline');
      }
    };
    
    checkServerHealth();
  }, []);

  // Function to take photo using camera
  const takePhoto = async () => {
    const options = {
      mediaType: 'photo',
      quality: 0.8,
      maxWidth: 1280,
      maxHeight: 1280,
    };

    try {
      const result = await launchCamera(options);
      if (result.assets && result.assets[0]) {
        setImage(result.assets[0].uri);
        setResults(null); // Clear previous results
      }
    } catch (error) {
      console.error('Camera error:', error);
      Alert.alert('Error', 'Failed to open camera');
    }
  };

  // Function to pick image from gallery
  const pickImage = async () => {
    const options = {
      mediaType: 'photo',
      quality: 0.8,
      maxWidth: 1280,
      maxHeight: 1280,
    };

    try {
      const result = await launchImageLibrary(options);
      if (result.assets && result.assets[0]) {
        setImage(result.assets[0].uri);
        setResults(null); // Clear previous results
      }
    } catch (error) {
      console.error('Gallery error:', error);
      Alert.alert('Error', 'Failed to open gallery');
    }
  };

  // Function to detect objects in the image
  const detectImage = async () => {
    if (!image) {
      Alert.alert('Error', 'Please select an image first');
      return;
    }

    setLoading(true);
    try {
      const response = await detectObjects(image);
      setResults(response);
    } catch (error) {
      console.error('Detection error:', error);
      Alert.alert('Error', 'Failed to process image. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  // Get color based on risk level
  const getRiskColor = (risk) => {
    switch (risk) {
      case 'high': return '#ff4d4d';
      case 'medium': return '#ffbb33';
      default: return '#33cc33';
    }
  };

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="light-content" />
      
      {/* Header */}
      <View style={styles.header}>
        <Text style={styles.title}>Observo</Text>
        <View style={[
          styles.statusIndicator, 
          { backgroundColor: serverStatus === 'online' ? '#33cc33' : 
                            serverStatus === 'checking' ? '#ffbb33' : '#ff4d4d' }
        ]} />
      </View>

      <ScrollView contentContainerStyle={styles.scrollContainer}>
        {/* Image Preview */}
        <View style={styles.imageContainer}>
          {image ? (
            <Image source={{ uri: image }} style={styles.image} resizeMode="contain" />
          ) : (
            <View style={styles.placeholder}>
              <Icon name="image-outline" size={80} color="#666" />
              <Text style={styles.placeholderText}>No image selected</Text>
            </View>
          )}
          
          {/* Overlay detection boxes on the image */}
          {results && results.detections && results.detections.length > 0 && (
            <View style={StyleSheet.absoluteFill}>
              {results.detections.map((item) => (
                <View
                  key={item.id}
                  style={[
                    styles.detectionBox,
                    {
                      left: (item.bbox.x / 640) * width,
                      top: (item.bbox.y / 640) * width,
                      width: (item.bbox.width / 640) * width,
                      height: (item.bbox.height / 640) * width,
                      borderColor: getRiskColor(item.risk_level),
                    },
                  ]}
                >
                  <Text style={[styles.detectionLabel, { backgroundColor: getRiskColor(item.risk_level) }]}>
                    {item.label} ({Math.round(item.confidence * 100)}%)
                  </Text>
                </View>
              ))}
            </View>
          )}
        </View>

        {/* Action Buttons */}
        <View style={styles.actionButtons}>
          <TouchableOpacity style={styles.button} onPress={takePhoto}>
            <Icon name="camera" size={24} color="#fff" />
            <Text style={styles.buttonText}>Camera</Text>
          </TouchableOpacity>
          
          <TouchableOpacity style={styles.button} onPress={pickImage}>
            <Icon name="image" size={24} color="#fff" />
            <Text style={styles.buttonText}>Gallery</Text>
          </TouchableOpacity>
          
          <TouchableOpacity 
            style={[styles.button, { opacity: image ? 1 : 0.5 }]} 
            onPress={detectImage}
            disabled={!image || loading}
          >
            <Icon name="magnify" size={24} color="#fff" />
            <Text style={styles.buttonText}>Detect</Text>
          </TouchableOpacity>
        </View>

        {/* Loading Indicator */}
        {loading && (
          <View style={styles.loadingContainer}>
            <ActivityIndicator size="large" color="#4C8FFB" />
            <Text style={styles.loadingText}>Processing image...</Text>
          </View>
        )}

        {/* Results */}
        {results && results.detections && (
          <View style={styles.resultsContainer}>
            <Text style={styles.resultsTitle}>
              Detection Results ({results.detections.length})
            </Text>
            
            {results.detections.length === 0 ? (
              <Text style={styles.noResultsText}>No objects detected</Text>
            ) : (
              results.detections.map((item) => (
                <View 
                  key={item.id} 
                  style={[
                    styles.resultItem, 
                    { borderLeftColor: getRiskColor(item.risk_level) }
                  ]}
                >
                  <View style={styles.resultHeader}>
                    <Text style={styles.resultLabel}>{item.label}</Text>
                    <Text style={styles.resultConfidence}>
                      {Math.round(item.confidence * 100)}%
                    </Text>
                  </View>
                  
                  <View style={styles.resultDetails}>
                    <Text style={styles.resultRisk}>
                      Risk Level: <Text style={{ color: getRiskColor(item.risk_level) }}>
                        {item.risk_level.toUpperCase()}
                      </Text>
                    </Text>
                    
                    {item.risk_level === 'high' && (
                      <Text style={styles.warningText}>
                        Requires immediate attention!
                      </Text>
                    )}
                  </View>
                </View>
              ))
            )}
          </View>
        )}
      </ScrollView>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#121212',
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 20,
    paddingVertical: 15,
    backgroundColor: '#1E1E1E',
  },
  title: {
    fontSize: 22,
    fontWeight: 'bold',
    color: '#FFFFFF',
  },
  statusIndicator: {
    width: 10,
    height: 10,
    borderRadius: 5,
  },
  scrollContainer: {
    padding: 20,
  },
  imageContainer: {
    width: '100%',
    height: width * 0.8,
    borderRadius: 10,
    overflow: 'hidden',
    backgroundColor: '#1E1E1E',
    marginBottom: 20,
    position: 'relative',
  },
  image: {
    width: '100%',
    height: '100%',
  },
  placeholder: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  placeholderText: {
    color: '#666',
    marginTop: 10,
  },
  actionButtons: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    marginBottom: 20,
  },
  button: {
    backgroundColor: '#4C8FFB',
    paddingVertical: 12,
    paddingHorizontal: 20,
    borderRadius: 8,
    flexDirection: 'row',
    alignItems: 'center',
  },
  buttonText: {
    color: '#FFFFFF',
    marginLeft: 8,
    fontWeight: '600',
  },
  loadingContainer: {
    padding: 20,
    alignItems: 'center',
  },
  loadingText: {
    color: '#FFFFFF',
    marginTop: 10,
    fontSize: 16,
  },
  resultsContainer: {
    backgroundColor: '#1E1E1E',
    borderRadius: 10,
    padding: 15,
    marginBottom: 20,
  },
  resultsTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#FFFFFF',
    marginBottom: 15,
  },
  noResultsText: {
    color: '#888',
    textAlign: 'center',
    padding: 20,
  },
  resultItem: {
    backgroundColor: '#2A2A2A',
    borderRadius: 8,
    marginBottom: 10,
    padding: 12,
    borderLeftWidth: 4,
  },
  resultHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 6,
  },
  resultLabel: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#FFFFFF',
  },
  resultConfidence: {
    fontSize: 14,
    color: '#BBBBBB',
  },
  resultDetails: {
    marginTop: 5,
  },
  resultRisk: {
    fontSize: 14,
    color: '#DDDDDD',
  },
  warningText: {
    color: '#ff4d4d',
    fontSize: 13,
    marginTop: 4,
  },
  detectionBox: {
    position: 'absolute',
    borderWidth: 2,
    backgroundColor: 'rgba(0,0,0,0.1)',
  },
  detectionLabel: {
    position: 'absolute',
    top: -20,
    left: 0,
    backgroundColor: 'rgba(255, 0, 0, 0.7)',
    color: 'white',
    fontSize: 10,
    padding: 2,
    borderRadius: 2,
  },
});

export default HomeScreen;
