In browser-based apps, updating the DOM is done by a companion library called ReactDOM. In mobile apps, React Native uses native components to render the user interface.

In React apps, a component can only return a single element. To return multiple elements, we wrap them in a fragment, which is represented by empty angle brackets.

To render a list in JSX, we use the ‘array.map()’ method. When mapping items, each item must have a unique key, which can be a string or a number.

When state or props React creates a **new virtual DOM tree** and compares it with the **previous one** using a diffing algorithm.
So yes, **at the moment of diffing**, React holds:
1. **The previous virtual DOM** (the old state),    
2. **The new virtual DOM** (just created based on the updated state).