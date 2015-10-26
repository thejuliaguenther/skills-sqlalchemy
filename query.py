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
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.

Brand.query.filter(Brand.id == 8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

Brand.query.filter((Model.name == 'Corvette') & (Model.brand_name == 'Chevrolet')

# Get all models that are older than 1960.

Model.query.filter(Model.year < 1960)

# Get all brands that were founded after 1920.

Brand.query.filter(Brand.founded > 1920)

# Get all models with names that begin with "Cor".

Model.query.filter(Model.name.like('Cor%'))

# Get all brands with that were founded in 1903 and that are not yet discontinued.

Brand.query.filter((Brand.founded == 1903) & ( Brand.discontinued == None))

# Get all brands with that are either discontinued or founded before 1950.

Brand.query.filter((Brand.founded <= 1950) | ( Brand.discontinued !=None))

# Get any model whose brand_name is not Chevrolet.

Model.query.filter(Model.brand_name != 'Chevrolet')

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''
    model_info = db.session.query(Model.name, Model.brand_name, Brand.headquaters).filter(Model.year == year)
    
    return model_info

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

     brand_models= db.session.query(Model.brand_name, Model.name)
     return brand_models

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    brands_with_mystr = db.session.query((Brand.name == mystr) | (Brand.name.like('%'+mystr+'%')))
    return brands_with_mystr


def get_models_between(start_year, end_year):
    
    models_between = db.session.query((Model.year > start_year) & (Model.year < end_year))
    return models_between

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

Right now, this returns an object at the address 0x103645710. However, the SQL that this 
statement creates (SELECT * FROM Brands WHERE name = 'Ford';)will return the object 
"1|Ford|1903|Dearborn, MI". 

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

Association tables help illustrate many-to-many relationships and exist only to 
connect tables together.
