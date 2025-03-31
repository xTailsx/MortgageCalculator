function calculateMortgage() {
    // Get input values from the form
    const loanAmount = document.getElementById('loanAmount').value;
    const interestRate = document.getElementById('interestRate').value;
    const loanTerm = document.getElementById('loanTerm').value;
    const offsetAmount = document.getElementById('offsetAmount').value;
    const extraRepayments = document.getElementById('extraRepayments').value;
    const repaymentFrequency = document.getElementById('repaymentFrequency').value;

    // Send the data to the backend for calculation
    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `loanAmount=${loanAmount}&interestRate=${interestRate}&loanTerm=${loanTerm}&offsetAmount=${offsetAmount}&extraRepayments=${extraRepayments}&repaymentFrequency=${repaymentFrequency}`
    })
    .then(response => response.json())
    .then(data => {
        // Update the results on the page
        document.getElementById('monthlyRepayment').innerText = `Monthly Repayment: $${data.monthly_repayment}`;
        document.getElementById('totalRepayment').innerText = `Total Repayment: $${data.total_repayment}`;
        document.getElementById('totalInterest').innerText = `Total Interest Paid: $${data.total_interest}`;
        document.getElementById('loanDuration').innerText = `Loan Duration: ${data.loan_duration_years} years`;
    });
}
