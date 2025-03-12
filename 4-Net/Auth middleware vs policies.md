Auth middleware:
- Extracts user identity from a token or cookie.
- Adds user claims to HttpContext.User
- NO decide access rights.Only identify the user.
Policies:
🔹 Authentication policies enforce authorization rules after authentication.  
🔹 They define rules like roles, claims, and permissions for API endpoints.  
🔹 They are part of the authorization system (`UseAuthorization()` middleware.
