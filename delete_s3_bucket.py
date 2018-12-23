#!/usr/bin/env python3

import boto3
import json
from botocore.errorfactory import BaseClientExceptions

with open('config.json') as f:
    config = json.load(f)

s3 = boto3.client(
    's3',
    aws_access_key_id=config['aws_access_key_id'],
    aws_secret_access_key=config['aws_secret_access_key'],
    region_name=config['region_name']
)

bucket_config = config['s3']['buckets'][1]

busket_name = bucket_config['name']
list_objects = s3.list_objects(Bucket=busket_name)

if ('Contents' in list_objects):
    for obj in list_objects['Contents']:
        s3.delete_objects(Bucket=bucket_config['name'], Delete={
            'Objects': [
                {
                    'Key': obj['Key']
                }
            ],
            'Quiet': True
        })

if bucket_config['type'] == 'static-hosting':
    s3.delete_bucket_website(Bucket=busket_name)

s3.delete_bucket(Bucket=busket_name)



