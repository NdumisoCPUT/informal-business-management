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
C4Context
    Person(businessOwner, "Business Owner", "Manages inventory, sales, and customer interactions")
    System(mobileApp, "Informal Business Management App", "Provides digital business tools")
    System_Ext(firebaseDB, "Firebase Database", "Stores inventory, sales, and customer data")
    System_Ext(whatsappAPI, "WhatsApp API", "Sends customer messages")
    System_Ext(firebaseAuth, "Firebase Auth", "Handles authentication")

    businessOwner -> mobileApp: Uses
    mobileApp -> firebaseDB: Stores/Retrieves data
    mobileApp -> whatsappAPI: Sends promotions
    mobileApp -> firebaseAuth: Authenticates users
