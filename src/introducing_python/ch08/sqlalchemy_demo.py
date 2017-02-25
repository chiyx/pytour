#! /usr/bin/env python3
# coding = utf-8

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

conn = sa.create_engine('sqlite:///zoo.db')
Base = declarative_base()


class Zoo(Base):
    __tablename__ = 'zoo'
    critter = sa.Column('critter', sa.String, primary_key=True)
    count = sa.Column('count', sa.Integer)
    damages = sa.Column('damages', sa.Float)

    def __init__(self, critter, count, damages):
        self.critter = critter
        self.count = count
        self.damages = damages

    def __repr__(self):
        return "<Zoo({}, {}, {}) >".format(self.critter,
                                           self.count, self.damages)

Base.metadata.create_all(conn)
# data
first = Zoo('duck', 10, 0.0)
second = Zoo('bear', 2, 1000.0)
third = Zoo('weasel', 1, 2000.0)

Session = sessionmaker(bind=conn)
session = Session()
session.add_all([first, second, third])
session.commit()


# meta = sa.MetaData()
# zoo = sa.Table('zoo', meta,
#                sa.Column('critter', sa.String, primary_key=True),
#                sa.Column('count', sa.Integer),
#                sa.Column('damages', sa.Float)
#                )
# meta.create_all(conn)
# conn.execute(zoo.insert(
#     ('bear', 2, 1000.0)
# ))
# conn.execute(zoo.insert(
#     ('weasel', 1, 2000.0)
# ))
# conn.execute(zoo.insert(
#     ('duck', 10, 0)
# ))
# result = conn.execute(zoo.select())
# rows = result.fetchall()
# print(rows)
