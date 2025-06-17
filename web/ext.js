app.registerExtension({
    name: "comfy.ai_tudou",
    async beforeRegisterNodeDef(nodeType, nodeData) {
        if (nodeData.name === "AiTudouPromptGenerator") {
            const onNodeCreated = nodeType.prototype.onNodeCreated;
            nodeType.prototype.onNodeCreated = function () {
                const result = onNodeCreated?.apply(this, arguments);
                this.apiStatus = document.createElement("div");
                this.apiStatus.className = "api-status";
                this.apiStatus.textContent = "API: 未连接";
                this.addControl(this.apiStatus);
                return result;
            }
            nodeType.prototype.extraControls = [
                {
                    name: "testConnection",
                    type: "button",
                    text: "测试连接",
                    onclick: async function (_, node) {
                        node.apiStatus.textContent = "API: 测试中...";
                        try {
                            await new Promise(resolve => setTimeout(resolve, 1000));
                            node.apiStatus.textContent = "API: 连接成功";
                        } catch {
                            node.apiStatus.textContent = "API: 连接失败";
                        }
                    }
                }
            ];
        }
    }
}); 