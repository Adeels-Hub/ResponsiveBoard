- In addition to stopping the default action, it also **stops event propagation** (both bubbling and capturing phases).

- Combines `event.preventDefault()` and `event.stopPropagation()` in one.

- Considered less explicit and discouraged in modern JavaScript because its dual behavior can lead to unexpected side effects.