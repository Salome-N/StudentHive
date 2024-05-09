from sqlalchemy import Column, String, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship  # Import for relationship field
from models.base_model import BaseModel


class Hostel(BaseModel):
    """Hostel model for storing hostel information"""
    __tablename__ = 'hostel'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    owner_id = Column(Integer, ForeignKey('user.id'), nullable=False)  # Links to User model
    description = Column(Text, nullable=False)
    price = Column(Integer, nullable=False)
    city = Column(String(128), nullable=False)
    address = Column(String(256), nullable=False)
    contact_info = Column(String(128), nullable=False)

    # One-to-Many relationship with the Image model
    images = relationship("Image", backref='hostel', cascade='all, delete-orphan')

    def __init__(self, name, owner_id, description, price, city, address, contact_info):
        self.name = name
        self.owner_id = owner_id
        self.description = description
        self.price = price
        self.city = city
        self.address = address
        self.contact_info = contact_info