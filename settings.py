import os

# Flask settings
FLASK_DEBUG = True  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/curator_task_manager"
SQLALCHEMY_BINDS = "" 
SQLALCHEMY_TRACK_MODIFICATIONS = False

MOUNT_POINT_PROBIO = '/data/PROBIO/'
MOUNT_POINT_PSFF = '/data/PSFF/'
MOUNT_REF_GENOME_PATH = '/nfs/PROBIO/autoseq-genome/autoseq-genome.json'
MOUNT_LIB_PATH = '/nfs/PROBIO/INBOX'
MOUNT_SCRATCH_PATH = '/scratch/tmp/liqbio-tmp/'