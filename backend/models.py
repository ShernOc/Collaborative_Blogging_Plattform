from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates 

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

#User
class User(db.Model):
    __tablename__ = "users"
    #User table 
    
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(128), nullable = False)
    password = db.Column(db.String(128), nullable = False)
    is_admin = db.Column(db.Boolean, default = False)
    
    #relationship 
    
    
    #validation 
@validates("email")
def validate_email(self,key,email):
    if "@" not in email: 
        raise ValueError("Failed to load your email")
    return 

class Blog(db.Model):
    __tablename__= "blogs"
    
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(10), nullable = False )
    description = db.Column(db.String(256), nullable = False)
    editors = db.Column(db.)
    
    

#hint: if not saved local storage: save the project in the local storage 

# Collaborate on Blog: As a user, I want to invite other users to collaborate on my blog post.

    
    
    
#Blog
#Collaboration 
#Comment 


# A User can write a Comment of a Blog 


#Being able to 


# A User being able to publish the blog 

