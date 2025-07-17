<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/PyTorch-1.9%2B-orange?style=for-the-badge&logo=pytorch" alt="PyTorch Version">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

<h1 align="center">VISTA-S: Visual Inference System for Target Assessment</h1>
<h2 align="center">DualityAI Space Station Model</h2>

<p align="center">
  <b>Welcome to <strong>VISTA-S</strong></b> — a cutting-edge, high-precision AI system for <b>object detection</b> and visual inference.<br>
  Inspired by the mysteries of space, VISTA-S delivers powerful computer vision capabilities with ease and elegance. 🌌
</p>

---

## ✨ Features

- **State-of-the-Art Detection:** Built on YOLOv8 for high-precision object detection.
- **Optimized Performance:** Fast, efficient inference for real-time applications.
- **Interactive Demo:** Visualize and interact with predictions through an easy-to-use web app.
- **Seamless Data Integration:** Streamlined data preparation and handling for a smooth workflow.

---

## 📸 VISTA-S in Action


[![Watch the video](https://img.youtube.com/vi/gH7p3Jfavg0/maxresdefault.jpg)](https://youtu.be/gH7p3Jfavg0?si=kfichBROCP6rzNP4)

<p align="center">
  <img src="https://github.com/user-attachments/assets/ef5defcd-19df-4515-be84-acdd09346f24" width="47%" alt="Vista Sample 1">
  <img src="https://github.com/user-attachments/assets/bd32a41b-ecf9-48e3-b233-11f638d9783c" width="47%" alt="Vista Sample 2">
  <br><br>
  <img src="https://github.com/user-attachments/assets/ad7b5e0a-3c0a-47b6-8202-efc10d108cd2" width="47%" alt="Vista Sample 3">
  <img src="https://github.com/user-attachments/assets/1b65551c-454b-4799-b8dc-136a10ea9b26" width="47%" alt="Vista Sample 4">
</p>



---

## ⚡ Quickstart

**Get up and running in minutes!**

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

- **Download the Falcon Dataset:**  
  [Download here](#) <!-- Replace with actual link if available -->

- **Unzip & Place:**  
  Extract the dataset and copy its contents to:

  ```
  data/raw/
  ```

> **Note:** The dataset is NOT included in this repository due to its size. Please download it manually.

---

### 🏋️‍♂️ Training

Train the model on your machine:

```bash
python src/train.py
```

---

### 🔍 Inference

Detect objects in a sample image:

```bash
python src/detect.py data/raw/test/images/sample.jpg
```

---

### 🖥️ Demo Application

Experience VISTA-S through the interactive web app:

1. **Navigate to the app directory:**

    ```bash
    cd app
    ```

2. **Install requirements:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Start the backend server:**

    ```bash
    python backend.py
    ```

---

## 📊 Performance

VISTA-S achieves exceptional results on the Falcon dataset:

- **Precision:** ~0.9797
- **Recall:** ~0.9088
- **mAP@0.5:** ~0.9416
- **mAP@0.5:0.95:** ~0.8843

These scores are based on the YOLOv8 architecture.  
For detailed logs and more metrics, see the `models/logs/yolov8_observo/` directory.

---

## 📁 Project Structure

```
├── app/                   # Flask backend app
│   ├── backend.py
│   ├── routes.py
│   ├── simple_backend.py
│   ├── requirements.txt
│   └── templates/
│       └── index.html
├── config/
│   └── observo.yaml
├── data/
│   └── raw/
│       ├── classes.txt
│       ├── predict.py
│       ├── train.py
│       ├── visualize.py
│       ├── yolo_params.yaml
│       └── data/
├── docs/
│   └── report_outline.md
├── mobile/
│   ├── src/
│   │   ├── App.js
│   │   ├── api/
│   │   └── screens/
│   ├── package.json
│   ├── README.md
│   └── SETUP.md
├── models/
│   ├── weights/
│   └── logs/
├── notebooks/
│   ├── EDA.ipynb
│   └── train_yolov8.ipynb
├── src/
│   ├── detect.py
│   ├── train.py
│   ├── utils.py
│   └── constraints.txt
├── uploads/
├── Web_App_frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── hooks/
│   ├── package.json
│   └── vite.config.ts
├── environment.yaml
├── requirements.txt
├── requirements_minimal.txt
├── render.yaml
├── gunicorn_config.py
├── Procfile
├── .gitignore
├── .gitattributes
├── DEPLOYMENT.md
└── README.md
```

---

## ⚠️ DO NOT COMMIT SENSITIVE OR LARGE FILES

- **Model weights, logs, uploads, and raw data are excluded via `.gitignore`.**
- **Do NOT commit files in `models/weights/`, `models/logs/`, `uploads/`, or `data/raw/`.**
- **Notebooks and environment folders are also excluded.**

---

## 🤝 Contributing

We welcome your contributions!

1. **Fork** the repository.
2. **Create a branch** for your changes.
3. **Submit a pull request** with a clear description.

For major changes or new features, please open an issue first to discuss.

---

## 📄 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---

<p align="center">
  ✨ Explore the universe with VISTA-S! <br>
  Star the repo, open issues, or contribute to its growth.<br>
  Your feedback and contributions are always welcome.
</p>
