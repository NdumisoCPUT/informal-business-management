# Use Case Diagram
<img width="415" alt="Informal Business Management App" src="https://github.com/user-attachments/assets/e3cdcd1e-89dd-45a4-b103-a56c6afc431f" />

# Key Actors & Their Roles
Business Owner: Can manage inventory, track sales, and generate sales reports.
Customer: Can make purchases and receive promotions.
Admin: Can manage system settings.
System: Handles automatic cloud syncing and authentication.
Mobile App: Provides an interface for all users to interact with the system.
Payment Gateway: Handles secure payment transactions.

# Relationships Between Actors & Use Cases
1. The Business Owner actor can initiate the Generate Sales Report use case, which depends on the Track Sales use case.


2. The Customer actor can initiate the Make Purchase use case, which depends on the Process Payment use case.


3. The System automatically runs the Sync Data with Cloud use case, which depends on both the Manage Inventory and Track Sales use cases.


