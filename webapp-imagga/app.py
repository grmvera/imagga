from flask import Flask, render_template, request, url_for
import requests

app = Flask(__name__)

IMAGGA_API_KEY = 'acc_2e4752c2715fa67'
IMAGGA_API_SECRET = '3bdb738349ba28ab9b2d143798f3bb02'
TAGS_ENDPOINT = 'https://api.imagga.com/v2/tags'

@app.route('/')
def index():
    images = [
        'https://i.postimg.cc/XrzfZwzH/image1.jpg',  # Foto 1
        'https://i.postimg.cc/QBKpcFLX/image2.jpg',  # Foto 2
        'https://i.postimg.cc/Yv9NqXbL/image3.jpg'   # Foto 3
    ]
    return render_template('index.html', images=images)


@app.route('/analyze', methods=['POST'])
def analyze():
    image_url = request.form['image_url']
    try:
        response = requests.get(
            TAGS_ENDPOINT,
            auth=(IMAGGA_API_KEY, IMAGGA_API_SECRET),
            params={'image_url': image_url}
        )
        response.raise_for_status()
        
        data = response.json()
        tags = data.get('result', {}).get('tags', [])[:2]  # Solo los dos resultados principales
        return render_template('result.html', tags=tags, image_url=image_url)
    except requests.exceptions.RequestException as e:
        return f"Error al conectar con Imagga: {e}", 500
    except ValueError:
        return f"Error al procesar JSON: {response.text}", 500




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

