# SMA-Trading-System-Prototype

# Trading system Deployment on Azure

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

## Technical Skills
- Programming: Python, Bash
- Cloud Platforms: Microsoft Azure (VNet, VM, Key Vault, Monitor)
- DevOps: CI/CD, systemd, logging, monitoring
- APIs: REST, WebSocket
- Security: Azure Key Vault, managed identities, network security groups (NSGs)

## Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/raynayam/trading-bot-prototype-V1.git
   cd trading-bot-prototype-v1


# Set Up a VPC
 Create a VPC and configure the IP range
 Divide the vpc into 2 subnets, one for public and one for private
 set up gateway for bot to access VPC
 Create route tables to control traffic between subnets and internet
 Set up SSH and API traffic

 #Launch Virtual Machine
  such as ubuntu or microsoft and install python installed
  assign security group (SSH & API traffic)
  use SFTP client or git to upload bot to VM


# Install Dependencies
pip install -r requirements.txt

  

 # Set Up environment varaibles
Create and .env file and add your credentials
TRADOVATE_USERNAME=your_username
TRADOVATE_PASSWORD=your_password
AZURE_KEY_VAULT_URL=your_key_vault_url

 # Deploy to Azure using a virtual network and virtual machine on Azure. Good Luck in your Trading Journey :)
