
from kb_loader import load_rules
from engine import ForwardChainingEngine

KB_PATH = "kb/laptop_rules.json"


def ask_yes_no(question):
    """Ask the user a yes/no question and return their answer."""

    while True:
        answer = input(question).strip().lower()

        if answer in ("y", "yes"):
            return True
        elif answer in ("n", "no"):
            return False
        else:
            print("Please enter y or n.")


def collect_initial_facts():
    """Collect user preferences and convert them into facts."""

    facts = []

    # Portability
    if ask_yes_no("Is portability important? (y/n): "):
        facts.append("portable")

    # Battery life
    if ask_yes_no("Do you need long battery life? (y/n): "):
        facts.append("long_battery")

    # Budget
    while True:
        budget = input(
            "What is your budget level? (high/medium/low): "
        ).strip().lower()

        if budget in ("high", "medium", "low"):
            facts.append(f"budget_{budget}")
            break
        else:
            print("Please enter high, medium, or low.")

    # Gaming
    if ask_yes_no("Will you use the laptop for gaming? (y/n): "):
        facts.append("gaming")

    # Performance
    if ask_yes_no("Is high performance important? (y/n): "):
        facts.append("performance_priority")

    # Professional work
    if ask_yes_no("Will you use the laptop for professional work? (y/n): "):
        facts.append("professional_work")

    # Student status
    if ask_yes_no("Are you a student? (y/n): "):
        facts.append("student")

    # Everyday use
    if ask_yes_no("Will you primarily use the laptop for everyday tasks? (y/n): "):
        facts.append("everyday_use")

    return facts


def main():
    """Load rules, collect facts, run inference, and display results."""

    # Load the knowledge base
    rules = load_rules(KB_PATH)

    # Create the inference engine
    engine = ForwardChainingEngine(rules)

    # Collect initial facts from the user
    initial_facts = collect_initial_facts()

    # Add initial facts to working memory
    engine.assert_facts(initial_facts)

    # Run forward chaining
    engine.run()

    # Retrieve conclusions
    results = engine.conclusions()

    # Display recommendations
    print("\n========== LAPTOP RECOMMENDATIONS ==========")

    if results["recommendations"]:
        for recommendation in results["recommendations"]:
            laptop = recommendation.replace("recommend:", "")
            laptop = laptop.replace("_", " ").title()
            print(f"Recommendation: {laptop}")
    else:
        print("No laptop recommendations could be generated.")

    # Display specifications
    if results["specs"]:
        print("\n========== SPECIFICATIONS ==========")

        for spec in results["specs"]:
            print(spec.replace("spec:", "").replace("_", " ").title())

    # Display other facts
    print("\n========== INITIAL FACTS ==========")

    for fact in initial_facts:
        print(f"- {fact}")

    # Display fired rules
    print("\n========== FIRED RULES ==========")

    if engine.trace:
        for entry in engine.trace:
            print(f"\nRule: {entry['rule']}")
            print(f"Conditions: {', '.join(entry['antecedents'])}")
            print(f"Conclusion: {entry['consequent']}")
            print(f"Priority: {entry['priority']}")
    else:
        print("No rules were triggered.")

    print("\n============================================")
    print("Expert system finished.")


if __name__ == "__main__":
    main()

