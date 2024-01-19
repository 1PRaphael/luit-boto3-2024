import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_security_groups()

for security_group in response["SecurityGroups"]:
    print(security_group["GroupId"], security_group["VpcId"], 
          security_group["GroupName"], security_group["Description"], 
          )
    
   
    for permission in security_group["IpPermissions"]:
        if "FromPort" in permission:
            print(permission["FromPort"])

        if "IpProtocol" in permission:
            print(permission["IpProtocol"])

        if "ToPort" in permission:
            print(permission["ToPort"])

        if "IpRanges" in permission:
            for iprange in permission["IpRanges"]:
                print(iprange["CidrIp"])