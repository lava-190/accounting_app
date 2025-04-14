# app/modules/db.py
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from datetime import datetime

# SQLite database URL
DATABASE_URL = 'sqlite:///accounting.db'
engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Define the Unit model
class Unit(Base):
    __tablename__ = 'units'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String, default='')
    current_price = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)
    # One-to-many relationship with PriceHistory
    history = relationship("PriceHistory", back_populates="unit", cascade="all, delete-orphan")

# Define the PriceHistory model
class PriceHistory(Base):
    __tablename__ = 'price_history'
    id = Column(Integer, primary_key=True)
    unit_id = Column(Integer, ForeignKey('units.id'))
    price = Column(Float, nullable=False)
    changed_at = Column(DateTime, default=datetime.utcnow)
    unit = relationship("Unit", back_populates="history")

def init_db():
    Base.metadata.create_all(engine)

def get_all_units():
    session = Session()
    results = session.query(Unit).all()
    units_list = []
    for unit in results:
        units_list.append({
            'id': unit.id,
            'name': unit.name,
            'category': unit.category,
            'current_price': unit.current_price,
            'history': [{'price': h.price, 'changed_at': h.changed_at.isoformat()} for h in unit.history]
        })
    session.close()
    return units_list

def add_unit(data):
    session = Session()
    unit = Unit(
        name=data['name'],
        category=data.get('category', ''),
        current_price=data.get('current_price', 0.0)
    )
    session.add(unit)
    session.commit()
    # Create the initial price record
    ph = PriceHistory(unit_id=unit.id, price=unit.current_price)
    session.add(ph)
    session.commit()
    session.close()

def update_unit(data):
    session = Session()
    unit = session.query(Unit).filter_by(id=data['id']).first()
    if unit:
        if 'name' in data:
            unit.name = data['name']
        if 'category' in data:
            unit.category = data['category']
        if 'current_price' in data:
            unit.current_price = data['current_price']
            ph = PriceHistory(unit_id=unit.id, price=unit.current_price)
            session.add(ph)
        session.commit()
    session.close()

def delete_unit(unit_id):
    session = Session()
    unit = session.query(Unit).filter_by(id=unit_id).first()
    if unit:
        session.delete(unit)
        session.commit()
    session.close()
