var builder = WebApplication.CreateBuilder(args);
**startup class**
builder.Services.AddControllers(); // Adds support for controllers
builder.Services.AddEndpointsApiExplorer(); // Enables API endpoint metadata
builder.Services.AddSwaggerGen(); // Adds Swagger for API documentation
**Dependency Injection (DI)**
builder.Services.AddScoped<IVehicleService, VehicleService>();
builder.Services.AddScoped<IVehicleRepository, VehicleRepository>();

var app = builder.Build();

**Configure the HTTP request pipeline**
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

