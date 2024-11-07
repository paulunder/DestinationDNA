import joblib

# def load_pkl_file(filepath):
#     if not os.path.exists(filepath):
#         raise FileNotFoundError(f"The file {filepath} does not exist.")

#     return joblib.load(filepath)


def load_pkl_file(file_path):

    return joblib.load(filename=file_path)