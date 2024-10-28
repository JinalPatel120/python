from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Date ,func,DateTime,Float,Text
from sqlalchemy.orm import relationship
from .database import Base ,engine

Base.metadata.create_all(bind=engine)

class Symbol(Base):
    __tablename__ = "symbols"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True)
    ticker = Column(String(255))
    series = Column(String(16))
    date_listing = Column(Date)
    paid_value = Column(Integer,server_default = "0")
    market_lot = Column(Integer)
    isin_number = Column(String(255),server_default = "")
    face_value = Column(Integer,server_default = "0")
    category=Column(String(255),default='NSE')
    
  
    
class HistoricalData(Base):
    __tablename__ = 'historical_data'

    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, nullable=False)
    open = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    volume=Column(Float, nullable=False)
    instrument_token = Column(Integer, nullable=False) 
    symbol_id = Column(Integer, ForeignKey('symbols.id'), nullable=False)  # Foreign key reference to Symbol
    symbol= Column(String(255),ForeignKey('symbols.name'),nullable=False) 


