Instead of modifying the prop directly in the child, you should:
1. Pass a function from the parent as a prop to allow updates.
2. Call this function inside the child component when an event (like a button click) occurs.
3. The parent updates its state, which then updates the prop value being passed down to the child.
**What Actually Triggers Re-renders?**
A parent **only re-renders** when:
1- **Its state changes**, or    
2-**Its props change** (from _its_ parent, if it has one)
3-Or it's forced to re-render (e.g. via `forceUpdate()` in class components). 
So, whether or not a prop is **stored in parent state** doesn’t matter — what matters is whether something caused the **parent to re-render**, which would **re-render the child too**, unless memoization skips it. 