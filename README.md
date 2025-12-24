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
