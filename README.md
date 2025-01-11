# S3 Browser

S3 Browser is a Flask-based application that allows users to securely manage multiple AWS S3 accounts and perform S3 operations like uploading, downloading, and managing files. The application is designed with encryption and security in mind to handle sensitive AWS credentials.

This repository contains the source code for the S3 Browser application, Dockerization, and Kubernetes deployment.

## Features

- Manage multiple AWS S3 accounts.
- Store AWS access keys and secret keys securely (encrypted using Fernet).
- Perform S3 operations (listing buckets in an account).
- Secure authentication and environment configuration.
- Dockerized application for easy containerization.
- Kubernetes deployment for scalable and fault-tolerant infrastructure.

## Project Structure

```plaintext
s3_browser/
├── app.py               # Main Flask application
├── models.py            # Database models (SQLAlchemy)
├── routes/              # API routes for handling requests
│   ├── account_routes.py
│   └── s3_routes.py
├── utils/               # Utility functions
│   ├── encryption.py    # Encryption utility for storing credentials securely
│   └── aws_client.py    # AWS client for interacting with S3
├── config.py            # Configuration file (SQLAlchemy, encryption keys, etc.)
├── requirements.txt     # List of dependencies
├── migrations/          # Database migrations
└── Dockerfile           # Dockerfile for containerizing the app
└── k8s/                 # Kubernetes configurations (Deployment and Service)
    ├── deployment.yaml  # Kubernetes Deployment configuration
    └── service.yaml     # Kubernetes Service configuration
