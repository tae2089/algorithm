import boto3

s3 = boto3.client('s3')
s3.download_file('asa-data-expo-09', 'user-pays', '1987.csv.bz2')
