# Object State Modeling (Prioritized)

To ensure clarity and alignment with system priorities, the following state transition diagrams are organized from most critical to least critical based on their role in the SME Digitalization App. The top priority is placed on objects that directly support core operations like inventory management and financial tracking.
## Inventory Item
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
    note right of Approved : [valid & confirmed]

    PendingReview --> Rejected : validate  
    note right of Rejected : [invalid or duplicate]

    Rejected --> Draft : edit /resubmit

    Approved --> Archived : autoArchive  
    note right of Archived : [age > 30 days]

```
## Order
```mermaid
stateDiagram-v2
    [*] --> Created : /startOrder

    Created --> Confirmed : confirmOrder  
    note right of Confirmed : [payment selected]

    Confirmed --> Paid : receivePayment  
    note right of Paid : [payment successful]

    Paid --> Fulfilled : deliverItems  
    note right of Fulfilled : [all items delivered]

    Created --> Canceled : cancelOrder  
    note right of Canceled : [before confirmation]

    Confirmed --> Canceled : cancelOrder  
    note right of Canceled : [before payment]

    Fulfilled --> [*]
    Canceled --> [*]

```
## Payment
```mermaid
stateDiagram-v2
    [*] --> Initiated : /startPayment

    Initiated --> Processing : submitPayment

    Processing --> Successful : validatePayment  
    note right of Successful : [payment valid]

    Processing --> Failed : validatePayment  
    note right of Failed : [payment invalid]

    Failed --> Retried : retryPayment

    Retried --> Processing : submitPayment

    Successful --> [*]


```

## UserAccount
```mermaid
stateDiagram-v2
    [*] --> Registered : /createAccount

    Registered --> EmailVerified : verifyEmail  
    note right of EmailVerified : [verification link clicked]

    EmailVerified --> Active : completeProfile  
    note right of Active : [profile info completed]

    Active --> Suspended : flagViolation  
    note right of Suspended : [user broke policy]

    Suspended --> Active : reinstateAccount  
    note right of Active : [admin approval]

    Active --> Deactivated : requestDeletion  
    Suspended --> Deactivated : adminDelete

    Deactivated --> [*]

```
## Promotion
```mermaid
stateDiagram-v2
    [*] --> Draft : /createPromotion

    Draft --> Scheduled : schedulePromotion  
    note right of Scheduled : [start & end date set]

    Scheduled --> Active : activatePromotion  
    note right of Active : [current date = start date]

    Active --> Expired : expirePromotion  
    note right of Expired : [current date > end date]

    Active --> Canceled : cancelPromotion  
    note right of Canceled : [manually canceled]

    Expired --> [*]
    Canceled --> [*]

```
## CustomerProfile
```mermaid
stateDiagram-v2
    [*] --> New : /createProfile

    New --> Active : firstPurchase  
    note right of Active : [✓ initial transaction completed]

    Active --> Loyal : checkLoyalty  
    note right of Loyal : [✓ purchases ≥ 10]

    Active --> Dormant : checkInactivity  
    note right of Dormant : [✗ no activity > 30 days]

    Dormant --> Active : newPurchase  
    note right of Active : [✓ user returned]

    Active --> Blocked : flagAbuse  
    note right of Blocked : [✗ fraud detected]

    Blocked --> [*]

```


