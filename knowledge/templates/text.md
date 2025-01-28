# Template: Text

## Description
The text template is used to collect free-text input from users.

## Fields
- **type**: Always `text` for this template.
- **prop**: *(Optional)* The property name to store the user input in session if necessary.
- **message**: The prompt or question to display to the user.
- **routes**: Defines the next step after the user input.

## Example 1: With prop and regex route
```yaml
"USER-INPUT":
  type: text
  prop: dob
  message: "Kindly provide your dob in the format YYYY-MM-DD"
  routes:
    "re:\\d{4}-\\d{2}-\\d{2}": "NEXT-STEP"
```

## Example 2: Without prop
```yaml
"USER-INPUT-FLOW":
  type: text
  message: "Type *yes* to continue or *back* to return to main menu"
  routes:
    "yes": "NEXT-STEP"
    "back": "MENU-STEP"
```
