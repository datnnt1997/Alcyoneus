from sqlalchemy import create_engine
from sqlalchemy import distinct
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from settings import DB_URI_MYSQL, DB_POOL_SIZE
from citadel.models import Source, Decryption


engine_mysql = create_engine(DB_URI_MYSQL, pool_size=DB_POOL_SIZE, max_overflow=0)
db_session_mysql = sessionmaker(bind=engine_mysql, autocommit=True)


def get_source_decrption(domain):
    session = db_session_mysql()
    try:
        result = session.query(Decryption).join(Source).filter(Source.domain == domain).first()
        return result
    finally:
        session.close()
