import boto3

ec2 = boto3.client('ec2')

route_table_id='rtb-847ujd,sjsdkis'
subnet_id='subnet-847ujd,sjsdkis'

association = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id,
)

print(association['AssociationId'])