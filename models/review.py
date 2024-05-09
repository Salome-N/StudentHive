from sqlalchemy import Column, Integer, String, ForeignKey, Text
from models.base_model import BaseModel

class Review(BaseModel):
    """Review model for storing user reviews for hostels"""
    __tablename__ = 'review'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)  # Links to User model
    hostel_id = Column(Integer, ForeignKey('hostel.id'), nullable=False)  # Links to Hostel model
    rating = Column(Integer, nullable=False)  # Rating (e.g., 1-5)
    content = Column(Text, nullable=False)

    def __init__(self, author_id, hostel_id, rating, content):
        self.author_id = author_id
        self.hostel_id = hostel_id
        self.rating = rating
        self.content = content