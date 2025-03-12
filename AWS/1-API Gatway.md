It is a serverless reverse proxy. 
  Not need LoadBalancer.
  Can terminate SSL  
AWS API Gateway has three types:
1. Edge-Optimized – Uses CloudFront for global caching & low latency.
2. Regional – Directly accessible in a specific AWS region, ideal for APIs needing controlled access.
3. Private – Only accessible within a VPC via **VPC Endpoints** (AWS PrivateLink).
