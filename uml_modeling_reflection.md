## Comparing State Diagrams vs. Activity Diagrams

State diagrams helped me understand how individual objects behave across different stages in their lifecycle. For example, the `Order` object transitions from `Created` to `Confirmed`, `Paid`, and eventually `Fulfilled` or `Canceled`. These diagrams focus on object-specific behavior and event-triggered state changes.

Activity diagrams, on the other hand, were better suited for capturing complete workflows that involve both users and the system. Diagrams like “Make Purchase” or “Sync Data with Cloud” showed the sequence of actions, decisions, and even parallel flows between actors.

Although Mermaid doesn’t natively support full UML activity diagram syntax, I used `stateDiagram-v2` to implement both types. It allowed me to include start/end nodes, guards, decisions, and parallel actions using `fork` and `join`. For swimlanes, I simulated roles using naming conventions (e.g., `User_`, `System_`) to clarify responsibilities. While not perfect, it offered a consistent and lightweight way to model the logic directly in markdown.

