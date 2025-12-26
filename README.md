# Flask Demo App – CI, Docker & Containers

A simple Flask web application created to demonstrate containerization and a Continuous Integration (CI) pipeline for building and validating Docker images.

This project focuses on CI automation and container workflows rather than production deployment.

## This project demonstrates:

- A basic Flask web application
- Docker containerization
- Automated testing with pytest
- GitHub Actions CI pipeline
- Building and pushing Docker images to GitHub Container Registry (GHCR)
- Clear separation of Continuous Integration (build & test) from deployment

## CI Pipeline Overview

The CI pipeline is implemented using GitHub Actions.

On every push or pull request, the pipeline:

- Installs dependencies
- Runs automated tests
- Builds a Docker image
- Pushes the image to GitHub Container Registry (GHCR)

This pipeline validates code changes and ensures the application can be reliably built and containerized.


## Deployment

This application is containerized using Docker and deployed on **Render** as a container-based web service.

The Docker image is built and pushed to **GitHub Container Registry (GHCR)** using **GitHub Actions** on every push.

Deployment to Render is currently **manual**, which allows controlled releases.  
The setup can be easily extended to full CI/CD using a deploy webhook.


live demo: https://flask-suggestion-app-latest.onrender.com/index
           https://flask-suggestion-app-latest.onrender.com/trip

NOTE: PLEASE BE VERY PATIENT IM USING THE FREE TIER AND IT TAKES A MINUTE FOR IT TO LOAD THE VERY FIRST TIME THANK YOU!           
