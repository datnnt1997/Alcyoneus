# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String, text, JSON, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


Base.to_dict = to_dict


class Channel(Base):
    __tablename__ = 'channel'

    chid = Column(Integer, primary_key=True)
    chname = Column(String(50))
    domain = Column(String(20), unique=True)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    # Relationships
    source = relationship('Source')


class Source(Base):
    __tablename__ = 'source'

    sid = Column(Integer, primary_key=True)
    chid = Column(Integer, ForeignKey("channel.chid"))
    sname = Column(String(50))
    domain = Column(String(20), unique=True)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))

    # Relationships
    message = relationship('CosmicMessage')
    decryption = relationship('Decryption')


class Category(Base):
    __tablename__ = 'category'

    cid = Column(Integer, primary_key=True)
    cname = Column(String(50))
    domain = Column(String(20), unique=True)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    delete_time = Column(DateTime, server_default=None)

    # Relationships
    message = relationship('CosmicMessage')


class Decryption(Base):
    __tablename__ = 'decryption'

    did = Column(Integer, primary_key=True)
    sid = Column(Integer, ForeignKey("source.sid"))
    start_url = Column(String(512), nullable=False)
    pagination = Column(String(512), nullable=False)
    article_url = Column(String(512), nullable=False)
    category = Column(String(512), nullable=False)
    title = Column(String(512), server_default=None)
    author = Column(String(512), server_default=None)
    tags = Column(String(512), server_default=None)
    description = Column(String(512), server_default=None)
    content = Column(String(512), server_default=None)
    media = Column(String(512), server_default=None)
    pub_time = Column(String(512), server_default=None)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class CosmicMessage(Base):
    __tablename__ = 'cosmic_message'

    mid = Column(Integer, primary_key=True)
    sid = Column(Integer, ForeignKey("source.sid"))
    cid = Column(Integer, ForeignKey("category.cid"))
    url = Column(String(50), index=True, nullable=False)
    title = Column(String(100), index=True, server_default=None)
    author = Column(String(100), server_default=None)
    tags = Column(String(100), server_default=None)
    description = Column(String(500), server_default=None)
    content = Column(String, server_default=None)
    media = Column(JSON, server_default=None)
    pub_time = Column(DateTime, index=True, server_default=None)
    create_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    update_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    delete_time = Column(DateTime, server_default=None)



