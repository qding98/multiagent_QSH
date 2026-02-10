"""
LLM配置模块 (LLM Configuration Module)

管理DeepSeek API配置和LLM参数配置

配置项：
- DEEPSEEK_API_KEY: DeepSeek API密钥
- DEEPSEEK_BASE_URL: DeepSeek API基础URL
- DEEPSEEK_MODEL: 使用的模型名称
- llm_config: LLM配置字典
"""

import os

# ============================================================================
# DeepSeek API 配置
# ============================================================================

# 从环境变量读取API Key，如果不存在则使用占位符
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "sk-cc5b864ad13240a58f93c1f7b8f73ad8")
DEEPSEEK_BASE_URL = "https://api.deepseek.com"
DEEPSEEK_MODEL = "deepseek-chat"

# ============================================================================
# LLM 配置字典
# ============================================================================

llm_config = {
    "config_list": [
        {
            "model": DEEPSEEK_MODEL,
            "api_key": DEEPSEEK_API_KEY,
            "base_url": DEEPSEEK_BASE_URL,
        }
    ],
    "temperature": 0.7,  # 温度参数，控制生成的随机性
    "timeout": 120,      # 超时时间（秒）
}


def get_llm_config():
    """
    获取LLM配置字典

    Returns:
        dict: LLM配置字典
    """
    return llm_config


def validate_api_key():
    """
    验证API Key是否已配置

    Returns:
        bool: 如果API Key已配置返回True，否则返回False
    """
    if DEEPSEEK_API_KEY == "your-api-key-here":
        print("\n[错误] 请先配置您的 DeepSeek API Key！")
        print("方式1：设置环境变量 DEEPSEEK_API_KEY")
        print("方式2：在 config/llm_config.py 中直接修改 DEEPSEEK_API_KEY 变量")
        return False
    return True
