Book Recommender App
Description
This is a book recommender app that recommends books to users.

Requirements
Docker
Usage
Clone the repository:
git clone https://github.com/savchart/book-recommender.git
cd book-recommender
Build the Docker image:
docker build -t book-recommender .
Start the container:
docker run -p 8000:8000 --net host book-recommender
Access the app in your web browser at localhost.
Stop the Docker container
To stop the Docker container, run the following command:
docker stop $(docker ps -aq --filter ancestor=book-recommender)
Customizing the app
The config.py file contains the app configuration settings. You can modify the file to suit your needs.
If you make changes to the app code, you will need to rebuild the Docker image and run the container again.

App structure:
Flask web application that provides a book recommendation service. Here is a basic application schema:

app.py: the main file of the Flask application that defines the API endpoints and routes requests to appropriate functions.

config.py: a module that stores the application configuration settings such as the database URI, Flask secret key, etc.

requirements.txt: a file that lists the dependencies required to run the application.

Dockerfile: a file that defines the steps to build a Docker image for the application.

scripts/create_db.py: a script that creates a SQLite database and loads the book data into it.

templates/index.html: a Jinja2 HTML template file that is used to render the front-end of the application.

static/css: a directory that stores the CSS files used for styling the front-end.

The application appears to have a standard Flask structure with a single blueprint named "books". 
