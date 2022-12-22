import tensorflow as tf
import numpy as np
import gradio as gr
model = tf.keras.models.load_model("model.h5")
def predict(image):
  image = np.array(image).astype(np.float32) / 255.0
  image = image.reshape(1, 28, 28)
  prediction = model.predict(image)
  return np.argmax(prediction)
interface = gr.Interface(fn=predict,  
  inputs='sketchpad',
  outputs=gr.outputs.Label(num_top_classes=1),  
  server_port=10000, 
  server_name="0.0.0.0",
  css="footer {visibility: hidden}"
)
interface.launch()
