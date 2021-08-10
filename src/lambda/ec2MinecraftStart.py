import boto3
region = 'ap-northeast-1'
instances = ['xxxxxxxxxx']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    #result = ec2.describe_instances(InstanceIds=instances)
    #print(responce['Reservations'][0]['Instances'][0])#['PublicIpAddress'])
    return {
        'statusCode': 200,
        'body': 'stating ec'
    }
