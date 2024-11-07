import pickle

def load_pkl_file(filepath):
    with open(filepath, "rb") as file:
        return pickle.load(file)