def remove_empty_fields(skill_dict: dict) -> dict:
    
    return {
        key: value
        for key, value in skill_dict.items()
        if isinstance(value, list) and len(value) > 0
    }