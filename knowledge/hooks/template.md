# Hook: template

## Description
This hook is used for processing any business logic to do with dynamically creating or populating a message template.

## Use Cases
- Dynamically create a message.
- Fill in dynamic variables
- Fill in `flow` template types with initial flow payload.

## Example 1: Template
```yaml
"TEMPLATE-STAGE":
  type: text
  template: "example.engine_chatbot.hooks.greeting.username"
  message: "Good day {{ name }}. How are you today?"
  routes:
    "re:.*": "NEXT-STEP"
```

## Example 1: Python
```python
# example.engine_chatbot.hooks.greeting.py
from pywce import hook, HookArg, TemplateDynamicBody
from pywce.engine_logger import get_engine_logger

logger = get_engine_logger(__name__)

@hook
def username(arg: HookArg) -> HookArg:
    """
    A template to get default user whatsapp username.
    """
    logger.info(f"Received hook arg: {arg}")

    # set render payload data to match the required template dynamic var
    arg.template_body = TemplateDynamicBody(render_template_payload={"name": arg.user.name})

    return arg
```


## Example 2: Template
```yaml
"TEMPLATE-STAGE":
  type: text
  template: "example.engine_chatbot.hooks.greeting.username"
  message: "Good day {{ name }}. How are you today?"
  routes:
    "re:.*": "NEXT-STEP"

"NEXT-STEP":
  type: button
  message:
    title: Order
    body: "Nice to know you {{ s.uname }}. Would you like me to save your name for future chat?"
    footer: pywce
    buttons:
      - Save
      - Cancel
  routes:
    "save": "SAVE-NAME"
    "cancel": "PREVIOUS-STAGE"
```

## Example 2: Python
```python
# example.engine_chatbot.hooks.greeting.py
from pywce import hook, HookArg, TemplateDynamicBody, ISessionManager
from pywce.engine_logger import get_engine_logger

logger = get_engine_logger(__name__)


@hook
def username(arg: HookArg) -> HookArg:
    """
    A template to get default user whatsapp username.
    """
    logger.info(f"Received hook arg: {arg}")

    session: ISessionManager = arg.session_manager
    uid = arg.user.wa_id

    # set default username in session for retrieving later
    session.save(session_id=uid, key="uname", data=arg.user.name)

    # set render payload data to match the required template dynamic var
    arg.template_body = TemplateDynamicBody(render_template_payload={"name": arg.user.name})

    return arg
```
