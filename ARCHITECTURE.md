# Informal Business Management App - Architecture

## 1. Introduction
### Project Title:
Informal Business Management App

### Domain:
Retail / Small Business

### Problem Statement:
Informal businesses struggle with manual inventory tracking, financial record-keeping, and customer engagement, leading to inefficiencies and lost revenue. This system aims to digitalize these processes with a mobile-first solution.

## 2. C4 Model Architecture

### 2.1 Context Diagram
**System Overview:**  
The system consists of a mobile application that enables business owners to manage their inventory, track sales, and engage with customers. The system interacts with external services for cloud storage, messaging, and authentication.

```mermaid
graph TD
    businessOwner["Business Owner"]
    mobileApp["Informal Business Management App"]
    firebaseDB["Firebase Database"]
    whatsappAPI["WhatsApp API"]
    firebaseAuth["Firebase Auth"]

    businessOwner -->|Uses| mobileApp
    mobileApp -->|Stores/Retrieves Data| firebaseDB
    mobileApp -->|Sends Promotions| whatsappAPI
    mobileApp -->|Authenticates Users| firebaseAuth

