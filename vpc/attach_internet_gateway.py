import boto3

ec2 = boto3.client('ec2')

internet_gateway_id='igw-847ujd,sjsdkis'
vpc_id='vpc-847ujd,sjsdkis'

ec2.attach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id,
)