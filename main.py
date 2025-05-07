import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from PIL import Image
import numpy as np
from collections import Counter

# Load variables from .env file
load_dotenv()

# Create Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')

# Connect Bootstrap to Flask app
Bootstrap5(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the uploaded image and convert to a NumPy array.
        img = Image.open(request.files['img_file'])
        img_array = np.array(img)

        # Flatten the image array into a list of tuples. Each tuple holding the RGB(A?) of a pixel.
        pixel_list = [tuple(p) for p in np.reshape(img_array, (-1, img_array.shape[2]))]

        # Count the pixel colors, get the top 10, and convert to hex color codes.
        color_counter = Counter(pixel_list)
        rgb_colors = [c[0] for c in color_counter.most_common(10)]
        hex_colors = [f'#{c[0]:0>2x}{c[1]:0>2x}{c[2]:0>2x}' for c in rgb_colors]
        
        return render_template('index.html', colors=hex_colors)

    return render_template('index.html')


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
