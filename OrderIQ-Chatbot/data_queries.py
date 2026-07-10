import pandas as pd
import re
from datetime import datetime

df = pd.read_csv("dataset.csv")

def query_data(user_input):
    user_input = user_input.lower().strip()
    
    # Handle empty input
    if not user_input:
        return "Please type something so I can help you!"
    
    # Query 1 — Order status (now catches bare order IDs too)
    match = re.search(r'ord\d+', user_input, re.IGNORECASE)
    if match and ("status" in user_input or "order" in user_input or len(user_input.split()) <= 2):
        order_id = match.group().upper()
        result = df[df['OrderID'] == order_id]['OrderStatus'].values
        if len(result):
            return f"Order {order_id} status: {result[0]}"
        return f"I couldn't find order {order_id}."
    
    # Query 2 — Coupon info
    COUPON_INFO = {
        "SAVE10":   {"description": "10% off your order",       "type": "percentage"},
        "FREESHIP": {"description": "Free shipping on order",   "type": "shipping"},
        "WINTER15": {"description": "15% off your order",       "type": "percentage"},
    }

    if "coupon" in user_input or "discount" in user_input or "promo" in user_input:
        for code in ["SAVE10", "FREESHIP", "WINTER15"]:
            if code.lower() in user_input:
                count = df[df['CouponCode'] == code].shape[0]
                info = COUPON_INFO[code]
                return f"Coupon {code}: {info['description']}. It has been used {count} times."
        # General coupon list question
        return "We have 3 coupons: SAVE10, FREESHIP, and WINTER15."
    
    # Catch bare coupon codes
    for code in ["SAVE10", "FREESHIP", "WINTER15"]:
        if code.lower() in user_input:
            count = df[df['CouponCode'] == code].shape[0]
            info = COUPON_INFO[code]
            return f"Coupon {code}: {info['description']}. It has been used {count} times."

    # Query 3 — Most cancelled product
    if "cancel" in user_input:
        cancelled = df[df['OrderStatus'] == 'Cancelled']['Product'].value_counts()
        top = cancelled.idxmax()
        return f"Most cancelled product: {top} ({cancelled.max()} times)"
    
    # Query 4 — Products available
    if "product" in user_input or "sell" in user_input or "available" in user_input or "items" in user_input:
        products = df['Product'].unique().tolist()
        return f"We sell: {', '.join(products)}"
    
    # Query 5 — Referral source (expanded keywords)
    if any(word in user_input for word in ["referral", "source", "traffic", "customers come", "platform", "channel"]):
        top = df['ReferralSource'].value_counts().idxmax()
        return f"Top referral source: {top}"
    
    # Query 6 — Revenue (expanded keywords + fix for no data)
    if any(word in user_input for word in ["revenue", "sales", "total", "make", "earn", "money"]):
        year_match = re.search(r'20\d{2}', user_input)
        
        if not year_match and "this year" in user_input:
            year = str(datetime.now().year)
        elif year_match:
            year = year_match.group()
        else:
            year = None
        
        if year:
            filtered = df[df['Date'].str.startswith(year)]
            total = filtered['TotalPrice'].sum()
            if total == 0:
                return f"No sales data found for {year}. Available years: 2023, 2024, 2025."
            return f"Total revenue in {year}: ${total:,.2f}"
        
        total = df['TotalPrice'].sum()
        return f"Total revenue (all time): ${total:,.2f}"
    
    return None