from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import os

def run_calculation(calculation_key, status):
    # Pseudodaten für K-Means
    data = np.random.rand(100000, 2000)
    kmeans = KMeans(n_clusters=30, n_init="auto", init="k-means++")
    kmeans.fit(data)


    # Assuming 'kmeans.cluster_centers_' is your data source
    df = pd.DataFrame(kmeans.cluster_centers_)

    # Subdirectory and filename
    subdirectory = 'results'
    filename = f"{calculation_key}_results.csv"
    filepath = os.path.join(subdirectory, filename)

    # Create subdirectory if it doesn't exist
    if not os.path.exists(subdirectory):
        os.makedirs(subdirectory)

    # Save to CSV
    df.to_csv(filepath, index=False)

    print(f"Calc {calculation_key} finished")
    # Status zurücksetzen
    status["status"] = "Idle"
