#app.tasks
from fastapi import HTTPException
from kiteconnect import KiteConnect
from sqlalchemy.orm import Session
import time
from dotenv import load_dotenv
import os
from .models import Symbol,HistoricalData
import pandas as pd
import logging
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

from datetime import datetime
from datetime import timedelta

load_dotenv()

API_KEY = os.getenv('KITE_API_KEY')
API_SECRET = os.getenv('KITE_API_SECRET')
ACCESS_TOKEN=os.getenv('KITE_ACCESS_TOKEN')
kite = KiteConnect(api_key=API_KEY,access_token=ACCESS_TOKEN)



db_name = os.getenv('DB_NAME')
db_pass = os.getenv('DB_PASS')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_user = os.getenv('DB_USER')

# Database setup
DATABASE_URL = f"mysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
engine = create_engine(DATABASE_URL)
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_symbols():
    db:Session=SessionLocal()
    try: 
        query=db.query(Symbol)
        db_symbols = query.all()
        symbols = [ stock.name for stock in db_symbols]
        symbol_dict = [{stock.name:stock.id} for stock in db_symbols]
        return symbols
    finally:
        db.close()      
    
def get_instrument_tokens(symbols):
        instruments = kite.instruments("NSE")
        instrument_tokens = {}
        for instrument in instruments:
            if instrument['tradingsymbol'] in symbols:
                instrument_tokens[instrument['tradingsymbol']] = instrument['instrument_token']
        return instrument_tokens

@celery_app.task
def fetch_historical_data_task():
    db: Session = SessionLocal()  # Create a new database session
    try:
        # Fetch symbols and get instrument tokens
        logger.info("Fetching symbols from database. and access token",ACCESS_TOKEN)
        print("access token from env",ACCESS_TOKEN)
        symbols = fetch_symbols()
        instrument_token = get_instrument_tokens(symbols)
        start_date = datetime.now() - timedelta(days=365)
        end_date = datetime.now()
        logger.info(f"Requesting historical data for {len(symbols)} symbols.")        
        data = []
        logger.info(f"Number of symbols: {len(symbols)}")
        for symbol, token in instrument_token.items():
            print('helo jinal'.__len__())
            try:
                time.sleep(0.05)  
                historical_data = kite.historical_data(
                        instrument_token=token,
                        from_date=start_date,
                        to_date=end_date,
                        interval='day'
                    )    
                if historical_data:
                        records = [HistoricalData(
                                symbol=symbol,
                                date=row['date'],
                                open=row['open'],
                                high=row['high'],
                                low=row['low'],
                                close=row['close'],
                                volume=row['volume'],
                                instrument_token=token,
                                symbol_id = db.query(Symbol).filter_by(name=symbol).first().id
                                )
                             for row in historical_data]
                        if records:                           
                            data.extend(records)               
            except Exception as e:
                logger.error(f"Error fetching historical data: {e}")
                continue 
       
        print("hello from outside loop")
        logger.info("Reached the end of symbol processing loop.")
        logger.info(f"data is here: {data}")
       
        if data:
            db.bulk_save_objects(data)
            db.commit()
            logger.info(f"Data fetch and insertion complete. Inserted {len(data)} records.")
        else:
            logger.info('no data was inserted')

    except Exception as e:
        logger.error(f"General error occurred: {e}")
        
    finally:
        db.close() 
