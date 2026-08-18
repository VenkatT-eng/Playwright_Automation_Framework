"""
1) Create Booking (POST) ---> BookingID
2) Get Booking Details (GET) - By ID, By Names, By Dates
3) Create Token (POST /auth)
4) Partial Update Booking (PATCH)
5) Full Update Booking (PUT)
6) Delete Booking (DELETE)
"""

import pytest
import json
from playwright.sync_api import Playwright, APIRequestContext

# -------------------------------------------------------------------
# Base URL of the RESTful Booker API
# -------------------------------------------------------------------
base_url = "https://restful-booker.herokuapp.com"


# -------------------------------------------------------------------
# Utility Function: Reads and returns JSON data from a given file path
# -------------------------------------------------------------------
def read_json(file_path):
    file = open(file_path, "r")
    return json.load(file)


# -------------------------------------------------------------------
# Fixture: Creates a reusable Playwright Request Context for the session
# -------------------------------------------------------------------
@pytest.fixture(scope="session")
def request_context(playwright: Playwright):
    context = playwright.request.new_context()
    yield context
    context.dispose()


# -------------------------------------------------------------------
# 1) Create Booking (POST)
# -------------------------------------------------------------------
def test_create_booking(request_context):
    """Create a new booking and validate response"""
    data=read_json("./create_booking.json")

    # Send POST request to create booking
    response = request_context.post(f"{base_url}/booking", data=data)

    assert response.ok  # (or)  assert response.status_text=="OK"
    assert response.status == 200

    response_body = response.json()
    print("\nCreate Booking Response:", response_body)

    # Basic validation of response fields
    assert "bookingid" in response_body
    assert "booking" in response_body

    booking = response_body["booking"]

    # Validate key booking details
    assert booking["firstname"] == data["firstname"]
    assert booking["lastname"] == data["lastname"]
    assert booking["totalprice"] == data["totalprice"]
    assert booking["depositpaid"] == data["depositpaid"]
    assert booking["bookingdates"]["checkin"] == data["bookingdates"]["checkin"]
    assert booking["bookingdates"]["checkout"] == data["bookingdates"]["checkout"]

    # Store booking ID globally for reuse in subsequent tests
    global booking_id
    booking_id = response_body["bookingid"]
    print("Booing ID:", booking_id)



