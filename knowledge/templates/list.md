# Template: List

## Description
The list template is used to present users with a limited list of options that they can select by clicking a list item.


## Fields
- **type**: Always `list` for this template.
- **message**:
  - **title**: *(Optional)* The title of the message displayed at the top.
  - **body**: The body of the message providing additional information or context.
  - **footer**: *(Optional)* Footer text displayed at the bottom of the message.
  - **sections**: A list of sections with rows. A max of 3 sections in total and 10 row items in total only
- **routes**: Maps item ids to their corresponding next template or action.

## Example 1
```yaml
1000:
  type: list
  message:
    title: "System"
    body: "Great choice, select your ERP of choice from the options below"
    button: "Select ERP"
    sections:
      "Open Source":        # <- section title
        0:                  # <- items (rows) under that section
          title: ERPNext
          description: A versatile, open-source ERP
        1:
          title: Odoo
          description: A versatile open-source system for a medium organization
     "Business" 
        2:
          title: SAP
          description: A commercial ERP for medium-large organization
        "other":
          title: Other
  routes:
    0: 2000
    1: 3000
    2: 4000
    "other": 5000
```

## Example 2
```yaml
1000:
  type: list
  message:
    title: "System"
    body: "Great choice, select your ERP of choice from the options below"
    button: "Select ERP"
    sections:
      "ERPs":
        0:
          title: ERPNext
          description: A versatile, open-source ERP
        1:
          title: Odoo
          description: A versatile open-source system for a medium organization
        2:
          title: SAP
          description: A commercial ERP for medium-large organization
        "other":
          title: Other
  routes:
    0: 2000
    1: 3000
    2: 4000
    "other": 5000
```