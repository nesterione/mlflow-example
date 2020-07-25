#!/usr/bin/env/python
import os
import boto3
from botocore.client import Config
from minio import Minio
from minio.error import ResponseError
import zipfile

output_dir = '../data/raw'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

dest_file = os.path.join(output_dir,'imdb_raw_v1.zip')

if not os.path.exists(output_dir):
    

    client = Minio(os.environ.get('BUCKET_HOST').replace('http://',''),
        access_key=os.environ.get('BUCKET_KEY'),
        secret_key=os.environ.get('BUCKET_SECRET'),
        secure=False)

    try:
        client.fget_object('storage', 'imdb/imdb_raw_v1.zip', dest_file)
    except ResponseError as err:
        print(err)

    with zipfile.ZipFile(dest_file, 'r') as zip_ref:
        zip_ref.extractall(output_dir)