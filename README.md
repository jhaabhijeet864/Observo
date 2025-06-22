# 🛰️ Observo: DualityAI Space Station Model 🚀

Welcome to **Observo** — a high-performance AI model for object detection, inspired by the complexity and wonder of space exploration! 🌌

---

## ⚡️ Quick Setup

1️⃣ **Create Environment**  
```bash
conda env create -f environment.yaml
```

2️⃣ **Activate Environment**  
```bash
conda activate Observo
```

---

## 📦 Data Preparation

- ⬇️ Download and unzip the **Falcon dataset** into the following directory:  
  ```
  data/raw/
  ```

---

## 🏋️‍♂️ Training

Train the model with a single command:  
```bash
python src/train.py
```

---

## 🔍 Inference

Run object detection on a sample image:  
```bash
python src/detect.py data/raw/test/images/sample.jpg
```

---

## 🖥️ Demo Application

1. Move to the app directory:
    ```bash
    cd app
    ```
2. Install requirements:
    ```bash
    pip install -r requirements.txt
    ```
3. Start the backend server:
    ```bash
    python backend.py
    ```

---

✨ Enjoy exploring the universe of possibilities with Observo!  
Feel free to ⭐️ the repo, open issues, or contribute!
