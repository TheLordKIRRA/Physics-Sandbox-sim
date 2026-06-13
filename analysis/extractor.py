import json
import os
import numpy as np

log_path = "logs"
os.makedirs(log_path, exist_ok=True)

def log_data(config, result):
    index = len(os.listdir(log_path))

    # Convert NumPy types to native Python types
    def sanitize(o):
        if isinstance(o, np.bool_):
            return bool(o)
        if isinstance(o, np.integer):
            return int(o)
        if isinstance(o, np.floating):
            return float(o)
        return o

    sanitized_result = {k: sanitize(v) for k, v in result.items()}

    with open(f"{log_path}/episode_{index}.json", "w") as f:
        json.dump({'config': config, 'result': sanitized_result}, f, indent=2)

class TheoryExtractor:
    @staticmethod
    def generate_report(memory):
        with open("theory_report.txt", "w") as f:
            for i, (config, result) in enumerate(memory):
                f.write(f"Episode {i}\\n")
                f.write(f"Config: {config}\\n")
                f.write(f"Result: {result}\\n\\n")
