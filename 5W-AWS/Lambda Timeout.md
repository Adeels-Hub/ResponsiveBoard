The **default timeout** for an AWS Lambda function is **3 seconds**.

 **Timeout Range:**
- **Minimum:** 1 second
- **Maximum:** 15 minutes (900 seconds)

You can adjust the timeout in the **AWS Lambda console** under: **Configuration → General configuration → Edit → Timeout**  
Or via the AWS CLI:

**Amazon X-Ray** can help you discover the timeout value for downstream services.