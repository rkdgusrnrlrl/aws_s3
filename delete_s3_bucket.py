#!/usr/bin/env python3

import boto3
import json
from botocore.errorfactory import BaseClientExceptions

with open('config.json') as f:
    config = json.load(f)

s3 = boto3.resource(
    's3',
    aws_access_key_id=config['aws_access_key_id'],
    aws_secret_access_key=config['aws_secret_access_key'],
    region_name=config['region_name']
)

bucket_config = config['s3']['buckets'][0]
bucket = s3.Bucket(bucket_config['name'])
try:
    bucket.delete()
except Exception as e:
    if e.response['Error']['Code']:
        print("not exist busket")
