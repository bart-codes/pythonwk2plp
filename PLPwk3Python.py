def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    The discount is applied only if the percentage is 20% or higher.

    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage.

    Returns:
        float: The final price after the discount, or the original price if no discount is applied.
    """
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Return the final price
        return price - discount_amount
    else:
        # No discount applied, return the original price
        return price

# --- Main Program ---
try:
    # Prompt the user to enter the original price
    original_price = float(input("Enter the original price of the item: "))
    
    # Prompt the user to enter the discount percentage
    discount_percentage = float(input("Enter the discount percentage: "))

    # Call the function to calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Check if a discount was applied and print the appropriate message
    if final_price < original_price:
        print(f"\nDiscount applied! The final price is: ${final_price:.2f}")
    else:
        print(f"\nNo discount was applied. The original price is: ${original_price:.2f}")

except ValueError:
    print("Invalid input. Please enter a valid number for the price and percentage.")
