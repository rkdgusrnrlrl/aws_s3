#!/usr/bin/env python3

import boto3
import json
import mimetypes

with open('config.json') as f:
    config = json.load(f)

s3 = boto3.client(
    's3',
    aws_access_key_id=config['aws_access_key_id'],
    aws_secret_access_key=config['aws_secret_access_key'],
    region_name='ap-northeast-2'
)
bucket_config = config['s3']['buckets'][1]
bucket_name = bucket_config['name']
s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=bucket_config['CreateBucketConfiguration'])

s3.put_bucket_website(Bucket=bucket_name, WebsiteConfiguration={
    'IndexDocument': {
        'Suffix': 'index.html'
    },
})
policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadForGetBucketObjects",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::%s/*" % bucket_name
        }
    ]
}

policy_str = json.dumps(policy)
s3.put_bucket_policy(Bucket=bucket_name, Policy=policy_str)

file = 'index.html'

mime = mimetypes.MimeTypes().guess_type(file)[0]

with open(file, 'rb') as f:
    s3.put_object(Key=file, Bucket=bucket_name, ContentType=mime[0], Body=f)
