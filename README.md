# Xiaobei 0964 Preset Library Agent Guidance Review

This review area contains the 0964A-F preset-library visible-entry agent-guidance v0 artifacts.

Scope:
- Entry-level guidance for the visible preset-library card only.
- Not full field-level explanation.
- No frontend/backend/runtime/provider/memory/registry write.
- No draft preference write or publish/activate.

Local validation:

```powershell
python -m py_compile scripts/validate_preset_library_visible_entry_agent_guidance_scope_contract_0964A.py scripts/validate_preset_library_visible_entry_agent_guidance_response_schema_contract_0964B.py scripts/validate_preset_library_visible_entry_agent_guidance_fixture_contract_0964C.py scripts/validate_preset_library_visible_entry_agent_guidance_readonly_preview_apply_0964D.py scripts/validate_preset_library_visible_entry_agent_guidance_smoke_0964E.py scripts/validate_preset_library_visible_entry_agent_guidance_v0_seal_0964F.py
python scripts/validate_preset_library_visible_entry_agent_guidance_v0_seal_0964F.py --root . --external-dir reports/0964F_PRESET_LIBRARY_VISIBLE_ENTRY_AGENT_GUIDANCE_V0_SEAL_20260607_081529
```

Key status:
- 0964A=CONTRACT_PASS
- 0964B=CONTRACT_PASS
- 0964C=CONTRACT_PASS
- 0964D=PASS
- 0964E=PASS
- 0964F=SEALED
- NEXT_STAGE=0965A_PRESET_DRAFT_PREFERENCE_SELECTION_GATE
