import boto3

file_name = "boto3_test_pair"
keyname='boto3_test_pair.pem'

ec2 = boto3.client('ec2')

response = ec2.create_key_pair(
    KeyName=keyname,
)

with open(file_name, 'w') as f:
    f.write(response["KeyMaterial"])