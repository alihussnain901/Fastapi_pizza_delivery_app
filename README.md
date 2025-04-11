# 🍕 FastAPI Pizza Delivery App

A modern, scalable, and fast Pizza Delivery API built with **FastAPI**, **SQLAlchemy**, and deployed on **Kubernetes** with full **CI/CD automation**. This project supports JWT authentication, order management, user registration, and more — all in a clean and modular architecture.

---

## 🚀 Features

- 🧑‍💻 User Registration & Login (with JWT Authentication)
- 🛒 Place, View, and Manage Orders
- 📦 Product (Pizza) Management
- 🔐 Secure password hashing (using PassLib)
- 🗳️ Voting or liking system (optional)
- 📄 SQLAlchemy Models and Pydantic Schemas
- ⚙️ RESTful API with FastAPI and automatic docs (Swagger UI & Redoc)
- 📦 Containerized with Docker
- 🔄 Continuous Integration with GitHub Actions
- 🚀 Continuous Delivery with Argo CD
- ☸️ Deployed on Kubernetes

---

## 🛠️ Tech Stack

| Layer           | Tech Stack                                   |
|----------------|-----------------------------------------------|
| Backend         | [FastAPI](https://fastapi.tiangolo.com/)     |
| ORM             | [SQLAlchemy](https://www.sqlalchemy.org/)    |
| Authentication  | JWT (OAuth2PasswordBearer)                   |
| Hashing         | PassLib                                       |
| Database        | PostgreSQL / SQLite (configurable)           |
| CI              | GitHub Actions                                |
| CD              | Argo CD                                       |
| Deployment      | Kubernetes                                     |
| Containerization| Docker                                        |

---

## ⚙️ CI/CD Workflow

- **CI (GitHub Actions)**:
  - Linting, testing, and building Docker image on every push.
  - Image is pushed to a container registry (Docker Hub/GitHub Container Registry).

- **CD (Argo CD)**:
  - Automatically syncs and deploys updated images to the Kubernetes cluster.
  - Monitors Git repository for any configuration changes.

---

## 🚀 Deployment on Kubernetes

- The app is deployed on a Kubernetes cluster using:
  - ConfigMaps and Secrets for configuration
  - PostgreSQL as a persistent backend
  - Services and Ingress for routing traffic
- Argo CD handles GitOps-style deployment from your GitHub repository

---

## 📄 API Documentation

FastAPI automatically provides interactive API documentation:

- Swagger UI: `http://<your-domain>/docs`
- ReDoc: `http://<your-domain>/redoc`

---

## 📦 Getting Started (Local Dev)

```bash
# Clone the repository
git clone https://github.com/your-username/pizza-delivery-app.git
cd pizza-delivery-app

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start development server
uvicorn main:app --reload


