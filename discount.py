def calculate_discount(price, discount_percent):
    # Check if the discount is equal or above 20%
    if discount_percent >= 20:
        # Apply the discount
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        # Return the original price if discount is less than 20%
        return price

# Example Buyer x
original_price = 978
discount = 21
final_price = calculate_discount(original_price, discount)
print(f"The final price after applying the discount is: {final_price}")
