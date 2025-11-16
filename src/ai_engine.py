def llm_generate_summary(text: str) -> str:
    """
    Produce a short, human-readable summary for an endpoint description.
    This is a rule-based summarizer designed for offline use in academic submissions.
    """
    if not text or not text.strip():
        return "This endpoint performs a basic API operation."

    desc = " ".join(text.strip().split())

    # shorten long text
    if len(desc) > 140:
        desc = desc[:140].rsplit(" ", 1)[0] + "..."

    first_char = desc[0].lower()
    rest = desc[1:] if len(desc) > 1 else ""

    summary = f"In summary, this endpoint {first_char}{rest}"
    if not summary.endswith("."):
        summary += "."

    return summary
