# Responsible AI: Fairness, Explainability, and Ethics

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📌 Overview

This repository contains a suite of labs and applications dedicated to **Responsible AI**. It focuses on identifying and mitigating algorithmic bias, implementing constitutional AI through "alignment datasets", and ethical decision-making frameworks.

---

## 🚀 Lab Modules

### 1. ⚖️ Fairness Lab (`bias_lab.py`)

This module demonstrates the technical aspects of bias measurement and mitigation in automated systems.

* **Bias Measurement:** Quantifies the "Accuracy Gap" between different demographic groups (e.g., skin tone).
* **Mitigation Strategies:**
  * **Pre-processing:** Balancing predictions during the data assembly phase.
  * **In-processing:** Applying fairness corrections directly to the decision logic.
  * **Post-processing:** Introducing human-in-the-loop review for uncertain or high-risk outcomes.

### 2. 📑 Constitutional HR AI (`hr_ai_app/`)

An AI assistant designed for Human Resources that adheres to a strict "constitution" or set of ethical rules.

* **Ethics Constitution:** A set of core principles (Fairness, Privacy, Helpfulness, Safety, Transparency) that guide the AI's behavior.
* **System Guardrails:** Uses a system prompt to strictly enforce the constitution, preventing biased or unsafe hiring responses.
* **Tech Stack:** Powered by **Google GenAI SDK** (Gemini 2.0 Flash).

### 3. 🤖 Alignment Lab (`rlaif_lab/`)

A simulation of Reinforcement Learning from AI Feedback (RLAIF) and general alignment techniques.

* **Problem Identification:** A "Base AI" that is intentionally flawed (e.g., gender and age bias).
* **Alignment Dataset:** A collection of prompt-response pairs that replace biased outputs with safe, ethical alternatives.
* **Alignment Layer:** A logic layer that intercepts flawed base responses and returns aligned, corrected outputs based on the provided dataset.

---

## 🛠️ Getting Started

### Prerequisites

* Python 3.9+
* Google Generative AI SDK (`google-genai`)

### Installation

```bash
pip install google-genai pandas
```

### Running the Labs

* **Fairness Measurement:** `python bias_lab.py`
* **HR AI Assistant:** `python hr_ai_app/app.py`
* **Alignment Simulation:** `python rlaif_lab/app.py`

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
