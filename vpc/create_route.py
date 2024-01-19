import boto3

ec2 = boto3.client('ec2')

route_table_id='rtb-847ujd,sjsdkis'
internet_gateway_id='igw-847ujd,sjsdkis'

ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway_id,
    RouteTableId=route_table_id,
)
