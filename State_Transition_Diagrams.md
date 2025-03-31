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
