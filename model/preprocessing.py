import os
import shutil
from sklearn.model_selection import train_test_split

# Paths
data_dir = 'dataset'
train_dir = 'train'
val_dir = 'validation'

# Ensure the train and validation directories exist
print('Creating Train and Validation Directories...')
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)
for category in ['Normal', 'Tuberculosis']:
    os.makedirs(os.path.join(train_dir, category), exist_ok=True)
    os.makedirs(os.path.join(val_dir, category), exist_ok=True)

# Load dataset
print('Loading Dataset...')
normal_images = [os.path.join(data_dir, 'Normal', f) for f in os.listdir(os.path.join(data_dir, 'Normal')) if f.endswith(('.png', '.jpg', '.jpeg'))]
tb_images = [os.path.join(data_dir, 'Tuberculosis', f) for f in os.listdir(os.path.join(data_dir, 'Tuberculosis')) if f.endswith(('.png', '.jpg', '.jpeg'))]

# Split dataset
print('Splitting Dataset...')
normal_train, normal_val = train_test_split(normal_images, test_size=0.2, random_state=42)
tb_train, tb_val = train_test_split(tb_images, test_size=0.2, random_state=42)

# Helper function to copy images
def copy_images(image_paths, dest_dir):
    for image_path in image_paths:
        shutil.copy(image_path, dest_dir)

# Copy images to train and validation directories
print('Copying images to respectiful directories...')
copy_images(normal_train, os.path.join(train_dir, 'Normal'))
copy_images(normal_val, os.path.join(val_dir, 'Normal'))
copy_images(tb_train, os.path.join(train_dir, 'Tuberculosis'))
copy_images(tb_val, os.path.join(val_dir, 'Tuberculosis'))

print("Dataset preprocessing complete.")

