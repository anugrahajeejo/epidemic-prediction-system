import pandas as pd
import numpy as np

# -------------------------
# CLEAN DENGUE DATASET
# -------------------------

dengue = pd.read_csv("dengue.csv")

dengue = dengue.rename(columns={
    "Time": "month",
    "Case": "cases",
    "Temperature": "temperature",
    "Rainfall": "rainfall",
    "Humidity": "humidity"
})

dengue = dengue[["month","temperature","rainfall","humidity","cases"]]

# outbreak label
dengue["outbreak"] = (dengue["cases"] > dengue["cases"].mean()).astype(int)

dengue.to_csv("dengue_processed.csv", index=False)


# -------------------------
# CLEAN MALARIA DATASET
# -------------------------

malaria = pd.read_csv("malaria.csv")

# clean cases column
malaria["No. of cases"] = malaria["No. of cases"].astype(str)
malaria["cases"] = malaria["No. of cases"].str.extract(r'(\d+)')
malaria["cases"] = pd.to_numeric(malaria["cases"], errors="coerce")

# remove empty rows
malaria = malaria.dropna(subset=["cases"])

# generate synthetic environmental factors
np.random.seed(42)

malaria["month"] = np.random.randint(1,13,len(malaria))
malaria["temperature"] = np.random.uniform(22,34,len(malaria))
malaria["rainfall"] = np.random.uniform(50,300,len(malaria))
malaria["humidity"] = np.random.uniform(60,95,len(malaria))

# outbreak label
malaria["outbreak"] = (malaria["cases"] > malaria["cases"].median()).astype(int)

malaria = malaria[["month","temperature","rainfall","humidity","cases","outbreak"]]

malaria.to_csv("malaria_processed.csv", index=False)


print("Datasets successfully prepared!")