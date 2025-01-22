# Chatbot Examples

## Example 1: Food Ordering Bot
```yaml
"START-ORDER":
  type: button
  message:
    title: Food Order
    body: "What type of food would you like to order?"
    buttons:
      - Pizza
      - Sushi
      - Burgers
  routes:
    "Pizza": "PIZZA-MENU"
    "Sushi": "SUSHI-MENU"
    "Burgers": "BURGER-MENU"
```

## Example 2: Insurance Claims Bot
```yaml
"CLAIM-START":
  type: button
  message:
    title: Insurance Claim
    body: "How can we assist you today?"
    buttons:
      - File a Claim
      - Check Claim Status
      - Speak to an Agent
  routes:
    "File a Claim": "CLAIM-DETAILS"
    "Check Claim Status": "CLAIM-STATUS"
    "Speak to an Agent": "AGENT-CONTACT"
```
