# Home Assistant Dashboard Designer Skill

Skill portable conforme au format Agent Skills : un dossier nommé comme le champ `name`, contenant un `SKILL.md` avec frontmatter YAML, plus des ressources chargées à la demande.

## Installation

```bash
npx skills add teefloo/home-assistant-dashboard-designer
```

## Contenu

- `SKILL.md` : instructions principales.
- `references/` : sélection des composants, architecture, validation et sources.
- `assets/` : questionnaire, manifeste de livraison et squelette YAML.
- `scripts/validate_dashboard.py` : validation statique prudente.
- `evals/eval_queries.json` : requêtes de test d'activation.

## Validation rapide

```bash
skills-ref validate ./home-assistant-dashboard-designer
python home-assistant-dashboard-designer/scripts/validate_dashboard.py path/to/dashboard.yaml
```

Le second script nécessite PyYAML pour parser la syntaxe :

```bash
python -m pip install pyyaml
```
[![skills.sh](https://skills.sh/b/teefloo/home-assistant-dashboard-designer)](https://skills.sh/teefloo/home-assistant-dashboard-designer)