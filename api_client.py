import requests
import base64

class AiTudouClient:
    def __init__(self, api_key, base_url="https://ai.ai-tudou.com/v1"):
        self.api_key = api_key
        self.base_url = base_url

    def generate_prompt(self, params):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        messages = [{"role": "user", "content": params["text"]}]
        if params.get("image"):
            base64_image = self._image_to_base64(params["image"])
            messages[0]["content"] = [
                params["text"],
                {"type": "image_url", "image_url": f"data:image/png;base64,{base64_image}"}
            ]
        payload = {
            "model": params.get("model", "gpt-4o"),
            "messages": messages,
            "temperature": params.get("temperature", 0.5),
            "max_tokens": params.get("max_tokens", 2048),
            "detail": params.get("detail_mode", "high")
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
        except KeyError:
            return "API响应格式错误"

    def _image_to_base64(self, image_tensor):
        from PIL import Image
        import io
        i = 255. * image_tensor.cpu().numpy()
        img = Image.fromarray(i.astype('uint8'))
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode('utf-8') 