import argparse, json, zipfile
from pathlib import Path
CODE='0964D'; TITLE='PRESET_LIBRARY_VISIBLE_ENTRY_AGENT_GUIDANCE_READONLY_PREVIEW_APPLY'; SLUG='preset_library_visible_entry_agent_guidance_readonly_preview_apply_0964D'; EXPECTED_STATUS='PASS'; PREFIX=f"{CODE}_{TITLE}_"; MARKER='ALL_0964D_PRESET_LIBRARY_VISIBLE_ENTRY_AGENT_GUIDANCE_READONLY_PREVIEW_APPLY_CHECKS_OK'; FALSE_KEYS=['real_agent_runtime_modified', 'agent_runtime_modified', 'provider_called', 'retrieval_enabled', 'provider_context_injection', 'memory_store_written', 'memory_read', 'memory_write', 'registry_store_written', 'preset_library_store_written', 'real_registry_entry_created', 'active_preset_scheme_created', 'published_preset_scheme_created', 'agent_published', 'agent_activated', 'ordinary_teacher_activated', 'admin_publish_performed', 'admin_activation_performed', 'frontend_modified', 'frontend_workbench_index_modified', 'backend_modified', 'runtime_modified', 'endpoint_created', 'route_created', 'import_created', 'server_modified', 'field_level_full_explanation_created', 'all_fields_explanation_created', 'formal_generation_created', 'student_data_read', 'feishu_read', 'env_secret_read']
def load_json(path): return json.loads(Path(path).read_text(encoding="utf-8-sig"))
def find_external(root, explicit):
    if explicit: return Path(explicit)
    reports=root/"reports"/PREFIX.rstrip("_")
    if reports.exists(): return reports
    ext_root=root.parent/"xiaobei-core-external-reports"; matches=sorted(ext_root.glob(PREFIX+"*")) if ext_root.exists() else []
    if matches: return matches[-1]
    raise SystemExit(f"external report dir missing for {PREFIX}")
def assert_false(obj,label):
    bad=[k for k in FALSE_KEYS if obj.get(k) is not False]
    if bad: raise AssertionError(f"{label} forbidden flags not false: {bad}")
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--root",default="."); ap.add_argument("--external-dir",default=None); args=ap.parse_args()
    root=Path(args.root).resolve(); external=find_external(root,args.external_dir).resolve()
    contract=load_json(root/"docs/foundation"/f"{SLUG}.json"); result=load_json(external/f"{SLUG}_result.json"); checklist=load_json(external/f"{SLUG}_checklist.json"); manifest=load_json(external/f"{SLUG}_manifest.json")
    if contract.get("final_status")!=EXPECTED_STATUS or result.get("final_status")!=EXPECTED_STATUS: raise AssertionError("final_status mismatch")
    for label,obj in [("contract",contract),("result",result),("checklist",checklist)]: assert_false(obj,label)
    if contract.get("guidance_scope")!='preset_library_entry_only_not_all_fields': raise AssertionError("scope mismatch")
    if CODE in ['0964B','0964C','0964D','0964E','0964F']:
        schema=load_json(root/'docs/foundation/preset_library_visible_entry_agent_guidance_response_schema_0964B.json')
        for key in ['trigger','entry_explanation','forbidden_actions','field_level_full_explanation_created']:
            if key not in schema.get('required',[]): raise AssertionError(f'schema missing {key}')
    if CODE in ['0964D','0964E','0964F']:
        preview=load_json(root/'outputs/preset_library_guidance_0964D/agent_guidance_preview_0964D.json')
        if preview.get('preview_count')!=4: raise AssertionError('preview count mismatch')
        assert_false(preview,'preview')
        for r in preview.get('responses',[]):
            if r.get('scope_boundary')!='preset_library_entry_only_not_all_fields': raise AssertionError('response scope mismatch')
            if r.get('field_level_full_explanation_created') is not False: raise AssertionError('field explanation expanded')
    if CODE in ['0964E','0964F']:
        smoke=load_json(root/'outputs/preset_library_guidance_0964E/agent_guidance_smoke_0964E.json')
        if smoke.get('all_checks_pass') is not True or any(v is not True for v in smoke.get('checks',{}).values()): raise AssertionError('smoke failed')
        assert_false(smoke,'smoke')
    entries=manifest.get('zip_entries',[])
    if [n for n in entries if chr(92) in n or n.startswith('/') or '..' in Path(n).parts]: raise AssertionError('unclean zip entry')
    zip_path=external/manifest.get('zip_file',f'{SLUG}_review_package.zip')
    if zip_path.exists():
        with zipfile.ZipFile(zip_path,'r') as zf: names=zf.namelist()
        if sorted(names)!=sorted(entries): raise AssertionError('zip manifest mismatch')
    print(MARKER)
if __name__=='__main__': main()
