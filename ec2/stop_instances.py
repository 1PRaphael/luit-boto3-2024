import boto3

def stop_instances(client, instance_id):
    response = ec2.stop_instances(
        InstanceIds=[
            instance_id,
        ],
    )

    print(instance_id, "stopped")

def start_instances(client, instance_id):
    response = client.start_instances(
        InstanceIds=[
            instance_id,
        ],
    )

    print(instance_id, "started")

def terminate_instances(client, instance_id):
    response = client.terminate_instances(
        InstanceIds=[
            instance_id,
        ],
    )

    print(instance_id, "terminated")


if __name__ == '__main__':
    instance_id = 'i-dfsl48hwrej'
    

    ec2 = boto3.client('ec2')
    terminate_instances(ec2, instance_id)
