import json
import boto3
import uuid

s3 = boto3.client('s3')
BUCKET_NAME = "lifelink-donor-data-unique"
FILE_KEY = "donors/all_donors.json"

def lambda_handler(event, context):
    body = json.loads(event.get('body', '{}'))

    new_donor = {
        "donor_id": str(uuid.uuid4()),
        "name": body.get("name"),
        "blood_group": body.get("blood_group"),
        "phone": body.get("phone"),
        "location": body.get("location"),
        "availability": True
    }

    try:
        response = s3.get_object(Bucket=BUCKET_NAME, Key=FILE_KEY)
        donors = json.loads(response["Body"].read())
    except:
        donors = []

    donors.append(new_donor)

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=FILE_KEY,
        Body=json.dumps(donors)
    )

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Donor Registered"})
    }
