
import ast, json
from typing import Dict, Any

def parse_fastapi_file(path: str) -> Dict[str, Any]:
    """Parse a FastAPI Python module and extract endpoints metadata."""
    with open(path, 'r') as f:
        src = f.read()
    tree = ast.parse(src, filename=path)
    endpoints = []
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            for d in node.decorator_list:
                if isinstance(d, ast.Call) and hasattr(d.func, 'attr'):
                    method = d.func.attr
                    path = None
                    for kw in d.keywords:
                        if kw.arg == 'path':
                            if isinstance(kw.value, ast.Constant):
                                path = kw.value.value
                    if path is None and d.args:
                        first = d.args[0]
                        if isinstance(first, ast.Constant):
                            path = first.value
                    if path is None:
                        continue
                    summary = None
                    for kw in d.keywords:
                        if kw.arg == 'summary' and isinstance(kw.value, ast.Constant):
                            summary = kw.value.value
                    doc = ast.get_docstring(node)
                    if summary is None and doc:
                        summary = doc.split('\n')[0]
                    endpoints.append({
                        'function': node.name,
                        'path': path,
                        'method': method.upper(),
                        'summary': summary or '',
                    })
    return {'file': path, 'endpoints': endpoints}

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('file')
    p.add_argument('--out', default='docs/openapi.json')
    args = p.parse_args()
    parsed = parse_fastapi_file(args.file)
    print(json.dumps(parsed, indent=2))
    with open(args.out, 'w') as f:
        json.dump(parsed, f, indent=2)
