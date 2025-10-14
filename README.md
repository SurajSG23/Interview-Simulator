# Activity Diagram

<img width="400" alt="Screenshot 2025-10-13 103847" src="https://github.com/user-attachments/assets/c8d71a73-4fca-45a3-932c-7efa73469514" />

# Generation / Sampling parameters

---

### 1. **Temperature**

* **Controls creativity or randomness.**
* **Low temperature (e.g. 0.2):** more focused, predictable answers.
  → Good for facts, coding, or precise tasks.
* **High temperature (e.g. 0.8–1.0):** more creative, varied, and less repetitive.
  → Good for brainstorming, stories, or idea generation.
---

### 2. **Top-p (Nucleus Sampling)**

* Decides **how much of the probability space** to consider.
* Model only looks at the **top portion of most likely words** that together add up to a probability *p*.

  * Example: `top-p = 0.9` → model only considers the top 90% most likely next words, ignoring rare ones.

---

### 3. **Top-k**

* Another way to control randomness.
* Limits the model to the **top-k most likely words** at each step.

  * Example: `top-k = 50` → model only considers the 50 most likely next words.

---

### 4. **Max Tokens**

* Limits how **long** the response can be.
* The model stops when it reaches this limit — even if the sentence isn’t finished.

  * Example: `max_tokens = 100` → response can be up to ~100 words/tokens long.

---

### 5. **Presence Penalty**

* Controls how much the model **avoids repeating topics.**
* Higher value → model more likely to **bring up new ideas**.

  * Example: if you’re writing a story, a higher presence penalty keeps it fresh.

---

### 6. **Frequency Penalty**

* Controls how much the model avoids **repeating the same words or phrases.**
* Higher value → fewer repetitions.

  * Example: useful to stop “hello hello hello...” loops.

---

### 7. **Stop Sequences**

* A list of words/phrases that tell the model **where to stop generating.**

  * Example: `stop = ["END", "\n\n"]` → model stops when it sees “END” or a double newline.

---

### 8. **Seed**

* Controls **randomness reproducibility.**
* Using the same seed + same parameters = same output every time.
  Good for **testing or debugging.**

---

### Quick Summary Table

| Parameter             | What It Controls        | Example Use                     |
| --------------------- | ----------------------- | ------------------------------- |
| **Temperature**       | Creativity / randomness | 0.2 = focused, 1.0 = creative   |
| **Top-p**             | Probability cutoff      | 0.9 = only top 90% likely words |
| **Top-k**             | Number cutoff           | 50 = only top 50 choices        |
| **Max Tokens**        | Response length         | 200 = up to ~200 tokens         |
| **Presence Penalty**  | New ideas vs repetition | 1.0 = more new topics           |
| **Frequency Penalty** | Repeated words          | 1.0 = less repetition           |
| **Stop**              | Where to end            | ["END"]                         |
| **Seed**              | Reproducibility         | same seed → same output         |

---
### Recommended Parameter Settings for Different Tasks

| **Task Type**                                | **Temperature** | **Top-p**  | **Top-k** | **Max Tokens**        | **Presence Penalty** | **Frequency Penalty** | **Stop Sequences**          | **Seed** | **Goal / Effect**                     |
| -------------------------------------------- | --------------- | ---------- | --------- | --------------------- | -------------------- | --------------------- | --------------------------- | -------- | ------------------------------------- |
| **Coding / Technical tasks**                 | 0.1 – 0.3       | 0.8 – 1.0  | 40 – 100  | Medium (e.g. 300–800) | 0.0 – 0.2            | 0.0 – 0.2             | Often none or default       | Optional | Precise, deterministic, no randomness |
| **Factual Q&A / Study notes**                | 0.2 – 0.4       | 0.8 – 0.95 | 40 – 100  | Medium (300–700)      | 0.0 – 0.2            | 0.0 – 0.3             | Optional                    | Optional | Accurate and focused responses        |
| **Creative writing / Storytelling / Poetry** | 0.7 – 1.0       | 0.8 – 1.0  | 50 – 200  | High (500–1500+)      | 0.5 – 1.0            | 0.3 – 0.7             | Sometimes (“THE END”, etc.) | Optional | Free, expressive, unpredictable       |
| **Brainstorming / Idea generation**          | 0.6 – 0.9       | 0.8 – 1.0  | 50 – 150  | Medium (400–1000)     | 0.5 – 1.0            | 0.3 – 0.6             | Optional                    | Optional | Diverse and creative outputs          |
| **Conversational chat / Assistant use**      | 0.5 – 0.8       | 0.8 – 1.0  | 50 – 100  | Medium (500–1000)     | 0.2 – 0.6            | 0.2 – 0.5             | Often system-defined        | Optional | Natural, friendly flow                |
| **Summarization / Paraphrasing**             | 0.2 – 0.5       | 0.7 – 0.9  | 40 – 100  | Based on text length  | 0.0 – 0.2            | 0.0 – 0.3             | Optional                    | Optional | Clear, structured summaries           |
| **Translation**                              | 0.1 – 0.3       | 0.8 – 0.9  | 40 – 80   | Medium (300–700)      | 0.0                  | 0.0 – 0.2             | Optional                    | Optional | Accurate, faithful translation        |
| **Roleplay / Dialogue generation**           | 0.6 – 0.9       | 0.8 – 1.0  | 50 – 150  | Medium-high           | 0.6 – 1.0            | 0.3 – 0.7             | Optional                    | Optional | Lively, character-driven replies      |

---