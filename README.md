# ComfyUI Ai土豆-GPT助手插件

## 功能简介
本插件为ComfyUI集成了土豆-GPT API，支持多模态输入（文本+图像），可生成视频/动画提示词，支持模型选择、参数调节、历史管理等。

## 安装方法
1. 将本文件夹（comfy_ai_tudou）放入 `ComfyUI/custom_nodes/` 目录下。
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 重启ComfyUI。

## 使用方法
1. 在ComfyUI界面中，添加"土豆-GPT提示生成器"节点（AiTudouPromptGenerator）。
2. 填写API Key（建议用环境变量或配置文件管理密钥安全）。
3. 输入文本提示，可选上传图像。
4. 可调节模型、随机度、最大token、细节模式等参数。
5. 点击运行，节点将调用土豆-GPT API生成提示词。
6. 前端支持API连接状态指示和测试按钮。

## 依赖
- requests
- pillow

## 常见问题
- 若API调用失败，请检查API Key和网络连接。
- 图像输入需为ComfyUI标准IMAGE类型。
- 如需扩展历史管理、模板系统等功能，可参考源码注释。

## 进阶扩展建议
- 支持对话历史管理、动作模板、预设保存/加载
- API密钥隐藏、请求缓存、异步调用、错误友好提示

---
如有问题或建议，欢迎反馈！ 