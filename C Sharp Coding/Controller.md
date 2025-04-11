using Microsoft.AspNetCore.Mvc;
[ApiController]
[Route("api/[controller]")]

[HttpGet("availability")]
public async Task<IActionResult> GetAvailability([FromQuery] VehicleAvailabilityRequest request)

[HttpPost("reserve")]
public async Task<IActionResult> ReserveVehicle([FromBody] ReservationRequest request)

return Ok(ResponseHelper.CreateResponse(result));