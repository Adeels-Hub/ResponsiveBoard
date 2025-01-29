- Transform arrays without mutating the original.
- Used in almost all data transformation tasks.
- Shallow Copy except value types
```
const numbers = [1, 2, 3];
const squared = numbers.map(n => n ** 2);
console.log(squared); // [1, 4, 9]

```
