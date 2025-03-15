```mermaid
graph TD;
  %% Define Actors
  BusinessOwner["Business Owner"]
  Customer["Customer"]
  Admin["Admin"]
  System["System"]
  MobileApp["Mobile App"]
  PaymentGateway["Payment Gateway"]

  %% Define Use Cases
  ManageInventory["Manage Inventory"]
  TrackSales["Track Sales"]
  GenerateReport["Generate Sales Report"]
  MakePurchase["Make Purchase"]
  ReceivePromotions["Receive Promotions"]
  ManageSettings["Manage System Settings"]
  SyncCloud["Sync Data with Cloud"]
  ProcessPayment["Process Payment"]

  %% Define Relationships
  BusinessOwner -- Uses --> ManageInventory
  BusinessOwner -- Uses --> TrackSales
  BusinessOwner -- Generates --> GenerateReport
  Customer -- Uses --> MakePurchase
  Customer -- Receives --> ReceivePromotions
  Admin -- Manages --> ManageSettings
  System -- Syncs --> SyncCloud
  MobileApp -- Integrates --> ProcessPayment
  PaymentGateway -- Processes --> ProcessPayment

  %% Organizing Layout
  classDef actor fill:#f9f,stroke:#333,stroke-width:2px;
  classDef usecase fill:#ccf,stroke:#333,stroke-width:2px;
  
  class BusinessOwner,Customer,Admin,System,MobileApp,PaymentGateway actor;
  class ManageInventory,TrackSales,GenerateReport,MakePurchase,ReceivePromotions,ManageSettings,SyncCloud,ProcessPayment usecase;
