#!/usr/bin/env python3
"""Second-pass scrubbing: remove Grab-specific domain terms (driver, passenger, booking, ride-hailing)."""

import re
from pathlib import Path

KB_FILE = Path(__file__).parent.parent / "knowledge-base" / "ml-ds-llm-fundamentals.md"

def scrub(content: str) -> str:
    # ─── ride-hailing → marketplace / platform ─────────────────────────
    content = content.replace("ride-hailing cancellations", "order cancellations")
    content = content.replace("ride-hailing platform", "marketplace platform")
    content = content.replace("ride-hailing company", "tech company")
    content = content.replace("ride-hailing vocabulary", "domain-specific vocabulary")
    content = content.replace("ride-hailing context", "e-commerce context")
    content = content.replace("ride-hailing", "marketplace")
    content = content.replace("<ride-hailingchat>", "<chat_log>")
    content = content.replace("</ride-hailingchat>", "</chat_log>")

    # ─── driver → provider / seller ────────────────────────────────────
    content = content.replace("driver induced the passenger to cancel",
                              "seller caused the customer to cancel their order")
    content = content.replace("driver induced cancellation",
                              "seller-induced cancellation")
    content = content.replace("driver induced", "seller-induced")
    content = content.replace("Driver induced", "Seller-induced")
    content = content.replace('"driver moving away: 60%"', '"seller unresponsive: 60%"')
    content = content.replace("driver moving away", "seller unresponsive")
    content = content.replace("driver stationary", "seller idle")
    content = content.replace("Driver CANCELS", "Seller CANCELS")
    content = content.replace("Driver cancels", "Seller cancels")
    content = content.replace('Driver: "please cancel"', 'Seller: "please cancel this order"')
    content = content.replace('Driver: "Hi, I\'m here"', 'Seller: "Order is ready"')
    content = content.replace('driver said "cancel the booking please"',
                              'seller said "please cancel this order"')
    content = content.replace("Driver was moving away and ignoring messages",
                              "Seller was unresponsive and ignoring messages")
    content = content.replace("driver intent from passenger messages",
                              "seller intent from customer messages")
    content = content.replace('"sender":"driver"', '"sender":"seller"')
    content = content.replace("driver/passenger ID", "seller/customer ID")
    content = content.replace("Driver / passenger IDs", "Seller / customer IDs")
    content = content.replace("driver segments", "provider segments")
    content = content.replace("driver's past performance", "provider's past performance")
    content = content.replace("driver's past", "provider's past")

    # ─── passenger → customer ──────────────────────────────────────────
    content = content.replace("Passenger: \"ok\"", "Customer: \"ok\"")
    content = content.replace("Pax no show", "Customer no-show")
    content = content.replace("Pax feedback", "Customer feedback")
    content = content.replace("cross-passenger", "cross-user")

    # ─── booking → order / request ─────────────────────────────────────
    content = content.replace("completed bookings—missing cancelled ride patterns",
                              "completed orders—missing cancelled order patterns")
    content = content.replace("classifies the booking", "classifies the request")
    content = content.replace("per booking to measure", "per request to measure")
    content = content.replace("per-booking classification", "per-request classification")
    content = content.replace("booking workflow", "order workflow")
    content = content.replace("booking APIs", "order APIs")
    content = content.replace("bookings, POI, geocoding", "orders, products, search")
    content = content.replace("classify bookings as", "classify requests as")
    content = content.replace("Booking requests", "Service requests")
    content = content.replace("booking request", "service request")
    content = content.replace("New booking request", "New service request")
    content = content.replace("booking_ref", "order_ref")
    content = content.replace("booking details", "order details")
    content = content.replace("load_booking_data", "load_order_data")
    content = content.replace("BookingClassifier", "OrderClassifier")
    content = content.replace("| Booking |", "| Request |")
    content = content.replace("the second booking", "the second request")
    content = content.replace("cancel the booking", "cancel the order")

    # ─── OPI → Incident severity ───────────────────────────────────────
    content = content.replace("OPI Severity Matrix (a tech company framework)",
                              "Incident Severity Matrix")
    content = content.replace("OPI ticket", "incident ticket")

    # ─── Travellers project → generic ──────────────────────────────────
    content = content.replace("In Travellers,", "In a travel assistant project,")
    content = content.replace("Travellers Application", "Multi-Tool Agent Application")
    content = content.replace("Travellers 1", "a content curation project")
    content = content.replace("Travellers 2", "a travel assistant project")

    return content

def main():
    print(f"Reading {KB_FILE}...")
    original = KB_FILE.read_text(encoding="utf-8")
    scrubbed = scrub(original)

    changes = sum(1 for a, b in zip(original.splitlines(), scrubbed.splitlines()) if a != b)
    print(f"Changed {changes} lines.")
    KB_FILE.write_text(scrubbed, encoding="utf-8")
    print("Done.")

if __name__ == "__main__":
    main()
