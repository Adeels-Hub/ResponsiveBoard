### 

1. **What are the different data types in JavaScript?**  
    **Answer**: JavaScript has the following data types:
    - Primitive: `String`, `Number`, `Boolean`, `Null`, `Undefined`, `Symbol`, `BigInt`.
    - Non-Primitive: `Object`.

---

2. **What is `var`, `let`, and `const`? How do they differ?**  
    **Answer**:
    - `var`: Function-scoped, can be re-declared, not block-scoped.
    - `let`: Block-scoped, cannot be re-declared.
    - `const`: Block-scoped, cannot be re-declared or reassigned.

---

3. **What is the difference between `null` and `undefined`?**  
    **Answer**:
    - `null`: Explicitly assigned to represent no value.
    - `undefined`: Default value for variables that have been declared but not assigned.

---

4. **Explain the difference between `==` and `===`.**  
    **Answer**:
    - `==`: Checks for value equality after type coercion.
    - `===`: Checks for strict equality (no type conversion).

---

5. **What is `hoisting` in JavaScript?**  
    **Answer**: Hoisting is JavaScript's behavior of moving variable and function declarations to the top of their scope during compilation.

---

6. **What are closures in JavaScript? Provide an example.**  
    **Answer**: A closure is a function that retains access to its outer scope even after the outer function has returned.
    
    javascript
    
    CopyEdit
    
    `function outer() {     let count = 0;     return function inner() {         count++;         console.log(count);     }; } const increment = outer(); increment(); // 1 increment(); // 2`
    

---

7. **What is the difference between synchronous and asynchronous programming?**  
    **Answer**:
    - Synchronous: Code is executed line-by-line.
    - Asynchronous: Code doesn't wait; it moves to the next line while an operation completes (e.g., using callbacks, promises).

---

8. **How does the `this` keyword work in JavaScript?**  
    **Answer**: `this` refers to the object that is currently executing the function. Its value depends on how the function is called.

---

9. **What is a `promise`? How is it different from callbacks?**  
    **Answer**: A `promise` represents a value that may be available in the future. Unlike callbacks, promises allow chaining with `.then()` and `.catch()` for cleaner syntax.

---

10. **What is an `arrow function`? How does it differ from regular functions?**  
    **Answer**:

- Arrow functions have a concise syntax and do not bind their own `this`.

javascript

CopyEdit

`const add = (a, b) => a + b; // Arrow function`

---

### **Functions and Scope**

11. **What is the difference between function declarations and function expressions?**  
    **Answer**:

- Declaration: `function foo() {}` (hoisted).
- Expression: `const foo = function() {};` (not hoisted).

---

12. **What is the difference between global and local scope?**  
    **Answer**:

- Global: Accessible everywhere in the program.
- Local: Accessible only within the function or block.

---

13. **What is an IIFE (Immediately Invoked Function Expression)?**  
    **Answer**: A function executed immediately after being defined.

javascript

CopyEdit

`(function () {     console.log("IIFE executed"); })();`

---

14. **How does JavaScript handle block-level scope?**  
    **Answer**: Variables declared with `let` and `const` have block-level scope, while `var` does not.

---

15. **What are default parameters in functions?**  
    **Answer**: Default values assigned to function parameters if no argument is passed.

javascript

CopyEdit

``function greet(name = "Guest") {     console.log(`Hello, ${name}`); } greet(); // "Hello, Guest"``

---

### **Objects and Prototypes**

16. **What is the difference between a `class` and a `prototype`?**  
    **Answer**:

- `class`: Syntactic sugar for creating objects with shared methods.
- `prototype`: Underlying mechanism for sharing methods across instances.

---

17. **How does inheritance work in JavaScript?**  
    **Answer**: Inheritance is achieved through prototypes (`Object.create()`) or `class` syntax.

---

18. **How do you create an object in JavaScript?**  
    **Answer**: Using object literals, constructors, or `Object.create()`.

javascript

CopyEdit

`const obj = { key: "value" };`

---

19. **What are the ways to iterate over an object in JavaScript?**  
    **Answer**:

- `for...in`
- `Object.keys()`
- `Object.entries()`

---

20. **What is the difference between `Object.create()` and using the `new` keyword?**  
    **Answer**:

- `Object.create()`: Creates an object with a specific prototype.
- `new`: Creates an instance of a constructor.

---

### **Event Handling**

21. **What is the difference between `event.preventDefault()` and `event.stopPropagation()`?**  
    **Answer**:

- `preventDefault()`: Stops the default behavior of an element.
- `stopPropagation()`: Stops the event from bubbling up the DOM.

---

22. **What is event delegation?**  
    **Answer**: A technique where a single event listener is added to a parent element to handle events on its child elements.

---

23. **How do you add and remove event listeners?**  
    **Answer**:

javascript

CopyEdit

`element.addEventListener("click", handler); element.removeEventListener("click", handler);`

---

24. **What are the phases of event propagation?**  
    **Answer**:

- Capturing phase
- Target phase
- Bubbling phase

---

25. **What is the difference between `addEventListener` and inline event handlers?**  
    **Answer**: `addEventListener` allows multiple handlers and better separation of concerns.

---

### **Asynchronous JavaScript**

26. **What is the `async`/`await` syntax?**  
    **Answer**: Syntactic sugar for working with promises, making asynchronous code look synchronous.

---

27. **How does the event loop work in JavaScript?**  
    **Answer**: The event loop handles asynchronous tasks by moving them from the task queue to the call stack.

---

28. **What is the purpose of `setTimeout` and `setInterval`?**  
    **Answer**:

- `setTimeout`: Executes a function after a delay.
- `setInterval`: Repeats execution at fixed intervals.

---

29. **Explain the difference between `call`, `apply`, and `bind`.**  
    **Answer**:

- `call`: Invokes a function with arguments passed individually.
- `apply`: Invokes a function with arguments passed as an array.
- `bind`: Returns a new function with bound context.

---

30. **What is a callback function?**  
    **Answer**: A function passed as an argument to another function and executed later.