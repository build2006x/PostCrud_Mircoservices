from pydantic import BaseModel
from typing import Optional
#pydantic vaildation for the user input we get from the user input 
#pydantic is data vaildataion purpose usecase 

class Vaild(BaseModel):
     ids:int
     username:str
     title:str
     description:str 

class post_vaild(Vaild):
      id:Optional[int] = None
      username:str
      title:str
      description:str

class delete(BaseModel):
     id:int 
     



