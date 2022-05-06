#  Date: 2021.03.01
#  Author: dharapx
#  Feel free to use this code
#  ------------------------------------------------------------------------------------------------
# This is an API. which are having four end points to perform the CRUD operation with SQLite
#  ------------------------------------------------------------------------------------------------
from typing import List

import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import methods
import model
import schema
from db_handler import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

# initiating app
app = FastAPI(
    title="Address Book Application",
    description="Use address book app by using this API",
    version="1.0.0"
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/retrieve_all_address_details', response_model=List[schema.Address])
def retrieve_all_Address_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    address = methods.get_address(db=db, skip=skip, limit=limit)
    return address


@app.post('/add_new_address', response_model=schema.AddressAdd)
def add_new_address(address: schema.AddressAdd, db: Session = Depends(get_db)):
    address_data = methods.get_address_by_lat_long(db=db, latitude=address.latitude, longitude=address.longitude)
    if address_data:
        raise HTTPException(status_code=400, detail=f"Latitude {address.latitude}"
              f" and Lonitude {address.longitude} already exist in database")
    return methods.add_address_details_to_db(db=db, address=address)


@app.delete('/delete_address_by_id')
def delete_address_by_id(sl_id: int, db: Session = Depends(get_db)):
    details = methods.get_address_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to delete")

    try:
        methods.delete_address_details_by_id(db=db, sl_id=sl_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}


@app.put('/update_address_details', response_model=schema.Address)
def update_address_details(sl_id: int, update_param: schema.UpdateAddress, db: Session = Depends(get_db)):
    details = methods.get_address_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to update")

    return methods.update_address_details(db=db, details=update_param, sl_id=sl_id)