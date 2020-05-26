import boto3

aws_mgt=boto3.session.Session(profile_name="KalyanS", region_name="us-east-2")
ec2_con=aws_mgt.client(service_name="ec2")

response=ec2_con.describe_volumes()['Volumes']
print(response)