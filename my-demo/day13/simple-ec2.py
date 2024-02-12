#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/run_instances.html
import boto3

client = boto3.client('ec2')
response = client.run_instances(
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/xvda',
            'Ebs': {
                'VolumeSize': 8,
            },
        },
    ],
    ImageId='ami-0449c34f967dbf18a',
    InstanceType='t2.micro',
    KeyName='mahesh-aws',
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[
        'sg-06f10533ad8576c5e',
    ],
    SubnetId='subnet-06d09724014e296b7',
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'name',
                    'Value': 'boto3-server',
                },
            ],
        },
    ],
)

print(response)
