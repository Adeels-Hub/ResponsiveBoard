<pre><code class="language-js">// 1. Object Literal
const obj1 = { name: "Adeel" };
console.log(obj1.name);

// 2. new Object()
const obj2 = new Object({ age: 30 });
console.log(obj2.age);

// 3. Constructor Function
function Person(name) { this.name = name; }
const obj3 = new Person("Ali");

// 4. ES6 Class
class Car { constructor(model) { this.model = model; } }
const obj4 = new Car("Tesla");

// 5. Object.create()
const proto = { greet() { return "Hi"; } };
const obj5 = Object.create(proto);

// 6. Factory Function
const createUser = (name) => ({ name });
const obj6 = createUser("Zara");

// 7. From JSON String
const jsonStr = '{"city":"Lahore"}';
const obj7 = JSON.parse(jsonStr);

// 8. Object.assign()
const obj8 = Object.assign({}, { x: 42 });
console.log(obj8.x); </pre></code>
