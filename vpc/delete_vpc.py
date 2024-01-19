import boto3

ec2 = boto3.client('ec2')

vpc_id='vpc-847ujd,sjsdkis'

ec2.delete_vpc(
    VpcId=vpc_id,
)