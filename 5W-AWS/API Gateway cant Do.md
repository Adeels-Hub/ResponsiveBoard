**WAF Can do**
API Gateway lacks built-in deep inspection and threat mitigation.
PI Gateway has throttling but not as flexible or rule-based.
API Gateway only supports basic throttling and auth, not complex WAF logic.
DOS

**ALB Cant Do**

API Gateway has size limits (10MB payload max for REST APIs).
API Gateway does not support session stickiness.
API Gateway requires VPC Link and cannot natively route to private subnets.
based routing with more control API Gateway routing is limited to stages and routes.
API Gateway TLS is more limited and abstracted.