# fastapi_CURD_assignment

This FastAPI project implements CRUD operations for two entities: Items and User Clock-In Records. It provides 10 APIs to perform create, read, update, delete operations, along with filtering and aggregation capabilities.

The project uses MySQL as the database and follows best practices for API development, documentation, and error handling.

# Project Structure

• app/ - Contains the FastAPI application and all related modules.
• models.py - Defines the Pydantic models for Items and Clock-In Records.
• crud.py - Handles CRUD operations for the entities.
• main.py - Contains the API routes and application startup logic.
• database.py - Handles MySQL connection using SQLAlchemy.
• schemas.py - Defines request and response schemas for the API endpoints.
• README.md - This file explaining the project and its setup.

# How to Set Up and Run Locally
1. Clone the Repository
   --> If you have not done so already, clone the project from GitHub:
       [ git clone https://github.com/your-github-username/fastapi-assignment.git ]

3. Navigate to the Project Directory
    --> example:
        [ cd C:\Users\bhara\OneDrive\Desktop\fastapi\fastapi-assignment ]

5. Install Dependencies
   --> Install the necessary dependencies using pip:
       [ pip install -r requirements.txt ]

6. Update the Database Configuration
   --> Make sure to update your MySQL database credentials in the database.py file.
       [ SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:Bharath@localhost/dbname" ]

7. Run the FastAPI Application
   --> Start the FastAPI server using Uvicorn: [ uvicorn app:app --reload ]
   --> The application will now be running on http://127.0.0.1:8000.

8. Access Swagger Documentation
   --> Swagger UI is automatically available for testing the APIs:[ http://127.0.0.1:8000/docs ]



# API Endpoints
# Items API
1.POST /items - Create a new item.
   -Input: Name, Email, Item Name, Quantity, Expiry Date (YYYY-MM-DD).
   -The Insert Date is automatically added.

2.GET /items/{id} - Retrieve an item by ID.

3.GET /items/filter - Filter items by:
   -Email (exact match),
   -Expiry Date (items expiring after the provided date),
   -Insert Date (items inserted after the provided date),
   -Quantity (items with quantity greater than or equal to the provided 
   number).

4.GET /items/aggregate - MongoDB aggregation to count items grouped by email.

5.DELETE /items/{id} - Delete an item by ID.

6.PUT /items/{id} - Update an item’s details by ID.


# Clock-In Records API

1.POST /clock-in - Create a new clock-in entry.
  -Input: Email, Location.
  -The Insert DateTime is automatically added.
  
2.GET /clock-in/{id} - Retrieve a clock-in record by ID.

3.GET /clock-in/filter - Filter clock-in records by:
  -Email (exact match),
  -Location (exact match),
  -Insert DateTime (clock-ins after the provided date).
  
4.DELETE /clock-in/{id} - Delete a clock-in record by ID.

5.PUT /clock-in/{id} - Update a clock-in record by ID.


# Hosting the Application
--> After testing locally, you can host this application on a free platform 
    like Heroku or Koyeb.

Example: 'Heroku'

Steps to Host on Heroku
------------------------------
1.Create a Procfile: Add a Procfile to your project root with the following content:
[ web: uvicorn app:app --host=0.0.0.0 --port=${PORT:-8000} ]

2.Push to Heroku:
  -Login to Heroku and create a new app.
  -Set up a Git remote and push your code:
  [ git add .
    git commit -m "Deploying FastAPI to Heroku"
    git push heroku master ]
    
3.Open the App: Once the deployment is successful, open your application and the Swagger documentation URL:
[ https://your-heroku-app.herokuapp.com/docs ]


# Conclusion

This FastAPI application demonstrates CRUD operations, filtering, and aggregation using MySQL. It is a scalable, well-documented API application adhering to FastAPI's best practices.
