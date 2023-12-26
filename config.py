# config.py

class Config:
    # Ustawienia dotyczące bazy danych
    # Uwaga: Poniższe wartości to przykładowe. Dostosuj je do swoich własnych danych.
    DB_HOST = "localhost"  # Adres hosta bazy danych
    DB_PORT = 5432  # Port bazy danych
    DB_USERNAME = "your_db_user"  # Nazwa użytkownika bazy danych
    DB_PASSWORD = "your_db_password"  # Hasło bazy danych
    DB_NAME = "your_db_name"  # Nazwa bazy danych

    # Ustawienia dla powiadomień email
    # Uwaga: Wprowadź swoje dane, aby umożliwić powiadomienia email.
    EMAIL_ADDRESS = "your_email@example.com"  # Adres e-mail
    EMAIL_PASSWORD = "your_email_password"  # Hasło do konta e-mail
    ADMIN_EMAIL = "admin@example.com"  # Adres e-mail administratora

    # Inne ustawienia
    # Uwaga: Poniższe ustawienia to przykładowe. Dostosuj je do swoich potrzeb.
    LOG_FILE_PATH = "security_analysis.log"  # Ścieżka do pliku dziennika logów
    DEBUG_MODE = False  # Tryb debugowania
