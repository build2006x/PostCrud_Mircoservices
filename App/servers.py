from App.database import Blog,find
from App.schema import Vaild 
from sqlalchemy.orm import Session
from passlib.context import CryptContext

#hashing the username in the db

def hash_password(username):
    bcrypt = CryptContext(schemes=['bcrypt'],deprecated='auto')
    return bcrypt.hash(username)

#here i seprated my server of the like query i done on the table to do the operation
#get post 

def get_post(db:Session):
   return  db.query(Blog).all()

#post request 

def add_blog(data:Vaild,db:Session):
   addBlogs = Blog(
      username = data.username,
      title = data.title,
      description = data.description
   )
   db.add(addBlogs)
   db.commit()
   return data


def delete_post(id:int,db:Session):
   blog_del = db.query(Blog).filter(Blog.ids == int(id)).first()
   db.delete(blog_del)
   db.commit()
   return blog_del


def update_details(id,data,db:Session):
   update_data = db.query(Blog).filter(Blog.ids == id).first()
   if not update_data:
      return {"error": "Blog post not found"}
   update_data.username = data.username
   update_data.title    = data.title
   update_data.description   = data.description
   db.commit()
   return data


