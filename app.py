from botocore.exceptions import ClientError
from flask import Flask, jsonify, request
import boto3

app = Flask(__name__)

s3 = boto3.client('s3')

@app.route('/s3/raw/upload', methods=['POST'])
def hello_world():
    if "file" not in request.files:
        return jsonify({'error': 'No file found'})
    file = request.files['file']

    try:
        if file.filename == '':
            return jsonify({'error': 'No file found'})

        s3.upload_fileobj(file.stream, "raw-techpix", file.filename)

        return jsonify("Success")
    except ClientError as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')