from langchain_huggingface import ChatHuggingFace ,HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt
import os
load_dotenv()

st.set_page_config(
    page_title= "My App",
    page_icon= "🤖"
)

hf_token = st.secrets.get("HF_API_TOKEN")
if hf_token is None:
    st.error("HF_API_TOKEN is missing! Please add it in Streamlit Secrets.")
    st.stop()

st.write("Loaded key starts with:", hf_token[:6])

input1 = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    # task="text-generator",
    api_token=hf_token,
    model_kwargs={
            "temperature": 0.7,
            "max_new_tokens": 1000,
            "do_sample": True
        }
)





st.header("Code Explainer & Debugger Bot")
Code_input = st.text_area("Enter Your CODE")
style_input = st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Intermediate", "Advanced/Technical", "Step-by-Step Tutor", "Concise Review"])
length_input = st.selectbox("Select Explanation Length", ["Short → 2–3 sentences", "Medium → 1–2 paragraphs", "Detailed → Multi-paragraph", "Very Detailed → Includes line-by-line breakdown with detailed explanation of each line, debugging suggestions, and alternatives."])

#CAN USE IF DO ONT WANT TO USE TEMPLATE.JSON
# template = PromptTemplate(
#     template="""  
# Please analyze the following code: {Code_input}

# Provide the explanation with the following specifications:
# Explanation Style: {style_input}
# Explanation Length: {length_input}

# Instructions:

# 1. Line-by-Line Explanation:
# - Clearly explain what each line of the code is doing.
# - Use simple language, but don’t skip important technical details.

# 2. Debugging & Fixes:
# - Identify any errors, inefficiencies, or bad practices in the code.
# - Suggest corrected versions or optimizations with proper reasoning.

# 3. Alternative Approaches:
# - If applicable, show how the same code can be written in a cleaner way or
# in another programming language (based on user input).

# 4. Analogies:
# - Use simple, real-world analogies to explain tricky concepts (e.g., memory allocation, loops, OOP).


# Step 1: Statement Purpose and Function
# - Describe what this line of code is doing at a high level.
# - Explain why it might be used in a program.
# - Include any language-specific context (e.g., declaration rules in C, object creation in Java, dynamic assignment in Python).

# Step 2: Type and Memory/Storage Considerations
# - Identify the data type or object type involved.
# - Explain how the language stores this data:
#     - Static languages (C, C++, Java): memory allocated on stack/heap with fixed type.
#     - Dynamic languages (Python, JavaScript, Ruby): memory allocated for an object and a reference is created.
# - Mention scope: local, global, or class-level storage.

# Step 3: How the Language Evaluates This Line
# - Describe the step-by-step evaluation process:
#     a. The right-hand side expression (literal, function call, or object) is evaluated.
#     b. Memory is allocated or a reference is assigned.
#     c. The result is associated with a storage location or identifier.
#     d. Any bookkeeping (reference counting, garbage collection) is updated if applicable.

# Step 4: Potential Edge Cases
# - Describe unusual or boundary scenarios:
#     - Type changes or mismatches.
#     - Overflow or underflow in static languages.
#     - Null/undefined/uninitialized behavior.
# - Explain how the program will behave in these situations.

# Step 5: Real-World Analogy
# - Provide an intuitive analogy for the line of code:
#     - Think of it like a labeled jar, container, or instruction in a workflow.
#     - Explain how the “label” and “contents” interact with the program logic.
#     - Include an analogy for dynamic vs static typing if relevant.

# Step 6: Example Execution (Optional)
# - Provide a small hypothetical example showing:
#     - Input or initial state
#     - How this line transforms the state
#     - Output or side effects after execution

# Step 7: Additional Notes
# - Include language-specific nuances, pitfalls, or best practices.
# - Highlight potential improvements or alternative approaches.

    
# If certain details cannot be inferred from the code (e.g., missing function definitions, incomplete logic), respond with:
# "Insufficient information available" instead of guessing.

# Ensure the explanation is clear, practical, and aligns with the provided style and length.
# Important Notes:
# - If certain details cannot be inferred, respond: "Insufficient information available."
# - Ensure the explanation is **very detailed, step-by-step, and clear**, like a tutorial.
# - Adapt explanations based on the detected programming language.

# If certain details cannot be inferred from the code (e.g., missing function definitions, incomplete logic), respond with:
# "Insufficient information available" instead of guessing.

# Ensure the explanation is clear, practical, and aligns with the provided style and length
# """,
# input_variables=['Code_input','style_input', 'length_input']
# )

template = load_prompt('template.json')

prompt = template.invoke({
    'Code_input':Code_input,
    'style_input':style_input,
    'length_input': length_input
})


if st.button("Analyse"):
    st.write("Processing....")
    result = model.invoke(prompt)
    st.write("Result: ")
    st.write(result.content)















