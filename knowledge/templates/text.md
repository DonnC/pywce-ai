# Template: Text

## Description
The text template is used to collect free-text input from users.

## Fields
- **type**: Always `text` for this template.
- **prop**: The property name to store the user input.
- **message**: The prompt or question to display to the user.
- **routes**: Defines the next step after the user input.

## Example
```yaml
"USER-INPUT":
  type: text
  prop: user_message
  message: "Please describe your issue:"
  routes:
    "re:.*": "NEXT-STEP"
```
