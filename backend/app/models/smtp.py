from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text
from sqlalchemy.sql import func
from app.db.base import Base

class SMTPAccount(Base):
    __tablename__ = "smtp_accounts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, doc="Friendly label for this SMTP")
    host = Column(String, nullable=False)
    port = Column(Integer, nullable=False)
    username = Column(String, nullable=False)
    encrypted_password = Column(String, nullable=False)
    
    # Security: TLS, SSL, NONE
    security = Column(String, default="TLS")
    
    is_active = Column(Boolean, default=True)
    
    # Audit fields
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())