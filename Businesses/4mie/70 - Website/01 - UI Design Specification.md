# 4mie UI Design Specification

Comprehensive UI/UX documentation for the 4mie Form E guidance application.

---

## Table of Contents

1. [Design Philosophy](#design-philosophy)
2. [Design System](#design-system)
3. [Information Architecture](#information-architecture)
4. [Wireframes - Desktop](#wireframes-desktop)
5. [Wireframes - Mobile](#wireframes-mobile)
6. [Component Library](#component-library)
7. [Interaction Patterns](#interaction-patterns)
8. [Accessibility](#accessibility)
9. [Implementation Notes](#implementation-notes)

---

## Design Philosophy

### Core Principles

**1. Calm, Not Clinical**
Users are going through one of life's most stressful events. The UI should feel like a supportive guide, not a government form or a cold legal tool.

**2. Progressive Disclosure**
Never overwhelm. Show one thing at a time. Let complexity unfold naturally as the user progresses.

**3. Visible Progress**
Completing Form E feels endless. Constant progress feedback maintains motivation and reduces anxiety.

**4. Trust Through Transparency**
Be clear about what data is collected, how it's used, and what the tool does and doesn't do.

**5. Forgiving & Flexible**
Allow users to go back, edit, save, and return. Mistakes should be easy to fix.

### User Emotional Journey

```
Start        →    Middle           →    End
───────────────────────────────────────────────
Anxious           Focused              Relieved
Overwhelmed       Engaged              Accomplished
Uncertain         Trusting             Confident

UI Response:
Reassuring        Clear & Guided       Celebratory
Simple            Efficient            Supportive
```

### Design Metaphor

**The Helpful Friend Who Knows Legal Stuff**

Not a solicitor (too formal), not a chatbot (too impersonal), but a knowledgeable friend sitting with you, asking questions, and writing things down for you.

---

## Design System

### Colour Palette

```
┌─────────────────────────────────────────────────────────────┐
│ PRIMARY COLOURS                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ████████  Primary         #2D7D9A   Calm teal              │
│  ████████  Primary Dark    #1E5A6E   Hover states           │
│  ████████  Primary Light   #E8F4F7   Backgrounds            │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ SECONDARY COLOURS                                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ████████  Success         #5BA88B   Complete, positive     │
│  ████████  Warning         #E8B44F   Attention needed       │
│  ████████  Error           #D66853   Problems (use rarely)  │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ NEUTRALS                                                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ████████  Text Primary    #1A1A1A   Main text              │
│  ████████  Text Secondary  #6B7280   Supporting text        │
│  ████████  Border          #E5E7EB   Dividers, borders      │
│  ████████  Background      #F8F9FA   Page background        │
│  ████████  Surface         #FFFFFF   Cards, inputs          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Typography

```
┌─────────────────────────────────────────────────────────────┐
│ FONT FAMILY                                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Primary: Inter (Google Fonts)                               │
│ Fallback: -apple-system, BlinkMacSystemFont, sans-serif     │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ TYPE SCALE                                                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│ Display    32px / 40px line    Semi-bold   Hero headlines   │
│ H1         28px / 36px line    Semi-bold   Page titles      │
│ H2         22px / 28px line    Semi-bold   Section titles   │
│ H3         18px / 24px line    Medium      Card titles      │
│ Body       16px / 26px line    Regular     Main content     │
│ Small      14px / 20px line    Regular     Supporting       │
│ Caption    12px / 16px line    Regular     Labels, hints    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Spacing System

```
Base unit: 4px

xs:   4px    Tight spacing
sm:   8px    Between related elements
md:   16px   Standard spacing
lg:   24px   Between sections
xl:   32px   Major sections
2xl:  48px   Page margins
3xl:  64px   Hero spacing
```

### Border Radius

```
sm:   4px    Inputs, small buttons
md:   8px    Cards, modals
lg:   12px   Large cards
full: 9999px Pills, avatars
```

### Shadows

```
sm:   0 1px 2px rgba(0,0,0,0.05)      Subtle lift
md:   0 4px 6px rgba(0,0,0,0.07)      Cards
lg:   0 10px 15px rgba(0,0,0,0.1)     Modals, dropdowns
```

---

## Information Architecture

### Site Map

```
4mie.com
│
├── / (Landing Page)
│   ├── Hero
│   ├── How it works
│   ├── Pricing
│   ├── FAQ
│   └── CTA
│
├── /login
├── /signup
│
├── /app (Authenticated)
│   ├── /app/dashboard
│   │   └── Sessions list (new, in progress, complete)
│   │
│   ├── /app/session/[id]
│   │   ├── /disclaimer
│   │   ├── /interview (main chat interface)
│   │   ├── /review (section review)
│   │   └── /complete (download & next steps)
│   │
│   ├── /app/documents
│   │   └── Upload & manage evidence
│   │
│   └── /app/settings
│       └── Account, billing
│
├── /pricing
├── /about
├── /privacy
├── /terms
└── /contact
```

### User Flow

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│ Landing  │───▶│  Signup  │───▶│Disclaimer│───▶│Interview │
└──────────┘    └──────────┘    └──────────┘    └────┬─────┘
                                                     │
                     ┌───────────────────────────────┤
                     │                               │
                     ▼                               ▼
              ┌──────────┐                    ┌──────────┐
              │   Save   │                    │  Review  │
              │  & Exit  │                    │ Section  │
              └────┬─────┘                    └────┬─────┘
                   │                               │
                   ▼                               │
              ┌──────────┐                         │
              │Dashboard │◀────────────────────────┤
              │ (Resume) │                         │
              └──────────┘                         ▼
                                            ┌──────────┐
                                            │ Complete │
                                            │ Download │
                                            └────┬─────┘
                                                 │
                                                 ▼
                                            ┌──────────┐
                                            │ Solicitor│
                                            │  Upsell  │
                                            └──────────┘
```

---

## Wireframes - Desktop

### Screen 1: Landing Page

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ 🏠 4mie                           How it works  Pricing  Login  [Start] │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│                                                                             │
│                         Form E Made Simple                                  │
│                                                                             │
│              AI-guided divorce financial statement.                         │
│              Solicitor-ready in under an hour.                              │
│                                                                             │
│                    ┌─────────────────────────┐                              │
│                    │   Start Your Form E     │                              │
│                    └─────────────────────────┘                              │
│                                                                             │
│                    ✓ No legal jargon                                        │
│                    ✓ Save and resume anytime                                │
│                    ✓ Court-ready PDF output                                 │
│                                                                             │
│ ─────────────────────────────────────────────────────────────────────────── │
│                                                                             │
│                           How it works                                      │
│                                                                             │
│    ┌─────────────┐      ┌─────────────┐      ┌─────────────┐                │
│    │      1      │      │      2      │      │      3      │                │
│    │             │      │             │      │             │                │
│    │  Answer     │ ───▶ │  AI writes  │ ───▶ │  Download   │                │
│    │  questions  │      │  Form E     │      │  & review   │                │
│    │             │      │             │      │             │                │
│    └─────────────┘      └─────────────┘      └─────────────┘                │
│                                                                             │
│    Chat naturally        We turn your         Get your PDF                  │
│    in plain English      answers into         ready for court               │
│                          proper Form E                                      │
│                          language                                           │
│                                                                             │
│ ─────────────────────────────────────────────────────────────────────────── │
│                                                                             │
│                            Pricing                                          │
│                                                                             │
│    ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐            │
│    │     Basic       │  │      Pro        │  │     Pro+        │            │
│    │                 │  │   POPULAR       │  │                 │            │
│    │     £99         │  │     £199        │  │     £299        │            │
│    │                 │  │                 │  │                 │            │
│    │ • Form E PDF    │  │ • Everything in │  │ • Everything in │            │
│    │ • Basic         │  │   Basic         │  │   Pro           │            │
│    │   guidance      │  │ • AI-optimised  │  │ • Solicitor     │            │
│    │                 │  │   narratives    │  │   review        │            │
│    │                 │  │ • Evidence      │  │                 │            │
│    │                 │  │   bundle        │  │                 │            │
│    │                 │  │                 │  │                 │            │
│    │    [Start]      │  │    [Start]      │  │    [Start]      │            │
│    └─────────────────┘  └─────────────────┘  └─────────────────┘            │
│                                                                             │
│ ─────────────────────────────────────────────────────────────────────────── │
│                                                                             │
│  ⚠️ 4mie is not a law firm. We provide guidance, not legal advice.          │
│     Always have a solicitor review your Form E before court submission.     │
│                                                                             │
│ ─────────────────────────────────────────────────────────────────────────── │
│                                                                             │
│  4mie    Privacy  Terms  Contact           © 2025 4mie. Form E, For Me.     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Screen 2: Sign Up / Login

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ 🏠 4mie                                                                 │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│                        ┌───────────────────────────────┐                    │
│                        │                               │                    │
│                        │      Create your account      │                    │
│                        │                               │                    │
│                        │  ┌───────────────────────┐    │                    │
│                        │  │ Email                 │    │                    │
│                        │  └───────────────────────┘    │                    │
│                        │                               │                    │
│                        │  ┌───────────────────────┐    │                    │
│                        │  │ Password              │    │                    │
│                        │  └───────────────────────┘    │                    │
│                        │                               │                    │
│                        │  ┌───────────────────────┐    │                    │
│                        │  │     Create account    │    │                    │
│                        │  └───────────────────────┘    │                    │
│                        │                               │                    │
│                        │  ─────── or continue with ─── │                    │
│                        │                               │                    │
│                        │  ┌───────────────────────┐    │                    │
│                        │  │     G  Google         │    │                    │
│                        │  └───────────────────────┘    │                    │
│                        │                               │                    │
│                        │  Already have an account?     │                    │
│                        │  Log in                       │                    │
│                        │                               │                    │
│                        │  ─────────────────────────    │                    │
│                        │  🔒 Your data is encrypted     │                    │
│                        │     and never shared          │                    │
│                        │                               │                    │
│                        └───────────────────────────────┘                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Screen 3: Disclaimer Acceptance

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ 🏠 4mie                                              mark@example.com ▼ │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│                        ┌───────────────────────────────────────┐            │
│                        │                                       │            │
│                        │        Before we begin                │            │
│                        │                                       │            │
│                        │  Form E is a legal document that      │            │
│                        │  you'll sign under oath. Please       │            │
│                        │  confirm you understand:              │            │
│                        │                                       │            │
│                        │  ┌─────────────────────────────────┐  │            │
│                        │  │                                 │  │            │
│                        │  │  □  This is guidance, not       │  │            │
│                        │  │     legal advice. A solicitor   │  │            │
│                        │  │     should review my Form E     │  │            │
│                        │  │     before I submit it.         │  │            │
│                        │  │                                 │  │            │
│                        │  │  □  I must provide truthful     │  │            │
│                        │  │     information. I have a       │  │            │
│                        │  │     legal duty of full and      │  │            │
│                        │  │     frank disclosure.           │  │            │
│                        │  │                                 │  │            │
│                        │  │  □  I understand that false     │  │            │
│                        │  │     statements could result     │  │            │
│                        │  │     in serious consequences.    │  │            │
│                        │  │                                 │  │            │
│                        │  └─────────────────────────────────┘  │            │
│                        │                                       │            │
│                        │  ┌─────────────────────────────────┐  │            │
│                        │  │   I understand, let's begin     │  │            │
│                        │  └─────────────────────────────────┘  │            │
│                        │                                       │            │
│                        │           (button disabled until      │            │
│                        │            all boxes checked)         │            │
│                        │                                       │            │
│                        └───────────────────────────────────────┘            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Screen 4: Main Interview Interface (Core App)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ 🏠 4mie                                    [Save progress]  [Exit]      │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│ ┌───────────────────┐ ┌─────────────────────────────────────────────────┐   │
│ │                   │ │                                                 │   │
│ │    SECTIONS       │ │                                                 │   │
│ │                   │ │  ┌───────────────────────────────────────────┐  │   │
│ │ ┌───────────────┐ │ │  │ 🤖                                         │  │   │
│ │ │ ✓ Personal    │ │ │  │                                           │  │   │
│ │ └───────────────┘ │ │  │ Now let's talk about your bank accounts.  │  │   │
│ │ ┌───────────────┐ │ │  │                                           │  │   │
│ │ │ ✓ Marriage    │ │ │  │ I need to know about ALL accounts:        │  │   │
│ │ └───────────────┘ │ │  │                                           │  │   │
│ │ ┌───────────────┐ │ │  │   • Current accounts                      │  │   │
│ │ │ ✓ Children    │ │ │  │   • Savings accounts                      │  │   │
│ │ └───────────────┘ │ │  │   • ISAs                                  │  │   │
│ │ ┌───────────────┐ │ │  │   • Joint accounts                        │  │   │
│ │ │ ✓ Property    │ │ │  │   • Accounts you rarely use               │  │   │
│ │ └───────────────┘ │ │  │                                           │  │   │
│ │ ┌───────────────┐ │ │  │ The court requires 12 months of           │  │   │
│ │ │ ● Bank        │ │ │  │ statements for each account.              │  │   │
│ │ │   accounts    │ │ │  │                                           │  │   │
│ │ └───────────────┘ │ │  │ What's your main current account?         │  │   │
│ │ ┌───────────────┐ │ │  └───────────────────────────────────────────┘  │   │
│ │ │ ○ Investments │ │ │                                                 │   │
│ │ └───────────────┘ │ │                                                 │   │
│ │ ┌───────────────┐ │ │  ┌───────────────────────────────────────────┐  │   │
│ │ │ ○ Pensions    │ │ │  │ 👤                                        │  │   │
│ │ └───────────────┘ │ │  │                                           │  │   │
│ │ ┌───────────────┐ │ │  │ My main account is with Barclays, it's    │  │   │
│ │ │ ○ Income      │ │ │  │ a current account in my name only.        │  │   │
│ │ └───────────────┘ │ │  │ Balance is about £2,300.                  │  │   │
│ │ ┌───────────────┐ │ │  │                                           │  │   │
│ │ │ ○ Budget      │ │ │  └───────────────────────────────────────────┘  │   │
│ │ └───────────────┘ │ │                                                 │   │
│ │ ┌───────────────┐ │ │  ┌───────────────────────────────────────────┐  │   │
│ │ │ ○ Other info  │ │ │  │ 🤖                                         │  │   │
│ │ └───────────────┘ │ │  │                                           │  │   │
│ │ ┌───────────────┐ │ │  │ Got it - Barclays current account, sole   │  │   │
│ │ │ ○ Settlement  │ │ │  │ name, approximately £2,300.               │  │   │
│ │ └───────────────┘ │ │  │                                           │  │   │
│ │                   │ │  │ Do you have any other accounts?           │  │   │
│ │ ───────────────── │ │  │                                           │  │   │
│ │                   │ │  └───────────────────────────────────────────┘  │   │
│ │  ████████░░░░░░   │ │                                                 │   │
│ │  40% complete     │ │  ┌─────────────────────────────────────────┐    │   │
│ │                   │ │  │ Type your answer...                     │    │   │
│ │  ~25 min left     │ │  │                                         │    │   │
│ │                   │ │  └─────────────────────────────────────────┘    │   │
│ │                   │ │                                                 │   │
│ │                   │ │                          [Continue →]           │   │
│ │                   │ │                                                 │   │
│ └───────────────────┘ └─────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Screen 5: Section Summary Card (Inline)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│     ┌───────────────────────────────────────────────────────────────────┐   │
│     │                                                                   │   │
│     │  ✓ Bank Accounts Complete                                         │   │
│     │                                                                   │   │
│     │  ┌─────────────────────────────────────────────────────────────┐  │   │
│     │  │                                                             │  │   │
│     │  │  Account                      Type        Balance   Share   │  │   │
│     │  │  ─────────────────────────────────────────────────────────  │  │   │
│     │  │  Barclays                     Current     £2,340    100%    │  │   │
│     │  │  Barclays                     Savings     £15,000   100%    │  │   │
│     │  │  Nationwide                   ISA         £8,200    100%    │  │   │
│     │  │  NatWest (joint with Sarah)   Current     £2,200    50%     │  │   │
│     │  │  ─────────────────────────────────────────────────────────  │  │   │
│     │  │  Total value of your interest            £26,640            │  │   │
│     │  │                                                             │  │   │
│     │  └─────────────────────────────────────────────────────────────┘  │   │
│     │                                                                   │   │
│     │  📎 Documents needed:                                             │   │
│     │     □ 12 months statements - Barclays Current                     │   │
│     │     □ 12 months statements - Barclays Savings                     │   │
│     │     □ 12 months statements - Nationwide ISA                       │   │
│     │     □ 12 months statements - NatWest Joint                        │   │
│     │                                                                   │   │
│     │  ┌───────────────┐  ┌────────────────────────────────┐            │   │
│     │  │ Edit answers  │  │ Looks good, continue →         │            │   │
│     │  └───────────────┘  └────────────────────────────────┘            │   │
│     │                                                                   │   │
│     └───────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Screen 6: Complexity Flag / Solicitor Recommendation

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│     ┌───────────────────────────────────────────────────────────────────┐   │
│     │                                                                   │   │
│     │  ⚠️  Professional advice recommended                              │   │
│     │                                                                   │   │
│     │  Based on what you've told me, your situation has some            │   │
│     │  complexities that would benefit from professional input:         │   │
│     │                                                                   │   │
│     │  • Business interests valued over £50,000                         │   │
│     │  • Defined benefit pension scheme                                 │   │
│     │                                                                   │   │
│     │  These areas can significantly affect your settlement and         │   │
│     │  may require specialist valuation.                                │   │
│     │                                                                   │   │
│     │  ┌─────────────────────────────────────────────────────────────┐  │   │
│     │  │                                                             │  │   │
│     │  │   Get a solicitor review                                    │  │   │
│     │  │   Fixed fee: £199                                           │  │   │
│     │  │                                                             │  │   │
│     │  │   ✓ Review of your complete Form E                          │  │   │
│     │  │   ✓ Advice on complex areas                                 │  │   │
│     │  │   ✓ 30-minute phone consultation                            │  │   │
│     │  │                                                             │  │   │
│     │  │   [Add to my order]                                         │  │   │
│     │  │                                                             │  │   │
│     │  └─────────────────────────────────────────────────────────────┘  │   │
│     │                                                                   │   │
│     │  [Continue without solicitor review]                              │   │
│     │                                                                   │   │
│     └───────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Screen 7: Save & Exit Confirmation

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│     ┌───────────────────────────────────────────────────────────────────┐   │
│     │                                                                   │   │
│     │                    Save and exit?                                 │   │
│     │                                                                   │   │
│     │              ┌─────────────────────┐                              │   │
│     │              │     ████████░░░     │                              │   │
│     │              │      65%            │                              │   │
│     │              └─────────────────────┘                              │   │
│     │                                                                   │   │
│     │         Your progress is automatically saved.                     │   │
│     │         You can return anytime to continue.                       │   │
│     │                                                                   │   │
│     │         ✓ Personal details                                        │   │
│     │         ✓ Marriage & family                                       │   │
│     │         ✓ Property                                                │   │
│     │         ✓ Bank accounts                                           │   │
│     │         ✓ Investments                                             │   │
│     │         ○ Pensions (not started)                                  │   │
│     │         ○ Income (not started)                                    │   │
│     │         ○ Budget (not started)                                    │   │
│     │         ○ Other information (not started)                         │   │
│     │                                                                   │   │
│     │     ┌─────────────────┐  ┌─────────────────────┐                  │   │
│     │     │ Keep working    │  │ Save and exit       │                  │   │
│     │     └─────────────────┘  └─────────────────────┘                  │   │
│     │                                                                   │   │
│     └───────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Screen 8: Dashboard (Returning User)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ 🏠 4mie                                    [Documents]  [Settings]  ▼   │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│   Welcome back, Mark                                                        │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                                                                     │   │
│   │   📝 Your Form E                                                    │   │
│   │                                                                     │   │
│   │   ┌─────────────────────────────────────────────────────────────┐   │   │
│   │   │                                                             │   │   │
│   │   │   Status: In progress                                       │   │   │
│   │   │                                                             │   │   │
│   │   │   ██████████████░░░░░░░░░░░░░░░░  65% complete              │   │   │
│   │   │                                                             │   │   │
│   │   │   Last edited: Today at 2:34 PM                             │   │   │
│   │   │   Next section: Pensions                                    │   │   │
│   │   │                                                             │   │   │
│   │   │   ┌─────────────────────────────────────────────┐           │   │   │
│   │   │   │            Continue where I left off        │           │   │   │
│   │   │   └─────────────────────────────────────────────┘           │   │   │
│   │   │                                                             │   │   │
│   │   │   [Review completed sections]  [Start over]                 │   │   │
│   │   │                                                             │   │   │
│   │   └─────────────────────────────────────────────────────────────┘   │   │
│   │                                                                     │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                                                                     │   │
│   │   📎 Documents to gather                                            │   │
│   │                                                                     │   │
│   │   The following documents are needed for your Form E:               │   │
│   │                                                                     │   │
│   │   □ Bank statements - 12 months (4 accounts)                        │   │
│   │   □ Property valuation                                              │   │
│   │   □ Mortgage statement                                              │   │
│   │   □ Pension CETV (not yet requested)                                │   │
│   │                                                                     │   │
│   │   [Upload documents]                                                │   │
│   │                                                                     │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Screen 9: Final Summary / Completion

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ ┌─────────────────────────────────────────────────────────────────────────┐ │
│ │ 🏠 4mie                                                         ▼       │ │
│ └─────────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│                         ✓ Your Form E is ready                              │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                                                                     │   │
│   │   FINANCIAL SUMMARY                                                 │   │
│   │                                                                     │   │
│   │   ┌─────────────────────────────────────────────────────────────┐   │   │
│   │   │                                                             │   │   │
│   │   │   Assets                                                    │   │   │
│   │   │   ─────────────────────────────────────────────────         │   │   │
│   │   │   Property (your share)              £135,000               │   │   │
│   │   │   Bank accounts                      £26,640                │   │   │
│   │   │   Investments                        £12,500                │   │   │
│   │   │   Pensions (CETV)                    £89,000                │   │   │
│   │   │   Other assets                       £8,500                 │   │   │
│   │   │   ─────────────────────────────────────────────────         │   │   │
│   │   │   Total assets                       £271,640               │   │   │
│   │   │                                                             │   │   │
│   │   │   Liabilities                                               │   │   │
│   │   │   ─────────────────────────────────────────────────         │   │   │
│   │   │   Total debts                        -£18,400               │   │   │
│   │   │                                                             │   │   │
│   │   │   ═════════════════════════════════════════════════         │   │   │
│   │   │   NET WORTH                          £253,240               │   │   │
│   │   │                                                             │   │   │
│   │   │   Monthly budget                     £3,200                 │   │   │
│   │   │                                                             │   │   │
│   │   └─────────────────────────────────────────────────────────────┘   │   │
│   │                                                                     │   │
│   │   [View full breakdown]                                             │   │
│   │                                                                     │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                                                                     │   │
│   │   DOWNLOADS                                                         │   │
│   │                                                                     │   │
│   │   ┌─────────────────────────────────────────────────────────────┐   │   │
│   │   │  📄  Download Form E (PDF)                              ↓   │   │   │
│   │   └─────────────────────────────────────────────────────────────┘   │   │
│   │                                                                     │   │
│   │   ┌─────────────────────────────────────────────────────────────┐   │   │
│   │   │  📁  Download evidence bundle (ZIP)                     ↓   │   │   │
│   │   └─────────────────────────────────────────────────────────────┘   │   │
│   │                                                                     │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                                                                     │   │
│   │   ⚠️  IMPORTANT: Next steps                                         │   │
│   │                                                                     │   │
│   │   1. Have a solicitor review your Form E before submitting          │   │
│   │   2. Sign the Statement of Truth (page 28)                          │   │
│   │   3. Attach all supporting documents                                │   │
│   │   4. File with the court by your deadline                           │   │
│   │                                                                     │   │
│   │   ┌─────────────────────────────────────────────────────────────┐   │   │
│   │   │                                                             │   │   │
│   │   │   📞  Get solicitor review - £199                           │   │   │
│   │   │                                                             │   │   │
│   │   │   A qualified family solicitor will:                        │   │   │
│   │   │   ✓ Review your complete Form E                             │   │   │
│   │   │   ✓ Check for errors or omissions                           │   │   │
│   │   │   ✓ Advise on your settlement proposals                     │   │   │
│   │   │   ✓ 30-minute phone consultation                            │   │   │
│   │   │                                                             │   │   │
│   │   │   [Add solicitor review]                                    │   │   │
│   │   │                                                             │   │   │
│   │   └─────────────────────────────────────────────────────────────┘   │   │
│   │                                                                     │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Wireframes - Mobile

### Mobile: Main Interview

```
┌─────────────────────────┐
│ 4mie           [≡] [×]  │
├─────────────────────────┤
│ Bank accounts     5/12  │
│ ████████████░░░░░ 42%   │
├─────────────────────────┤
│                         │
│ ┌─────────────────────┐ │
│ │ 🤖                   │ │
│ │                     │ │
│ │ Now let's talk      │ │
│ │ about your bank     │ │
│ │ accounts.           │ │
│ │                     │ │
│ │ I need to know      │ │
│ │ about ALL accounts: │ │
│ │                     │ │
│ │ • Current accounts  │ │
│ │ • Savings           │ │
│ │ • ISAs              │ │
│ │ • Joint accounts    │ │
│ │                     │ │
│ │ What's your main    │ │
│ │ current account?    │ │
│ └─────────────────────┘ │
│                         │
│ ┌─────────────────────┐ │
│ │ 👤                  │ │
│ │ Barclays current,   │ │
│ │ sole name, about    │ │
│ │ £2,300              │ │
│ └─────────────────────┘ │
│                         │
│ ┌─────────────────────┐ │
│ │ 🤖                   │ │
│ │ Got it. Any other   │ │
│ │ accounts?           │ │
│ └─────────────────────┘ │
│                         │
├─────────────────────────┤
│ ┌─────────────────────┐ │
│ │ Type your answer... │ │
│ └─────────────────────┘ │
│         [Continue →]    │
└─────────────────────────┘
```

### Mobile: Section Summary

```
┌─────────────────────────┐
│ 4mie           [≡] [×]  │
├─────────────────────────┤
│                         │
│  ✓ Bank Accounts        │
│    Complete             │
│                         │
│ ┌─────────────────────┐ │
│ │                     │ │
│ │ Barclays Current    │ │
│ │ Sole · £2,340       │ │
│ │                     │ │
│ │ Barclays Savings    │ │
│ │ Sole · £15,000      │ │
│ │                     │ │
│ │ Nationwide ISA      │ │
│ │ Sole · £8,200       │ │
│ │                     │ │
│ │ NatWest Joint       │ │
│ │ 50% · £1,100        │ │
│ │                     │ │
│ ├─────────────────────┤ │
│ │ Your total: £26,640 │ │
│ └─────────────────────┘ │
│                         │
│ 📎 4 statements needed  │
│                         │
│ ┌─────────────────────┐ │
│ │      Edit           │ │
│ └─────────────────────┘ │
│ ┌─────────────────────┐ │
│ │   Continue →        │ │
│ └─────────────────────┘ │
│                         │
└─────────────────────────┘
```

### Mobile: Navigation Menu

```
┌─────────────────────────┐
│ 4mie              [×]   │
├─────────────────────────┤
│                         │
│  Your progress: 42%     │
│  ████████░░░░░░░░░░░    │
│                         │
│ ─────────────────────── │
│                         │
│  ✓ Personal details     │
│  ✓ Marriage & family    │
│  ✓ Children             │
│  ✓ Property             │
│  ● Bank accounts        │
│  ○ Investments          │
│  ○ Pensions             │
│  ○ Income               │
│  ○ Budget               │
│  ○ Other information    │
│  ○ Settlement           │
│  ○ Summary              │
│                         │
│ ─────────────────────── │
│                         │
│  [Save and exit]        │
│                         │
│  [Help]                 │
│                         │
└─────────────────────────┘
```

---

## Component Library

### Buttons

```
PRIMARY (Main CTA)
┌─────────────────────────────┐
│       Continue →            │  Background: Primary
└─────────────────────────────┘  Text: White
                                 Radius: md
                                 Padding: 12px 24px

SECONDARY
┌─────────────────────────────┐
│       Edit answers          │  Background: White
└─────────────────────────────┘  Border: Primary
                                 Text: Primary

TERTIARY (Text link style)
    Save and exit               Text: Primary
                                Underline on hover

DISABLED
┌─────────────────────────────┐
│       Continue →            │  Background: Border color
└─────────────────────────────┘  Text: Text Secondary
                                 Cursor: not-allowed
```

### Input Fields

```
DEFAULT
┌─────────────────────────────────────────┐
│ Your answer                             │
│                                         │
│                                         │
└─────────────────────────────────────────┘
Border: Border color
Background: Surface
Radius: sm
Padding: 12px 16px

FOCUSED
┌─────────────────────────────────────────┐
│ Your answer                             │
│ Typing here...                          │
│                                         │
└─────────────────────────────────────────┘
Border: Primary (2px)
Box-shadow: Primary light

WITH LABEL
Email address
┌─────────────────────────────────────────┐
│ mark@example.com                        │
└─────────────────────────────────────────┘
Label: Caption size, Text Secondary

ERROR STATE
Email address
┌─────────────────────────────────────────┐
│ notanemail                              │
└─────────────────────────────────────────┘
Please enter a valid email address
Border: Error
Helper text: Error color
```

### Cards

```
STANDARD CARD
┌─────────────────────────────────────────┐
│                                         │
│  Card Title                             │
│                                         │
│  Card content goes here. Can contain    │
│  multiple lines of text and other       │
│  components.                            │
│                                         │
│  [Action button]                        │
│                                         │
└─────────────────────────────────────────┘
Background: Surface
Border: none
Shadow: md
Radius: md
Padding: 24px

SUCCESS CARD
┌─────────────────────────────────────────┐
│ ✓ Section Complete                      │
│                                         │
│  Content...                             │
│                                         │
└─────────────────────────────────────────┘
Left border: 4px Success color

WARNING CARD
┌─────────────────────────────────────────┐
│ ⚠️ Attention needed                     │
│                                         │
│  Content...                             │
│                                         │
└─────────────────────────────────────────┘
Left border: 4px Warning color
Background: Warning at 10% opacity
```

### Progress Indicators

```
PROGRESS BAR
████████████░░░░░░░░░░░░░░░░░░  42%

Bar background: Border color
Bar fill: Primary
Text: Small, Text Secondary

SECTION STATUS
✓ Complete    (Success color)
● Current     (Primary color)
○ Pending     (Border color)
```

### Chat Messages

```
AI MESSAGE
┌───────────────────────────────────────┐
│ 🤖                                     │
│                                       │
│ Message content from the AI goes      │
│ here. Can include:                    │
│                                       │
│ • Bullet points                       │
│ • Multiple paragraphs                 │
│                                       │
│ And questions to the user.            │
└───────────────────────────────────────┘
Background: Primary Light
Radius: md (squared top-left)
Max-width: 85%
Align: left

USER MESSAGE
┌───────────────────────────────────────┐
│                                    👤 │
│                                       │
│ User's response goes here.            │
│                                       │
└───────────────────────────────────────┘
Background: Surface
Border: Border color
Radius: md (squared top-right)
Max-width: 85%
Align: right
```

---

## Interaction Patterns

### Auto-save

- Save after each completed answer (debounced 2 seconds)
- Show subtle "Saved" indicator
- Never lose user data

```
Typing... → (pause 2s) → ✓ Saved (fade after 2s)
```

### Section Navigation

- Completed sections are clickable for review
- Current section highlighted
- Pending sections visible but greyed
- Clicking pending section shows "Complete current section first"

### Keyboard Shortcuts (Desktop)

```
Enter          → Submit current answer (if valid)
Shift + Enter  → New line in text area
Escape         → Open save/exit dialog
Ctrl + S       → Force save
```

### Error Handling

```
VALIDATION ERROR (inline)
┌─────────────────────────────────────────┐
│ 50000                                   │
└─────────────────────────────────────────┘
Please enter a valid amount (e.g., £50,000)

SYSTEM ERROR (toast)
┌─────────────────────────────────────────┐
│ ⚠️ Couldn't save. Retrying...           │
└─────────────────────────────────────────┘
(Auto-retry, then show "Contact support" if persists)

CONNECTION LOST (banner)
┌─────────────────────────────────────────────────────────────┐
│ 📡 Connection lost. Your work is saved locally.   [Retry]   │
└─────────────────────────────────────────────────────────────┘
```

### Loading States

```
BUTTON LOADING
┌─────────────────────────────┐
│     ◌ Processing...         │
└─────────────────────────────┘

CONTENT LOADING
┌─────────────────────────────────────────┐
│                                         │
│  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░          │
│  ░░░░░░░░░░░░░░░░░░░                    │
│  ░░░░░░░░░░░░░░░░░░░░░░░░░              │
│                                         │
└─────────────────────────────────────────┘
(Skeleton loading with subtle animation)
```

---

## Accessibility

### WCAG 2.1 AA Compliance

**Colour Contrast**
- All text meets 4.5:1 contrast ratio minimum
- Large text (18px+) meets 3:1 minimum
- Interactive elements have visible focus states

**Keyboard Navigation**
- All interactive elements focusable via Tab
- Logical tab order
- Skip links to main content
- Escape closes modals/menus

**Screen Readers**
- Semantic HTML (headings, landmarks, lists)
- ARIA labels where needed
- Form labels properly associated
- Progress announced on section completion

**Motion**
- Respect `prefers-reduced-motion`
- No essential animations
- No auto-playing content

### Focus States

```
BUTTON FOCUS
┌─────────────────────────────┐
│       Continue →            │
└─────────────────────────────┘
┌───────────────────────────────┐  ← 2px offset outline
                                    Primary color

INPUT FOCUS
┌─────────────────────────────────────────┐
│ Type here                               │
└─────────────────────────────────────────┘
Border becomes Primary (2px)
Subtle box-shadow
```

---

## Implementation Notes

### Tech Recommendations

**Framework**: Next.js 14 (App Router)
**Styling**: Tailwind CSS
**Components**: shadcn/ui (customised to design system)
**Forms**: React Hook Form
**State**: Zustand (for form state persistence)
**Animation**: Framer Motion (minimal, respects reduced motion)

### Component Structure

```
/components
  /ui
    Button.tsx
    Input.tsx
    Card.tsx
    Progress.tsx
    ChatMessage.tsx
  /interview
    InterviewLayout.tsx
    SectionSidebar.tsx
    ChatArea.tsx
    SectionSummary.tsx
  /common
    Header.tsx
    Footer.tsx
    LoadingState.tsx
```

### Key Technical Considerations

1. **Auto-save**: Debounced saves to database + local storage backup
2. **Offline support**: Service worker for basic offline access
3. **Streaming**: AI responses should stream for better UX
4. **PDF generation**: Server-side with pdf-lib or Puppeteer
5. **File uploads**: Presigned S3 URLs, client-side compression

### MVP Scope

**Include:**
- Landing page
- Auth (email + Google)
- Disclaimer flow
- Main interview (chat-style)
- Section summaries
- Progress tracking
- PDF download
- Basic mobile responsive

**Defer to v1.1:**
- Document upload/management
- Solicitor integration
- Evidence bundle generation
- Full offline support
- Native mobile app

---

## Appendix: Design Resources

### Inspiration

- **Typeform**: Progressive disclosure, one question at a time
- **Lemonade**: Conversational insurance, friendly tone
- **Notion**: Clean, calm productivity aesthetic
- **Linear**: Minimal, focused interface

### Tools for Visual Design

- **Figma**: Wireframes → high-fidelity
- **Excalidraw**: Quick sketches
- **Coolors**: Palette generation
- **Realtime Colors**: Preview palette on UI

### Icon Libraries

- **Lucide**: Clean, consistent (recommended)
- **Heroicons**: Good alternative
- Avoid: Overly playful or complex icons

---

*Document version: 1.0*
*Created: December 2025*
*For: 4mie MVP Development*
