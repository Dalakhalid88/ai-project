# AI Image Classification Project

This project is a simple image classifier built using [Teachable Machine](https://teachablemachine.withgoogle.com/) and deployed with TensorFlow in Python.

## 💡 What it does
- Takes an input image (`test.jpg`)
- Loads a trained model (`keras_model`)
- Predicts the class using TensorFlow
- Prints the predicted label in the terminal

## 📁 Project Structure
- `predict.py` — Python script for prediction
- `test.jpg` — Example image for testing
- `labels.txt` — Class names from Teachable Machine
- `keras_model/` — Exported TensorFlow model (saved_model format)

## 🚀 How to Run
Make sure Python and the following packages are installed:
```bash
pip install tensorflow-macos tensorflow-metal pillow
Then run:

```bash
python predict.py


🙋‍♀️ Created by:

Dala Khalid — as part of an AI course task.
