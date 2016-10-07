#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto3
import json

# バケット名
f = open('./DeleteBucketsList.json', 'r')
BucketsData = json.load(f)
BucketKeyList = BucketsData['BucketList']
rc = len(BucketKeyList)

for k in BucketKeyList:
	AWS_S3_BUCKET_NAME = k['name']
	client = boto3.client('s3')
	flag = "True"
	while flag=="True":
		objects = client.list_object_versions(
		Bucket=AWS_S3_BUCKET_NAME,
		#Prefix='log'
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
	print "-------------%s's all objects deleted-----------------" %(AWS_S3_BUCKET_NAME)
else:
	print "-------------%d Buckets applied-----------------" %(rc)

	
	




	
        
