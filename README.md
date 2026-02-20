# ClashRoyaleML

## Setup
Create environment:
```bash
conda create -n clashml python=3.10 -y
conda activate clashml
pip install -r requirements.txt
pip install ipykernel
python -m ipykernel install --user --name clashml --display-name "Python (clashml)"
```

Open ClashRoyaleEDA.ipynb and select "Python (clashml)"

## Download Dataset

We use the Clash Royale dataset from Hugging Face:

https://huggingface.co/datasets/Grandediw/clash-royale-battle 

Download with:
```bash
hf download Grandediw/clash-royale-battle \
  --repo-type dataset \
  --local-dir data/
```