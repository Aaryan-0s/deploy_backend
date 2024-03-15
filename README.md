# CAAS

## Configuration

The application requires a set of environment variables to be defined. These variables are used to configure the database connection.
This application also uses an SMTP backend for sending emails. You'll need to provide the SMTP server details in your `.env` file.

- Create a `.env` file in the root folder of the project and add the following variables:

        DB_DRIVER = driver
        DB_USER = username
        DB_PASS = password
        DB_HOST = host
        DB_PORT = port
        DB_NAME = DB_name


        MAIL_HOST = smtp.gmail.com
        MAIL_PORT = 587
        MAIL_USERNAME = gmail account
        MAIL_PASSWORD = your google account password OR app password
