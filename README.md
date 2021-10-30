# ViT Terraform FastAPI ECS Deployment

## Setup

`git clone <repo>`

### Run Dockerized FastAPI Locally

`docker build -t vit-fastapi .`

`docker run -p 80:80 vit-fastapi:latest`

Go to localhost:80/docs to test interactive api.

## Random notes and ideas while under construction

RUN python -c 'from sentence_transformers import SentenceTransformer; SentenceTransformer("<model-name>")'

## References

[1](https://radix.ai/blog/2020/12/swiftly-writing-and-deploying-apis-to-stay-agile/)
