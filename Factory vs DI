## Storage Abstraction Choice: Factory vs Dependency Injection

For this project, the **Factory Pattern** was chosen instead of Dependency Injection (DI).

The `RepositoryFactory` class is responsible for selecting the correct storage backend (e.g., InMemory or FileSystem) based on a given storage type.

Using the Factory Pattern allows:
- Easy switching between different storage implementations without modifying business logic.
- Centralized control of object creation.
- Simpler dependency management without needing an external DI framework.
- Support for the **Open/Closed Principle** (open for extension, closed for modification).

In contrast, Dependency Injection would have required external configuration to inject the repository at runtime, which was unnecessary for this project’s scale.

Therefore, the Factory Pattern provided a lightweight, effective abstraction for storage mechanisms.
