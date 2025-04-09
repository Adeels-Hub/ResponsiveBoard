Install VS Plugin and CI/CD
**C#**: Install **StyleCop Analyzers** in your project:
Angular: Cant be configured direcctly. U have to use ESLint and setup esLint config file

**Configure SonarQube to Use the Appropriate Profiles**
 Go to **SonarQube Dashboard > Quality Profiles**.    
 Create or select profiles for each language:    
    - **C#:** Import or create a profile that follows **MS styles (StyleCop)**.        
    - **TypeScript/JavaScript (React and Angular):** Use ESLint with configurations according to the respective guidelines.        
8. Set the **quality profile for each project** by linking them to the correct language profile.