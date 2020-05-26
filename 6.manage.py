import boto3
import sys

aws_mgt=boto3.session.Session(profile_name="KalyanS")
ec2_con=aws_mgt.client(service_name="ec2", region_name="us-east-2")
ec2_con_re=aws_mgt.resource(service_name="ec2", region_name="us-east-2")
response_ec2=ec2_con.describe_instances()

while True:
    print("Manage all ec2 instances from here")
    print("""
        1. Show all instances with current state
        2. Start instance
        3. Stop instance
        4. Restart instance
        5. Terminate instance
        6. Exit""")

    opt=int(input("Enter your option: "))
    if opt==1:
        print("Displaying all EC2 instances")
        print("--------------------------")
        for each_item in response_ec2['Reservations']:
            for each_inst in each_item['Instances']:
                print(each_inst['InstanceId'], each_inst['State']['Name'])
                print("--------------------------")

    elif opt==2:
        print("-------------")
        instance_id=input('Enter your EC2 Instance ID: ')
        ec2_inst=ec2_con_re.Instance(instance_id)
        print(ec2_inst.start())
        print("Your instance is starting")

    elif opt==3:
        print("-------------")
        instance_id=input('Enter your EC2 Instance ID: ')
        ec2_inst=ec2_con_re.Instance(instance_id)
        print(ec2_inst.stop())
        print("Your instance is stopping")

    elif opt==4:
        print("-------------")
        instance_id=input('Enter your EC2 Instance ID: ')
        ec2_inst=ec2_con_re.Instance(instance_id)
        print(ec2_inst.reboot())
        print("Your instance is restarting")
        
    elif opt==5:
        print("-------------")
        instance_id=input('Enter your EC2 Instance ID: ')
        ec2_inst=ec2_con_re.Instance(instance_id)
        print(ec2_inst.terminate())
        print("Your instance is terminating")
        
    elif opt==6:
        print("-------------")
        sys.exit()

    else:
        print("------------------------")
        print("any of the below options")
        print("------------------------")
