from .api_client import OpenAIClient

class OpenAIGPTNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "api_key": ("STRING", {"default": ""}),
                "text_prompt": ("STRING", {"multiline": True}),
                "model": ([
                    "gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo",
                    "deepseek-chat", "deepseek-coder",
                    "google-gemini-pro", "google-gemini-1.5-pro",
                    "qwen-turbo", "qwen-plus", "qwen-max"
                ], {"default": "gpt-4o"}),
                "temperature": ("FLOAT", {"default": 0.5, "min": 0.0, "max": 1.0, "step": 0.01}),
                "max_tokens": ("INT", {"default": 2048, "min": 128, "max": 4096}),
                "detail_mode": (["high", "low"], {"default": "high"}),
            },
            "optional": {
                "input_image": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("generated_prompt",)
    FUNCTION = "generate"
    CATEGORY = "OpenAI GPT"

    def generate(self, api_key, text_prompt, model, temperature, max_tokens, detail_mode, input_image=None):
        client = OpenAIClient(api_key)
        params = {
            "text": text_prompt,
            "model": model,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "detail_mode": detail_mode,
            "image": input_image
        }
        result = client.generate_prompt(params)
        return (result,) 