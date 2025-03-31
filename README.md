# MortgageCalculator
This project is a simple Mortgage Calculator built using Flask to visually represent the loan balance over time. It allows users to calculate mortgage details with different variables.

#Features
Mortgage calculator that computes loan details.

Frontend built with HTML, JavaScript, and CSS.

Backend powered by Python and Flask.

#Prerequisites
Make sure you have the following installed:

Python 3.x

pip (Python package manager)

#Required Python Libraries:
Flask: Web framework for building the application.

#Installation Instructions
Clone the Repository

Clone the repository to your local machine using the following command:

bash
Copy
git clone https://github.com/your-username/mortgage-calculator.git
Install Dependencies

Navigate to the project directory and install the required Python libraries:

bash
Copy
cd mortgage-calculator
pip install -r requirements.txt
Create a Virtual Environment (Optional)

If you prefer using a virtual environment, create and activate it:

For macOS/Linux:

bash
Copy
python3 -m venv venv
source venv/bin/activate
For Windows:

bash
Copy
python -m venv venv
.\venv\Scripts\activate
Run the Application

To start the Flask server, run the following command:

bash
Copy
python app.py
The application should now be accessible in your browser at http://127.0.0.1:5000/.

![image](https://github.com/user-attachments/assets/b58fb824-31f7-4337-ab35-7e7fdb3ad234)


## Folder Structure

Here is the folder structure of the project:


mortgage-calculator/ ├── app.py # Flask app for backend logic ├── templates/ # HTML templates (Flask renders these) │ └── index.html # Main page with mortgage calculator and graph ├── static/ # Static assets like CSS and JS │ ├── css/ │ │ └── style.css # Custom CSS for styling │ └── js/ │ └── script.js # Custom JavaScript (if needed) └── requirements.txt # Python dependencies (Flask)
