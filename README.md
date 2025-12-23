# Flask Demo App – CI, Docker & Containers

A simple Flask web application created to demonstrate containerization and a CI pipeline that automatically builds and publishes Docker images.

---

## What this project demonstrates

- A basic Flask web application
- Docker containerization
- Automated testing
- GitHub Actions CI pipeline
- Building and publishing Docker images to GitHub Container Registry (GHCR)
- Separation of Continuous Integration (build & test) from deployment

---

## CI Pipeline Overview

The CI pipeline is implemented using **GitHub Actions**.

On every **push or pull request**, the pipeline:
1. Installs dependencies
2. Runs automated tests
3. Builds a Docker image
4. Pushes the image to **GitHub Container Registry (GHCR)**

Pipeline flow:

