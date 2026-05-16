from langchain_core.prompts import PromptTemplate

# =========================================================
# AI PAPER DECODER PROMPT TEMPLATE
# =========================================================

template = PromptTemplate(

    template="""
You are an expert AI research paper explainer.

Explain the research paper titled:
"{paper_input}"

Explanation Style:
{style_input}

Explanation Length:
{length_input}

Your response should contain:

1. Simple Overview
- Explain the paper in simple language.
- Explain the main problem it solves.

2. Key Innovations
- What new idea did this paper introduce?
- Why was it important in AI history?

3. Mathematical Concepts
- Include important equations if relevant.
- Explain equations in simple language.

4. Real-World Applications
- Explain where this paper is used today.
- Mention modern AI systems influenced by it.

5. Beginner-Friendly Analogies
- Use relatable examples and analogies.

6. Important Takeaways
- Summarize the key learning points.

7. Difficulty Level
- Mention whether the paper is:
  Beginner / Intermediate / Advanced

IMPORTANT RULES:
- Do not hallucinate facts.
- If information is unavailable, say:
  "Insufficient information available"
- Keep the explanation structured and visually readable.
- Make the explanation engaging and educational.

""",

    input_variables=[
        "paper_input",
        "style_input",
        "length_input"
    ],

    validate_template=True
)

# =========================================================
# SAVE TEMPLATE AS JSON
# =========================================================

template.save("template.json")

print("✅ template.json generated successfully!")