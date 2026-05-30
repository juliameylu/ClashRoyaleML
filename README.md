# ClashRoyaleML

Predicts Clash Royale battle outcomes using a leakage-aware ML pipeline on 1.73M filtered battles. Compares XGBoost, logistic regression, and a dummy baseline with thorough evaluation including ROC/PR curves, threshold sweeps, confidence buckets, and card-pair lift analysis.

Built as a final project for CSC 466 / Knowledge Discovery from Data (Cal Poly SLO, Winter 2026).

---

## Results

### Model Comparison

| Model | AUC | Accuracy | F1 |
|-------|-----|----------|----|
| XGBoost (600 estimators, hist) | **0.638** | **0.597** | **0.596** |
| Logistic Regression | 0.605 | 0.570 | — |
| Dummy (most_frequent) | — | 0.500 | — |

XGBoost improves meaningfully over random chance and the logistic baseline, but gains are modest — player skill, meta shifts, and unobserved card synergies are not fully captured in static deck features alone.

### Key Design Decisions

- **Temporal train/test split** (80/20 on `battleTime`): prevents data leakage from meta drift and avoids memorizing player patterns.
- **Leakage prevention**: dropped sequential row index, player/clan identifiers, winner/loser labels, and post-outcome-derived columns.
- **`DeckBinarizer`**: custom `BaseEstimator`/`TransformerMixin` for multi-hot deck encoding. Decks need multi-hot (not one-hot) because each deck is a set of 8 cards.
- **`make_long`**: transforms each battle into two training rows (winner-as-player + loser-as-player) to create balanced labels.
- **Arena/game-mode filtering**: 2.82M → 1.73M rows after filtering to high arenas (75th+ percentile) and the most common game mode.

### Evaluation Methodology

Beyond a single accuracy number, the notebooks include:
- ROC and PR curves for all three models
- Confidence buckets (how well-calibrated are the predictions?)
- Threshold sweep over [0.05, 0.95] — accuracy, F1, precision, recall vs. threshold
- Feature importances from XGBoost
- Card-pair lift analysis — which card combinations correlate with wins above base rate?

---

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

Convert CSV to Parquet
```bash
python scripts/convert_to_parquet.py
```
