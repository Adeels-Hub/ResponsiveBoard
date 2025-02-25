- **Props are immutable**: React treats props as read-only to maintain a **unidirectional data flow** (from parent to child).
- **Direct modification won't trigger a re-render**: If you modify a prop directly inside a child component, React won’t detect the change, and the UI may not update as expected.
- **Maintains predictability and consistency**: Keeping data updates centralized in the parent ensures that the state is predictable and managed in one place.


