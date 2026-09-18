import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv
from google import genai

from rag import get_best_kb

from decision_engine import (
    evaluate_retrieval,
    determine_action,
)

# ============================================================
# CONTROLLED KB CLASSIFICATION
# ============================================================

KB_CLASSIFICATION = {
    "KB001_VPN_Password_Change.md": {
        "category": "Network",
        "subcategory": "VPN",
    }
}

# ============================================================
# CONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(ENV_PATH)

API_KEY = os.getenv("GEMINI_API_KEY")


# ============================================================
# STREAMLIT PAGE
# ============================================================

st.set_page_config(
    page_title="AI Service Desk Copilot",
    page_icon="🛠️",
    layout="wide",
)

st.title("🛠️ AI Service Desk Copilot")
st.caption("Knowledge-grounded IT Service Desk assistant")


# ============================================================
# TICKET INPUT
# ============================================================

ticket = st.text_area(
    "Ticket Description",
    placeholder=(
        "Example: User cannot connect to VPN after changing "
        "their corporate password."
    ),
    height=180,
)


# ============================================================
# ANALYZE TICKET
# ============================================================

if st.button("Analyze Ticket", type="primary"):

    # --------------------------------------------------------
    # Validate ticket
    # --------------------------------------------------------

    if not ticket.strip():
        st.warning("Please enter a ticket description.")
        st.stop()

    # --------------------------------------------------------
    # Validate API key
    # --------------------------------------------------------

    if not API_KEY:
        st.error(
            "GEMINI_API_KEY is not configured in the .env file."
        )
        st.stop()

    try:
        # ----------------------------------------------------
        # Retrieve approved KB
        # ----------------------------------------------------

        kb_result = get_best_kb(ticket)
        decision = evaluate_retrieval(kb_result)

        action_decision = determine_action(decision)

        if kb_result is None:
            retrieval_accepted = False
            retrieval_score = 0.0
            retrieval_reason = "No retrieval result."
            kb_text = "No approved knowledge article was retrieved."
            category = "Not determined"
            subcategory = "Not determined"

        else:
            retrieval_accepted = kb_result["accepted"]
            retrieval_score = kb_result["score"]
            retrieval_reason = kb_result["reason"]

            best_match = kb_result["best_match"]

            if retrieval_accepted and best_match:
                kb_text = best_match["text"]

                kb_file_name = best_match["file_name"]

                classification = KB_CLASSIFICATION.get(
                    kb_file_name
                )

                if classification:
                    category = classification["category"]
                    subcategory = classification["subcategory"]
                else:
                    category = "Not determined"
                    subcategory = "Not determined"

            else:
                kb_text = "No approved knowledge article was retrieved."
                category = "Not determined"
                subcategory = "Not determined"
        # ----------------------------------------------------

        client = genai.Client(
            api_key=API_KEY
        )

        # ----------------------------------------------------
        # AI Service Desk Prompt
        # ----------------------------------------------------

        retrieval_score_text = f"{retrieval_score:.4f}"
        prompt = f"""
You are an AI Service Desk Knowledge Assistant.

Your job is to analyze the Service Desk ticket using ONLY
the approved knowledge retrieved below.

IMPORTANT RULES:

1. Use ONLY the retrieved approved knowledge.
2. Do NOT invent troubleshooting steps.
3. Do NOT invent root causes.
4. Do NOT use general IT knowledge to fill missing information.
5. Do NOT request passwords.
6. Do NOT request MFA codes.
7. Do NOT request authentication secrets.
8. Do NOT recommend prohibited actions.
9. If the KB is rejected or the retrieved KB does not contain
   enough information, clearly say:
   "Available KB information is insufficient."

10. Identify the KB used only if a KB was accepted.

11. Distinguish confirmed KB information from unsupported assumptions.

12. Do not claim that a troubleshooting step is approved unless
    it is explicitly supported by the retrieved KB.

13. Do not create a KB ID that is not present in the retrieved KB.

14. Do not assign Category or Subcategory unless they are explicitly
    supported by the accepted KB. If the KB is rejected, use:
    Category: Not determined
    Subcategory: Not determined

15. Do not convert the retrieval similarity score into a percentage
    or replace it with 0%.

16. The KB Match Score must be reported using the exact retrieval
    score supplied by the application.

17. Do not independently calculate, estimate, or change the KB Match Score.

18. If the KB is rejected, do not provide troubleshooting steps,
    even if you know possible troubleshooting from general IT knowledge.

19. Confidence must reflect the evidence available from the approved KB.
    Do not claim 100% confidence merely because the ticket resembles
    the KB.

20. Never treat unsupported information as confirmed information.
21. The application has determined the following classification:
    Category: {category}
    Subcategory: {subcategory}

    Use these values exactly. Do not change, reinterpret, or invent
    a different Category or Subcategory.

SERVICE DESK TICKET:
{ticket}

RETRIEVAL DECISION:
Accepted: {retrieval_accepted}
Retrieval Score: {retrieval_score_text}
Retrieval Reason: {retrieval_reason}

RETRIEVED APPROVED KNOWLEDGE:
{kb_text}

Return the analysis using exactly this structure:

AI Decision:

Confidence:

Decision Reason:

Category:

Subcategory:

Incident Summary:

Relevant KB:

KB Match Score:
(Report the exact Retrieval Score supplied above.)

Approved Troubleshooting:

Steps Already Completed:

Unsupported Information / Assumptions:
"""

        # ----------------------------------------------------
        # Generate AI response
        # ----------------------------------------------------

        if decision["action"] == "PROCEED":
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt,
            )
        else:
            response = None

        # ----------------------------------------------------
        # Display retrieval decision
        # ----------------------------------------------------

        st.subheader("Retrieval Decision")

        if retrieval_accepted:
            st.success("✅ KB Accepted")
        else:
            st.warning("⚠️ KB Rejected")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Best KB Score",
                f"{retrieval_score:.4f}"
            )

        with col2:
            st.metric(
                "Threshold",
                "0.7400"
            )

        with col3:
            st.metric(
                "Decision",
                "Accepted" if retrieval_accepted else "Rejected"
            )

        st.caption(retrieval_reason)

        # ----------------------------------------------------
        # Display AI analysis
        # ----------------------------------------------------

        st.subheader("AI Analysis")

        if response is not None and response.text:
            st.text(response.text)
        elif response is None:
            st.warning(
                "AI analysis was not performed because the retrieval decision was ABSTAIN."
        )
        else:
            st.warning(
                "The AI model returned an empty response."
        )

        # ----------------------------------------------------
        # Application-controlled retrieval facts
        # ----------------------------------------------------

        st.subheader("Application Retrieval Facts")

        st.write(
            f"**Retrieval Decision:** "
            f"{'Accepted' if retrieval_accepted else 'Rejected'}"
        )

        st.write(
            f"**Actual KB Match Score:** "
            f"{retrieval_score:.4f}"
        )

        st.write(
            f"**Retrieval Threshold:** "
            f"{0.7400:.4f}"
        )

        # ----------------------------------------------------
        # Optional: show retrieved KB
        # ----------------------------------------------------

        with st.expander("Retrieved Approved Knowledge"):
            st.text(kb_text)

    except Exception as e:

        st.error(
            f"Application error: {e}"
        )