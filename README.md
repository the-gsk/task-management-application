# Task Management Application

## Overview
This is a simple task management application built with Django. It allows users to create, view, update, and delete tasks. The application includes basic user authentication for user management.

## Features
- User Authentication: Implement user registration and login functionality using Django's built-in authentication system.

- Task Model: Created a Task model with the following fields:
  - Title: A short description of the task.
  - Description: Additional details about the task.
  - Due Date: Date when the task is due.
  - Status: Whether the task is pending, in progress, or completed.
  - Assignee: The user responsible for the task.

- Task List:
  - Created a page where authenticated users can see a list of their tasks.
  - Display tasks in a table or list format, showing details like title, due date, and status.
  - Include options to mark tasks as complete and delete tasks.

- Task Creation and Editing:
  - Implement a page where users can create new tasks.
  - Users should be able to edit existing tasks.
  - Use Django forms for task creation and editing.

- Task Detail View:
  - Create a page that displays the full details of a task when a user clicks on it.
  - Include an option to go back to the task list.

## Installation
1. Clone the repository to your local machine:
  - https://github.com/the-gsk/task-management-application.git


2. Create a virtual environment on python (3.10):
  - https://docs.python.org/3/
  - https://docs.python.org/3/library/venv.html

3. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

1. Install project dependencies:
    ```
    pip install -r requirements.txt
    ```

2. Run database migrations:
    ```
    python manage.py migrate
    ```

3. Start the development server:
    ```
    python manage.py runserver
    ```

## => Through the Web Pages
1. For Access the Register User in your web browser at http://localhost:8000/accounts/register/

2. For Access the Login User in your web browser at http://localhost:8000/accounts/login/

3. For Access the Logout User in your web browser at http://localhost:8000/accounts/logout/

4. For Access the Task Board in your web browser at http://localhost:8000/tasks/

5. Further Task Realted things you will see on web page (ex: Task Create, Task Details, Task Edit/Update and Task Delete)
  <div style="display: flex; align-items: center;">
    <img src="https://xp.io/storage/1zTiGZ90.png" alt="Project Logo" style="width: 33%; margin-right: 10px;" />
    <img src="https://xp.io/storage/1zTkq2c4.png" alt="Project Logo" style="width: 33%; margin-right: 10px;" />
    <img src="https://xp.io/storage/1zTv969H.png" alt="Project Logo" style="width: 33%; margin-right: 10px;" />
  </div>
  <div style="display: flex; align-items: center;">
    <img src="https://xp.io/storage/1zTmHM0J.png" alt="Project Logo" style="width: 33%; margin-right: 10px;" />
    <img src="https://xp.io/storage/1zR8ibsR.png" alt="Project Logo" style="width: 33%; margin-right: 10px;" />
    <img src="https://xp.io/storage/1zTtdgSC.png" alt="Project Logo" style="width: 33%; margin-right: 10px;" />
  </div>

  
## => Through the Api

### API Documentation
#### User Authentication
- **Login Endpoint:**
  - URL: `http://127.0.0.1:8000/api/login/`
  - Method: POST
  - Request Body:
    ```json
    {
      "username": "testuser",
      "password": "testpassword"
    }
    ```
  - Description: Use this endpoint to authenticate a user and obtain an authentication token.
  
- **Register Endpoint:**
  - URL: `http://127.0.0.1:8000/api/register/`
  - Method: POST
  - Request Body:
    ```json
    {
      "username": "testuser",
      "password": "testpassword"
    }
    ```
  - Description: Use this endpoint to signup a user and obtain.
#### Task Management

- **Task List Endpoint:**
  - URL: `http://127.0.0.1:8000/api/tasks/`
  - Method: GET
  - Headers:
    - Authorization: Token <>your-auth-token<>
    - Content-Type: application/json
  - Description: Use this endpoint to retrieve a list of her tasks.
  
- **Create Task Endpoint:**
  - URL: `http://127.0.0.1:8000/api/tasks/`
  - Method: POST
  - Headers:
    - Authorization: Token <>your-auth-token<>
    - Content-Type: application/json
  - Request Body:
    ```json
    {
      "title": "taskssk5",
      "description": "this task is related to ssks",
      "due_date": "2023-07-09",
      "status": "pending"
    }
    ```
  - Description: Use this endpoint to create a new task with the provided details.
  
- **Task Update (PATCH) Endpoint:**
  - URL: `http://127.0.0.1:8000/api/tasks/<task-id>/`
  - Method: PATCH
  - Headers:
    - Authorization: Token <>your-auth-token<>
    - Content-Type: application/json
  - Request Body (Example to update the title):
    ```json
    {
      "status": "completed"
    }
    ```
  - Description: Use this endpoint to partially update a task by providing the fields you want to change.

- **Task Update (PUT) Endpoint:**
  - URL: `http://127.0.0.1:8000/api/tasks/<task-id>/`
  - Method: PUT
  - Headers:
    - Authorization: Token <>your-auth-token<>
    - Content-Type: application/json
  - Request Body (Example to update all fields):
    ```json
    {
      "title": "Updated Task Title",
      "description": "Updated task description",
      "due_date": "2023-08-15",
      "status": "completed"
    }
    ```
  - Description: Use this endpoint to fully update a task by providing all the fields.

- **Task Delete Endpoint:**
  - URL: `http://127.0.0.1:8000/api/tasks/<task-id>/`
  - Method: DELETE
  - Headers:
    - Authorization: Token <>your-auth-token<>
  - Description: Use this endpoint to delete a task by specifying its ID.

## Testing
- Unit tests have been included for key components, such as user registration, task creation, and task editing.
- Use Django's testing framework to run the tests.

To run the tests, use the following command:
```
  python manage.py test
```

## Usage
- Register a new user account and log in account you created during Registration.

- Create, view, update, and delete tasks as a logged-in user.


<!-- ## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these guidelines:
- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and write tests if applicable.
- Submit a pull request with a clear description of your changes. -->

<!-- ## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. -->

<!-- ## Acknowledgments
- Thanks to the Django community for their excellent documentation and resources. -->
<!-- -  -->

