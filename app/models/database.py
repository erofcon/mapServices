from os import environ
import databases

DB_NAME = environ.get('DB_NAME', 'test_db')
DB_USER = environ.get('DB_USER', 'admin')
DB_PASS = environ.get('DB_PASS', 'admin')
DB_HOST = environ.get('DB_HOST', '127.0.0.1')

SQLALCHEMY_DATABASE_URL = f'postgres://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}'

REMOTE_DATABASE_URL = "postgresql://tamirlan:Gls22058@192.168.1.252/vms_ws"

local_database = databases.Database(url=SQLALCHEMY_DATABASE_URL)
remote_database = databases.Database(url=REMOTE_DATABASE_URL)
