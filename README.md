# Multiplication Table Generator App

A simple Flask web application that generates a multiplication table for any number (integer or decimal) entered by the user. The app features a modern, responsive UI styled with Tailwind CSS and handles invalid inputs gracefully.

## Features
- Input any number to generate its multiplication table (1 to 10).
- Responsive design with a clean, card-based layout.
- Error handling for invalid inputs with a visual shake animation.
- Built with Flask and Tailwind CSS (via CDN).

## Project Structure
```
multiplication_table_app/
├── templates/
│   └── index.html       # HTML template for the UI
├── app.py              # Main Flask application
├── requirements.txt    # Project dependencies
└── README.md           # This file
```

## Setup Instructions

**1. Clone the Repository**
```
git clone https://github.com/your-username/multiplication_table_app.git
cd multiplication_table_app
```
**2. Create and Activate a Virtual Environment:**
```
python -m venv venv
.\venv\Scripts\activate
```
**3. Install Dependencies:**
```
pip install -r requirements.txt
```

**4. Run the Application:**
```
python app.py
```

## Technologies Used

- Flask: Python web framework for backend logic.
- Tailwind CSS: Utility-first CSS framework for styling (via CDN).
