from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def calculate_mortgage(loan_amount, interest_rate, loan_term, offset_amount, extra_repayments, repayment_frequency):
    """
    Calculate mortgage repayment details.
    """
    # Adjust the loan amount based on the offset account
    adjusted_loan_amount = loan_amount - offset_amount

    # Monthly interest rate
    monthly_interest_rate = (interest_rate / 100) / 12

    # Number of payments based on repayment frequency (monthly, fortnightly, weekly)
    if repayment_frequency == "monthly":
        num_payments = loan_term * 12
    elif repayment_frequency == "fortnightly":
        num_payments = loan_term * 26
    elif repayment_frequency == "weekly":
        num_payments = loan_term * 52
    else:
        num_payments = loan_term * 12  # Default to monthly if the frequency is incorrect

    # Monthly repayment calculation using the PMT formula
    if monthly_interest_rate == 0:  # If no interest rate, simple division
        monthly_repayment = adjusted_loan_amount / num_payments
    else:
        monthly_repayment = (adjusted_loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)

    # Add extra repayments if provided
    if extra_repayments > 0:
        monthly_repayment += extra_repayments

    # Calculate total repayment and total interest
    total_repayment = monthly_repayment * num_payments
    total_interest = total_repayment - loan_amount

    # Return results
    return {
        "monthly_repayment": round(monthly_repayment, 2),
        "total_repayment": round(total_repayment, 2),
        "total_interest": round(total_interest, 2),
        "loan_duration_years": loan_term,
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get the data from the request
    loan_amount = float(request.form['loanAmount'])
    interest_rate = float(request.form['interestRate'])
    loan_term = int(request.form['loanTerm'])
    offset_amount = float(request.form['offsetAmount'])
    extra_repayments = float(request.form['extraRepayments'])
    repayment_frequency = request.form['repaymentFrequency']

    # Perform mortgage calculation
    result = calculate_mortgage(loan_amount, interest_rate, loan_term, offset_amount, extra_repayments, repayment_frequency)

    # Return results as JSON
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
