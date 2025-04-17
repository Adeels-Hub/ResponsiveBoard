Custom Annotations:
    fine-grained rate limiting, custom timeouts, redirects, and rewrites
    Request and Response Manipulation
    Custom Load Balancing Algorithms
End-to-End TLS Encryption
  - AGIC requires **TLS termination** at the Application Gateway and cannot pass through encrypted traffic directly to pods.
Cloud Agnosity
Edge Caching
Multi-Tenancy
Light weight and high throughput

Deployed via ingree.yaml and values.yaml
Scaling is managed by **Kubernetes HPA or Cluster Autoscaler**.