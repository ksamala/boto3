import boto3

aws_mgt=boto3.session.Session(profile_name="KalyanS", region_name="us-east-2")

ec2_con=aws_mgt.client(service_name="ec2") #using client
s3_con=aws_mgt.resource(service_name="s3") #using resource
iam_con=aws_mgt.resource(service_name="iam") #using resource

response_ec2=ec2_con.describe_instances()

print("-------------")
print("EC2 instances")
print("-------------")
for each_item in response_ec2['Reservations']:
    for each_inst in each_item['Instances']:
        print(each_inst['InstanceId'])

print("---------")
print("IAM users")
print("---------")
for each_user in iam_con.users.all():
    print(each_user.name)

print("----------")
print("S3 buckets")
print("----------")
for each_buck in s3_con.buckets.all():
    print(each_buck.name)

print("----------------")