PROMPTS = {

    "casual": """
Rewrite the following text in a natural,
human conversational style.

Preserve all information.

Do not add new facts.

TEXT:
{text}
""",

    "professional": """
Rewrite the following text in a professional
business style.

Preserve all information.

TEXT:
{text}
""",

    "academic": """
Rewrite the following text in a formal academic style.

Keep all information unchanged.

TEXT:
{text}
""",

    "creative": """
Rewrite the following text naturally and creatively.

Do not change the meaning.

TEXT:
{text}
"""
}
