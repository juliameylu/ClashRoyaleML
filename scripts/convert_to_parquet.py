import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")
CSV_FILE = DATA_DIR / "BattlesStaging_01012021_WL_tagged.csv"
PARQUET_FILE = DATA_DIR / "clash_royale.parquet"

def main():
    if not CSV_FILE.exists():
        raise FileNotFoundError(f"{CSV_FILE} not found.")
    
    if PARQUET_FILE.exists():
        print("Parquet already exists. Skipping conversion.")
        return

    print("Loading CSV...")
    df = pd.read_csv(CSV_FILE)

    print("Saving as Parquet...")
    df.to_parquet(PARQUET_FILE, engine="pyarrow", compression="snappy")

    print("Conversion complete.")

if __name__ == "__main__":
    main()