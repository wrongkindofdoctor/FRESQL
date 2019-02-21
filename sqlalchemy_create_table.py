#!/usr/bin/python3
# Create a base class, define classes to map each table to, and create an engine to store a sqlite3 database in your local directory
## Create a base class, define classes to map each table to, and create an engine to store a sqlite3 database in your local directory
# Example adapted from http://www.lizsander.com/programming/2015/09/08/SQLalchemy-part-2.html
from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging
# Create an engine that stores data in the local directory's sqlalchemy_example.db file.
# echo: logging module used for error messages
engine = create_engine('sqlite:///sqlalchemy_example.db',echo = True)
# Create a session to store, and later submit, the database
Session = sessionmaker(bind = engine)
session = Session()
# define basic sqlalchemy table class
Base = declarative_base()
# Define a class that the experiment table will be mapped to
# Here we define columns for the experiment name, components, layout, io_layout,
   # namelist_paths, data_file_paths
   # Notice that each column is also a normal Python instance attribute.
class Experiment(Base):
   __tablename__ = 'experiment' 
   name = Column(String(50), nullable=False, primary_key=True)
   components = Column(String(500), nullable=False)
   layout = Column(String(10), nullable=False)
   io_layout = Column(String(10), nullable=False)
   namelist_paths = Column(String(1000), nullable=False)
   data_file_paths = Column(String(1000), nullable=False)
# create the experiment table in the engine
Base.metadata.create_all(engine)
# Insert an experiment into the 'experiment' table
new_experiment = Experiment(name='mom6_double_gyre', components='mom6,shared,ocean_shared',layout='16,16',io_layout='1,1',namelist_paths='/lustre/f2/pdata/gfdl_o/some_namelist.nml', data_file_paths='/lustre/f2/pdata/gfdl_o/input_data/some_netcdf_file.nc')
# Add and commit 
session.add(new_experiment)
session.commit()
new_exp = session.query(Experiment).filter(Experiment.name == 'mom6_double_gyre')
for row in new_exp:
   print('Experiment name is:', row.name,'\n','Experiment layout is:',row.layout)

