import boto3
from datetime import datetime
import os

# Define the roles to assume in other accounts, including a name or identifier for each
roles_to_assume = [
    {'role_arn': 'arn:aws:iam::023898247285:role/list_users', 'account_name': 'adidasaws'},
    {'role_arn': 'arn:aws:iam::575307893982:role/list_users', 'account_name': 'carrefour'},
    {'role_arn': 'arn:aws:iam::277737129844:role/list_users', 'account_name': 'deliveryaws'},
    {'role_arn': 'arn:aws:iam::038948803938:role/list_users', 'account_name': 'Dev-PCI'},
    {'role_arn': 'arn:aws:iam::492465598180:role/list_users', 'account_name': 'dominosaws'},
    {'role_arn': 'arn:aws:iam::169842437727:role/list_users', 'account_name': 'galinmanage'},
    {'role_arn': 'arn:aws:iam::529920410683:role/list_users', 'account_name': 'GrowPlayground'},
    {'role_arn': 'arn:aws:iam::575774386730:role/list_users', 'account_name': 'htzoneaws'},
    {'role_arn': 'arn:aws:iam::146976730351:role/list_users', 'account_name': 'inManage LTD'},
    {'role_arn': 'arn:aws:iam::890827601494:role/list_users', 'account_name': 'InmanageQnap'},
    {'role_arn': 'arn:aws:iam::767397962108:role/list_users', 'account_name': 'masav'},
    {'role_arn': 'arn:aws:iam::251781337860:role/list_users', 'account_name': 'mcdonalds'},
    {'role_arn': 'arn:aws:iam::744780822679:role/list_users', 'account_name': 'oneaws'},
    {'role_arn': 'arn:aws:iam::410271831463:role/list_users', 'account_name': 'pcigrow'},
    {'role_arn': 'arn:aws:iam::680841093639:role/list_users', 'account_name': 'perelview'},
    {'role_arn': 'arn:aws:iam::633307939380:role/list_users', 'account_name': 'Restart Group Lab'},
    {'role_arn': 'arn:aws:iam::030284724768:role/list_users', 'account_name': 'RestartIT'},

]

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path for the output file relative to the script's directory
output_file_path = os.path.join(script_dir, 'iam_users_list.txt')

def assume_role(role_arn, session_name):
    """
    Assumes the specified role and returns the credentials.
    """
    sts_client = boto3.client('sts')
    assumed_role = sts_client.assume_role(
        RoleArn=role_arn,
        RoleSessionName=session_name
    )
    return assumed_role['Credentials']

def list_iam_users(credentials, account_name, output_file):
    """
    Lists IAM users in the specified account using the provided credentials
    and writes the output to a file.
    """
    session = boto3.Session(
        aws_access_key_id=credentials['AccessKeyId'],
        aws_secret_access_key=credentials['SecretAccessKey'],
        aws_session_token=credentials['SessionToken']
    )
    iam = session.client('iam')
    output_file.write(f"Listing IAM users in {account_name}:\n")
    print("Scanning: " + account_name)
    try:
        response = iam.list_users()
        for user in response['Users']:
            output_file.write(f"- {user['UserName']}\n")
    except Exception as e:
        output_file.write(f"Error listing users in {account_name}: {e}\n")

# Open a file to write the output
with open(output_file_path, 'w') as output_file:
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    output_file.write(f"Report generated on: {current_time}\n\n")
    for role in roles_to_assume:
        creds = assume_role(role['role_arn'], "ListUsersSession")
        list_iam_users(creds, role['account_name'], output_file)