import os
from PIL import Image
import numpy as np
from sklearn.model_selection import train_test_split

IMG_SIZE = (128, 128)

def load_images(data_dir):
    X, y = [], []
    for label, folder in enumerate(['real', 'forged']):
        folder_path = os.path.join(data_dir, folder)
        if not os.path.exists(folder_path):
            print(f"Warning: {folder_path} does not exist")
            continue
        for fname in os.listdir(folder_path):
            try:
                img_path = os.path.join(folder_path, fname)
                img = Image.open(img_path).convert('RGB').resize(IMG_SIZE)
                X.append(np.array(img))
                y.append(label)
            except Exception as e:
                print(f"Error loading {img_path}: {e}")
    return np.array(X), np.array(y)

def split_dataset(X, y, test_size=0.2, random_state=42):
    return train_test_split(X, y, test_size=test_size, random_state=random_state)