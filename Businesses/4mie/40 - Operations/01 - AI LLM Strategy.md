# 4mie AI LLM Strategy: Market Analysis, Tokens, & Interaction Design

## 1. LLM Market Analysis (Dec 2025)
**Top Models for Legal Doc Gen (Form E)**:

| Model             | Strengths                  | Weaknesses   | Cost (per 1M tok In/Out) | Score |
|:------------------|:---------------------------|:-------------|:-------------------------|:-----:|
| Claude Opus 4 (Rec) | Best reasoning, low hallucination, 200k ctx | Pricier | $15/$75 | 9.5/10 |
| Claude Sonnet 4   | Fast, capable, good value  | Less depth than Opus | $3/$15 | 9.2/10 |
| GPT-4o            | Versatile, structured output | Some hallucinations | $2.50/$10 | 9.0/10 |
| Gemini 2.0 Flash  | Very fast, good reasoning  | Less proven for legal | $0.10/$0.40 | 8.8/10 |
| Grok 2            | Good reasoning, real-time data | Newer ecosystem | ~$2/$10 | 8.5/10 |
| Llama 3.3 70B     | Open source, self-hostable | Requires infra | Free (self-host) | 8.3/10 |

**Rec**: Claude Sonnet 4 for drafts (cost-effective), Claude Opus 4 for final compilation (quality). Hybrid approach balances cost and quality.

Legal AI market: $5B, 25% CAGR.

## 2. Token Estimates
**Semi-Complex Form E**: 35k-60k total (avg 45k).
- Input: 20k-35k (prompts/history).
- Output: 15k-25k (narratives).
**Cost estimates per form**:
- Sonnet 4 only: ~£0.30-0.50/form
- Opus 4 only: ~£1.80-2.50/form
- Hybrid (Sonnet drafts + Opus final): ~£0.80-1.20/form (recommended)

| Complexity | Total Tokens |
|------------|--------------|
| Simple | 20k-30k |
| Semi | **35k-60k** |
| Complex | 60k+ |

## 3. Interaction Structure: Hybrid Modular Chat
**Claude Opus 4 handles full context (200k)** – but use **sectional + state** for cost optimization.

### Flow
```
Signup → Disclaimer → Chat Dashboard
↓
Global Intake → Section Loop → Compile Bundle
```

### State (Postgres JSONB)
- Global Summary (2k-5k tok)
- Facts JSON (5k)
- Sections Array

### Per-Turn Prompt
```
[System: Truthful Form E expert.
Summary: {summary} Facts: {json} Section: {desc}
User: {input}]

JSON: {narrative, questions[], fact_updates}
```

### Phases (15-25 turns)
1. Intake (overview).
2. Section Group (3-5; Q→Draft→Review).
3. **Red Team / Forensic Audit (Crucial Step)**:
    - **Model**: Claude Opus 4
    - **Prompt**: "You are opposing counsel. Find every inconsistency between Income (S2) and Budget (S3). Find missing evidence for Assets (S2). Create a Schedule of Deficiencies."
    - **Output**: User-facing "Fix This" list.
4. Final Compile (50k call).

**Benefits**: 20% cheaper, iterative UX, **Audit Shield** protects credibility.
**Impl**: Vercel AI SDK + Zod. Total ~45k tok.

**Next**: Prompt templates, A/B tests.

See [[00 - Tech Stack and MVP Build Plan]].