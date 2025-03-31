# Object State Modeling (Prioritized)

To ensure clarity and alignment with system priorities, the following state transition diagrams are organized from most critical to least critical based on their role in the SME Digitalization App. The top priority is placed on objects that directly support core operations like inventory management and financial tracking.
## InventoryItem
```mermaid
stateDiagram-v2
    [*] --> InStock : /initialSync

    InStock --> LowStock : stockUpdate [qty < threshold]
    LowStock --> OutOfStock : stockUpdate [qty == 0]
    LowStock --> InStock : stockUpdate [qty restored]
    OutOfStock --> InStock : manualCorrection [qty > 0]

    OutOfStock --> Reordered : placeRestock /logRequest
    Reordered --> InStock : receiveStock /updateQty


```
## CashFLowEntry
```mermaid
stateDiagram-v2
    [*] --> Draft : /addEntry

    Draft --> PendingReview : submit

    PendingReview --> Approved : validate  
    note right of Approved : [✓ valid & confirmed]

    PendingReview --> Rejected : validate  
    note right of Rejected : [✗ invalid or duplicate]

    Rejected --> Draft : edit /resubmit

    Approved --> Archived : autoArchive  
    note right of Archived : [age > 30 days]




```
