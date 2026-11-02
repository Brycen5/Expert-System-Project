
import unittest

from engine import Rule, ForwardChainingEngine


class TestForwardChainingEngine(unittest.TestCase):

    def setUp(self):
        self.rules = [
            Rule(
                antecedents=["budget_high", "portable", "long_battery"],
                consequent="recommend:premium_ultrabook",
                priority=5,
                name="Premium Ultrabook"
            ),
            Rule(
                antecedents=["gaming", "performance_priority"],
                consequent="recommend:gaming_laptop",
                priority=4,
                name="Gaming Laptop"
            ),
            Rule(
                antecedents=["recommend:premium_ultrabook"],
                consequent="spec:long_battery_life",
                priority=2,
                name="Premium Battery Specification"
            )
        ]

        self.engine = ForwardChainingEngine(self.rules)

    def test_rule_can_fire(self):
        self.engine.assert_facts(
            ["budget_high", "portable", "long_battery"]
        )

        self.assertTrue(self.engine.can_fire(self.rules[0]))

    def test_rule_cannot_fire_with_missing_fact(self):
        self.engine.assert_facts(["budget_high", "portable"])

        self.assertFalse(self.engine.can_fire(self.rules[0]))

    def test_forward_chaining(self):
        self.engine.assert_facts(
            ["budget_high", "portable", "long_battery"]
        )

        self.engine.run()

        self.assertIn(
            "recommend:premium_ultrabook",
            self.engine.facts
        )

        self.assertIn(
            "spec:long_battery_life",
            self.engine.facts
        )

    def test_conclusions(self):
        self.engine.assert_facts(
            ["budget_high", "portable", "long_battery"]
        )

        self.engine.run()
        results = self.engine.conclusions()

        self.assertIn(
            "recommend:premium_ultrabook",
            results["recommendations"]
        )

        self.assertIn(
            "spec:long_battery_life",
            results["specs"]
        )

        self.assertIn(
            "budget_high",
            results["other_facts"]
        )


if __name__ == "__main__":
    unittest.main()
