# pywce Engine Architecture

## Key Components
1. **Templates**: YAML-based definitions for conversation steps.
2. **Hooks**: Python functions triggered at specific points (e.g., `on-receive`).
3. **Routes**: Define the flow of conversation based on user actions.
4. **Engine**: Processes templates and integrates hooks for seamless execution.

## Supported Template Types
- `button`
- `text`
- `list`
- `request-location`
- `media`

## Hook Types
- `on-receive`: Triggered when an input is received.
- `validation`: Validates user inputs.
- `external-api`: Calls an external API.

## Workflow
1. User interaction starts with a `button` or `text` template.
2. Hooks process inputs and guide the conversation.
3. Routes direct the user to the next template.
4. The engine manages state, input storage, and flow execution.
