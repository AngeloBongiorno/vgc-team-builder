def load_system_prompt(prompt_file_path: str, **kwargs: str) -> str:
    with open(prompt_file_path, 'r') as f:
        return f.read().format(**kwargs)
