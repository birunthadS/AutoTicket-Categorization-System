# Prompts Used

## Main Classification Prompt

The system uses a structured prompt that instructs the Llama 3.2 model to:

* Analyze ticket subject and description.
* Select one category and one subcategory from predefined values.
* Assign a priority level (High, Medium, Low).
* Generate a short reason.
* Return only valid JSON.

## Few-Shot Examples

The prompt includes example tickets such as:

### Example 1

Subject:
VPN not connecting

Category:
Network

Subcategory:
VPN

Priority:
High

### Example 2

Subject:
Laptop not turning on

Category:
Hardware

Subcategory:
Laptop

Priority:
High

### Example 3

Subject:
Password reset required

Category:
Access & Authentication

Subcategory:
Password Reset

Priority:
Low

## Output Format

The AI model returns:

{
"category": "",
"subcategory": "",
"priority": "",
"reason": ""
}

## Validation

The output is validated against predefined category and subcategory mappings before being stored.
