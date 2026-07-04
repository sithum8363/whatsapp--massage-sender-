# WhatsApp Message Sender Automation

A Python automation project for scheduling and sending WhatsApp messages at a user-specified time. The project uses the `whatpy` library to automate message delivery through WhatsApp.

## Overview

This project was created to automate the process of sending a WhatsApp message based on a scheduled time. The user provides the message details and the required sending time, and the program handles the automated sending process.

## Features

- Automates WhatsApp message sending
- Supports time-based message scheduling
- Simple Python implementation
- Reduces the need to manually send scheduled messages
- Can be extended with a graphical user interface, contact management, or recurring schedules

## Technologies Used

- Python
- whatpy
- WhatsApp Web
- Web browser automation

## How It Works

The basic workflow of the project is:

1. Run the Python application.
2. Provide the required recipient information.
3. Enter the message to be sent.
4. Set the required sending time.
5. The application waits for the scheduled time.
6. The message is sent through WhatsApp automation.

## Installation

Clone the repository:

```bash
git clone https://github.com/sithum8363/whatsapp--massage-sender-.git
cd whatsapp--massage-sender-
```

Install the project dependency:

```bash
pip install whatpy
```

If the package name used by the project environment differs, check the imports in the Python source file and install the matching package.

## Usage

Run the main Python file from the project directory:

```bash
python main.py
```

If the repository uses a different entry-point filename, replace `main.py` with the actual Python filename.

Before running the program:

- Make sure you have an active internet connection.
- Make sure WhatsApp Web can be opened in your browser.
- Complete WhatsApp Web authentication if requested.
- Keep the computer active around the scheduled sending time.

## Example Project Structure

```text
whatsapp--massage-sender-/
├── main.py
├── requirements.txt
└── README.md
```

The actual repository structure may differ depending on the source filenames used in the project.

## Use Cases

This project can be useful for:

- Personal reminder messages
- Scheduled greetings
- Time-based notifications
- Learning Python automation
- Experimenting with messaging automation workflows

## Limitations

- The computer must be running when the scheduled message is sent.
- Internet connectivity is required.
- Browser and WhatsApp Web availability can affect automation.
- Changes to third-party libraries or the WhatsApp Web interface may affect functionality.
- Scheduled automation should be tested before relying on it for important communication.

## Responsible Use

Use this project only for legitimate communication with people who expect or consent to receive the messages. Avoid spam, harassment, excessive automated messaging, or attempts to bypass platform restrictions.

## Future Improvements

Possible improvements include:

- Add a Tkinter graphical user interface
- Add contact selection
- Support multiple scheduled messages
- Store scheduled messages in a local database
- Add recurring message schedules
- Add message history and status tracking
- Improve input validation and error handling
- Add configuration through environment variables

## Disclaimer

This project is intended for educational and personal automation purposes. It is not affiliated with or endorsed by WhatsApp.

## Author

Sithum Marasinghe
