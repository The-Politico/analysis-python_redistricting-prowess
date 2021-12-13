# Imports from python.
import os


# Imports from other dependencies.
import boto3


S3_REGION_AZ = "us-east-1"
S3_MAX_AGE = "15"

S3_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME")

BUCKET_ROOT_URL = f"http://{S3_BUCKET_NAME}.s3.{S3_REGION_AZ}.amazonaws.com"

S3_CLIENT = boto3.client(
    "s3",
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
)

UPLOADED_FILES_ACL = "public-read"

UPLOADED_FILES_CACHE_HEADER = str(
    ",".join(
        [
            f"max-age={S3_MAX_AGE}",
            "stale-if-error=300",
            "stale-while-revalidate=5",
        ]
    )
)

BASE_FILE_PATH = "interactives/2021/redistricting-tracker-data"
