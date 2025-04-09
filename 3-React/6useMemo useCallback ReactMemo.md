- **`useMemo`**: When a derived value is computationally expensive and should only re-compute when specific dependencies change.
- **`useCallback`**: Useful when passing callbacks to child components (especially optimized ones like `React.memo`) to prevent unnecessary re-renders.
- **`React.memo`**: **Purpose**: Prevents a component from re-rendering if its props **haven't changed** (shallow comparison).

Non-Pure Components
- If the component relies on something outside of its props (e.g., global state, context, or mutable variables), `React.memo` won't prevent re-renders caused by those external dependencies.