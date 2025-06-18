from .nodes import OpenAIGPTNode

NODE_CLASS_MAPPINGS = {
    "OpenAIGPTNode": OpenAIGPTNode,
    "AiTuDou_GPTNode": OpenAIGPTNode  # 兼容老名字
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "OpenAIGPTNode": "土豆-GPT提示生成器",
    "AiTuDou_GPTNode": "土豆-GPT提示生成器"  # 兼容老名字
}
WEB_DIRECTORY = "./web"
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY'] 