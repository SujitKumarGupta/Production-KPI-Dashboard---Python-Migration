"""Generate sample_production_data.xlsx with 60 days, 3 shifts/day, 5 machines."""
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent / "sample_production_data.xlsx"

def generate(days=60, machines=5):
    start = datetime.today() - timedelta(days=days-1)
    records = []
    machine_names = [f"Machine_{i+1}" for i in range(machines)]
    shifts = ["Shift1", "Shift2", "Shift3"]

    for d in range(days):
        date = (start + timedelta(days=d)).date()
        for shift in shifts:
            for m in machine_names:
                # realistic ranges
                output = int(np.random.normal(loc=500, scale=60))
                output = max(50, output)
                defects = int(np.random.binomial(n=output, p=0.02))
                downtime = int(max(0, np.random.normal(loc=20, scale=10)))
                records.append({
                    "Date": date,
                    "Shift": shift,
                    "Machine": m,
                    "Output": output,
                    "Defects": defects,
                    "DowntimeMinutes": downtime
                })

    df = pd.DataFrame.from_records(records)
    df.to_excel(OUT, index=False)
    print(f"Wrote sample data to {OUT}")

if __name__ == '__main__':
    generate()
