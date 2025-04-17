# Creational Patterns (Task 2)

This section documents the implementation of all six creational design patterns as required for this project.

## Directory

All pattern implementations are located in the `/creational_patterns/` directory.

## Pattern Use Cases in Context

| Pattern         | Use Case in SME App                            |
|----------------|--------------------------------------------------|
| Simple Factory | To create various promotional message formats (WhatsApp, SMS, Email) |
| Factory Method | To switch between payment processors (e.g., Card, PayPal)            |
| Abstract Factory | To generate related inventory item types like bakery or beverages |
| Builder         | To build structured and customizable sales reports |
| Prototype       | To clone existing orders for recurring purchases |
| Singleton       | To manage global system settings across components |

## How to Run the Demonstration

Use the `main.py` file in the project root to test all patterns:

```bash
python main.py

