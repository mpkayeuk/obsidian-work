# Cursor Development Plan for CIOJoy Website (with Context)

This document provides a sequence of prompts for an AI code generator (like Cursor) to build the CIOJoy marketing website. Each prompt includes aliased paths to our strategy documents to provide rich context.

**Instructions:** Use these prompts in order. The linked documents contain the detailed information needed to complete each task.

---

### Phase 1: Project Setup & Foundation

**Prompt 1: Initial Project Setup**
```
Using `npx create-next-app@latest .`, initialize a new Next.js 14+ project in the current directory. When prompted by the installer, select TypeScript, Tailwind CSS, and the `app` router. This will turn the current project root into the Next.js project root.
```

**Prompt 2: Configure Tailwind CSS**
```
Configure `tailwind.config.ts` with the brand colours and typography defined in our [Website Plan](@docs/src/70 - Website/00 - Website Plan.md#2-branding--tech-stack). The primary background is `#04026F` and the accent is `#FAE900`.
```

---

### Phase 2: Core Components

**Prompt 3: Create the Navbar**
```
Create a responsive Navbar component. It should be on a dark blue background. The navigation links should match the site structure defined in the [Website Plan](@docs/src/70 - Website/00 - Website Plan.md#3-site-structure). Add a call-to-action button on the far right: "Start Your Subscription".
```

**Prompt 4: Create the Footer**
```
Create a simple Footer component with links to the main pages, social media icons, and a copyright notice: `© CIOJoy Ltd [Current Year]`.
```

---

### Phase 3: Home Page Construction

**Prompt 5: Build the Hero Section**
```
Create the hero section for the Home page. Use the messaging from our [Elevator Pitch document](@docs/src/60 - Pitches/00 - Elevator Pitch.md) as the primary copy. The main headline should be: "Stop Worrying About Tech. Start Growing Your Business." The subheadline should be: "CIOJoy provides expert technology leadership on a flexible monthly subscription, helping you ship faster and improve profitability." Add a primary CTA button "View Pricing" and a secondary CTA "Our Services".
```

**Prompt 6: Build the "Problem" Section**
```
Below the hero, create a section titled "Are you facing these challenges?". Using the information in our [Customer Personas document](@docs/src/30 - Marketing and Sales/02 - Customer Personas.md), create two cards. The first card should be for "Sarah, The Startup CEO," titled "Developer Fog." The second card should be for "David, The Managing Partner," titled "Wasted Billable Hours."
```

**Prompt 7: Build the "Solution" Section**
```
Create a section titled "A Smarter Way to Handle Technology." This section should briefly explain the "unlimited requests" model defined in our [Service Offerings Overview](@docs/src/20 - Services/00 - Service Offerings Overview.md#the-unlimited-model).
```

---

### Phase 4: Additional Pages

**Prompt 8: Build the Pricing Page**
```
Create the Pricing page. The main headline should be "Simple, Transparent Pricing." Build a responsive three-column pricing table using the details from our [Subscription Tiers document](@docs/src/50 - Legal and Finance/00 - Subscription Tiers.md). Each column needs a "Subscribe" button.
```

**Prompt 9: Build the Services Page**
```
Create the Services page. It should have two main sections, based on our [Service Offerings Overview](@docs/src/20 - Services/00 - Service Offerings Overview.md). The first section describes the three Fractional CIO tiers. The second section is dedicated to the premium "Technical Co-Founder as a Service" program.
```

---

### Phase 5: Stripe & User Onboarding

**Prompt 10: Set up Stripe Checkout**
```
Create a new Next.js API route that uses the Stripe Node.js library to create a new Stripe Checkout session. It should take a price ID as input and return a checkout URL. This will be used by the "Subscribe" buttons on the pricing page.
```

**Prompt 11: Create the Stripe Webhook Endpoint**
```
Create a new API route at `api/webhooks/stripe` to handle incoming Stripe webhooks. The logic for this function should follow the sequence laid out in our [User Provisioning Flow document](@docs/src/70 - Website/00 - Website Plan.md#4-user-provisioning-flow-marketing-site---execution-site). For now, just log the `checkout.session.completed` event and add comments explaining where the user creation and email notification logic will go.
```