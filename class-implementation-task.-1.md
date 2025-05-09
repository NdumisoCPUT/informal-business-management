# Class Implementation (Task 1)

This implementation uses **Python** as the preferred programming language because of its:
- Clear and readable syntax
- Object-oriented support
- Speed of development and testing capabilities

## Class Structure

All classes from the UML diagram have been implemented under the `/src` directory:
- UserAccount, Order, InventoryItem
- Payment, SalesReport, CashFlowEntry
- SystemSettings, PromotionalMessage

## Design Decisions

- All attributes are declared as **private** using double underscores (`__attribute`) to ensure encapsulation.
- Methods listed in the class diagram are included as part of each class, with room for further logic during pattern application.
- Class relationships are modeled using **composition**, for example:
  - `Order` contains multiple `InventoryItem` instances
  - `SalesReport` reflects information compiled from `Order` and `Payment`
- The `main.py` file demonstrates basic interaction:
  - Creating a user account
  - Creating inventory items
  - Creating and submitting an order
  - Calculating order totals

