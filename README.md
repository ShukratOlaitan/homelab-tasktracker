# Homelab TaskTracker

## Overview

TaskTracker is a FastAPI application deployed to a Kubernetes cluster running on Proxmox using GitOps with ArgoCD.

## Architecture

![alt text](<Architecture diagram.png>)

## Technologies

- Kubernetes
- Proxmox
- ArgoCD
- Docker
- Docker Hub
- FastAPI
- PostgreSQL
- Longhorn
- MetalLB

## Deployment Flow

![alt text](<Deployment Flow (Gitops).png>)

## Repository Structure

```text
homelab-tasktracker/
├── backend/              # FastAPI application code
├── kubernetes/base/      # Kubernetes manifests managed by ArgoCD
├── kubernetes/overlays/  # Environment-specific manifests
├── docs/                 # Architecture notes and project documentation
├── docker-compose.yml    # Local multi-container development
└── README.md

## Local Development
The application was first built and tested locally on my Mac using FastAPI, PostgreSQL, Docker, and Docker Compose.

Local workflow:
cd backend
./venv/bin/python -m uvicorn main:app --reload

Docker Compose workflow 
docker compose up -d
curl http://localhost:8000/health
curl http://localhost:8000/tasks

## Kubernetes Deployment
Kubernetes Deployment

The application is deployed to a 5-node Kubernetes cluster running on Proxmox.

Kubernetes resources used:

Namespace
Deployments
Services
Secrets
PersistentVolumeClaim
Longhorn storage
Readiness and liveness probes
Resource requests and limits

Main namespace:
tasktracker

Verify deployment:
kubectl get pods -n tasktracker
kubectl get svc -n tasktracker
kubectl get pvc -n tasktracker

## GitOps Workflow
ArgoCD is used to manage the Kubernetes deployment from GitHub.

Workflow:
GitHub Repository
        ↓
ArgoCD watches kubernetes/base
        ↓
ArgoCD syncs desired state
        ↓
Proxmox Kubernetes cluster is updated

The ArgoCD application points to:
Repository: https://github.com/ShukratOlaitan/homelab-tasktracker
Branch: main
Path: kubernetes/base
Namespace: tasktracker

Current GitOps status:
Healthy
Synced
Sync OK

## Lessons Learned

- Docker service discovery
- Kubernetes Secrets
- PVCs and Longhorn
- ArgoCD GitOps
- PostgreSQL persistence

## Screenshots

- ArgoCD Healthy + Synced
![alt text](<Screenshot 2026-06-23 at 15.30.30-1.png>)

- Kubernetes Pods Running

![alt text](<Screenshot 2026-06-23 at 15.43.06-1.png>)

- Proxmox cluster nodes
![alt text](<Screenshot 2026-06-23 at 15.43.33-2.png>)