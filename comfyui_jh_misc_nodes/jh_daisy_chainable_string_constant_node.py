import re
from typing import Any


class JHDaisyChainableStringConstantNode:
    @classmethod
    def INPUT_TYPES(cls) -> dict[str, Any]:
        return {
            "required": {},
            "optional": {
                "text": (
                    "STRING",
                    {
                        "multiline": True,
                        "dynamicPrompts": False,
                        "default": "",
                    },
                ),
                "input_text": (
                    "STRING",
                    {
                        "multiline": True,
                        "dynamicPrompts": False,
                        "default": "",
                        "forceInput": True,
                    },
                ),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "execute"
    CATEGORY = "JH Misc. Nodes"
    EXPERIMENTAL = True

    def execute(self, text: str, input_text: str = "") -> tuple[str]:
        text = re.sub(r"\n+", " ", text).strip()
        if input_text is not None:
            text = f"{input_text} {text}".strip()

        return (text,)