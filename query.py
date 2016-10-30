"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries

# Get the brand with the **id** of 8.
Brand.query.get(8)
# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter(Model.name == 'Corvette', Model.brand_name == 'Chevrolet').all()
# Get all models that are older than 1960.
Model.query.filter(Model.year < 1960).all()
# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded >1920).all()
# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()
# Get all brands that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()
# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
Brand.query.filter((Brand.discontinued.isnot(None))|(Brand.founded < 1950)).all()
# Get all models whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != 'Chevrolet').all()
# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''
    mdls = Model.query.options(db.joinedload('brands')).all()

    for model in mdls:
        if model.year == year:
        print model.name, model.brand.name, model.brand.headquarters

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''
    mdls = Model.query.options(db.joinedload('brands')).all()
    display = {}

# I feel like there should be a way to incorporporate group_by in the query 
# and run loops for each brand name, but I couldn't get the composition right.
# Dictionaries to the rescue!
    for model in mdls:
# Feed the query into a dictionary with brandname keys and sets of 
# models for values (to kill redundancy) str() because everything is Unicode
         display.setdefault(str(model.brand_name),{str(model.name)})
         display[str(model.brand_name)].add(str(model.name))
#Print a readable list
    for key, value in display.iteritems():
         print "\n" + key
         for item in value:
             print " * " + item

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?
# 
# <flask_sqlalchemy.BaseQuery at 0x7fbb0c15d0d0>
# type is flask_sqlalchemy.BaseQuery  Soooo: it's a BaseQuery object. Our query 
# is a query.
#
# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?
#
# Association tables manage many to many relationships. Minimally, they hold 
# fields for a foreign keyed field from each of the tables it's associating, 
# allowing rows in each of the associated tables to be referenced and maintaining 
# the referential integrity of the database.

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
#works for perfect case matches
    Brand.query.filter.((Brand.name.like(mystr + '%'))|(Brand.name.like('%' + mystr + '%'))|(Brand.name.like('%' + mystr))|(Brand.name == mystr)).all()

def get_models_between(start_year, end_year):
    Model.query.filter(Model.year > start_year, Model.year < end_year).all()
