# CI/CD Pipeline using Docker and GitHub Actions

This is a complete DevOps college project that demonstrates how to create a simple Python Flask application, containerize it using Docker, and automate its build and testing process using a GitHub Actions CI/CD pipeline.

## Project Folder Structure

```text
├── .github/
│   └── workflows/
│       └── main.yml        # GitHub Actions workflow configuration for CI/CD
├── app.py                  # Main Python Flask application code
├── Dockerfile              # Docker configuration to build the container image
├── requirements.txt        # Python dependencies (Flask, Werkzeug)
└── README.md               # Project documentation (this file)
```

## How to Run Locally

### Prerequisites
- Python 3.9+ installed
- Docker installed (optional, for running via container)

### 1. Run using Python directly
1. Open a terminal in the project folder.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open your browser and go to `http://localhost:5000`

### 2. Run using Docker
1. Open a terminal in the project folder.
2. Build the Docker image:
   ```bash
   docker build -t my-flask-app .
   ```
3. Run the Docker container:
   ```bash
   docker run -p 5000:5000 my-flask-app
   ```
4. Open your browser and go to `http://localhost:5000`

---

## Viva Questions & Explanations

Here are some short, beginner-friendly explanations of the key technologies used in this project to help you prepare for your viva:

### 1. What is CI/CD?
- **CI (Continuous Integration):** It is the practice of automating the integration of code changes from multiple contributors into a single software project. When a developer pushes code, automated tests are run to ensure the new code doesn't break the application.
- **CD (Continuous Deployment/Delivery):** It is the practice of automatically deploying the tested code to a production or staging environment so users can access the new features quickly.
- **Why use it?** It helps catch bugs early, speeds up development, and reduces manual effort in building and testing.

### 2. What is Docker?
- Docker is a platform that allows developers to package an application and all its dependencies (libraries, frameworks, etc.) into a single unit called a **container**.
- **Why use it?** It solves the "it works on my machine" problem. A Docker container will run exactly the same way on any computer, whether it's your laptop or a server in the cloud.
- **What is a Dockerfile?** A Dockerfile is a text file containing a list of instructions (like `FROM`, `COPY`, `RUN`, `CMD`) used to build a Docker image.

### 3. What are GitHub Actions?
- GitHub Actions is a CI/CD tool built directly into GitHub. It allows you to automate tasks (called workflows) right from your GitHub repository.
- **How does it work in this project?** We created a `.github/workflows/main.yml` file. Every time we push code to the `main` branch, GitHub Actions automatically starts a virtual machine (Ubuntu), sets up Python, installs dependencies, builds our Docker image, and runs it to verify that everything works correctly.

### 4. Explain the Application (app.py)
- It is a simple web server built using **Flask**, which is a lightweight Python web framework.
- It has a single route (`/`) that returns a simple greeting message.
- It runs on port `5000` and uses `host='0.0.0.0'` so that the application can be accessed from outside the Docker container.
