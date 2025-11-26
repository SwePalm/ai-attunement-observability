# ai-attunement-observatory

An ongoing observatory where multiple AI models imagine five waves of AI driven change,  
and where we track how their stories shift over time.

This is not a prediction engine. It is a place to **listen** to different models, compare their assumptions, and explore how AI, economics, politics, and culture might co-evolve.

## Quick start

- Browse the base prompt templates in [`prompts/`](prompts/) to see exactly how the frameworks and meta analyses are generated.
- Open the primary notebooks in the repo root for runnable examples (view directly on GitHub or Nbviewer for a zero-setup tour):
  - [`full_framework_gemeni.ipynb`](full_framework_gemeni.ipynb): single-model notebook that walks through generating a full five-wave framework.
  - [`scenario_pipeline_litellm.ipynb`](scenario_pipeline_litellm.ipynb): pipeline example showing how to chain scenario prompts via LiteLLM.
  - [`scenario_pipeline_gemeni.ipynb`](scenario_pipeline_gemeni.ipynb): Gemini-focused variant of the scenario pipeline workflow.
- This repository is an experiment—feel free to explore in read-only notebook viewers first, then clone if you want to rerun locally.

---

## 1. What this is

The **AI Attunement Observatory** is a living project with three main goals:

1. **Generate futures**  
   Use multiple LLMs from different ecosystems to create structured **five wave frameworks** for how AI might reshape society.

2. **Compare and synthesize**  
   Extract what these models **agree on** (structural patterns and likely cascades) and where they **disagree** (control points, values, and conflicts).

3. **Track drift over time**  
   Repeat the same protocol every few months to see how model narratives and probabilities change as the wider AI ecosystem evolves.

The focus is on **attunement**, not certainty. The value is in patterns, tensions and questions that help humans think.

---

## 2. Why this exists

A single model can give a persuasive story about “the future of AI”.  
Several different models, asked the same question in a structured way, reveal something else:

- Shared backbones that look **hard to avoid**  
- Divergent mid-waves where **human choices and politics still matter**  
- Cultural and systemic flavor in how different ecosystems imagine control, scarcity and resistance

This repo collects those stories, the prompts that generated them, and the meta-analyses that sit on top.

If you want to see how AI systems themselves talk about AI, this is the observatory.

---

## 3. What is in this repo

Planned structure (early version):

- `runs/YYYY-MM/`  
  A full experiment run for a given month.
  - `frameworks/`  
    One five wave framework per model in Markdown.
  - `meta/`  
    Syntheses and probability tables for that run.
  - `prompts/`  
    The exact prompts used for frameworks and meta analysis.
  - `notes.md`  
    Short notes about models, settings and context.

- `prompts/`  
  The current base prompt templates for:
  - generating five wave frameworks  
  - running the cross framework meta analysis

- `scripts/`  
  Helper scripts for running models and assembling results  
  (to be added as the project evolves).

- `comms/`
  Drafts for Substack posts and LinkedIn summaries that explain the work in human language.

The first complete run is **2025 11** and includes frameworks from six models and a combined meta analysis called **The Quantification Paradox**.

---

### Run your own pass (experimental)

If you want to reproduce a monthly run with your own model choices, here is the simplest manual path:

- Copy or adapt the prompt templates in [`prompts/`](prompts/) so the framing, synthesis, and meta-analysis instructions match your experiment.
- Create a local `.env` file that includes the API keys for the model endpoints you plan to call (e.g., OpenRouter or any LiteLLM-compatible provider). Keep secrets out of version control.
- Update [`attunement/config.py`](attunement/config.py) with any endpoint choices, model names, or parameter tweaks you need for your run. Treat the config file as the single place to define what models and settings your pass will use.
- Pick a model endpoint (e.g., OpenRouter via [`scenario_pipeline_openrouter.ipynb`](scenario_pipeline_openrouter.ipynb) or LiteLLM via [`scenario_pipeline_litellm.ipynb`](scenario_pipeline_litellm.ipynb)). Open the relevant notebook in the repo root and run the cells manually—these pipelines are intended for exploratory use, so stepwise execution is expected.
- Save outputs under a new `runs/YYYY-MM/` directory following the convention described above: include `frameworks/` for per-model five-wave narratives, `meta/` for syntheses, and a `notes.md` file capturing the models, parameters, and context for the pass.
- Keep everything in Markdown and simple text so the artifacts stay diffable and easy to review over time.

Assumptions: these pipelines are run by hand in notebooks, and you can substitute any compatible endpoint as long as you honor the same file layout for the resulting run.

---

## 4. How the experiment works (high level)

1. **Ask each model the same question**  
   Use a shared prompt that asks for a **five wave timeline** of AI driven change, including technology, economics and governance.

2. **Store the outputs as frameworks**  
   One Markdown file per model, with simple metadata at the top  
   (model name, ecosystem, date, prompt version).

3. **Run a meta analysis**  
   Use a separate prompt to build a cross model synthesis:
   - a shared thesis  
   - a phase by phase consensus for Wave 1 and Wave 5  
   - a divergence map for Waves 2–4  
   - a probability and volatility mapping for wave transitions

4. **Repeat over time**  
   Every few months, run the same process again.  
   Compare runs to see how the stories and probabilities drift.

---

## 5. How you can use this

You can use this repo to:

- Read the **individual frameworks** to see how different models think about AI, markets and governance.
- Use the **meta analyses** as input to your own workshops, talks or strategy sessions.
- Fork the repo and:
  - plug in your own models  
  - tweak the prompts  
  - run your own meta analysis pipeline

If you do something interesting with it, feel free to open an issue and describe your experiment.

---

## 6. Status and roadmap

Status: **Early version, first full run recorded.**  
Things that are likely to appear over time:

- Cleaner scripts for running all models and storing results
- Notebooks that compare multiple runs and visualize drift
- More structured reflection on cultural and ecosystem differences between models

---

## 7. License

Assume the code and prompt templates are intended to be reused and adapted.  
The narrative texts generated by models may have mixed origins, so handle with care if you plan to use them commercially.


