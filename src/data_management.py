import joblib
import os

def load_pkl_file(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"The file {filepath} does not exist.")

    return joblib.load(filepath)