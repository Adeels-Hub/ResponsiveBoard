Loss of `this` in Callbacks
When a function is passed as a callback, `this` can change unexpectedly (often becoming `undefined` or referring to the global object).

Event Handlers and `this`
In DOM event listeners, `this` often refers to the element the event was triggered on, not the object that registered the handler.

Method Extraction
When methods are passed around as references, `this` loses its original context.
