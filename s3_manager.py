import boto3
from botocore.exceptions import ClientError

BUCKET = "olagoke-file-storage-2026"
REGION = "eu-north-1"

s3 = boto3.client("s3", region_name=REGION)


def upload_file(local_path, key=None):
    key = key or local_path.split("/")[-1]
    try:
        s3.upload_file(
            local_path, BUCKET, key,
            ExtraArgs={"ContentType": "text/plain"}
        )
        print(f"Uploaded {local_path} -> s3://{BUCKET}/{key}")
    except ClientError as e:
        print("Upload failed:", e)


def download_file(key, local_path):
    try:
        s3.download_file(BUCKET, key, local_path)
        print(f"Downloaded s3://{BUCKET}/{key} -> {local_path}")
    except ClientError as e:
        print("Download failed:", e)


def list_files():
    response = s3.list_objects_v2(Bucket=BUCKET)
    for obj in response.get("Contents", []):
        print(f"{obj['Key']}  ({obj['Size']} bytes)")


def get_metadata(key):
    try:
        r = s3.head_object(Bucket=BUCKET, Key=key)
        print(f"Key:           {key}")
        print(f"Size:          {r['ContentLength']} bytes")
        print(f"Content type:  {r['ContentType']}")
        print(f"Last modified: {r['LastModified']}")
        print(f"ETag:          {r['ETag']}")
    except ClientError as e:
        print("Metadata failed:", e)


def delete_file(key):
    try:
        s3.delete_object(Bucket=BUCKET, Key=key)
        print(f"Deleted {key}")
    except ClientError as e:
        print("Delete failed:", e)


if __name__ == "__main__":
    upload_file("test.txt")
    list_files()
    get_metadata("test.txt")
    download_file("test.txt", "downloaded_test.txt")
    # delete_file("test.txt")  # uncomment later to clean up
