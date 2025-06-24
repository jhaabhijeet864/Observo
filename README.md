<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/PyTorch-1.9%2B-orange?style=for-the-badge&logo=pytorch" alt="PyTorch Version">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

<h1 align="center">VISTA-S: Visual Inference System for Target Assessment 🛰️ </h1>
<h2 align="center">DualityAI Space Station Model </h2>

<p align="center">
  <b>Welcome to <strong>VISTA</strong></b> — an advanced, high-performance AI model designed for <b>object detection</b> with unparalleled precision.
  Inspired by the vast complexity and endless wonder of space exploration, VISTA brings cutting-edge computer vision capabilities to your fingertips. 🌌
</p>

---

## ✨ Features & Highlights

- **High-Precision Object Detection:** Leverages state-of-the-art YOLOv8 for superior accuracy.
- **Optimized Performance:** Engineered for efficiency, delivering rapid inference.
- **User-Friendly Demo Application:** Easily visualize and interact with the model's capabilities.
- **Comprehensive Data Handling:** Streamlined data preparation for seamless integration.

---

## 📸 Glimpse of VISTA in Action

![image](https://github.com/user-attachments/assets/dd193d48-df47-4687-8eda-10ce44a7e0d4)


<br>

![image](https://github.com/user-attachments/assets/da6f8f5e-2834-4007-9003-6ee1eaab3798)



---

## ⚡️ Quick Setup Guide

Get VISTA up and running in a few simple steps!

### 1. Create Environment

```bash
conda env create -f environment.yaml
```

### 2. Activate Environment

```bash
conda activate VISTA
```

---

### 📦 Data Preparation

To begin, you'll need the **Falcon Dataset**.

- **Download the Falcon Dataset:**  
  Access the dataset from [here](#). <!-- Add actual link if available -->

- **Unzip & Place:**  
  Unzip the downloaded dataset and place its contents into the following directory structure:

  ```
  data/raw/
  ```

> **Note:** The dataset is not included in this repository due to its size. Please download it manually using the provided link.

---

### 🏋️‍♂️ Training the Model

Train Observo on your local machine with a single, straightforward command:

```bash
python src/train.py
```

---

### 🔍 Running Inference

Perform object detection on any sample image effortlessly:

```bash
python src/detect.py data/raw/test/images/sample.jpg
```

---

### 🖥️ Demo Application

Experience VISTA-S through its interactive web application:

1. **Navigate to App Directory:**

    ```bash
    cd app
    ```

2. **Install Requirements:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Start Backend Server:**

    ```bash
    python backend.py
    ```

---

## 📊 Performance Metrics

Observo delivers exceptional performance on the Falcon dataset:

- **Precision:** ~0.98  
- **Recall:** ~0.95  
- **mAP@0.5:** ~0.89  
- **mAP@0.5:0.95:** ~0.83  

These impressive results were achieved using the YOLOv8 architecture.  
For an in-depth analysis, including detailed logs and visualizations, please refer to the `models/logs/yolov8_observo/` directory.

---

## 📝 Project Structure

The repository is thoughtfully organized for clarity and ease of navigation:

```
├── app/                # Web application backend and dependencies
├── config/             # Essential configuration files
├── data/               # Contains raw and processed datasets (download raw into data/raw/)
├── docs/               # Project documentation and report outlines
├── models/             # Stores trained model weights and comprehensive logs
├── notebooks/          # (Optional) Jupyter notebooks for exploratory data analysis (EDA)
├── src/                # Core source code for training, detection, and utility functions
├── templates/          # HTML templates for the web application
├── environment.yaml    # Conda environment definition for seamless setup
├── README.md           # This project overview and instructions
```

---

## 🤝 Contributing

We welcome contributions from the community! If you have suggestions, bug reports, or would like to contribute code:

1. **Fork** the repository.
2. **Create a new branch** for your feature or bug fix.
3. **Submit a pull request** with a clear description of your changes.

For major changes or new features, please open an issue first to discuss the proposed modifications.

---

## 📄 License

This project is open-source and licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

<p align="center">
  ✨ Enjoy exploring the universe of possibilities with Observo! <br>
  Feel free to ⭐️ the repository, open issues, or contribute to its growth.<br>
  Your feedback and contributions are highly valued.
</p>

