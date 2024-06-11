from sqlalchemy import Column, ForeignKey, Integer, SmallInteger, String
from sqlalchemy.orm import relationship, validates

from database.base import Base
from utils.exceptions import InvalidRateValueError


class Cinema(Base):
    """
    A Cinema entity representing a cinema in the database.
    - Attributes:
        - id (int): The unique identifier of the cinema.
        - manager_id (int): FK(manager.id) cinema manager. nullable
        - name (int): name of the cinema.
        - rate(int): average rate of the cinema which is drieved from cinema_rates table.
    - Relationships:
        - movie: the Movie which the comment belongs to
        - user: the User which the comment belongs to
        - parent: the parent Comment
    """

    __tablename__ = 'cinemas'

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    manager_id = Column("manager_id", Integer, ForeignKey("managers.id"), default=None, nullable=True)
    name = Column("name", String(length=50), nullable=False)
    rate = Column("rate", SmallInteger, default=None)

    manager = relationship("Manager", back_populates="cinemas")

    def __repr__(self): 
        return f"<Cinema(name='{self.name}', manager='{self.manager_id}', rate='{self.rate}'>"
    

    @validates('rate')
    def validate_rate(self,value):
        if not 0 <= value <=5 :
            raise InvalidRateValueError(f'Invalid rate {value}')
        return value
    
