# PYWCE - Python WhatsApp ChatBot Engine

pywce is a template-driven python whatsapp chatbot engine. It allows developers to create whatsapp chatbot in a template driven approach.
It allows you define conversation flow and to focus on business logic.

## Key Components

1. **Templates**: YAML-based definitions for conversation steps.
2. **Hooks**: Python functions triggered at specific points (e.g. `on-receive`).
3. **Routes**: Define the flow of conversation based on user actions.
4. **Engine**: Handles the heavy lifting for you. Processes templates and integrates hooks for seamless execution.

## Supported Template Types

These are the YAML template "types" which corresponds to WhatsApp supported message types.

Below is the template type and the corresponding WhatsApp message type it produces when rendered on the WhatsApp user interface

`template_type > whatsapp_message_type`

- button > button or interactive button
- cta > (Call-To-Action) CTA url button
- text > text
- list > interactive list
- request-location > request_location (requests user to share their location)
- media > send image or document or sticker or video
- flow > interactive flow
- location > location
- dynamic > special type that can create any of the above template types dynamically

## Hook Types

Hooks are the python functions which superpower chatbot business logic.

Hooks supercharge the pywce engines. It makes it possible to hook custom, additional functionality during message processing.

A developer creates these to give the chatbot the ability to process information. They usually receive 1 argument, the `HookArg` model as below

```python
@dataclass
class WaUser:
    '''
    A WhatsApp user object, compute general whatsapp user data
    
    :name: default user name from whatsapp profile

    :wa_id: whatsapp waId which is the user whatsapp mobile number
    
    :msg_id: the current whatsapp message id
    
    :timestamp: the webhook message timestamp
    '''    
    name: str = None
    wa_id: str = None
    msg_id: str = None
    timestamp: str = None

@dataclass
class TemplateDynamicBody:
    '''
    Specifically used when processing templated message.
    
    :typ: The message type of the dynamically generated template. Used in dynamic template types
    
    :initial_flow_payload: Dict payload to act as initial WhatsApp Flow message data. When user defines a flow which takes initial data before its rendered to user. This parameter works with `flow` template message type
    
    :render_template_payload: Very useful for `template` hooks. Its used to dynamically populate 
    {{ var }} mustache or jinja like placeholders for dynamically generated template messages
    '''
    typ: MessageTypeEnum = None
    initial_flow_payload: Dict[str, Any] = None
    render_template_payload: Dict[str, Any] = None


    # main model
@dataclass
class HookArg:
    """
    The main hook parameter model

    :user: The current whatsapp user object
    
    :params: Defined in the YAML template as `params` field. These serves as static variables passed to hooks for any processing as required by the business logic
    
    :template_body: For templates or flows or dynamic body processing
    
    :from_trigger: Whether the message was triggered by template triggers
    
    :user_input: the raw user input, usually a str if message was a button or text
    
    :flow: The WhatsApp flow message, flow name
    
    :additional_data: Usually used when processing `router` hook on YAML template where it contains the next route to go to
    
    :session_manager: ISessionManager implementation. The engine user session manager instance.
    """
    user: WaUser
    params: Dict[str, Any] = field(default_factory=dict)
    template_body: TemplateDynamicBody = None
    from_trigger: bool = False
    user_input: str = None
    flow: str = None
    additional_data: Dict[str, Any] = None
    session_manager: ISessionManager = None
```

The engine supports the following hooks and their definitions and where they are usually used.
Hooks are segmented into Before and After. 
Before hooks are processed before a YAML template is processed for sending to WhatsApp.
After hooks are processed after user responds to a rendered YAML template message.

The following are the hooks in the order in which they are processed.

**Before Hooks**:
- `template`: Triggered before a message is send to user. Used to dynamically populate all `{{var}}` variables found in the template. Used to dynamically create a message.
- `on-generate`: Triggered as means to perform any other logic needed before a message is processed and send to user

**After Hooks**:
- `validator` - Mainly used to perform any necessary and required data validation or business logic validation
- `on-receive`: Triggered when an input is received. Usually used to save data to db, perform a network request, perform any computation as needed soon after user sends a respond.
- `middleware`: Triggered as means to perform any other business logic after a user replies.


## Workflow

1. User interaction starts with a `button` or `text` or any supported template type.
2. Hooks process inputs and guide the conversation.
3. Routes direct the user to the next template.
4. The engine manages state, input storage, and flow execution.
````
