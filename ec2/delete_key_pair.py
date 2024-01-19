import boto3

keyname = 'boto3_test_pair.pem'

ec2 = boto3.client('ec2')

response = ec2.delete_key_pair(
    KeyName=keyname,
)

print(response)