from invoke import task
import os
import shutil
import sys

SETTINGS_FILE_BASE = 'pelicanconf.py'
SETTINGS_FILE_PUBLISH = 'publishconf.py'

CONFIG = {
    'settings_base': SETTINGS_FILE_BASE,
    'settings_publish': SETTINGS_FILE_PUBLISH,
    # 'deploy_path': 'output',
    # 's3_bucket': 'your-s3-bucket-name',
}

@task
def clean(c):
    """Remove generated files"""
    if os.path.isdir('output'):
        shutil.rmtree('output')
        os.makedirs('output')

@task
def build(c):
    """Build local version of site"""
    c.run('pelican -s {settings_base}'.format(**CONFIG))

@task
def rebuild(c):
    """Full rebuild of local version of site"""
    clean(c)
    build(c)

@task
def publish(c):
    """Build publish version of site"""
    c.run('pelican -s {settings_publish}'.format(**CONFIG))

@task
def s3_upload(c, bucket_name=None):
    """Upload the site to S3"""
    if not bucket_name:
        print("Please provide a bucket name: invoke s3_upload --bucket-name=my-bucket")
        return
    publish(c)
    c.run('aws s3 sync output/ s3://{0} --acl public-read --delete'.format(bucket_name))

@task
def serve(c):
    """Serve site at http://localhost:8000"""
    c.run('pelican --listen')
