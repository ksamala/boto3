#displays account information


import boto3
aws_mgt=boto3.session.Session(profile_name="KalyanS", region_name="us-east-2")
sts_con=aws_mgt.client(service_name="sts")
response=sts_con.get_caller_identity()
print(response)
print("====================================")
print("Account number is in method 1")
print(response.get('Account'))
print("====================================")
print("Account number is in method 2")
print(response['Account'])
print("====================================")
