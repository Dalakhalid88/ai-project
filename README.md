# 🧠 AI Image Classification Project

This is a simple image classification project built using [Teachable Machine](https://teachablemachine.withgoogle.com/) and deployed with TensorFlow in Python.

---

## 💡 What It Does

- 📷 Takes an input image (`test.jpg`)
- 📦 Loads a trained model (`keras_model`)
- 🧠 Predicts the class using TensorFlow
- 🖨️ Prints the predicted label in the terminal

---

## 📁 Project Structure

```
ai-project/
├── keras_model/    → Exported TensorFlow model
├── labels.txt      → Class labels from Teachable Machine
├── predict.py      → Prediction script
└── test.jpg        → Example image to test
```

---

## 🚀 How to Run

Make sure Python and the following packages are installed:

```bash
pip install tensorflow-macos tensorflow-metal pillow
```

Then run:

```bash
python predict.py
```

---

## 👩‍💻 Created by

**Dala Khalid** — as part of an AI course task.
