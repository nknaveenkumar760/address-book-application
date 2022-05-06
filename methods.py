#  -------------------------------------------------------------------------------
#  Here we are having methods for API
#  -------------------------------------------------------------------------------

from sqlalchemy.orm import Session
import model
import schema


def get_address(db: Session, skip: int = 0, limit: int = 100):
    """
    This method will return address details
    :param limit:
    :param skip:
    :param db: database session object
    :return: data row if exist else None
    """

    return db.query(model.Address).offset(skip).limit(limit).all()


def get_address_by_lat_long(db: Session, latitude: float, longitude: float):
    """
    This method will return address details
    :param longitude:
    :param latitude:
    :param db: database session object
    :return: data row if exist else None
    """

    return db.query(model.Address).filter(model.Address.latitude == latitude, model.Address.longitude == longitude).first()


def add_address_details_to_db(db: Session, address: schema.AddressAdd):
    """
    this method will add a new record to database. and perform the commit and refresh operation to db
    :param address:
    :param db: database session object
    :return: a dictionary object of the record which has inserted
    """
    address_details = model.Address(
        latitude=address.latitude,
        longitude=address.longitude,
    )
    db.add(address_details)
    db.commit()
    db.refresh(address_details)
    return model.Address(**address.dict())


def update_address_details(db: Session, sl_id: int, details: schema.UpdateAddress):
    """
    this method will update the database
    :param db: database session object
    :param sl_id: serial id of record or Primary Key
    :param details: Object of class schema.UpdateAddress
    :return: updated address record
    """
    db.query(model.Address).filter(model.Address.id == sl_id).update(vars(details))
    db.commit()
    return db.query(model.Address).filter(model.Address.id == sl_id).first()


def get_address_by_id(db: Session, sl_id: int):
    """
    This will delete the record from database based on primary key
    :param sl_id: serial id of record or Primary Key
    :param db: database session object
    :return: None
    """
    try:
        db.query(model.Address).filter(model.Address.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)


def delete_address_details_by_id(db: Session, sl_id: int):
    """
    This will delete the record from database based on primary key
    :param db: database session object
    :param sl_id: serial id of record or Primary Key
    :return: None
    """
    try:
        db.query(model.Address).filter(model.Address.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)
