import boto3

ec2 = boto3.client('ec2')

destinationCidrBlock = '0.0.0.0/0'
route_table_id='rtb-847ujd,sjsdkis'

ec2.delete_route(
    DestinationCidrBlock=destinationCidrBlock,
    RouteTableId=route_table_id,
)
