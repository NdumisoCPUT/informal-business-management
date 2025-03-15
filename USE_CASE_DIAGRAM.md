```mermaid
%% Use Case Diagram with Proper UML Format
graph TD;
  
  %% Define Actors
  actor BusinessOwner as "Business Owner"
  actor Customer as "Customer"
  actor Admin as "Admin"
  actor System as "System"
  actor MobileApp as "Mobile App"
  actor PaymentGateway as "Payment Gateway"

  %% Define Use Cases (Using Ovals)
  subgraph SystemBoundary["Informal Business Management App"]
    ManageInventory("Manage Inventory")
    TrackSales("Track Sales")
    GenerateReport("Generate Sales Report")
    MakePurchase("Make Purchase")
    ReceivePromotions("Receive Promotions")
    ManageSettings("Manage System Settings")
    SyncCloud("Sync Data with Cloud")
    ProcessPayment("Process Payment")
  end

  %% Define Relationships
  BusinessOwner -->|Uses| ManageInventory
  BusinessOwner -->|Uses| TrackSales
  BusinessOwner -->|Generates| GenerateReport
  Customer -->|Uses| MakePurchase
  Customer -->|Receives| ReceivePromotions
  Admin -->|Manages| ManageSettings
  System -->|Syncs| SyncCloud
  MobileApp -->|Integrates| ProcessPayment
  PaymentGateway -->|Processes| ProcessPayment

  %% Define Extensions & Inclusions
  GenerateReport -->>|Includes| TrackSales
  MakePurchase -->>|Includes| ProcessPayment
  SyncCloud -->>|Includes| TrackSales

