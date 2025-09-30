

# 🤖 Code Explainer & Debugger Bot

An interactive **Streamlit + LangChain + Hugging Face** powered tool that helps you **understand and debug code** in the style and detail level you prefer.

Whether you’re a **beginner just learning**, an **intermediate developer seeking clarity**, or an **advanced programmer looking for detailed debugging and optimization tips**, this bot adapts explanations to your needs.



## 🚀 Features

✅ **Explain Any Code** – Paste your code and get instant explanations.

✅ **Choose Explanation Style** – Beginner-friendly, step-by-step tutor, concise review, or deeply technical.

✅ **Custom Explanation Length** – Short summaries, multi-paragraph guides, or even **line-by-line breakdowns**.

✅ **Debugging & Fixes** – Detects errors, inefficiencies, and bad practices.

✅ **Alternative Approaches** – Suggests cleaner, optimized, or language-specific rewrites.

✅ **Real-World Analogies** – Complex programming concepts explained with simple analogies.



## 🛠️ Tech Stack

* **[Streamlit](https://streamlit.io/)** – UI framework for building the interactive web app.
* **[LangChain](https://www.langchain.com/)** – Orchestrates prompt templates and LLM workflows.
* **[Hugging Face Inference API](https://huggingface.co/)** – Provides the language model backend.
* **Python (dotenv, os)** – For environment and configuration management.



## 📦 Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/Vansh27189/Code-Explainer-Debugger-Bot.git
   cd Code-Explainer-Debugger-Bot
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your Hugging Face API key:

   * Get a token from [Hugging Face](https://huggingface.co/settings/tokens).
   * Add it to your **Streamlit secrets** (`.streamlit/secrets.toml`):

     ```toml
     HF_API_TOKEN = "your_huggingface_token_here"
     ```

---

## ▶️ Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

This will open the bot in your browser.

---

## 🎯 How to Use

1. **Paste Code** – Enter any code snippet (Python, C++, Java, JS, etc.).

2. **Pick Explanation Style** –

   * Beginner-Friendly
   * Intermediate
   * Advanced/Technical
   * Step-by-Step Tutor
   * Concise Review

3. **Select Explanation Length** –

   * Short (2–3 sentences)
   * Medium (1–2 paragraphs)
   * Detailed (multi-paragraph)
   * Very Detailed (line-by-line with debugging & alternatives)

4. **Analyze** – Click the **Analyse** button and let the bot explain your code.

---

## 🧑‍💻 Example

**Input:**

```python
def add_numbers(a, b):
    return a + b
```

**Output (Beginner-Friendly, Short):**
👉 This function takes two numbers, `a` and `b`, and returns their sum. It’s a simple way to add numbers together.

---

## 🔮 Future Enhancements

* Support for **multiple programming languages** with auto-detection.
* Option to **download explanations as PDF/Markdown**.
* Integration with **VS Code extensions** for in-editor debugging help.

---

## 🤝 Contributing

Pull requests are welcome! Feel free to open issues if you’d like to suggest improvements.

---

## 📜 License

MIT License – free to use and modify.

---


