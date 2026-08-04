# Bulk Email Sender with Mailpit Testing

A lightweight, automated Python script designed to send personalized bulk emails using the SMTP protocol. This project features dynamic payload customization (injecting recipient names into the email subject and body) and is pre-configured to log errors and test safely using **Mailpit** as a local, fake SMTP server.

---

## 🚀 Features

* **Bulk Personalization**: Dynamically injects recipient names into both the email subject line and body text.
* **CSV Data Source**: Reads receiver details efficiently using Python's native `csv.DictReader`.
* **Safe Testing Environment**: Pre-configured to route emails through [Mailpit](https://github.com/axllent/mailpit) to intercept and preview emails without sending them to real addresses.
* **Error Logging**: Catches delivery failures and appends timestamped error tracking to a local log file.
* **Resource Management**: Uses Python `with` context managers to guarantee secure file handling and server connection closures.

---

## 🛠️ Prerequisites

Before running the script, ensure you have the following installed on your local machine:

1. **Python 3.x** – [Download Python](https://www.python.org/)
2. **Mailpit** – An open-source email and SMTP testing tool. 
   * Install via Homebrew (macOS): `brew install mailpit`
   * Install via Docker: `docker run -d --name=mailpit -p 8025:8025 -p 1025:1025 axllent/mailpit`
   * Or download the binary directly from the [Mailpit Releases Page](https://github.com/axllent/mailpit/releases).

---

## 📁 Project Structure

```text
├── bulk_email_sender.py   # Main Python automation script
├── mailpit test_1.csv     # Input CSV file containing recipient metadata
└── error_file.text        # Append-only log file generated on delivery failures
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME
```

### 2. Prepare the Input Data
Create a file named `mailpit test_1.csv` in the root directory. Ensure it contains `Name` and `Email` headers exactly as shown below:

```csv
Name,Email
Alice Johnson,alice@example.com
Bob Smith,bob@example.com
Charlie Brown,charlie@example.com
```

### 3. Start Mailpit
Launch your local Mailpit instance. If using the direct binary or homebrew, run:
```bash
mailpit
```
* **SMTP Server** runs on: `localhost:1025`
* **Web UI Dashboard** runs on: `http://localhost:8025`

---

## 💻 Usage

1. Open the project folder in **VS Code**.
2. Run the Python script:
   ```bash
   python bulk_email_sender.py
   ```
3. Monitor your terminal output. Successful deliveries will display:
   ```text
   Connecting to email server...
   SUccessfully send Email to: Alice Johnson
   SUccessfully send Email to: Bob Smith
   ```
4. Open your browser and navigate to `http://localhost:8025` to view, inspect, and verify your formatted emails inside the Mailpit web dashboard.

---

## 🪵 Error Handling & Logs

If the SMTP server disconnects or a specific payload fails to send, the script catches the exception, prints it to the console, and appends a record to `error_file.text` with a standardized ISO timestamp:

```text
Error sending email: [Exception details here]
Error occurred at 2026-08-04 20:24:00
```

---

## 🔒 Security Note

The current implementation utilizes a hardcoded placeholder sender address (`mondaysamaila32@gmail.com`) pointing to a local testing environment (`localhost:1025`). **Before moving this script to a live production server** (such as Gmail SMTP or SendGrid):
* Remove hardcoded email strings.
* Transition credentials into an isolated `.env` file using libraries like `python-dotenv`.
* Upgrade the connection protocol from standard unsecured SMTP (`smtplib.SMTP`) to secure `smtplib.SMTP_SSL` or implement `STARTTLS`.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
