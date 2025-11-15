
import json, os
from typing import Dict, Any

def build_openapi_from_parsed(parsed: Dict[str, Any]) -> Dict[str, Any]:
    paths = {}
    for ep in parsed.get('endpoints', []):
        p = ep['path']
        if p not in paths:
            paths[p] = {}
        paths[p][ep['method'].lower()] = {
            'summary': ep.get('summary', ''),
            'responses': {
                '200': {'description': 'Successful response'}
            }
        }
    return {
        'openapi': '3.0.0',
        'info': {'title': 'Auto-generated API', 'version': '1.0.0'},
        'paths': paths
    }

def save_openapi_json(spec: Dict[str, Any], out_path: str):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        json.dump(spec, f, indent=2)

def save_markdown_for_endpoints(parsed: Dict[str, Any], out_dir: str):
    os.makedirs(out_dir, exist_ok=True)
    for ep in parsed.get('endpoints', []):
        fname = os.path.join(out_dir, f"{ep['method'].lower()}_{ep['path'].strip('/').replace('/', '_') or 'root'}.md")
        with open(fname, 'w') as f:
            f.write(f"# {ep['method']} {ep['path']}\n\n")
            f.write(f"**Summary:** {ep.get('summary','')}\n\n")
            f.write('**Generated examples:**\n\n')
            f.write('```json\n')
            f.write('{\n  "sample": "value"\n}\n')
            f.write('```\n')
