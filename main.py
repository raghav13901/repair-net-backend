from flask import Flask, request
from PIL import Image
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import os
from flask_cors import CORS, cross_origin
from super_resolution import SRGan

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route("/", methods=['POST'])
def home_view():
    rq = request.form.to_dict()
    a = list(request.form.to_dict([0]).keys())
    url = a[0]+"=media&token="+rq['token']
    image = Image.open(requests.get(url, stream=True).raw)

    obj = SRGan()
    print('a')
    output_img = obj.inference(image)
    output_img.show()


    # cred = credentials.Certificate('repairnet-74117-046770d2b6ad.json')
    # firebase_admin.initialize_app(cred, {
    #     'storageBucket': 'repairnet-74117.appspot.com'
    # })
    # image.save('myImage.jpg')
    # fileName = "myImage.jpg"
    # bucket = storage.bucket()
    # blob = bucket.blob(fileName)
    # blob.upload_from_filename(fileName)
    # blob.make_public()
    # os.remove("myImage.jpg")
    # return blob.public_url
    return 'a'

if __name__ == '__main__':
    app.run(host='localhost', port=7000)