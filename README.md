# 🚀 Prime Checker Pro (FastAPI + Docker + CI/CD)

A full-stack DevOps demonstration project featuring a high-performance Python API, a responsive web interface, and fully automated deployment pipelines.

## 🛠 Tech Stack
* **Framework:** FastAPI (Python 3.13)
* **Containerization:** Docker
* **CI/CD:** GitHub Actions
* **Testing:** Pytest
* **Frontend:** HTML5 / CSS3 / JavaScript (Fetch API)

## 🌟 Features
- **Semantic Versioning:** Tagged releases (v1.0.0).
- **Automated Testing:** Every push is validated by the GitHub "Robot".
- **Dockerized:** Consistent environment across any machine.
- **Prime Logic:** Real-time calculation with a user-friendly UI.

## 🚀 Quick Start (Local)
1. Install dependencies:
   `pip install -r requirements.txt`
2. Run the app:
   `uvicorn main:app --reload`
3. Visit: `http://127.0.0.1:8000`

## 🐳 Docker Deployment
Build the image:
`docker build -t my-fastapi-app .`

Run the container:
`docker run -d -p 8081:80 my-fastapi-app`

## 🤖 CI/CD Pipeline
This repo uses **GitHub Actions** to:
1. Lint the code.
2. Run unit tests via `pytest`.
3. Verify the Docker build process.