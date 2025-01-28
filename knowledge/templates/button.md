# Template: Button

## Description
The button template is used to present users with a limited set of options that they can select by clicking a button.


## Fields
- **type**: Always `button` for this template.
- **message**:
  - **title**: *(Optional)* The title of the message displayed at the top.
  - **body**: The body of the message providing additional information or context.
  - **footer**: *(Optional)* Footer text displayed at the bottom of the message.
  - **buttons**: A list of button labels. A max of 3 only
- **routes**: Maps button labels to their corresponding next template or action.

## Example 1
```yaml
"START":
  type: button
  message:
    title: Welcome to Our Service
    body: "Choose an option to get started:"
    buttons:
      - Option 1
      - Option 2
  routes:
    "Option 1": "OPTION-1-TEMPLATE"
    "Option 2": "OPTION-2-TEMPLATE"
```