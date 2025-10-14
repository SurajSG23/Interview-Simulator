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
