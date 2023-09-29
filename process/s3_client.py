import os
from functools import wraps

import boto3
from boto3 import resource
from boto3.s3.transfer import TransferConfig
from botocore.config import Config as BotoConfig


class UnboundBucketException(Exception):
    pass


def bucket_required(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.bucket_name:
            raise UnboundBucketException()
        kwargs.update({"Bucket": self.bucket_name})
        func(self, *args, **kwargs)

    return wrapper


def transfer(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        kwargs.update({"Config": self.transfer_config})
        func(self, *args, **kwargs)

    return wrapper


class S3Client:
    def __init__(
        self,
        endpoint_url=os.environ.get("S3_ENDPOINT"),
        access_key_id=os.environ.get("S3_ACCESS_ID"),
        secret_access_key=os.environ.get("S3_SECRET_KEY"),
        concurrent_upload=1,
    ):
        self.endpoint_url = endpoint_url
        self.client = boto3.client(
            "s3",
            endpoint_url=endpoint_url,
            aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key,
            config=BotoConfig(max_pool_connections=concurrent_upload),
        )
        self.resource = resource(
            "s3",
            endpoint_url=endpoint_url,
            aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key,
            config=BotoConfig(max_pool_connections=concurrent_upload),
        )
        self.transfer_config = TransferConfig(
            use_threads=True, max_concurrency=concurrent_upload
        )
        self.bucket_name = None
        self._bucket = None
        self.bind_bucket(os.environ.get("S3_BUCKET"))

    def bind_bucket(self, bucket_name):
        self.client.get_bucket_location(Bucket=bucket_name)
        self.bucket_name = bucket_name
        self._bucket = self.resource.Bucket(bucket_name)
        return self

    def unbind_bucket(self):
        self.bucket_name = None
        self._bucket = None
        return self

    @property
    def bucket(self):
        if not self._bucket:
            raise UnboundBucketException()
        return self._bucket

    @bucket_required
    def put(self, *args, **kwargs):
        return self.client.put_object(*args, **kwargs)

    @bucket_required
    @transfer
    def upload(self, *args, **kwargs):
        return self.client.upload_fileobj(*args, **kwargs)

    @bucket_required
    @transfer
    def upload_file(self, *args, **kwargs):
        return self.client.upload_file(*args, **kwargs)

    @bucket_required
    @transfer
    def download(self, *args, **kwargs):
        return self.client.download_fileobj(*args, **kwargs)
