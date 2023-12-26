# config.py

class Config:
    # Database settings
    # Note: The following values are examples. Customize them with your own data.
    DB_HOST = "localhost"  # Database host address
    DB_PORT = 5432  # Database port
    DB_USERNAME = "your_db_user"  # Database username
    DB_PASSWORD = "your_db_password"  # Database password
    DB_NAME = "your_db_name"  # Database name

    # Email notification settings
    # Note: Enter your details to enable email notifications.
    EMAIL_ADDRESS = "your_email@example.com"  # Email address
    EMAIL_PASSWORD = "your_email_password"  # Email account password
    ADMIN_EMAIL = "admin@example.com"  # Administrator's email address

    # Other settings
    # Note: The following settings are examples. Customize them according to your needs.
    LOG_FILE_PATH = "security_analysis.log"  # Path to the log file
    DEBUG_MODE = False  # Debug mode

