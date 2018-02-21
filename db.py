# PRODUCTS = [
#     {'title': 'Macbook Air 2015',
#      'price_rup' : 80500,'product_image':'/images/iphone.jpg',
#      'in_store': True},
#     {
#         'title': 'iphone X',
#         'price_rup' : 80500,
#         'product_image':'/images/iphone.jpg',
#         'in_store': True
#     },
#     {'title': 'iphone X',
#         'price_rup' : 80500,
#         'product_image':'/images/iphone.jpg',
#         'in_store': False
#     }
# ]
#
#
#

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db.sqlite')
Base = declarative_base()
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    price_rub = Column(Integer)
    product_image = Column(String)
    in_store = Column(Boolean)


def create_demo_products():

    products_info = [
        {'title': 'Macbook Air 2015',
         'price_rup' : 80500,'product_image':'/images/iphone.jpg',
         'in_store': True},
        {
            'title': 'iphone X',
            'price_rup' : 80500,
            'product_image':'/images/iphone.jpg',
            'in_store': True
        },
        {'title': 'iphone X',
            'price_rup' : 80500,
            'product_image':'/images/iphone.jpg',
            'in_store': False
        }
    ]

    session = Session()
    for product_info in products_info:

        product = Product()
        product.title = product_info['title']
        product.product_image = product_info['product_image']
        product.price_rup = product_info['price_rup']
        product.in_store = product_info['in_store']
        session.add(product)
    session.commit()


def create_all_tables():
    Base.metadata.create_all(engine)


if __name__== "__main__":
    create_all_tables()
    create_demo_products()



