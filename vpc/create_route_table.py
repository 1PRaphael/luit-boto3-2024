import boto3

ec2 = boto3.client('ec2')

routeTable = ec2.create_route_table(VpcId='vpc-847ujd,sjsdkis',)

print(routeTable['RouteTable']['RouteTableId'])