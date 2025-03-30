from datetime import date
from typing import List

# ---------------- Room Class ----------------
class Room:
    def __init__(self, room_number: str, room_type: str, amenities: List[str], price_per_night: float, is_available: bool = True):
        self.__room_number = room_number
        self.__room_type = room_type
        self.__amenities = amenities
        self.__price_per_night = price_per_night
        self.__is_available = is_available

    def get_room_number(self):
        return self.__room_number

    def is_available(self):
        return self.__is_available

    def set_availability(self, status: bool):
        self.__is_available = status

    def __str__(self):
        return f"Room {self.__room_number} ({self.__room_type}) - ${self.__price_per_night}/night - {'Available' if self.__is_available else 'Booked'}"

# ---------------- Guest Class ----------------
class Guest:
    def __init__(self, guest_id: str, name: str, email: str, contact: str):
        self.__guest_id = guest_id
        self.__name = name
        self.__email = email
        self.__contact = contact
        self.__loyalty_points = 0
        self.__bookings = []

    def add_booking(self, booking):
        self.__bookings.append(booking)

    def add_points(self, points):
        self.__loyalty_points += points

    def get_loyalty_points(self):
        return self.__loyalty_points

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"Guest: {self.__name}, Email: {self.__email}, Loyalty Points: {self.__loyalty_points}"

# ---------------- Booking Class ----------------
class Booking:
    def __init__(self, booking_id: str, guest: Guest, room: Room, check_in: date, check_out: date):
        self.__booking_id = booking_id
        self.__guest = guest
        self.__room = room
        self.__check_in = check_in
        self.__check_out = check_out
        room.set_availability(False)
        guest.add_booking(self)

    def get_guest(self):
        return self.__guest

    def get_room(self):
        return self.__room

    def get_stay_duration(self):
        return (self.__check_out - self.__check_in).days

    def __str__(self):
        return f"Booking {self.__booking_id} for {self.__guest.get_name()} in Room {self.__room.get_room_number()} from {self.__check_in} to {self.__check_out}"

# ---------------- Invoice Class ----------------
class Invoice:
    def __init__(self, invoice_id: str, booking: Booking, additional_charges: float = 0.0, discount: float = 0.0):
        self.__invoice_id = invoice_id
        self.__booking = booking
        self.__additional_charges = additional_charges
        self.__discount = discount

    def calculate_total(self):
        base_cost = self.__booking.get_stay_duration() * self.__booking.get_room()._Room__price_per_night
        return base_cost + self.__additional_charges - self.__discount

    def __str__(self):
        return f"Invoice {self.__invoice_id}: Total - ${self.calculate_total():.2f}"

# ---------------- Payment Class ----------------
class Payment:
    def __init__(self, payment_id: str, invoice: Invoice, payment_method: str, payment_date: date):
        self.__payment_id = payment_id
        self.__invoice = invoice
        self.__payment_method = payment_method
        self.__payment_date = payment_date

    def __str__(self):
        return f"Payment {self.__payment_id} made on {self.__payment_date} via {self.__payment_method} for {self.__invoice}"

# ---------------- Service Request Class ----------------
class ServiceRequest:
    def __init__(self, request_id: str, booking: Booking, request_type: str, status: str = "Pending"):
        self.__request_id = request_id
        self.__booking = booking
        self.__request_type = request_type
        self.__status = status

    def update_status(self, new_status):
        self.__status = new_status

    def __str__(self):
        return f"Service Request {self.__request_id} for {self.__request_type} - Status: {self.__status}"

# ---------------- Feedback Class ----------------
class Feedback:
    def __init__(self, feedback_id: str, guest: Guest, rating: int, comment: str):
        self.__feedback_id = feedback_id
        self.__guest = guest
        self.__rating = rating
        self.__comment = comment

    def __str__(self):
        return f"Feedback from {self.__guest.get_name()}: {self.__rating}/5 - {self.__comment}"

# ---------------- Loyalty Program Class ----------------
class LoyaltyProgram:
    def __init__(self, guest: Guest):
        self.__guest = guest
        self.__points_earned = 0
        self.__points_redeemed = 0

    def earn_points(self, points):
        self.__points_earned += points
        self.__guest.add_points(points)

    def redeem_points(self, points):
        if points <= self.__guest.get_loyalty_points():
            self.__points_redeemed += points
            self.__guest.add_points(-points)

    def __str__(self):
        return f"Loyalty Program for {self.__guest.get_name()} - Earned: {self.__points_earned}, Redeemed: {self.__points_redeemed}"
