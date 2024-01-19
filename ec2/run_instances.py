import boto3

def run_instances(client, ami_id, security_group_id, key_name, user_data=None):
    response = client.run_instances(
        ImageId=ami_id,
        InstanceType='t2.micro',
        KeyName=key_pair_name,
        MaxCount=1,
        MinCount=1,
        SecurityGroupIds=[
            security_group_id,
        ],
        SubnetId='subnet-03672900427657506',
        
        UserData=user_data,

    
)

    print(response["Instances"][0]["InstanceId"])

ami_id= 'ami-9486943oriesldj'
key_pair_name='boto3_test_pair.pem'
security_group_id='sg-sldifu48sfdl;'

user_data=''' #!/bin/bash
    apt update -y
    apt-get install -y apache2
    systemctl start apache2
    systemctl enable apache2'''

ec2 = boto3.client('ec2')
run_instances(ec2, ami_id, security_group_id, key_pair_name, user_data)
