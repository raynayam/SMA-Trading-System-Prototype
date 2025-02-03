# Trading-Bot-Prototype-V1

# Trading Bot Deployment on Azure

This project demonstrates the deployment of a Python-based trading bot on Microsoft Azure. The bot interacts with the Tradovate API to execute trades and monitor market data.

## Features
- Real-time market data streaming via WebSocket.
- Automated trade execution based on predefined strategies.
- Secure credential management using Azure Key Vault.
- Logging and monitoring with Azure Monitor.

## Prerequisites
- Python 3.8+
- Azure account
- Tradovate API credentials

## Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/raynayam/trading-bot-prototype-V1.git
   cd trading-bot-prototype-v1
# Install Dependencies
pip install -r requirements.txt


# Set Up environment varaibles
Create and .env file and add your credentials
TRADOVATE_USERNAME=your_username
TRADOVATE_PASSWORD=your_password
AZURE_KEY_VAULT_URL=your_key_vault_url

 # Deploy to Azure using a virtual network and virtual machine on Azure. Good Luck in your Trading Journey :)
