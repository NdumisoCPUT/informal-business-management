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
| Element      | Explanation                                                            |
|----------------------|----------------------------------------------------------------------------------|
| **Key States**       | InStock, LowStock, OutOfStock, Reordered                                        |
| **Key Transitions**  | stockUpdate, placeRestock, receiveStock, manualCorrection                       |
| **Guard Conditions** | qty < threshold, qty == 0, qty restored, qty > 0                                 |
| **Actions**          | /initialSync, /logRequest, /updateQty                                            |
| **FR Mapping**       | FR-002 (Inventory tracking), FR-006 (Restock alerts), FR-007 (Notifications)     |


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
| **Element**          | **Explanation**                                                                 |
|----------------------|----------------------------------------------------------------------------------|
| **Key States**       | Draft, PendingReview, Approved, Rejected, Archived                              |
| **Key Transitions**  | submit, validate, edit, autoArchive                                              |
| **Guard Conditions** | valid & confirmed, invalid or duplicate, age > 30 days                           |
| **Actions**          | /addEntry, /resubmit                                                             |
| **FR Mapping**       | FR-003 (Track income/expenses), FR-004 (Reject invalid entries), FR-006 (Archive for reporting/loans) |

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
| **Element**          | **Explanation**                                                                 |
|----------------------|----------------------------------------------------------------------------------|
| **Key States**       | Created, Confirmed, Paid, Fulfilled, Canceled                                   |
| **Key Transitions**  | confirmOrder, receivePayment, deliverItems, cancelOrder                         |
| **Guard Conditions** | payment selected, payment successful, before confirmation, before payment        |
| **Actions**          | /startOrder                                                                      |
| **FR Mapping**       | FR-003 (Order lifecycle), FR-005 (Cancel orders before payment), FR-006 (Delivery tracking) |

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
| **Element**          | **Explanation**                                                                 |
|----------------------|----------------------------------------------------------------------------------|
| **Key States**       | Initiated, Processing, Successful, Failed, Retried                              |
| **Key Transitions**  | submitPayment, validatePayment, retryPayment                                    |
| **Guard Conditions** | payment valid, payment invalid                                                   |
| **Actions**          | /startPayment                                                                    |
| **FR Mapping**       | FR-004 (Validate payments), FR-006 (Retry failed transactions), FR-007 (Log payment attempts) |

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
| **Element**          | **Explanation**                                                                 |
|----------------------|----------------------------------------------------------------------------------|
| **Key States**       | Registered, EmailVerified, Active, Suspended, Deactivated                       |
| **Key Transitions**  | verifyEmail, completeProfile, flagViolation, reinstateAccount, requestDeletion, adminDelete |
| **Guard Conditions** | verification link clicked, profile info completed, policy violation, admin approval |
| **Actions**          | /createAccount                                                                   |
| **FR Mapping**       | FR-001 (User onboarding), FR-005 (Admin account control), FR-006 (Deactivation rights) |

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
| **Element**          | **Explanation**                                                                 |
|----------------------|----------------------------------------------------------------------------------|
| **Key States**       | Draft, Scheduled, Active, Expired, Canceled                                     |
| **Key Transitions**  | schedulePromotion, activatePromotion, expirePromotion, cancelPromotion          |
| **Guard Conditions** | start & end date set, current date = start date, current date > end date, manually canceled |
| **Actions**          | /createPromotion                                                                 |
| **FR Mapping**       | FR-008 (Manage promotions), FR-007 (Campaign lifecycle), FR-006 (Expire/archive promos) |

## CustomerProfile
```mermaid
stateDiagram-v2
    [*] --> New : /createProfile

    New --> Active : firstPurchase  
    note right of Active : [initial transaction completed]

    Active --> Loyal : checkLoyalty  
    note right of Loyal : [purchases ≥ 10]

    Active --> Dormant : checkInactivity  
    note right of Dormant : [no activity > 30 days]

    Dormant --> Active : newPurchase  
    note right of Active : [user returned]

    Active --> Blocked : flagAbuse  
    note right of Blocked : [fraud detected]

    Blocked --> [*]

```
| **Element**          | **Explanation**                                                                 |
|----------------------|----------------------------------------------------------------------------------|
| **Key States**       | New, Active, Loyal, Dormant, Blocked                                            |
| **Key Transitions**  | firstPurchase, checkLoyalty, checkInactivity, newPurchase, flagAbuse           |
| **Guard Conditions** | initial transaction completed, purchases ≥ 10, no activity > 30 days, fraud detected |
| **Actions**          | /createProfile                                                                   |
| **FR Mapping**       | FR-007 (Loyalty & engagement), FR-005 (Handle dormancy), FR-006 (Flag abuse)     |


