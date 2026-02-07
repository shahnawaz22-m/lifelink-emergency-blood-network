import json
import boto3

s3 = boto3.client('s3')
BUCKET_NAME = "lifelink-donor-data-unique"
FILE_KEY = "donors/all_donors.json"

def lambda_handler(event, context):
    body = json.loads(event.get('body', '{}'))
    requested_group = body.get("blood_group", "").lower()

    try:
        response = s3.get_object(Bucket=BUCKET_NAME, Key=FILE_KEY)
        donors = json.loads(response["Body"].read())
    except:
        donors = []

    matching_donors = []

    for donor in donors:
        if (
            donor.get("blood_group", "").lower() == requested_group
            and donor.get("availability", True)
        ):
            matching_donors.append(donor)

    if not matching_donors:
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "No donors found"
            })
        }

    return {
        "statusCode": 200,
        "body": json.dumps({
            "matching_donors": matching_donors
        })
    }
