from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Job Post Model
class JobPost(BaseModel):
    company_name: str
    job_title: str
    industry: str
    job_description: str
    experience: int
    package_upto: float
    skills: List[str]
    location: str
    job_type: str
    email: str

# In-memory storage for job posts
job_posts = []

@app.post("/jobs/", response_model=JobPost, status_code=201)
def create_job_post(job_post: JobPost):
    job_posts.append(job_post)
    return job_post

@app.get("/", response_model=List[JobPost])
def get_job_posts():
    return job_posts

@app.get("/jobs/{job_id}", response_model=JobPost)
def get_job_post(job_id: int):
    if job_id < 0 or job_id >= len(job_posts):
        raise HTTPException(status_code=404, detail="Job post not found")
    return job_posts[job_id]

@app.put("/jobs/{job_id}", response_model=JobPost)
def update_job_post(job_id: int, updated_job_post: JobPost):
    if job_id < 0 or job_id >= len(job_posts):
        raise HTTPException(status_code=404, detail="Job post not found")
    job_posts[job_id] = updated_job_post
    return updated_job_post

@app.delete("/jobs/{job_id}", status_code=204)
def delete_job_post(job_id: int):
    if job_id < 0 or job_id >= len(job_posts):
        raise HTTPException(status_code=404, detail="Job post not found")
    job_posts.pop(job_id)
