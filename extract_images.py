from pathlib import Path
import pandas as pd

annots = pd.read_csv("annotations.csv")

for s in ["train", "test"]:
	for c in ["hp", "ssa"]:
		Path(f"data/{s}/{c}").mkdir(exist_ok=True, parents=True)

for idx in range(len(annots["Image Name"])):
	Path(f"images/{annots['Image Name'][idx]}").rename(Path(f"data/{annots['Partition'][idx]}/{annots['Majority Vote Label'][idx]}/{annots['Image Name'][idx]}"))

