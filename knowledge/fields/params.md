# Field: params

## Description
This YAML template attribute makes it possible to pass static variables to business logic defined in the hook

## Use Cases
- Pass any static variables or arguments from templates to python hooks

## Example 1: Template
```yaml
"TEMPLATE-STAGE":
  type: text
  on-receive: "example.engine_chatbot.hooks.slack_service.notify_queue"
  message: "Type *yes* if you want to get notified on Slack, else type anything else to continue"
  params:
    type: NOTIFICATION_TYPE
    channel: SLACK
  routes:
    "re:.*": "NEXT-STEP"
```

## Example 1: Python
```python
# example.engine_chatbot.hooks.slack_service.py
from pywce import HookArg

def notify_queue(arg: HookArg) -> HookArg:
  """
  if user answers yes, add user to slack notification queue
  """
  print(f"Received hook arg: {arg}")
  
  params = arg.params

  if arg.user_input.lower() == "yes":
    if params.get('channel') == 'SLACK':
        if params.get('type') == 'NOTIFICATION_TYPE':
            slack_service = SlackService()
            slack_service.add_to_notify(arg.user.wa_id)
  
  return arg
```
