from decision_engine import (
    evaluate_retrieval,
    determine_action,
)


test_cases = [
    {
        "name": "Strong KB",
        "result": {
            "score": 0.82
        }
    },
    {
        "name": "Below threshold",
        "result": {
            "score": 0.61
        }
    },
    {
        "name": "Exactly threshold",
        "result": {
            "score": 0.74
        }
    },
]


for test in test_cases:
    decision = evaluate_retrieval(test["result"])

    print("\n" + test["name"])
    print("Score:", test["result"]["score"])
    print("Accepted:", decision["accepted"])
    print("Action:", decision["action"])
    print("Reason:", decision["reason"])

print("\nACTION DECISION TESTS")
print("=" * 40)

accepted_result = {
    "accepted": True,
    "score": 0.82
}

rejected_result = {
    "accepted": False,
    "score": 0.61
}

print("\nApproved troubleshooting:")
print(
    determine_action(accepted_result)
)

print("\nEscalation required:")
print(
    determine_action(
        accepted_result,
        escalation_required=True
    )
)

print("\nKB rejected:")
print(
    determine_action(rejected_result)
)