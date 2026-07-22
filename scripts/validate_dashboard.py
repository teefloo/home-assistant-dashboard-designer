#!/usr/bin/env python3
"""Validation statique prudente de fichiers Lovelace YAML.

Usage:
  python scripts/validate_dashboard.py dashboard.yaml
  python scripts/validate_dashboard.py dashboards/

PyYAML est optionnel mais nécessaire pour valider la syntaxe YAML.
Le script ne remplace pas le chargement réel dans Home Assistant.
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

PLACEHOLDER_RE = re.compile(r"\b(?:REPLACE_ME_[A-Z0-9_]+|TODO_ENTITY|ENTITY_ID_HERE)")
CUSTOM_CARD_RE = re.compile(r"\btype\s*:\s*custom:([A-Za-z0-9_-]+)")
ENTITY_RE = re.compile(r"\b(?:entity|entity_id)\s*:\s*['\"]?([a-z_][a-z0-9_]*\.[a-zA-Z0-9_]+)")
CARD_MOD_RE = re.compile(r"\bcard_mod\s*:")


def yaml_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    return sorted(p for p in path.rglob("*") if p.suffix.lower() in {".yaml", ".yml"})


def parse_yaml(text: str, source: Path) -> str | None:
    try:
        import yaml  # type: ignore
    except ImportError:
        return "PyYAML absent : syntaxe YAML non parsée (pip install pyyaml)."
    try:
        yaml.safe_load(text)
    except Exception as exc:
        return f"Erreur YAML : {exc}"
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    args = parser.parse_args()

    if not args.path.exists():
        print(f"ERREUR: chemin introuvable: {args.path}", file=sys.stderr)
        return 2

    files = yaml_files(args.path)
    if not files:
        print("ERREUR: aucun fichier YAML trouvé", file=sys.stderr)
        return 2

    errors: list[str] = []
    warnings: list[str] = []
    custom_cards: Counter[str] = Counter()
    entities: Counter[str] = Counter()
    card_mod_count = 0

    for file in files:
        text = file.read_text(encoding="utf-8")
        parse_result = parse_yaml(text, file)
        if parse_result and parse_result.startswith("Erreur"):
            errors.append(f"{file}: {parse_result}")
        elif parse_result:
            warnings.append(parse_result)

        placeholders = sorted(set(PLACEHOLDER_RE.findall(text)))
        if placeholders:
            warnings.append(f"{file}: placeholders non remplacés: {', '.join(placeholders)}")

        custom_cards.update(CUSTOM_CARD_RE.findall(text))
        entities.update(ENTITY_RE.findall(text))
        card_mod_count += len(CARD_MOD_RE.findall(text))

    if card_mod_count > 10:
        warnings.append(f"card_mod apparaît {card_mod_count} fois : envisager une centralisation ou un thème.")

    print(f"Fichiers analysés: {len(files)}")
    print(f"Références d'entités détectées: {len(entities)}")
    if custom_cards:
        print("Cartes custom détectées:")
        for name, count in custom_cards.most_common():
            print(f"  - {name}: {count}")
    else:
        print("Cartes custom détectées: aucune")

    if warnings:
        print("\nAVERTISSEMENTS:")
        for warning in dict.fromkeys(warnings):
            print(f"  - {warning}")

    if errors:
        print("\nERREURS:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("\nValidation statique terminée sans erreur YAML détectée.")
    print("À compléter par une validation et des tests dans Home Assistant.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())