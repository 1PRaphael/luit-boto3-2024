import boto3

ec2 = boto3.client('ec2')

image_id = 'string'

response = ec2.deregister_image(
    ImageId=image_id,
)