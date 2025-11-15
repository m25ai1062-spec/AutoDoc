
import json, os
from typing import Dict, Any

def generate_summary_and_tests(openapi_spec: Dict[str, Any]) -> Dict[str, Any]:
    results = {'endpoints': []}
    for path, methods in openapi_spec.get('paths', {}).items():
        for method, info in methods.items():
            summary = info.get('summary') or f"{method.upper()} {path}"
            tests = [
                {'name': 'positive', 'description': 'Expect 200 or success', 'request': {'method': method.upper(), 'path': path}},
                {'name': 'negative', 'description': 'Invalid input -> expect 4xx', 'request': {'method': method.upper(), 'path': path + '?bad=1'}}
            ]
            results['endpoints'].append({
                'path': path,
                'method': method.upper(),
                'summary': summary,
                'tests': tests
            })
    return results

def save_results(results: Dict[str, Any], out_path: str):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        json.dump(results, f, indent=2)
