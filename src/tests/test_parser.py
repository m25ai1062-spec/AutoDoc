
from src.parser.parser import parse_fastapi_file
import os

def test_parse_sample_app():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    app_path = os.path.join(repo_root, 'examples', 'sample_fastapi_app', 'main.py')
    parsed = parse_fastapi_file(app_path)
    assert 'endpoints' in parsed
    assert any(e['path'] == '/hello' for e in parsed['endpoints'])
