#  VISTA: Visual Inference System for Target Assessment
#             DualityAI Space Station Model 🚀

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

- ⬇️ Download the Falcon Dataset 👉[here](https://falcon.duality.ai/secure/documentation/hackathon?highlight=hackathon) and unzip into the following directory:  
  ```
  data/raw/
  ```
  *Note: The dataset is not included in this repository due to size constraints. Please download it manually using the link above.*

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

## 📊 Results

- **Precision:** ~0.98
- **Recall:** ~0.95
- **mAP@0.5:** ~0.89
- **mAP@0.5:0.95:** ~0.83

*These results were achieved on the Falcon dataset using YOLOv8. See the `models/logs/yolov8_observo/` directory for detailed logs and visualizations.*

---

## 📝 Project Structure

```
├── app/                # Web app backend and requirements
├── config/             # Configuration files
├── data/               # Data folder (download dataset into data/raw/)
├── docs/               # Documentation and report outline
├── models/             # Model weights and logs
├── notebooks/          # (Optional) Jupyter notebooks for EDA
├── src/                # Source code for training, detection, utils
├── templates/          # Web app HTML templates
├── environment.yaml    # Conda environment definition
├── README.md           # Project overview and instructions
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the MIT License.

---

✨ Enjoy exploring the universe of possibilities with Observo!  
Feel free to ⭐️ the repo, open issues, or contribute!
