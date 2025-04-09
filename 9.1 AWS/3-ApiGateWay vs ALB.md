Use only ALB if handling **traditional web traffic** (ECS/EKS services).  
🔹 Add API Gateway in front of ALB if you need:
- Rate limiting, authentication, API keys
- Request transformation (e.g., mapping, validation)
- Throttling & security (WAF, IAM auth)