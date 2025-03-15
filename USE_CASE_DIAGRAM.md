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
  MakePurchase["Make Purchase"]
  ReceivePromotions["Receive Promotions"]
  GenerateReport["Generate Sales Report"]
  SyncCloud["Sync Data with Cloud"]
  ProcessPayment["Process Payment"]
  ManageSettings["Manage System Settings"]

  %% Define Relationships
  BusinessOwner -- Uses --> ManageInventory
  BusinessOwner -- Uses --> TrackSales
  BusinessOwner -- Generates --> GenerateReport
  Customer -- Uses --> MakePurchase
  Customer -- Receives --> ReceivePromotions
  System -- Syncs --> SyncCloud
  MobileApp -- Integrates --> ProcessPayment
  PaymentGateway -- Processes --> ProcessPayment
  Admin -- Manages --> ManageSettings
