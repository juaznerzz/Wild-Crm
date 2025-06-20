from flask import Flask, request, send_file, jsonify
from gtts import gTTS
from io import BytesIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/tts', methods=['POST'])
def tts():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    text = data['text']
    lang = data.get('lang', 'es')
    tts = gTTS(text=text, lang=lang)
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    return send_file(mp3_fp, as_attachment=True, download_name='speech.mp3', mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(debug=True)
