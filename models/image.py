from sqlalchemy import Column, String, ForeignKey, Integer
from models.base_model import BaseModel

class Image(BaseModel):
    """Image model for storing hostel images"""
    __tablename__ = 'image'
    id = Column(Integer, primary_key=True)
    image_url = Column(String(256), nullable=False)  # URL or path to the image file
    hostel_id = Column(Integer, ForeignKey('hostel.id'), nullable=False)  # Links to Hostel model

    def __init__(self, image_url, hostel_id):
        self.image_url = image_url
        self.hostel_id = hostel_id