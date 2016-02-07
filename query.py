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
brand_id_8 = Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
corvettes = Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()

# Get all models that are older than 1960.
old_cars = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
new_brands = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
model_names = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
not_discontinued = Brand.query.filter(Brand.founded == 1903,
                                      Brand.discontinued.is_(None))
not_discontinued = not_discontinued.all()

# Get all brands with that are either discontinued or founded before 1950.
brands = Brand.query.filter((Brand.discontinued.isnot(None)|
                             (Brand.founded < 1950))).all()

# Get any model whose brand_name is not Chevrolet.
not_chevie = Model.query.filter(Model.brand_name != 'Chevrolet').all()

# ==== Discussion questions:
# What is the returned value and datatype of Brand.query.filter_by(name='Ford')?
    # This method returns 'flask_sqlalchemy.BaseQuery' object. This object's
    # value is the query wherein the brand name is equal to 'Ford'. 
# In your own words, what is an association table, and what type of relationship
# (many to one, many to many, one to one, etc.) does an association
# table manage?
    # An association table is used when you have two related concepts in which
    # there is a meny-to-meny relationship. If we wanted to keep
    # track of which authors wrote which books and we had a table of books,
    # a table for authors, and a table which kept track of each unique
    # author/book contination, then the latter table would be an assocation
    # table. In the example the association table is only keeping track of the
    # relationship between authors and books (as one book can have more than
    # one author), and nothing else.

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    pass

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    pass

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
