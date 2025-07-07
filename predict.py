import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from keras.layers import TFSMLayer

# Load the trained model from Teachable Machine (SavedModel format)
model = tf.keras.Sequential([
    TFSMLayer("keras_model", call_endpoint="serving_default")
])

# Load and preprocess the input image
img_path = "test.jpg"
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array / 255.0

# Predict the class
predictions = model.predict(img_array)
predicted_class = int(np.argmax(predictions))

# Try to read class names from labels.txt (if available)
try:
    with open("labels.txt") as f:
        labels = f.readlines()
        label_name = labels[predicted_class].strip()
        print(f"\n✅ Prediction: The image belongs to class '{label_name}' (index {predicted_class})")
except:
    print(f"\n✅ Prediction: The image belongs to class index {predicted_class}")