# Deploy-ML-Models-in-the-Web

A simple way to deploy ML models in the web for testing or demo purposes using gradio and replacing heroku with Render.com



Gradio is a powerful tool that allows you to easily deploy your machine learning models in the web for testing or demo purposes. With just a few lines of code, you can have your model up and running in a web interface, where users can input data and get predictions from your model in real-time.

## Features
- Easy to use: Gradio has a simple and intuitive interface, making it easy to get started even if you have no prior experience with web development or deployment.

- Customizable: Gradio allows you to customize the look and feel of your interface, including the layout, colors, and font. You can also add your own custom CSS and JavaScript to further customize your interface.

- Responsive: Gradio's interfaces are designed to be responsive, meaning they will look great on any device, including smartphones, tablets, and laptops.

- Secure: Gradio uses secure server-side processing to protect your model and data. Your model is never exposed to the client, ensuring that your intellectual property is safe.


## Getting Started

To get started with Gradio, you will need to install the library using pip:

```
pip install gradio
```
Next, you will need to define your model as a function, and pass it to the Interface class:
```
import gradio as gr

def model(inputs):
  # Your model code here
  return output

interface = gr.Interface(model, inputs=inputs, outputs=outputs)
interface.launch()
```
You can then access your interface by visiting the URL displayed in the terminal.
For more information on using Gradio, check out the documentation

## Deploying to the web

To get started with Render, simply log in to render.com and connect your repository. You will then be able to deploy your models with just a few clicks.

You cant directly Deploy your app without a few settings like 
the start command 



```
gunicorn app:app
```

and for render's default server configuration would need configuring for Render.

- GRADIO_SERVER_PORT to 10000
- GRADIO_SERVER_NAME to 0.0.0.0

```
interface = gr.Interface(fn=predict,  
  inputs='sketchpad',
  outputs=gr.outputs.Label(num_top_classes=1),  
  server_port=10000, 
  server_name="0.0.0.0",
  css="footer {visibility: hidden}"
)

```

Then wait for the site to be live Happy Testing and Deploying
















