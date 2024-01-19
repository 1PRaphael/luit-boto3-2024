import boto3

ec2 = boto3.client('ec2')

description= 'My boto3 security group'
group_name = 'my-boto3-security-group'
vpc_id = 'vpc-847ujd,sjsdkis'



response = ec2.create_security_group(
    Description=description,
    GroupName=group_name,
    VpcId=vpc_id,
)

print(response["GroupId"])