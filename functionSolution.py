def solution(A, D):
    balance = 0
    monthly_card_payments = {i: 0 for i in range(1, 13)}

    for i in range(len(A)):
        amount = A[i]
        date_month = int(D[i][5:7])

        balance += amount

        if amount < 0:
            monthly_card_payments[date_month] += 1
        else:
            monthly_card_payments[date_month] -= 1

        if amount < 0 and monthly_card_payments[date_month] >= 3 and abs(monthly_card_payments[date_month]) >= 100:
            balance += 5

    balance -= 5 * 12

    return balance
