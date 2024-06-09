# Image Downloader

## Description
The Image Downloader is a versatile script designed to download images from Google search results based on a specified search query string. It supports resizing of downloaded images and securely stores them in a PostgreSQL database.It emphasizes asynchronous programming techniques to optimize efficiency and comes equipped with a suite of unit tests to ensure reliability and robustness. Additionally, Docker containers are used for convenient project encapsulation and deployment.

## Features
- Fetch images from Google search results based on a specified query string.
- Limit the maximum number of images to be fetched.
- Resize downloaded images to specified dimensions.
- Securely store images in a PostgreSQL database.
- Asynchronous programming for optimized efficiency.
- Docker containers for easy project encapsulation and deployment.

## Usage
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install dependencies using `pip install -r requirements.txt`.
4. Set up a PostgreSQL database using docker-compose by using `docker-compose up --build`.
5. Run `main.py` to start the script.
6. Follow the prompts to enter the search query, maximum number of images, and PostgreSQL database connection details.
7. The script will download, resize, and store the images in the database.

## How to Run Tests
1. Navigate to the project directory.
2. Run `pytest` to execute all unit tests.


