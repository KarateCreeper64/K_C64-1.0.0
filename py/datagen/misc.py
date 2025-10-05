import os

def create(file):
    if not(os.path.exists(file)):
        os.makedirs(os.path.dirname(file), exist_ok=True)
        open(file, "x").close()