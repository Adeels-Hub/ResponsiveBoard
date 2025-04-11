**Creating solution**
dotnet new sln -n PrimeGroup.CarRentalService

**Create NewWebApi and Test proj add to solution**
dotnet new webapi -n PrimeGroup.CarRentalService.Api
dotnet sln add PrimeGroup.CarRentalService.Api

dotnet new xunit -n PrimeGroup.CarRentalService.Api.Tests
dotnet sln add PrimeGroup.CarRentalService.Api.Tests

**Create Class Lib and Test proj add to solution**
dotnet new classlib -n PrimeGroup.CarRentalService.Core
dotnet sln add PrimeGroup.CarRentalService.Core.Tests

**Add reference**
dotnet add PrimeGroup.CarRentalService.Api reference PrimeGroup.CarRentalService.Core