def load_system_prompt(prompt_file_path: str, **kwargs: str) -> str:
    with open(prompt_file_path, 'r') as f:
        return f.read().format(**kwargs)


def build_tool_guidance() -> str:
    # TODO
    return "the tools are currently in development :), the system is not in prod yet" 
