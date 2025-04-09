Instead of modifying the prop directly in the child, you should:

1. Pass a function from the parent as a prop to allow updates.
2. Call this function inside the child component when an event (like a button click) occurs.
3. The parent updates its state, which then updates the prop value being passed down to the child.