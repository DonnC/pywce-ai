Crew AI Base
```yaml
name: pywce_chatbot_creator
description: A CrewAI crew designed to create pywce chatbot templates based on user prompts.
agents:
  - name: PromptAnalyzer
    role: "Analyze the user's prompt and extract key requirements for the chatbot."
    tasks:
      - Extract chatbot goals and purpose.
      - Identify the types of templates needed (e.g., `button`, `text`, etc.).
      - Determine any domain-specific requirements (e.g., insurance, food ordering).
    knowledge_sources:
      - "knowledge_base/examples/chatbot_examples.md"
      - "knowledge_base/flows/faq_flow.md"

  - name: TemplateDesigner
    role: "Design the chatbot templates and flow based on the PromptAnalyzer's output."
    tasks:
      - Select appropriate templates (e.g., `button`, `text`, etc.).
      - Define conversation flow, including message structure and routes.
      - Ensure template hooks are correctly placed.
    knowledge_sources:
      - "knowledge_base/templates/button.md"
      - "knowledge_base/templates/text.md"
      - "knowledge_base/architecture/overview.md"

  - name: HookIntegrator
    role: "Integrate hooks into the templates for additional functionality."
    tasks:
      - Map hooks (e.g., `on-receive`) to the templates based on flow requirements.
      - Generate Python implementations for the hooks.
    knowledge_sources:
      - "knowledge_base/hooks/on_receive.md"
      - "knowledge_base/architecture/overview.md"

  - name: Validator
    role: "Validate the generated chatbot template for consistency and completeness."
    tasks:
      - Ensure routes match template definitions.
      - Validate YAML syntax.
      - Check for missing fields or hooks.
    knowledge_sources:
      - "knowledge_base/templates/button.md"
      - "knowledge_base/architecture/overview.md"

  - name: OutputGenerator
    role: "Compile the final chatbot template and present it to the user."
    tasks:
      - Merge all components into a cohesive YAML file.
      - Provide a summary of the chatbot flow.
    knowledge_sources:
      - "knowledge_base/architecture/overview.md"

workflow:
  - PromptAnalyzer: 
      output_to: TemplateDesigner
  - TemplateDesigner: 
      output_to: HookIntegrator
  - HookIntegrator: 
      output_to: Validator
  - Validator: 
      output_to: OutputGenerator
```