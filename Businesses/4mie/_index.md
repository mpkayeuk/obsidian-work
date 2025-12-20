# 4mie - Divorce Financial Settlement App

## Status: Pre-Development
**Last Updated**: 2025-12-19

## Quick Summary
AI-powered SaaS platform helping UK individuals complete Form E (divorce financial statement) through conversational guidance, generating solicitor-ready documents and evidence bundles.

## Key Metrics & Targets
| Metric | Target |
|--------|--------|
| MVP Timeline | 7 weeks |
| Startup Cost | £3,500 |
| Break-even | 20 Pro users/month |
| Y1 Revenue Target | £140k |
| Y5 Revenue Target | £706k |

## Pricing (Canonical)
- **Basic** - £99: Draft Form E PDF (updates £49 each)
- **Pro** - £249: AI-optimised narratives + evidence bundle + unlimited updates until Final Order
- **Solicitor Review Add-on** - +£299: Partner solicitor review (can add to any tier)

## Key Links
### Planning
- [[10 - Business Plan/00 - Mission and Vision|Mission & Vision]]
- [[10 - Business Plan/01 - Market Research|Market Research]]
- [[10 - Business Plan/02 - Financial Projections|Financial Projections]]

### Product
- [[20 - Services/00 - Form E Guidance Service|Core Service Description]]
- [[40 - Operations/00 - Tech Stack and MVP Build Plan|Tech Stack & MVP Plan]]
- [[40 - Operations/01 - AI LLM Strategy|AI/LLM Strategy]]

### Go-to-Market
- [[30 - Marketing and Sales/00 - Launch Strategy|Launch Strategy]]
- [[70 - Website/00 - Landing Page Content|Landing Page Content]]
- [[60 - Pitches/00 - Investor Pitch Outline|Investor Pitch]]

### Legal & Resources
- [[50 - Legal and Finance/00 - Disclaimers and Terms|Disclaimers & Terms]]
- [[80 - Resources/00 - Form E Template and Links|Form E Resources]]

## Decisions Log
| Date | Decision | Rationale |
|------|----------|-----------|
| - | Hybrid pricing model (one-time + add-ons) | Matches one-off nature of divorce process |
| - | Claude recommended for production LLM | Best reasoning, lowest hallucination for legal |
| - | Vercel + Next.js stack | Fast MVP, low ops overhead |

## Next Actions
1. Set up code repository
2. Create Form E section-to-prompt mapping
3. Build conversational interview flow
4. Implement PDF generation

## Future Features (Backlog)
- Opposing Form E forensic analysis (bank statement anomaly detection)
- AI evidence analyzer
- Solicitor matching marketplace
- Scotland/NI Form E variants
