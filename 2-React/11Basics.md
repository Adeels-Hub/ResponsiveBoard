we don’t query and update the DOM. Instead, we describe our application using small, reusable components. React will take care of efficiently creating and updating DOM elements.

React components can be created using a function or a class. Function-based components are the preferred approach as they’re more concise and easier to work

When our application starts, React takes a tree of components and builds a JavaScript data structure called the virtual DOM. 

When the state or the data of a component changes, React updates the corresponding node in the virtual DOM to reflect the new state. Then, it compares the current version of virtual DOM with the previous version to identify the nodes that should be updated. It’ll then update those nodes in the actual DOM.