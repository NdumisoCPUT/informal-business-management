# Use Case Specifications
This document outlines the specifications for eight critical use cases from the Informal Business Management App Use Case Diagram.

## Use Case: Manage Inventory
Actor: Business Owner
Precondition: User must be logged in.
Postcondition: Inventory is updated.
Basic Flow:
1. User navigates to the inventory management section.
2. User adds, updates, or removes a product.
3. System updates the inventory list.
4. Changes are saved and displayed.
Alternative Flow: If an invalid product is added, the system notifies the user and prevents the update.

## Use Case: Generate Sales Report
Actor: Business Owner
Precondition: Sales transactions must exist.
Postcondition: A report is generated and displayed.
Basic Flow:
1. User selects the sales report option.
2. User specifies the date range.
3. System compiles and displays the report.
4. User can download the report.
Alternative Flow: If no sales data is found, the system notifies the user with an appropriate message.

## Use Case: Make Purchase
Actor: Customer
Precondition: Product must be available in inventory.
Postcondition: Purchase is recorded, and inventory is updated.
Basic Flow:
1. Customer selects a product.
2. Customer proceeds to checkout.
3. System processes payment.
4. Purchase is completed, and confirmation is sent.
Alternative Flow: If payment fails, the purchase is not recorded, and the user is notified.

## Use Case: Receive Promotions
Actor: Customer
Precondition: Customer has opted into promotions.
Postcondition: Promotional message is received.
Basic Flow:
1. System identifies eligible customers.
2. System sends promotional messages via WhatsApp.
3. Customers receive the message.
Alternative Flow: If the message fails, the system retries sending or logs an error.

## Use Case: Manage System Settings
Actor: Admin
Precondition: Admin must be logged in.
Postcondition: System settings are updated.
Basic Flow:
1. Admin accesses system settings.
2. Admin modifies necessary configurations.
3. System saves and applies changes.
Alternative Flow: If an invalid configuration is provided, the system notifies the admin and prevents changes.

## Use Case: Sync Data with Cloud
Actor: System
Precondition: System must have internet access.
Postcondition: Data is synced successfully.
Basic Flow:
1. System detects unsynced data.
2. System initiates data synchronization.
3. Data is successfully updated in the cloud.
Alternative Flow: If the internet is unavailable, the system retries later.

## Use Case: Process Payment
Actor: Mobile App, Payment Gateway
Precondition: Valid payment details must be provided.
Postcondition: Payment is successfully processed.
Basic Flow:
1. Customer enters payment details.
2. System validates the payment information.
3. Payment is processed and confirmed.
Alternative Flow: If payment fails, the user is notified and requested to retry.

## Use Case: User Login
Actor: Business Owner, Customer, Admin
Precondition: User must have valid credentials.
Postcondition: User gains access to the system.
Basic Flow:
1. User enters login credentials.
2. System validates the input.
3. If correct, user is granted access.
Alternative Flow: If login fails, the system displays an error message.

