#!/usr/bin/env python3
"""Builds catalog.json (the index the Agents Company app reads) from plugins/*/plugin.json. Standard library only."""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REQUIRED = ["id", "name", "description", "category", "developer", "website", "logo", "connection"]


def main():
    plugins, errors = [], []
    for d in sorted(os.listdir(os.path.join(ROOT, "plugins"))):
        path = os.path.join(ROOT, "plugins", d, "plugin.json")
        if not os.path.isfile(path):
            continue
        p = json.load(open(path))
        missing = [k for k in REQUIRED if k not in p]
        if missing:
            errors.append(f"{d}: missing {', '.join(missing)}")
        if p.get("id") != d:
            errors.append(f"{d}: id must match the folder name")
        if not os.path.isfile(os.path.join(ROOT, "plugins", d, p.get("logo", ""))):
            errors.append(f"{d}: logo file not found")
        c = p.get("connection", {})
        if c.get("type") == "mcp-oauth" and not str(c.get("mcp", "")).startswith("https://"):
            errors.append(f"{d}: mcp must be an https URL")
        p.setdefault("categories", [p.get("category")])
        plugins.append(p)
    if errors:
        sys.exit("\n".join(errors))
    out = json.dumps({"version": 1, "plugins": plugins}, indent=2, ensure_ascii=False) + "\n"
    if "--check" in sys.argv:
        current = open(os.path.join(ROOT, "catalog.json")).read() if os.path.exists(os.path.join(ROOT, "catalog.json")) else ""
        sys.exit(0 if current == out else "catalog.json is out of date: run scripts/build-catalog.py")
    open(os.path.join(ROOT, "catalog.json"), "w").write(out)
    print(f"catalog.json: {len(plugins)} plugins")


if __name__ == "__main__":
    main()
