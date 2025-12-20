# CIOJoy Marketing Website Plan

This document outlines the strategy, structure, content, and technical plan for the CIOJoy marketing website.

---

## 1. Core Strategy

*   **Primary Goal:** To clearly communicate the value of CIOJoy's services and persuade target personas (Sarah and David) to subscribe to a monthly plan.
*   **Target Audience:** Non-technical founders of early-stage startups and partners/directors of established professional services firms.
*   **Key Message:** CIOJoy is a flexible, expert partner that solves critical technology problems (speed, efficiency, strategy) for a predictable monthly fee, allowing leaders to focus on their core business.

---

## 2. Branding & Tech Stack

*   **Branding:**
    *   **Primary Colour (Background):** `#04026F` (Dark Blue)
    *   **Accent Colour (CTAs, Highlights):** `#FAE900` (Bright Yellow)
    *   **Text Colour:** White / Light Gray on dark backgrounds.
    *   **Typography:** A clean, modern sans-serif font (e.g., Inter, Manrope).
*   **Tech Stack:**
    *   **Framework:** Next.js with TypeScript.
    *   **Styling:** Tailwind CSS.
    *   **Deployment:** Vercel.
    *   **Payments:** Stripe Checkout & Stripe Customer Portal.

---

## 3. Site Structure

*   **/ (Home):** Main landing page with a strong hero section, summary of services, social proof, and clear calls-to-action (CTAs).
*   **/services:** A detailed breakdown of the Fractional CIO tiers and the "Technical Co-Founder as a Service" program.
*   **/who-its-for:** A page dedicated to our personas, Sarah and David, showing we understand their unique problems.
*   **/pricing:** A clear, interactive pricing table comparing the different subscription tiers.
*   **/blog:** A collection of articles (from our GTM strategy) to build authority and attract inbound leads.
*   **/about:** The story and mission of CIOJoy.
*   **/contact:** A simple contact form.

---

## 4. User Provisioning Flow (Marketing Site -> Execution Site)

This section outlines the journey a user takes from subscribing to gaining access to the private client portal (the "execution site").

*   **Objective:** To create a seamless, automated onboarding experience.

*   **The Flow:**
    1.  **Subscription:** A user clicks "Subscribe" on the pricing page.
    2.  **Checkout:** They are redirected to a Stripe Checkout session to enter their payment details.
    3.  **Success:** Upon successful payment, Stripe redirects them to a `your-site.com/thank-you` page.
    4.  **Webhook Trigger:** Simultaneously, Stripe sends a `checkout.session.completed` webhook event to a secure API endpoint on our Vercel site.
    5.  **User Creation:** This API endpoint (a Vercel Serverless Function) receives the webhook and automatically performs the following actions:
        *   Creates a new user account in a user management system (e.g., **Supabase** or **Firebase Auth** is recommended for this).
        *   Adds metadata to the user's account, such as their subscription tier.
    6.  **Welcome Email:** The serverless function triggers a welcome email to the user (using a service like **Resend** or **SendGrid**).
    7.  **Login Instructions:** The welcome email contains a "magic link" that logs the user directly into the execution site (`portal.ciojoy.com`) for the first time, where they can set a password.

*   **Technology Summary for Provisioning:**
    *   **Stripe Checkout:** For the initial subscription.
    *   **Stripe Webhook:** To automate the process.
    *   **Vercel Serverless Function:** To handle the webhook logic.
    *   **Supabase/Firebase Auth:** To manage user accounts for the execution site.
    *   **Resend/SendGrid:** To send the transactional welcome email.