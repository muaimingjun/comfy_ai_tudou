from .nodes import AiTudouPromptGenerator

NODE_CLASS_MAPPINGS = {
    "AiTudouPromptGenerator": AiTudouPromptGenerator
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "AiTudouPromptGenerator": "土豆-GPT提示生成器"
}
WEB_DIRECTORY = "./web"
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY'] 