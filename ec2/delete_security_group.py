import boto3

security_group_id = 'string'

ec2 = boto3.client('ec2')

ec2.delete_security_group(
    GroupId=security_group_id,
)
