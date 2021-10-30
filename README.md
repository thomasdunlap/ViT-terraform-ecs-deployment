# ViT Terraform FastAPI ECS Deployment

## Setup

`git clone <repo>`

### Run Dockerized FastAPI Locally

`docker build -t vit-fastapi -f Dockerfile.local .`

`docker run -p 80:80 vit-fastapi:latest`

Go to localhost:80/docs to test interactive api.

## Random notes and ideas while under construction

RUN python -c 'from sentence_transformers import SentenceTransformer; SentenceTransformer("<model-name>")'

## References

[Swiftly Writing and Deploying APIs to Stay Agile](https://radix.ai/blog/2020/12/swiftly-writing-and-deploying-apis-to-stay-agile/)
