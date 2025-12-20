# Tech Stack & MVP Build Plan for 4mie

## Tech Stack
- **Frontend**: Next.js 14 (App Router, React 18, Tailwind CSS for styling)
- **Backend**: Next.js API routes (Server Actions for form handling)
- **Database**: Postgres (via Vercel Postgres or Supabase for ease)
- **AI**: xAI API (Grok models for conversational Q&A and text generation)
- **Hosting**: Vercel (serverless, auto-deploys from GitHub)
- **Auth**: NextAuth.js or Clerk (user accounts for saving progress)
- **File Upload**: Vercel Blob or AWS S3 for evidence docs
- **Payments**: Stripe for subscriptions/one-time
- **Analytics**: Vercel Analytics, PostHog

## MVP Features & Build Roadmap
### Phase 1: Core Form E Generator (4 weeks)
1. User onboarding (email/signup, disclaimer acceptance)
2. Conversational AI chat: Section-by-section Q&A (map to Form E questions)
3. AI generation: Prompt xAI to write responses based on user input
4. PDF generation: Use pdf-lib or react-pdf for Form E output + supplements
5. Evidence upload list & bundle (zip folder)

### Phase 2: Polish & Compliance (2 weeks)
1. Solicitor partner integration (affiliate links)
2. User dashboard (save/resume)
3. Disclaimers everywhere

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