import tensorflow as tf
import numpy as np
import cv2 #lib for read image

class PredictImage:
  def __init__(self,model_path):
    self.model = tf.keras.models.load_model(model_path)

  def preprocessImage(self,img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (28,28), interpolation = cv2.INTER_AREA)
    img = img / 255.0 #Normalize to 0-1
    img = img.reshape(-1,28,28,1)
    return img

  def predict(self,img):
    img = self.preprocessImage(img)
    predictions = self.model.predict(img)
    return np.argmax(predictions[0])