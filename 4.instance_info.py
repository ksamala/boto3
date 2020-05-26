import boto3

aws_mgt=boto3.session.Session(profile_name="KalyanS", region_name="us-east-2")

ec2_con=aws_mgt.client(service_name="ec2")

response=ec2_con.describe_instances()['Reservations']
print("===========================")
for each_item in response:
    for each_inst in each_item['Instances']:
        print("Instance Id is {}\nImage Id is {}\nand Launch time is {}".format(each_inst['InstanceId'], each_inst['ImageId'], each_inst['LaunchTime'].strftime("%Y-%m-%d")))
        print("===========================")