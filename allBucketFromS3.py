#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto3
import json

# バケット名
AWS_S3_BUCKET_NAME = 'your_bucket_name'

client = boto3.client('s3')
# s3 = boto3.resource('s3')
# bucket = s3.Bucket(AWS_S3_BUCKET_NAME)
flag = "True"

while flag=="True":
	objects = client.list_object_versions(
	Bucket=AWS_S3_BUCKET_NAME,
	Prefix='your_bucket_prefix'
	)
	flag = str(objects['IsTruncated'])
	dataList = objects['Versions']
	for data in dataList:
		keyName = data['Key']
		versionId = data['VersionId']
		deleteData = client.delete_object(
		Bucket=AWS_S3_BUCKET_NAME,
		Key=keyName,
		VersionId=versionId
		)
		print deleteData
else:
	print flag
	print "-------------all deleted-----------------"

	
	




	
        
