import boto3

ec2 = boto3.client('ec2')

instance_id='i-sdifoweinsdl'
name='test_ec2'

response = ec2.create_image(
    Description='An AMI for my server',
    InstanceId=instance_id,
    Name=name,
)

print(response["ImageId"])