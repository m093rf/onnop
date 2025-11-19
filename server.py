from flask import Flask, request
import base64

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    data = request.json
    lat = data.get("lat")
    lon = data.get("lon")
    selfie_base64 = data.get("selfie")

    # حفظ الصورة
    selfie_bytes = base64.b64decode(selfie_base64.split(",")[1])
    with open("selfie.png", "wb") as f:
        f.write(selfie_bytes)

    # حفظ الموقع
    with open("location.txt", "w") as f:
        f.write(f"Latitude: {lat}, Longitude: {lon}\n")

    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
