import tensorflow as tf
from tensorflow.keras.preprocessing import image
#from tensorflow.keras.applications.vgg16 import preprocess_input # for VGG16
#from tensorflow.keras.applications.resnet50 import preprocess_input #for resnet50
import numpy as np

# Example function for model loading and prediction
def load_model():
    # Load your trained model here (TensorFlow, PyTorch, etc.)
    model = tf.keras.models.load_model('./model/tb_detection_model.h5')
    return model

def predict_tb(image_path):
    model = load_model()
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalize
    prediction = model.predict(img_array)
    if prediction[0][0] >= 0.5:
        return {'predicted': 'Positive'}
    else:
        return {'predicted': 'Negative'}

