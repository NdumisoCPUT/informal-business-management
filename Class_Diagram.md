```mermaid
classDiagram
    class UserAccount {
        +userId
        +name
        +email
        +password
        +role
        +login()
        +logout()
        +updateProfile()
    }

    class Order {
        +orderId
        +status
        +dateCreated
        +totalAmount
        +submit()
        +cancel()
        +calculateTotal()
    }

    class Payment {
        +paymentId
        +amount
        +method
        +status
        +timestamp
        +process()
        +retry()
        +validate()
    }

    class InventoryItem {
        +itemId
        +name
        +quantity
        +price
        +restockThreshold
        +updateStock()
        +checkAvailability()
    }

    class CashFlowEntry {
        +entryId
        +amount
        +type
        +status
        +date
        +validateEntry()
        +archiveEntry()
    }

    class SalesReport {
        +reportId
        +dateRange
        +totalRevenue
        +itemsSold
        +generate()
        +export()
        +saveToHistory()
    }

    class PromotionalMessage {
        +messageId
        +content
        +channel
        +targetGroup
        +sentDate
        +createMessage()
        +send()
        +logDelivery()
    }

    class SystemSettings {
        +settingId
        +name
        +value
        +lastModified
        +updateSetting()
        +restoreDefault()
    }

    %% Relationships
    UserAccount --> Order : places
    Order --> Payment : has
    Order --> InventoryItem : includes
    UserAccount --> CashFlowEntry : creates
    UserAccount --> PromotionalMessage : sends
    SalesReport --> Order : compiledFrom
    SalesReport --> Payment : compiledFrom
    UserAccount --> SystemSettings : manages
