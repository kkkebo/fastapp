from datetime import datetime
from sqlalchemy import Column, Integer, Float, String, Boolean, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship


from ..db_setup import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer, nullable=False)
    category = Column(String(200), nullable=False)
    gender = Column(String(100), nullable=False)

    interaction = relationship("Interaction", back_populates="owner") # связь, узнать по-точнее
    embedding = relationship("Embedding", back_populates="user")

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    news_url = Column(String, nullable=True)
    category = Column(String(200), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    feature_0 = Column(Text, nullable=False)  # Узнать какой тип данных будет у feature!
    feature_1 = Column(Text, nullable=False)

    interaction = relationship("Interaction", back_populates="news")


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    news_id = Column(Integer, ForeignKey("news.id"), nullable=False)
    created_at = Column(String, nullable=False)
    reaction = Column(Boolean)  # like/ dislike boolean или нет?

    owner = relationship("User", back_populates="interaction")
    news = relationship("News", back_populates="interaction")


class Embedding(Base):
    __tablename__ = "embeddings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    feature0 = Column(Float, nullable=False)
    feature1 = Column(Float, nullable=False)
    feature2 = Column(Float, nullable=False)
    feature3 = Column(Float, nullable=False)
    feature4 = Column(Float, nullable=False)
    feature5 = Column(Float, nullable=False)
    feature6 = Column(Float, nullable=False)
    feature7 = Column(Float, nullable=False)
    feature8 = Column(Float, nullable=False)
    feature9 = Column(Float, nullable=False)
    feature10 = Column(Float, nullable=False)
    feature11 = Column(Float, nullable=False)
    feature12 = Column(Float, nullable=False)
    feature13 = Column(Float, nullable=False)
    feature14 = Column(Float, nullable=False)
    feature15 = Column(Float, nullable=False)
    feature16 = Column(Float, nullable=False)
    feature17 = Column(Float, nullable=False)
    feature18 = Column(Float, nullable=False)
    feature19 = Column(Float, nullable=False)
    feature20 = Column(Float, nullable=False)
    feature21 = Column(Float, nullable=False)
    feature22 = Column(Float, nullable=False)
    feature23 = Column(Float, nullable=False)
    feature24 = Column(Float, nullable=False)
    feature25 = Column(Float, nullable=False)
    feature26 = Column(Float, nullable=False)
    feature27 = Column(Float, nullable=False)
    feature28 = Column(Float, nullable=False)
    feature29 = Column(Float, nullable=False)
    feature30 = Column(Float, nullable=False)
    feature31 = Column(Float, nullable=False)
    feature32 = Column(Float, nullable=False)

    user = relationship("User", back_populates="embedding")
