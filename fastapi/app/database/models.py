from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column, String, DateTime , ForeignKey
from sqlalchemy.orm import relationship 
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    username = Column(String, unique=True)  # Unique constraint added here
    hashed_password = Column(String)
    posts = relationship("Post", back_populates="user")

class Post(Base):
    __tablename__ ="post"
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, nullable=False , primary_key=True, index=True )    
    created_at = Column(DateTime, default=datetime.now)
    user_id = Column(String, ForeignKey('bills.id'))
    user = relationship("User", back_populates="posts")     
    user_id =   Column(UUID, ForeignKey('user.id'))
    text = Column(String)    


