#!/usr/bin/python3
# Create a base class, define classes to map each table to, and create an engine to store a sqlite3 database in your local directory
# Example adapted from https://www.blog.pythonlibrary.org/2010/09/10/sqlalchemy-connecting-to-pre-existing-databases/
from sqlalchemy import Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Describe database tables, then by define classes which will be mapped to those tables. In modern SQLAlchemy, these two tasks are usually performed together, using a system known as Declarative that include directives to describe the actual database table they will be mapped to.
# Create an engine that stores data in the local directory's sqlalchemy_example.db file.
engine = create_engine('sqlite:///sqlalchemy_example.db')
# Create the base class
Base = declarative_base()
# Define a class that the experiment table will be mapped to
class experiment(Base):
   __tablename__ = 'new_experiment'
   # Here we define columns for the experiment name, components, layout, io_layout,
   # namelist_paths, data_file_paths
   # Notice that each column is also a normal Python instance attribute.
   name = Column(String(50), nullable=False, primary_key=True)
   components = Column(String(500), nullable=False) # comma-separated list of components ‘mom6, shared, ocean_shared’
   layout = Column(String(10), nullable=False)
   io_layout = Column(String(10), default='1,1') # e.g., '1,1'
   namelist_paths = Column(String(1000)) # comma-separated list of paths
   data_file_paths = Column(String(1000)) # comma-separated list of paths
# define constructor to allow the class to initialize the experiment attributes
   def __init__(self, name, components,layout,io_layout,namelist_paths, data_file_paths):
      self.name = name
      self.components = components
      self.layout = layout
      self.io_layout = io_layout
      self.namelist_paths = namelist_paths
      self.data_file_paths = data_file_paths
# define constructor to return printable representation of the experiment object
   def __repr__(self):
      return "<Experiment: '%s', '%s', '%s','%s','%s','%s'>" % (self.name, self.components,self.layout, self.io_layout, self.namelist_paths, self.data_file_paths)
#
def loadSession():
   metadata = Base.metadata
   Session = sessionmaker(bind=engine)
   session = Session()
   return session
#
if __name__ == "__main__":
   session = loadSession()
   res = session.query(experiment).all()
   print(res[1].name)
