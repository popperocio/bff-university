# Backend University 2.0 Project

To run the backend using Docker for the first time:

1- Ensure Docker and Docker Compose are installed and running locally.
2- In your project directory, create a .env file based on the .env.example file.
3- Run the following commands in your terminal:

    ```
    docker-compose build
    docker-compose up
    ```

4- Verify that all services are running correctly.
5- If you want to run the app again, just run:

    ```
    docker-compose up
    ```

To set up and manage the backend using the Makefile:

1- Install dependencies:

    ```
    make install
    ```

2- Create and activate a virtual environment:

    ```
    make create-venv
    ```

3- Start the application:

    ```
    make start-app
    ```

4- Format the code:

    ```
    make format
    ```
5- Run tests:

    ```
    make test
    ```