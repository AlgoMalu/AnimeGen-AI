import json
import jsonschema
from jsonschema import validate
import os

def load_schema(schema_name):
    schema_path = os.path.join(os.path.dirname(__file__), f"{schema_name}_schema.json")
    with open(schema_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def validate_storyboard(data):
    """
    验证分镜脚本是否符合 JSON Schema
    """
    schema = load_schema("storyboard")
    try:
        validate(instance=data, schema=schema)
        
        # 业务逻辑验证：总时长检查
        total_duration = data['script_metadata']['total_duration']
        sum_shots_duration = sum(shot['duration'] for shot in data['shots'])
        
        if abs(total_duration - sum_shots_duration) > 0.5:
            return False, f"Duration mismatch: Meta({total_duration}s) vs Shots({sum_shots_duration}s)"
            
        return True, "Success"
    except jsonschema.exceptions.ValidationError as e:
        return False, e.message
    except Exception as e:
        return False, str(e)

if __name__ == "__main__":
    # 测试用例
    test_data = {
        "script_metadata": {
            "title": "Test Video",
            "total_duration": 15,
            "aspect_ratio": "9:16",
            "style": "Realistic"
        },
        "shots": [
            {
                "shot_id": 1,
                "duration": 5,
                "story_beat": "Intro",
                "visual_desc": "A man walking",
                "shot_size": "Medium Shot"
            },
            {
                "shot_id": 2,
                "duration": 10,
                "story_beat": "Ending",
                "visual_desc": "Close up of face",
                "shot_size": "Close-up"
            }
        ]
    }
    is_valid, msg = validate_storyboard(test_data)
    print(f"Validation Result: {is_valid}, Message: {msg}")
