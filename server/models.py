from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class Sweet(db.Model, SerializerMixin):
    __tablename__ = 'sweets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    # Add relationship
    vendor_sweets = db.relationship('VendorSweet',back_populates='sweet', cascade='all, delete-orphan')
    vendors = association_proxy('vendor_sweets','vendor' ,creator=lambda vendor_obj: VendorSweet(vendor=vendor_obj))
    # Add serialization
    # serialize_rules =('-vendor_sweets.sweet',)
    serialize_only=('id','name')
    
    def __repr__(self):
        return f'<Sweet {self.id}>'


class Vendor(db.Model, SerializerMixin):
    __tablename__ = 'vendors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    # Add relationship
    vendor_sweets = db.relationship('VendorSweet',back_populates='vendor', cascade='all, delete-orphan')
    sweets = association_proxy('vendor_sweets','sweet' ,creator=lambda sweet_obj: VendorSweet(sweet=sweet_obj))
    # Add serialization
    serialize_rules=('-vendor_sweets.vendor',)

    def __repr__(self):
        return f'<Vendor {self.id}>'


class VendorSweet(db.Model, SerializerMixin):
    __tablename__ = 'vendor_sweets'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)

    # Add relationships
    sweet_id = db.Column(db.Integer,db.ForeignKey('sweets.id'))
    vendor_id = db.Column(db.Integer,db.ForeignKey('vendors.id'))
    sweet = db.relationship('Sweet', back_populates='vendor_sweets')
    vendor = db.relationship('Vendor',back_populates='vendor_sweets')
    # Add serialization
    serialize_rules = ('-sweet.vendor_sweets','-vendor.vendor_sweets')
    # Add validation
    @validates('price')
    def validate_price(self,key,price):
        if price and not price < 0:
            return price
        return ValueError('Provide price greater than 0')

    def __repr__(self):
        return f'<VendorSweet {self.id}>'
