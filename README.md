# Info App

This application responds to HTTP GET requests with a timestamp and hostname.

## Building the Application

1. Navigate to the `app` directory:
cd app
2. Build the Docker image:
docker build -t info-app:latest .
## Deploying the Application

1. Create a local Kubernetes cluster using Kind:
kind create cluster --config config/kind-config.yaml
2. Load the Docker image into the Kind cluster:
kind load docker-image info-app:latest
3. Apply the Kubernetes manifests:
kubectl apply -f kubernetes/
4. Verify the deployment:
kubectl get pods
kubectl get services
kubectl get ingress

5. Access the application:
- If using Kind, you may need to port-forward the service:
  ```
  kubectl port-forward service/info-app-service 8080:80
  ```
- Then access the application at `http://localhost:8080`

## Testing Environment

This project uses Kind (Kubernetes in Docker) for local testing. The configuration file is located at `config/kind-config.yaml`.

To set up the testing environment, follow these steps:

1. Install Kind: https://kind.sigs.k8s.io/docs/user/quick-start/#installation

2. Create the cluster using the provided configuration:
kind create cluster --config config/kind-config.yaml

3. Follow the deployment instructions above to deploy the application to your local Kind cluster.

## Monitoring (Stretch Goal)

To add monitoring, we can use Prometheus and Grafana. Install them using Helm:
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/kube-prometheus-stack
Then, create a ServiceMonitor for your application to scrape metrics.

## Image Optimization (Stretch Goal)

To make the image smaller, we use a multi-stage build in the Dockerfile. See the `Dockerfile` in the `app` directory for details.
