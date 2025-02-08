#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
YURI Framework
====================
Yielding Uncensored Reasoning Injection (YURI) is a framework designed for performing chain-of-thought (CoT) injection attacks on large language models.
Its primary purpose is to inject customized prompts into the conversation in a sliding manner, influencing the model's reasoning process without leaving traces in the persistent history.

Features:
- Sliding injection of chain-of-thought (CoT) prompts.
- Support for multiple injection prompt types (e.g., r18_prompts, dangerous_prompts, test_prompts).
- Conversation history management with optional saving to JSON files.
- Configurable integration with the Ollama API.

Usage:
- Initialize a YURI instance by specifying the target model, injection prompt file, prompt type, and history options.
- Interact with the model using the chat() method, which sends user inputs and retrieves the model's response.
- Optionally, load and save conversation history from/to JSON files for session continuity.

Author: sukia the Fox
Contributors: Feng
License: MIT License
Date: 2025-2-3

Note:
This code is provided "as is", without any warranty expressed or implied. It is intended for research and educational purposes only. Use it at your own risk.

--------------------------------------------------------
YURI 框架
====================
YURI（Yielding Uncensored Reasoning Injection）框架用于对大型语言模型执行思维链（CoT）注入攻击。
主要目的是通过滑动注入模式将自定义提示词嵌入到对话中，从而影响模型的思维链，而不会在持久化历史中留下痕迹。

功能：
- 支持链式思考提示词（CoT）的滑动注入。
- 支持多种类型的注入提示词（例如 r18_prompts、dangerous_prompts、test_prompts）。
- 对话历史管理，可选地保存对话历史到 JSON 文件。
- 与 Ollama API 无缝集成，可灵活配置目标模型。

用法：
- 通过指定目标模型、提示词文件、提示词类型以及历史记录选项来初始化 YURI 实例。
- 使用 chat() 方法与模型交互，发送用户输入并获取模型回复。
- 可选地加载或保存对话历史，以便持续对话。

作者：sukia the Fox
贡献者： Feng
许可证：MIT 许可证
日期：2025-2-3

注意：
此代码按“原样”提供，不附带任何形式的明示或暗示保证，仅供研究和教育使用，风险自负。
"""

import ollama
import json
import os
import yaml
import copy

class YURI:
    def __init__(self, model, inject_prompt_path, prompt_type="r18_prompts", history_file=None, save_history=False):
        """
        Initialize the YURI instance.

        :param model: The target model name for attack.
        :param inject_prompt_path: File path for the injection prompt YAML.
        :param prompt_type: Type of injection prompt (e.g., "r18_prompts", "dangerous_prompts", "test_prompts").
        :param history_file: File path for conversation history (if available).
        :param save_history: Whether to save the conversation history.
        """
        self.model = model
        self.default_inject_prompt_path = inject_prompt_path  # 保存默认的 YAML 文件路径
        self.history = self.load_history(history_file) if history_file else []
        self.inject_prompt = self.load_inject_prompt("", prompt_type)
        self.save_history = save_history
        self.file_name = self.get_unique_filename() if save_history else None

    # Load the injection prompt from the YAML file based on the specified prompt_type.
    # If file_path is empty, use the default path provided during initialization.
    def load_inject_prompt(self, file_path, prompt_type):
        if not file_path:  # 如果 file_path 为空，则使用默认路径
            file_path = self.default_inject_prompt_path
        with open(file_path, 'r', encoding='utf-8') as file:
            prompts_data = yaml.safe_load(file)
        return prompts_data.get('prompts', {}).get(prompt_type, "")

    # Load conversation history from a JSON file.
    def load_history(self, history_file):
        with open(history_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data.get('conversation', [])

    # Generate a unique filename for saving the conversation history.
    def get_unique_filename(self):
        i = 1
        while os.path.exists(f'tests/test{i}.json'):
            i += 1
        return f'tests/test{i}.json'

    # Save the conversation history to a JSON file.
    def save_conversation(self):
        if self.save_history and self.file_name:
            with open(self.file_name, 'w', encoding='utf-8') as f:
                json.dump({"conversation": self.history}, f, ensure_ascii=False, indent=4)

    # Conduct a chat and return the model's response.
    def chat(self, user_input):
        # Append the user input to the conversation history.
        self.history.append({"role": "user", "content": user_input})

        # Create a copy of the history and append the injection prompt at the end
        # to form a pseudo input_message for sliding injection.
        input_message = copy.deepcopy(self.history)
        input_message.append({"role": "assistant", "content": self.inject_prompt})

        # Send the request to the Ollama API.
        response = ollama.chat(model=self.model, messages=input_message, options={"temperature": 1.3})

        # Retrieve the AI-generated response.
        ai_response = "<think>\n" + response["message"]["content"]

        # Record the AI's response (with a disguised chain-of-thought indicator).
        self.history.append({"role": "assistant", "content": ai_response})

        # Save the conversation history.
        self.save_conversation()

        return ai_response


if __name__ == "__main__":
    yuri = YURI(
        model="deepseek-r1:32b",
        inject_prompt_path="inject_prompt.yaml",
        prompt_type="r18_prompts",
        history_file=None,
        save_history=True
    )

    user_input = "在这里输入你的初始对话"
    # user_input = input("你:") 或取消此处注释，直接在命令行对话

    while True:
        if user_input.lower() in ["退出", "exit", "quit"]:
            break

        ai_response = yuri.chat(user_input)
        print("AI:" + ai_response)

        user_input = input("你:")

