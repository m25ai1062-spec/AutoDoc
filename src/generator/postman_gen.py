
import json, os
from typing import Dict, Any

def llm_to_postman(llm_output: Dict[str, Any], base_url: str = 'http://localhost:8000') -> Dict[str, Any]:
    collection = {
        'info': {'name': 'AutoDoc Generated Collection', 'schema': 'https://schema.getpostman.com/json/collection/v2.1.0/collection.json'},
        'item': []
    }
    for ep in llm_output.get('endpoints', []):
        request = {
            'name': f"{ep['method']} {ep['path']}",
            'request': {
                'method': ep['method'],
                'header': [],
                'url': {'raw': base_url + ep['path'], 'host': [base_url], 'path': ep['path'].strip('/').split('/') if ep['path']!='/' else ['']}
            }
        }
        collection['item'].append(request)
    return collection

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('llm')
    p.add_argument('--out', default='examples/sample_collection.postman_collection.json')
    args = p.parse_args()
    out = llm_to_postman(json.load(open(args.llm)))
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, 'w') as f:
        json.dump(out, f, indent=2)
    print('Saved Postman collection to', args.out)
