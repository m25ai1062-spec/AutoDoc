
import json
from src.parser.parser import parse_fastapi_file
from src.generator.generator import build_openapi_from_parsed, save_openapi_json, save_markdown_for_endpoints
from src.llm.llm_stub import generate_summary_and_tests, save_results
from src.generator.postman_gen import llm_to_postman

def run_pipeline(app_file: str, outdir: str = 'docs'):
    parsed = parse_fastapi_file(app_file)
    openapi = build_openapi_from_parsed(parsed)
    save_openapi_json(openapi, outdir + '/openapi.json')
    save_markdown_for_endpoints(parsed, outdir + '/endpoints')
    llm_out = generate_summary_and_tests(openapi)
    save_results(llm_out, outdir + '/llm_output.json')
    coll = llm_to_postman(llm_out)
    with open(outdir + '/sample_collection.postman_collection.json', 'w') as f:
        json.dump(coll, f, indent=2)
    print('Pipeline completed. Artifacts in', outdir)

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('app_file')
    p.add_argument('--out', default='docs')
    args = p.parse_args()
    run_pipeline(args.app_file, args.out)
