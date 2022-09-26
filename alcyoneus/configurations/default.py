import os

# CITADEL configurations
MYSQL_USER: str = os.getenv('MYSQL_USER', 'admin')
MYSQL_PASS: str = os.getenv('MYSQL_PASS', 'admin')
MYSQL_HOST: str = os.getenv('MYSQL_HOST', '0.0.0.0')
MYSQL_PORT: str = os.getenv('MYSQL_PORT', '3308')
MYSQL_DB: str = os.getenv('MYSQL_DB', 'citadel')
DB_URI_MYSQL: str = f'mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASS}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}?charset=utf8'
DB_POOL_SIZE: int = os.getenv('DB_POOL_SIZE', 5)
