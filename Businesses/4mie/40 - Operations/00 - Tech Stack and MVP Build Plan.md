# Tech Stack & MVP Build Plan for 4mie

## Tech Stack
- **Frontend**: Next.js 14 (App Router, React 18, Tailwind CSS for styling)
- **Backend**: Next.js API routes (Server Actions for form handling)
- **Database**: Postgres (via Vercel Postgres or Supabase for ease)
- **AI**: 
    - **Drafting**: Claude Sonnet 4 (Fast, conversational)
    - **Forensic Audit**: Claude Opus 4 (Deep reasoning, 'Red Team' analysis)
- **Hosting**: Vercel (serverless, auto-deploys from GitHub)
- **Auth**: NextAuth.js or Clerk (user accounts for saving progress)
- **File Upload**: Vercel Blob or AWS S3 for evidence docs
- **Payments**: Stripe for subscriptions/one-time
- **Analytics**: Vercel Analytics, PostHog

## MVP Features & Build Roadmap
### Phase 1: Core Form E Generator (4 weeks)
1. User onboarding (email/signup, disclaimer acceptance)
2. Conversational AI chat: Section-by-section Q&A (map to Form E questions)
3. AI generation: Prompt Claude Sonnet to write responses based on user input
4. PDF generation: Use pdf-lib or react-pdf for Form E output + supplements
5. Evidence upload list & bundle (zip folder)

### Phase 2: The "Solicitor Simulator" & Compliance (2 weeks)
1. **Forensic Audit Agent**: Build the logic to cross-reference Income vs. Expenses and Assets vs. Evidence.
2. **Validation Dashboard**: "To-Do List" of contradictions user must fix before download.
3. Solicitor partner integration (affiliate links)
4. User dashboard (save/resume)
5. Disclaimers everywhere

### Phase 3: Launch (1 week)
1. Landing page
2. SEO, Stripe

**Total MVP Time**: 7 weeks, solo dev possible.

## Deployment
1. GitHub repo: 4mie/4mie-app
2. Vercel connect
3. Env vars: XAI_API_KEY, DATABASE_URL, STRIPE_KEYS

## Costs (Monthly MVP)
- Vercel: Free tier
- Postgres: $0-20
- xAI API: ~$0.01/1k tokens (est $50/mo at launch)
- Domain: 4mie.com (registered)

Next: Code repo setup.