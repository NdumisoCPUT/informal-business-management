# Domain Model 

This domain model captures the core entities, their attributes, methods, and relationships based on the system functionality established across Assignments 4, 6, and 8.

| **Entity**        | **Attributes**                                     | **Methods**                                | **Relationships**                                      |
|-------------------|----------------------------------------------------|---------------------------------------------|---------------------------------------------------------|
| UserAccount       | userId, name, email, password, role                | login(), logout(), updateProfile()         | Places Order, Sends Payment, Manages Settings          |
| Order             | orderId, status, dateCreated, totalAmount          | submit(), cancel(), calculateTotal()       | Has InventoryItem, Linked to Payment                   |
| Payment           | paymentId, amount, method, status, timestamp       | process(), retry(), validate()             | Associated with Order                                  |
| InventoryItem     | itemId, name, quantity, price, restockThreshold    | updateStock(), checkAvailability()         | Included in Order                                      |
| CashFlowEntry     | entryId, amount, type, status, date                | validateEntry(), archiveEntry()            | Created by UserAccount                                 |
| SalesReport       | reportId, dateRange, totalRevenue, itemsSold       | generate(), export(), saveToHistory()      | Compiled from Orders and Payments                      |
| PromotionalMessage| messageId, content, channel, targetGroup, sentDate| createMessage(), send(), logDelivery()     | Sent by UserAccount                                    |
| SystemSettings    | settingId, name, value, lastModified               | updateSetting(), restoreDefault()          | Managed by Admin (UserAccount)                         |

---

### Business Rules

- A user must be authenticated to place an order or access financial records.
- Payments can be retried only if their status is "failed".
- Inventory items with zero stock cannot be included in a new order.
- Promotional messages must target a group before being sent.
- CashFlowEntry must be validated before being archived or used in reports.
- Sales reports are generated only for completed orders and processed payments.
- Only users with an Admin role can update System Settings.
