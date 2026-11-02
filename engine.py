from dataclasses import dataclass
from typing import List, Set, Dict, Any

@dataclass
class Rule:
    antecedents: List[str]
    consequent: str
    priority: int = 0
    name: str = ""

class ForwardChainingEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules
        self.facts: Set[str] = set()
        self.trace: List[Dict[str, Any]] = []

    def assert_facts(self, initial: List[str]) -> None:
        """Store initial facts into the working memory."""
        self.facts.update(initial)

    def can_fire(self, rule: Rule) -> bool:
        """Return True if all antecedents are true and consequent not yet known."""

        return (
        all(fact in self.facts for fact in rule.antecedents)
        and rule.consequent not in self.facts
    )

    def run(self) -> None:
        """Implement the forward chaining loop."""

    while True:

        # Find all rules that can currently fire
        applicable_rules = [
            rule for rule in self.rules
            if self.can_fire(rule)
        ]

        # Stop if no more rules can fire
        if not applicable_rules:
            break

        # Select the rule with the highest priority
        rule = max(applicable_rules, key=lambda r: r.priority)

        # Add the conclusion to working memory
        self.facts.add(rule.consequent)

        # Record the rule execution
        self.trace.append({
            "rule": rule.name,
            "antecedents": rule.antecedents,
            "consequent": rule.consequent,
            "priority": rule.priority
        })

    def conclusions(self) -> Dict[str, List[str]]:
        """Return separated results (recommendations, specs, other facts)."""

        recommendations = []
        specs = []
        other_facts = []

        for fact in self.facts:

            if fact.startswith("recommend:"):
                recommendations.append(fact)

            elif fact.startswith("spec:"):
                specs.append(fact)

            else:
                other_facts.append(fact)

        return {
        "recommendations": sorted(recommendations),
        "specs": sorted(specs),
        "other_facts": sorted(other_facts)
    }
