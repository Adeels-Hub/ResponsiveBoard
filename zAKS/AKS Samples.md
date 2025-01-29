#AKS-Code-Samples
Microsoft Azure’s official repositories and documentation are the **most comprehensive** and well-aligned with AKS features:
- **Link**: [AKS Documentation](https://learn.microsoft.com/en-us/azure/aks/)
- **GitHub Repository**: [Azure-Samples/aks-quickstart](https://github.com/Azure/azure-quickstart-templates)
#### Why Choose This?

1. **Covers Key AKS Features**:
    
    - NGINX Ingress and Application Gateway Ingress Controller (AGIC).
    - Helm-based deployments.
    - RBAC, Azure Active Directory (AAD) integration.
    - Monitoring via Azure Monitor and Prometheus.
    - Autoscaling with Horizontal Pod Autoscaler (HPA) and Cluster Autoscaler.
    - Private cluster and networking setups.
2. **Well-Documented**:
    
    - Includes step-by-step guides in both GitHub README files and official Microsoft Learn documentation.
3. **Real-World Examples**:
    
    - Includes examples like multi-container applications and hybrid ingress setups.
#### Examples from Azure Samples:
1. **NGINX + Ingress**:    
    - [aks-helloworld-nginx](https://github.com/Azure-Samples/aks-helloworld/tree/main/helm/aks-helloworld-nginx)
        - Deploys a simple app using NGINX Ingress.
        - Shows how to configure TLS and route traffic.
2. **AGIC**:    
    - [Application Gateway Ingress Controller](https://github.com/Azure/application-gateway-kubernetes-ingress)
        - Detailed examples for deploying AGIC and configuring it with Helm.
3. **Combination Scenarios**:    
    - Use both NGINX and AGIC for specific scenarios.

---
### **Runner-Up: Bitnami Helm Charts**
If you want **simplified deployment with excellent Helm chart examples**, Bitnami is a great option:
- **Link**: Bitnami Helm Charts
#### Why Choose This?
1. **Ready-to-Use Applications**:
    - Provides pre-configured Helm charts for popular apps.
    - Easily integrates with NGINX or other ingress controllers.
2. **Flexibility**:
    - Modify `values.yaml` to explore AKS features like HPA, ingress, and persistence.
#### Key Charts:
1. **NGINX Ingress**:    
    - NGINX Ingress Controller
        - Feature-rich and easy to deploy.
2. **Applications**:    
    - Deploy apps (e.g., WordPress, Ghost, etc.) and experiment with ingress.