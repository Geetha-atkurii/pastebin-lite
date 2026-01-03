from sqlalchemy import Column, String, Integer, Text
from app.database import Base

class Paste(Base):
    __tablename__ = "pastes"

    id = Column(String, primary_key=True, index=True)
    content = Column(Text, nullable=False)

    created_at = Column(Integer, nullable=False)
    expires_at = Column(Integer, nullable=True)

    max_views = Column(Integer, nullable=True)
    views = Column(Integer, nullable=False, default=0)
