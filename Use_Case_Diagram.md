graph TD
  %% Actors
  BO([Business Owner])
  C([Customer])
  AD([Admin])
  SYS([System])
  MA([Mobile App])
  PG([Payment Gateway])

  %% Use Cases
  A1[User Login]
  A2[Authenticate User]
  A3[Manage Inventory]
  A4[Generate Sales Report]
  A5[Make Purchase]
  A6[Track Sales]
  A7[Receive Promotions]
  A8[Manage System Settings]
  A9[Sync Data with Cloud]
  A10[Process Payment]

  %% Relationships
  A1 --> A2
  BO --> A1
  BO --> A3
  BO --> A4
  BO --> A5
  BO --> A6

  C --> A5
  C --> A7

  AD --> A8
  AD --> A9

  A9 --> A4
  A9 --> A3

  A5 --> A10
  A10 --> PG
  A10 --> MA

  A1 --> SYS



# Actors And Their Roles
<img width="296" alt="Actors and Their Roles" src="https://github.com/user-attachments/assets/9a832d95-2343-44b3-8ecc-72accb06ebb5" />

# Relationships Between Actors & Use Cases
1. The Business Owner actor can initiate the Generate Sales Report use case, which depends on the Track Sales use case.
2. The Customer actor can initiate the Make Purchase use case, which depends on the Process Payment use case.
3. The System automatically runs the Sync Data with Cloud use case, which depends on both the Manage Inventory and Track Sales use cases.


