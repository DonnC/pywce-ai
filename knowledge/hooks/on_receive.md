# Hook: On-Receive

## Description
This hook is triggered when the system receives a specific event or input. It is used for processing or validating user inputs before continuing the conversation flow.

## Use Cases
- Storing user input in a database.
- Validating input (e.g., phone number, email).
- Triggering external APIs.

## Example
```yaml
"USER-VALIDATION":
  type: text
  on-receive: "example.engine_chatbot.hooks.validate_user"
  message: "Please provide your phone number:"
  routes:
    "re:.*": "VALIDATION-RESULT"
```