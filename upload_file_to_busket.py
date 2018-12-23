#!/usr/bin/env python3

import boto3
import json

with open('config.json') as f:
    config = json.load(f)

s3 = boto3.client(
    's3',
    aws_access_key_id=config['aws_access_key_id'],
    aws_secret_access_key=config['aws_secret_access_key'],
    region_name=config['region_name']
)

bucket_config = config['s3']['buckets'][0]


file = 'index.html'
s3.upload_file(file, bucket_config['name'], file)
