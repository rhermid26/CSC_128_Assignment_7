# Tool Safety Scenarios

## 1. Function I did not write

I did not make an `unbook_room` function. If the chatbot had this function, it could remove someone's booking by mistake. I only made a `book_room` function that books a room and removes it from the available rooms.

## 2. If the model asks for a tool that does not exist

The agent checks if the tool is in `AVAILABLE_TOOLS`. If it is not there, the agent returns an `"Unknown tool"` message instead of trying to run it.

I tested this with:

```python
def test_unknown_tool():
    name = "delete_room"

    if name not in AVAILABLE_TOOLS:
        result = f"Unknown tool: {name}"

    assert result == "Unknown tool: delete_room"
```

This shows that a tool that does not exist will not be used.

## 3. Tool description I changed

My first description for `check_availability` was too short:

```text
Check study rooms.
```

The model did not always know when to use it.

I changed it to:

```text
Check which study rooms are free on a given weekday. Use this whenever a student asks about room availability.
```

This makes it clearer when the model should use the tool.
