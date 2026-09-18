BEST_KB_THRESHOLD = 0.74


def evaluate_retrieval(kb_result):
    if not kb_result:
        return {
            "accepted": False,
            "action": "ABSTAIN",
            "reason": "No retrieval result available.",
        }

    score = kb_result["score"]

    if score < BEST_KB_THRESHOLD:
        return {
            "accepted": False,
            "action": "ABSTAIN",
            "reason": "KB score is below the approved threshold.",
        }

    return {
        "accepted": True,
        "action": "PROCEED",
        "reason": "KB score meets the approved threshold.",
    }


def determine_action(retrieval_decision, escalation_required=False):
    if not retrieval_decision["accepted"]:
        return {
            "action": "ABSTAIN",
            "approval_required": False,
            "reason": "Approved KB evidence is unavailable.",
        }

    if escalation_required:
        return {
            "action": "ESCALATE",
            "approval_required": True,
            "reason": "Escalation requires human approval.",
        }

    return {
        "action": "RESPOND",
        "approval_required": False,
        "reason": "Approved KB troubleshooting can be provided.",
    }