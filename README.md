# pyrogram-Massenger

With this source and using the Pyrogram library, we will have access to Telegram.
This source is under development.

## Pre Installation
Before you begin, make sure you have the following installed:
- [Python](https://www.python.org/downloads/) **version 3.10.12**

## Obtaining API Keys
1. Go to [my.telegram.org](https://my.telegram.org/auth) and log in using your phone number.
2. Select "API development tools" and fill out the form to register a new application.
3. Save the API_ID and API_HASH items.

## Installation

1. Clone this repo

You can download the [**repository**](https://github.com/mohammadabdi75/pyrogram-Massenger) by cloning it to your system and installing the necessary dependencies:

```bash
git clone https://github.com/mohammadabdi75/pyrogram-Massenger.git
cd pyrogram-Massenger
```
2. Install requirements
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
nano setUsername.py or receiver.py # Place Your API and Token and Channel ID
python3 setUsername.py or receiver.py
```
## Usage

Place Your API and Token and Channel ID
```python
# Codes for API_ID and CHANNEL should be without " "
API_ID= Your API_ID
API_HASH= "Your API_HASH"
TOKEN= "Your TOKEN"
CHANNEL= Your CHANNEL
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

