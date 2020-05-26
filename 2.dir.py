import boto3

aws_mgt_con=boto3.session.Session(profile_name="KalyanS")

response=dir(aws_mgt_con)
print(response)

''' display all operations on S3'''
s3_con = aws_mgt_con.resource(service_name="s3", region_name="us-east-2")
print("====================================")
print("display all operations on S3")
for each_buk in s3_con.buckets.all():
    print(dir(each_buk))
    break

print("====================================")
print("use one of the methods from the above listed - using name for now")

for each_buk in s3_con.buckets.all():
    print(each_buk.name)

