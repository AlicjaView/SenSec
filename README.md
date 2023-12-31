# SenSec - System Monitoring, Analysis, and Security Tool
IN PREPARATION!

SenSec is an advanced tool created in Python that enables the monitoring, analysis, and security of computer systems. The project provides support for system protection, identification of potential threats, and response to unusual activities.

# Features

- System Log Monitoring: SenSec analyzes system logs to identify failed login attempts, unusual activity, and system changes.

- Attack Pattern Identification: Using the AttackPatternAnalyzer module, SenSec can detect attack patterns such as SQL injection attempts and brute force attacks.

- Vulnerability Analysis: SenSec allows for the analysis of system vulnerabilities, detection of security loopholes, and implementation of corrective actions.

- Advanced Network Scanning: Through the scanning module, SenSec can scan networks to find vulnerable hosts and potential threats.

# Installation

To install SenSec, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/SenSec.git`
2. Navigate to the project directory: `cd SenSec`
3. Install dependencies: `pip install -r requirements.txt`

# Repository Contents

- config.py: Configuration file with default setting values and informative comments.

- requirements.txt: File with project dependencies. It includes Python libraries required to run the project.
  
- .gitignore: A file containing expressions specifying which files and directories should be ignored by the Git version control system.

# Configuration

Before running SenSec, customize the settings in the `config.py` file according to your individual needs. Below are key settings that may require customization:

- Database Settings: Define the host address, port, username, password, and database name to configure the database connection.

  ```python
  DB_HOST = "localhost"
  DB_PORT = 5432
  DB_USERNAME = "your_db_user"
  DB_PASSWORD = "your_db_password"
  DB_NAME = "your_db_name"
  ```

- Email Notification Settings: Provide your email login credentials to configure email notifications. Also, enter the administrator's email address.

  ```python
  EMAIL_ADDRESS = "your_email@example.com"
  EMAIL_PASSWORD = "your_email_password"
  ADMIN_EMAIL = "admin@example.com"
  ```

- Other Settings: Customize other settings, such as the log file path or debug mode, according to your preferences.

  ```python
  LOG_FILE_PATH = "security_analysis.log"
  DEBUG_MODE = False
  ```

# Usage

Once configured, SenSec can be run using the `SenSec.py` file. Remember to adjust runtime arguments according to your specific needs.

`python SenSec.py`

# Project Support

If you want to contribute to the development of the SenSec project, feel free to report issues, create pull requests, and provide support to other users on the GitHub platform.

# License

SenSec is available under the [GNU General Public License v3.0 (GPL-3.0)](https://opensource.org/licenses/GPL-3.0).


This project was created by Alicja Wójcik.
