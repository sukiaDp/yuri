⚠️ **WIP (Work In Progress)**: This project is under development and not yet complete.
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
⚠️ **WIP（进行中，Work In Progress）**：此项目仍在开发中，尚未完成。
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
