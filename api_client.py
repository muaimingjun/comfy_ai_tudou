import requests
import base64

class OpenAIClient:
    def __init__(self, api_key, base_url="https://api.openai.com/v1"):
        self.api_key = api_key
        self.base_url = base_url

    def generate_prompt(self, params):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        messages = []
        user_content = {"type": "text", "text": params["text"]}
        messages.append({"role": "user", "content": [user_content]})

        if params.get("image"):
            base64_image = self._image_to_base64(params["image"])
            image_content = {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/png;base64,{base64_image}",
                    "detail": params.get("detail_mode", "high")
                }
            }
            messages[0]["content"].append(image_content)

        payload = {
            "model": params.get("model", "gpt-4o"),
            "messages": messages,
            "temperature": params.get("temperature", 0.5),
            "max_tokens": params.get("max_tokens", 2048),
        }
        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=payload,
                timeout=20
            )
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
        except requests.exceptions.RequestException as e:
            return f"网络错误: {str(e)}"
        except KeyError as e:
            return f"API响应格式错误: {e}. 完整响应: {response.json()}"

    def _image_to_base64(self, image_tensor):
        from PIL import Image
        import io
        i = 255. * image_tensor.cpu().numpy()
        img = Image.fromarray(i.astype('uint8'))
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode('utf-8') 