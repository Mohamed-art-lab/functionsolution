def calculate_balance(transaction_amounts, transaction_dates):    
    # Initial balance and transaction fee setup
    balance = 0
    transaction_fee = 5
    
    # Keep track of transactions by month using a dictionary
    monthly_transactions = {}
    
    # Process each transaction
    for amount, date in zip(transaction_amounts, transaction_dates):
        # Extract the month from the date
        month = int(date.split('-')[1])
        
        # Update balance based on transaction amount (positive or negative)
        balance += amount
        
        # Track negative transactions by month
        if amount < 0:
            monthly_transactions.setdefault(month, []).append(amount)
    
    # Process each month for additional fees
    for month in range(1, 13):
        # Check if conditions for fees are met
        if month in monthly_transactions and len(monthly_transactions[month]) >= 3 and sum(monthly_transactions[month]) >= -100:
            # Apply fees for transactions beyond the first 3
            balance += transaction_fee * (len(monthly_transactions[month]) - 3)
        else:
            # Apply standard monthly fee
            balance -= transaction_fee
    
    return balance
