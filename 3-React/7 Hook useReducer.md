It’s like `useState`, but with:
- Centralized logic for **state transitions**.    
- Support for **multiple actions**.    
- A structure similar to Redux.<pre><code class="language-js">
function reducer(state, action) {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
    case 'reset':
      return { count: 0 };
    default:
      throw new Error('Unknown action: ' + action.type);
  }
}
</code></pre>