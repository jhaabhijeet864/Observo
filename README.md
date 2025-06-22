# Observo: A DualityAI Space Station Model for Object Detection
## Setup  
1. `conda env create -f environment.yaml`  
2. `conda activate Observo`  

## Data  
Download and unzip the Falcon dataset into `data/raw/`  

## Train  
`python src/train.py`  

## Inference  
`python src/detect.py data/raw/test/images/sample.jpg`  

## Demo App  
```bash
cd app
pip install -r requirements.txt
python backend.py
