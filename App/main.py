from App.schema import Vaild,post_vaild
from fastapi import FastAPI ,Depends
from fastapi.middleware.cors import CORSMiddleware
from App import servers
from App.database import get_db
from sqlalchemy.orm import Session

app = FastAPI()

#middleware for task handling during the request repsone cycle during client and server 

origins = "http://localhost:5173"

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or specific domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#endpoint for the curd operation of the blog posts


#endpoint for getting the info from the db

@app.get('/get_blogs')
async def get_info(db:Session=Depends(get_db)):
    return servers.get_post(db)

#endpoint for creating a new post 

@app.post('/newpost')
async def new_post(data:post_vaild,db:Session=Depends(get_db)):
    return servers.add_blog(data,db)

#endpoint for the backend delete operation 

@app.delete('/delete/{id}')
async def remove_post(id:int,db:Session=Depends(get_db)):
    return servers.delete_post(id,db)


#endpoint for the updating the blog posts 

@app.put('/update/{id}')
async def update_post(id:int,data:post_vaild,db:Session=Depends(get_db)):
    return servers.update_details(id,data,db)