import boto3
region = 'ap-northeast-1'
instances = ['i-010926c6376db3e72']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    return {
        'statusCode': 200,
        'body': 'stoped your instances'
    }
