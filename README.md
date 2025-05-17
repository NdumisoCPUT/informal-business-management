# Informal Business Management App
A mobile-first application that helps informal SMEs manage inventory, track cash flow, and engage with customers.

## Board Customization Summary
To align our Kanban board with our project workflow and Agile best practices, we made several customizations to improve clarity, collaboration, and delivery:

## Custom Columns Added
Testing
Added to separate completed development work from work still under quality assurance. This ensures features are verified before being marked as complete.

Blocked
Introduced to highlight tasks that cannot proceed due to external dependencies, delays, or unresolved issues. This helps identify and resolve bottlenecks quickly.

In Review
Created to track tasks that are completed but awaiting peer or stakeholder review. This supports our Agile goal of continuous feedback.

Column Overview
Backlog: Unstarted tasks that are still in the queue.

Ready: Tasks that are ready to be picked up in the next cycle.

In Progress: Work currently being implemented by the team.

In Review: Tasks awaiting review before QA or completion.

Testing: Tasks undergoing verification or user testing.

Blocked: Tasks temporarily paused due to external factors.

Done: Fully completed and verified work.

## Why These Changes Were Made
These customizations help the team stay aligned on task status, identify delays early, and ensure we maintain quality before delivery. It also makes our board easier to read and helps visualize the full workflow from idea to deployment.

## Repository Justification

A generic `Repository<T, ID>` interface was used to avoid duplication across different entity repositories.

This approach allows defining standard CRUD operations once and reusing them across multiple entities like `InventoryItem`, `Order`, etc.  
It follows the **DRY (Don't Repeat Yourself)** principle, reduces code duplication, and ensures consistency across the repository layer.

## 🚀 Getting Started

This guide will help you set up the project locally for development and testing.

### Prerequisites
- Python 3.12+
- Git
- pip

### Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/informal-business-management.git
cd informal-business-management
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the API**

```bash
uvicorn src.api.main:app --reload
```

5. **Run tests**

```bash
pytest
```

---

## 🌟 Features for Contribution

Here are suggested areas for first-time and advanced contributors:

| Feature | Description | Label |
|--------|-------------|-------|
| API Error Handling | Improve exception messages for invalid input | `good-first-issue` |
| Swagger Enhancements | Add summaries/descriptions to all endpoints | `good-first-issue` |
| PDF Invoicing | Generate downloadable PDF receipts for orders | `feature-request` |
| Mobile Payments | Add support for mobile money APIs (e.g. MTN Momo) | `feature-request` |
| Retry Logic | Enhance PaymentService with retry mechanism | `feature-request` |
| Localization | Translate Swagger UI into isiXhosa/isiZulu | `feature-request` |

---

Want to contribute something not listed here? Check the [open issues](../../issues) or propose your idea in a new issue!


## System Documentation
- [System Specification](SPECIFICATION.md)
- [Architecture & C4 Diagrams](ARCHITECTURE.md)
- [Stakeholder Analysis](STAKEHOLDERS.md)
- [System Requirements](SYSTEM_REQUIREMENTS.md)
- [Reflection](REFLECTION.md)
- [Use Case Diagram](Use_Case_Diagram.md)
- [Use Case Specifications](Use_Case_Specifications.md)
- [User Stories](https://github.com/NdumisoCPUT/informal-business-management/wiki)
- [template-comparison](template-comparison.md)
-  [kanban_explanation](kanban_explanation.md)
-  [traceability_table](traceability_table.md)
-  [Activity_diagrams](Activity_diagrams.md)
- [State_Transition_Diagrams](State_Transition_Diagrams.md)
- [uml_modeling_reflection.md](uml_modeling_reflection.md)
- [Class Implementation](class-implementation-task.-1.md)
- [CHANGELOG](CHANGELOG.md)
- [Factory_vs_DI](Factory_vs_DI.md)
- [PROTECTION-RULE](PROTECTION-RULE.md)
- [PROTECTION](PROTECTION.md)
- [ci-pipeline-test-results](ci-pipeline-test-results.md)
- [pr-blocked-tests](pr-blocked-tests.md)
- [release-artifact-screenshot](release-artifact-screenshot.md)
- [workflows](workflows.md)
- [Code_of_Conduct](Code_Of_Conduct)
- [Contribution Guidelines](./Contribution.md)
- [Improvement Reflection](./IMPROVEMENT_REFLECTION.md)
- [Kanban Board Overview](./Board.md)
- [Swagger UI](./Swagger UI.md)
- [Domain Model](./Domain_Model.md)
- [Test Summary](./Test_Tests.md)

  


  
   




