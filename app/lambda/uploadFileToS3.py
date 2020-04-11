from flask import Flask, escape, request, render_template
import boto3
from botocore.client import Config

app = Flask(__name__, template_folder='template')

ACCESS_KEY_ID = 'AKIAI3HGHAES6K5SNOQQ'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 'anurag1306171a'

@app.route('/')
def index():
    return render_template('/app/template/index.html')

# a route where we will display a welcome message via an HTML template
@app.route("/uploader", methods=['GET','POST'])
def upload():
    if request.method == 'POST':

        file = request.files['file']

        if file :
            FILE_NAME = file.filename
            # data = open(FILE_NAME, 'rb')
            # S3 Connect
            s3 = boto3.resource(
                's3',
                aws_access_key_id=ACCESS_KEY_ID,
                aws_secret_access_key=ACCESS_SECRET_KEY,
                config=Config(signature_version='s3v4')
            )

            # Image Uploaded
            # s3.Bucket(BUCKET_NAME).put_object(Key=FILE_NAME, Body=data, ACL='public-read')
            s3.Bucket(BUCKET_NAME).put_object(Key=FILE_NAME, ACL='public-read')

            print ("Done")
            return render_template('index.html', message=FILE_NAME + ' -> Uploaded to S3 *(' + BUCKET_NAME + ')* - AWS !');

# run the application
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
