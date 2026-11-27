# Cloud File Storage Using Amazon S3 (Boto3)

A Python script that connects to Amazon S3 with the official AWS SDK (Boto3) and manages files in a private bucket: upload, list, metadata extraction, download and delete.

## Features
- Upload files to S3, with the content type detected automatically
- List all objects in the bucket
- Extract object metadata (size, content type, last modified, ETag)
- Download files from S3
- Delete files from S3

## AWS setup
- **Bucket:** `olagoke-file-storage-2026` (region `eu-north-1`)
- **Block Public Access:** ON, so the bucket is private
- **IAM user:** `cloud-storage-user`, with no console access and programmatic access only
- **IAM policy:** `S3FileStorageAccess` (least privilege, scoped to this one bucket)
  - `s3:ListBucket` on the bucket
  - `s3:GetObject`, `s3:PutObject`, `s3:DeleteObject` on the objects in the bucket

## Security practices
- A dedicated IAM user is used instead of root credentials
- Permissions follow least privilege and cover a single bucket
- Access keys are stored locally with `aws configure`, never in the code or the repo
- Public access to the bucket is blocked

## Requirements
- Python 3.8+
- An AWS account, an S3 bucket, and an IAM user with access keys

```
pip install boto3 awscli
aws configure
```

When prompted, enter your access key ID, secret access key, region (`eu-north-1`) and output format (`json`).

## Usage
1. Put `s3_manager.py` and a file called `test.txt` in the same folder.
2. Set `BUCKET` in `s3_manager.py` to your bucket name.
3. Run:

```
python s3_manager.py
```

## Example output
```
Uploaded test.txt -> s3://olagoke-file-storage-2026/test.txt
test.txt  (13 bytes)
Key:           test.txt
Size:          13 bytes
Content type:  text/plain
Last modified: 2026-11-27 01:14:03+00:00
ETag:          "688c235ddacd4955d7ca4c2a9e9ffbdd"
Downloaded s3://olagoke-file-storage-2026/test.txt -> downloaded_test.txt
```

## Functions
| Function | Purpose |
|---|---|
| `upload_file(local_path, key)` | Upload a local file to the bucket |
| `list_files()` | List objects and their sizes |
| `get_metadata(key)` | Show size, content type, last modified and ETag |
| `download_file(key, local_path)` | Download an object to the laptop |
| `delete_file(key)` | Remove an object from the bucket |

## Challenges and fixes
- **Wrong file extension:** Notepad saved the script as `s3_manager.py.txt`, so Python could not run it. I enabled file name extensions in File Explorer and removed the `.txt`.
- **Wrong content type:** the first upload showed `binary/octet-stream`. I fixed it by detecting the type with `mimetypes` and passing it as `ContentType` on upload, and the metadata now shows `text/plain`.

## Notes
Never commit your access keys, the downloaded `.csv` file, or the `~/.aws` folder to this repo.# s3-boto3-file-storage
