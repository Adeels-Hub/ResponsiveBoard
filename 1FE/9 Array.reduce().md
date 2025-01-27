- Aggregate array elements into a single value.
- Critical for complex array operations (e.g., summing values).

```
const numbers = [1, 2, 3, 4];
const sum = numbers.reduce((total, n) => total + n, 0);
console.log(sum); // 10

```