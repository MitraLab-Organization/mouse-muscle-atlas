#!/usr/bin/env python3
"""
Convert OWL ontology to JSON tree for interactive display.

Extracts owl:Class elements with rdfs:subClassOf (direct parent only),
rdfs:label, and IAO_0000115 (definition). Outputs a hierarchy suitable
for a collapsible tree with search.

Usage:
    python scripts/owl_to_tree.py
    python scripts/owl_to_tree.py --owl src/ontology/mma-edit.owl --output docs/ontology-tree.json
"""

import argparse
import json
import re
from pathlib import Path
from collections import defaultdict

ROOT_DIR = Path(__file__).parent.parent
DEFAULT_OWL = ROOT_DIR / "src" / "ontology" / "mma-edit.owl"
DEFAULT_OUTPUT = ROOT_DIR / "docs" / "ontology-tree.json"

# OBO IRI base
OBO_BASE = "http://purl.obolibrary.org/obo/"


def extract_id(iri: str) -> str:
    """Extract BAP_0000001 from full IRI."""
    if iri.startswith(OBO_BASE):
        return iri[len(OBO_BASE):]
    return iri.split("/")[-1] if "/" in iri else iri


def parse_owl(owl_path: Path) -> tuple[dict, dict]:
    """
    Parse OWL RDF/XML and extract class hierarchy.
    Returns (id -> {name, definition, parent_id}, children_map).
    """
    content = owl_path.read_text(encoding="utf-8")

    # Match owl:Class blocks with rdf:about
    class_pattern = re.compile(
        r'<owl:Class\s+rdf:about="([^"]+)"[^>]*>(.*?)</owl:Class>',
        re.DOTALL
    )

    # Match rdfs:subClassOf rdf:resource (direct parent, not Restriction)
    subclass_pattern = re.compile(
        r'<rdfs:subClassOf\s+rdf:resource="([^"]+)"\s*/>'
    )
    label_pattern = re.compile(
        r'<rdfs:label[^>]*>([^<]+)</rdfs:label>'
    )
    def_pattern = re.compile(
        r'<obo:IAO_0000115[^>]*>([^<]+)</obo:IAO_0000115>'
    )

    structures = {}
    for match in class_pattern.finditer(content):
        iri = match.group(1)
        body = match.group(2)

        # Skip if it's owl:Thing or external ontology (not BAP)
        if "BAP_" not in iri and "owl:" not in iri:
            continue

        struct_id = extract_id(iri)
        if not struct_id.startswith("BAP_"):
            continue

        # Get direct parent (first rdf:resource subClassOf, not owl:Restriction)
        parents = subclass_pattern.findall(body)
        parent_id = None
        for p in parents:
            pid = extract_id(p)
            if pid.startswith("BAP_") and "owl:" not in p:
                parent_id = pid
                break

        label_match = label_pattern.search(body)
        name = label_match.group(1).strip() if label_match else struct_id

        def_match = def_pattern.search(body)
        definition = def_match.group(1).strip() if def_match else ""

        structures[struct_id] = {
            "id": struct_id,
            "name": name,
            "definition": definition,
            "parent": parent_id,
        }

    return structures


def build_tree(structures: dict) -> list:
    """Convert flat structures to nested tree. Returns list of root nodes."""
    children = defaultdict(list)
    in_structures = set(structures.keys())
    for sid, s in structures.items():
        parent = s.get("parent")
        if parent in in_structures:
            children[parent].append(sid)
        else:
            children[None].append(sid)

    for parent in children:
        children[parent].sort(key=lambda x: structures.get(x, {}).get("name", x))

    def make_node(sid: str) -> dict:
        s = structures.get(sid, {})
        child_ids = children.get(sid, [])
        node = {
            "id": s["id"],
            "name": s["name"],
            "definition": s["definition"] or None,
        }
        if child_ids:
            node["children"] = [make_node(cid) for cid in child_ids]
        return node

    root_ids = children.get(None, [])
    return [make_node(rid) for rid in sorted(root_ids, key=lambda x: structures.get(x, {}).get("name", x))]


def main():
    parser = argparse.ArgumentParser(description="Convert OWL to JSON tree")
    parser.add_argument("--owl", type=Path, default=DEFAULT_OWL, help="Input OWL file")
    parser.add_argument("--output", "-o", type=Path, default=DEFAULT_OUTPUT, help="Output JSON file")
    args = parser.parse_args()

    if not args.owl.exists():
        print(f"Error: OWL file not found: {args.owl}")
        return 1

    print(f"Parsing {args.owl}...")
    structures = parse_owl(args.owl)
    print(f"  Found {len(structures)} classes")

    tree = build_tree(structures)
    output = {"structures": structures, "tree": tree}

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":
    exit(main())
