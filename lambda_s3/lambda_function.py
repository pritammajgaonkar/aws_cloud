import boto3

def lambda_handler(event, context):
    
    s3 = boto3.client("s3")
    if event:
        print("Event:", event)
        file_obj = event["Records"][0]
        fileName = str(file_obj['s3']['object']['key'])
        print("Filename:", fileName)
        fileObj = s3.get_object(Bucket = "yamendra", Key=fileName)
        fileContents = fileObj['Body'].read().decode('utf-8')
        print("fileContents:", fileContents)
        
