import boto3

ec2 = boto3.client('ec2')

subnetId='subnet-847ujd,sjsdkis'

ec2.delete_subnet(
    SubnetId=subnetId,
)

