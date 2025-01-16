# Django Chat Application with Responsive Frontend and AWS Integration

This project is a comprehensive application combining frontend development, a Django-based chat application, and AWS integration. Below is a detailed overview of the features and setup instructions.

## Features

### Frontend Development
1. **Responsive Webpage**
   - **Fixed Navbar:** A navbar that remains fixed while scrolling.
   - **Three Sections Below Navbar:**
     - A collapsible left menu.
     - A main content area.
     - A right-side panel.
   - **Footer:** A footer fixed at the bottom of the page.
   - **Responsive Behavior:**
     - Shrinks page width dynamically based on screen size:
       - 992px - 1600px: Shrinks to 90%.
       - 700px - 767px: Shrinks to 80%.
       - 600px - 700px: Shrinks to 75%.
       - ≤ 600px: Shrinks to 50%.

2. **JavaScript Functionality**
   - Dynamically adjusts webpage width based on screen size using JavaScript.

### Django Chat Application
1. **User Authentication:**
   - Users can sign up and log in.
2. **User Interface:**
   - Collapsible left menu displaying all registered users.
   - Chat interface to initiate chats with selected users.
3. **Data Handling:**
   - Stores user data and chat messages in the database.
   - Retrieves and displays old messages in the chat interface.
4. **WebSocket Integration:**
   - Real-time chat functionality using WebSockets.
5. **User-Friendly Design:**
   - Ensures the chat interface is functional and intuitive.

### AWS Integration
1. **AWS Lambda Functions:**
   - Adds two numbers and returns the result.
   - Uploads a document or PDF file to an S3 bucket.

## Live Demo
[Chat Application on PythonAnywhere](https://ankki.pythonanywhere.com/)

## Repository
[GitHub Repository](https://github.com/ankki457/Django-Chat-Application)

## Setup Instructions

### Prerequisites
- Python 3.10 or higher
- Django 4.2 or higher
- Pip and virtual environment tools

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ankki457/Django-Chat-Application.git
   cd Django-Chat-Application
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv mysite-virtualenv
   source mysite-virtualenv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Database Setup
1. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

### Start the Server
1. Run the development server:
   ```bash
   python manage.py runserver
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

### AWS Lambda Setup
1. Create AWS Lambda functions using the provided Python scripts:
   - Function to add two numbers.
   - Function to upload files to an S3 bucket.

2. Deploy the functions in your AWS environment.

## Contributing
Feel free to fork this repository, submit pull requests, or open issues to suggest improvements.
