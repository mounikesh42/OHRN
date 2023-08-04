# FOSS JOB Portal - Django Project

FOSS JOB Portal is a Django-based web application designed to serve as a job portal for Free and Open Source Software (FOSS) enthusiasts and companies looking to hire talent within the FOSS community.

## Requirements

- Python 3+
- Django  
## How to Run the Project

Follow the steps below to set up and run the FOSS JOB Portal Django project on your local machine:

1. **Clone the Repository**: Clone this repository to your local machine using the following command:

git clone <https://github.com/mounikesh42/OHRN.git>

2. **Navigate to Project Directory**: Change into the project directory:

cd foss-job-portal/OHRN/backend

3. **Create and Activate Virtual Environment** (Optional but recommended):

python -m venv env
source env/bin/activate # On Windows, use env\Scripts\activate



4. **Install Dependencies**: Install the required Python packages using pip:

pip install -r requirements.txt

5. **Apply Migrations**: Create the necessary database tables by applying migrations:

python manage.py makemigrations

python manage.py migrate


6. **Run the Development Server**: Start the Django development server:

python manage.py runserver


7. **Access the Application**: Open your web browser and go to `http://localhost:8000/` to access the FOSS JOB Portal.

