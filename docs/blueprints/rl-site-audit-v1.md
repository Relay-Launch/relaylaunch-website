# RelayLaunch.com Site Audit & Upgrade Plan (v1)

This document reviews the current RelayLaunch.com homepage and identifies updates to align it with the **new Control Center positioning**, **tagline**, and **service model** we have defined.

Use it as a checklist when you (or Claude + a designer) rebuild the site.

Primary brand decisions this audit assumes:

- **Primary tagline:** `Ops on Autopilot. You on Strategy.`  
- **Category descriptor:** `The Control Center for Your Digital Ops.`  
- **Hero direction:** Rocket RL badge + Relay▸Launch wordmark + Control Center dashboard visuals.  
- **Core offers:** Control Center Foundations, Automation Design & Build, Managed Digital Infrastructure & AIOps (retainer), backed by the service playbook and metrics docs. [code_file:175][code_file:170]  
- **Target client:** SMB / mid‑market B2B orgs that are already using or planning AI and automations, but lack a coherent infrastructure and control layer.[web:209][web:213]

---

## 1. Overall alignment

**Current site story:**

- Focuses on *"stop paying $400/month for tools that don't talk"* and consolidating 5–8 SMB tools into one connected stack (website, email, social, scheduling, payments, analytics).
- Offers productized packages (Signal, Blueprint, Relay, Sustain) centered on:
  - Custom website builds (Astro),  
  - Marketing automations (n8n, Mailchimp),  
  - Social content, SEO, and reporting.
- Positions RelayLaunch primarily as a **full-service digital presence + automation agency** for small businesses.

**New direction:**

- Positions RelayLaunch as a **digital infrastructure and AIOps partner** offering:
  - A reusable, multi‑tenant **Control Center** product for automations + infra.  
  - Consulting projects and retainers shaped around infrastructure, automation, and governance rather than broad marketing services. [code_file:175][code_file:131]  
- Emphasizes metrics (leads, automations, hours saved, change usage), approvals, and a well‑defined build + run framework. [code_file:170]

**Implication:**

- The current site is strong for a **"done‑for‑you digital presence agency"** but underplays the **Control Center, infra, AIOps, and governance** story.
- We want to shift from "replace your tech stack and do your marketing" to "design and run the infrastructure and control center that keeps all your AI and automations under control."

---

## 2. Hero section

**Current hero:**

> "Stop paying $400/month for tools that don't talk to each other."  
> "The average small business juggles 5–8 separate platforms ... RelayLaunch replaces that entire stack with one connected system, running your business while you focus on your clients."

**Issues:**

- Very tool‑price focused; positions you as a **tool consolidation cost‑saver**, not primarily as an infra/control center partner.
- Heavy emphasis on *"replace your entire stack"* may scare more technical or mid‑market buyers who already have critical systems they cannot just rip out.
- Doesn't mention AI, agents, approvals, or the Control Center by name, which are all key differentiators in 2026. [web:208][web:209][web:214]

**Recommended hero update (structure):**

- Logo: Rocket RL badge + Relay▸Launch wordmark.  
- Tagline under logo: `Ops on Autopilot. You on Strategy.`
- **New headline (choose one direction):**
  - "Tired of scattered AI tools? Meet your Control Center."  
  - or "Turn AI experiments into reliable operations."
- **Subhead:**
  - Two sentences that:
    - Reference AI + automation chaos in SMB/mid‑market. [web:209][web:210][web:213]  
    - Explicitly name the Control Center as the solution and mention infra + governance (not just marketing tools). [code_file:175][code_file:170]
- Primary CTA: `Book a Control Center assessment`.  
- Secondary CTA: `See a 3‑minute dashboard tour` (or "Explore the demo tenant").
- Visual: Screenshot/mock of the RelayLaunch Control Center seeded with realistic metrics and approvals, not just a marketing site mock. [code_file:134]

**Copy example for subhead:**

> "SMBs are racing to adopt AI and automations, but most end up with scattered tools, fragile workflows, and no clear picture of what's actually running. RelayLaunch designs and runs a single Control Center for your digital ops so your systems run on autopilot and you stay focused on strategy."

---

## 3. Stats band (33.2M / 37% / $300–500 / 5–10 hrs)

**Current content:**

- Focuses on small businesses overspending on disconnected tools and losing 5–10 hours/week to manual data entry.

**What to change:**

- Refresh stats to reflect **AI + automation adoption and pain**, not just tool count:
  - % of SMBs piloting AI but lacking production governance and measurement.[web:209][web:215][web:214]  
  - Average number of SaaS/AI tools and the proportion that are manually glued together.
- Introduce at least one metric about **automation/AI readiness** or **operational gains** (hours saved, uplift) to align with your Control Center metrics. [code_file:170]

**Placement:**

- Keep this band, but reframe as "Why AI‑ready infrastructure matters" instead of "Stop paying $400/month for tools."

---

## 4. "Why RelayLaunch" section

**Current themes:**

- Veteran‑owned, mission‑driven.  
- Infrastructure‑first + AI (already a good direction).  
- Full service (web, SEO, AI agents, workflows, cloud).  
- Clear fixed pricing.

**Upgrade recommendations:**

1. **Rename section:** `Why a Control Center Partner` or `Why RelayLaunch for Digital Ops` to make the category obvious.
2. **Tighten bullets around Control Center/AIOps:**
   - Swap generic "web, SEO, content" emphasis for:
     - "Control Center product + playbook" (link to how it works). [code_file:175]  
     - "Infrastructure and automation designed together."  
     - "Approvals, metrics, and audit built in from day one." [code_file:170]
3. **Keep the Veteran‑owned story**, but anchor it in reliability and mission completion for infra/ops.

---

## 5. "The Problem" section

**Current framing:**

> "You became a business owner. Not a software administrator."  
> Pain bullets about logging into 6 dashboards, manual work, inconsistent branding, etc.

**What to keep:**

- The emotional hook (they didn’t want to be IT + ops + marketer all at once).

**What to update:**

- Add **AI/automation‑specific pain**:
  - Shadow scripts and bots no one fully owns.  
  - Ad‑hoc AI experiments living in notebooks or Zapier.  
  - Risk of breaking customer‑facing flows with unreviewed changes. [web:214][web:211]
- Emphasize lack of **visibility and accountability**:
  - "No single place that shows which automations and agents are live, what they touch, and what value they create."

**Visual:**

- Consider swapping or augmenting the current "5–8 tools" icons with a small diagram showing **scattered bots/workflows** vs a single Control Center view.

---

## 6. "The Solution" section

**Current framing:**

> "One system. One dashboard. Everything connected."  
> Heavily focused on website, email, social, scheduling, and a Slack dashboard.

**Required evolution:**

- Explicitly name the **RelayLaunch Control Center** as the product.  
- Reframe sub‑bullets to match your Control Center feature set:
  - Tenant dashboards with leads, automations run, and hours saved. [code_file:170]  
  - Inventory of workflows and AI agents with health status.  
  - Approvals and change requests with usage against budget. [code_file:175]  
  - Activity stream of all significant changes and runs.

**Copy sketch:**

> "RelayLaunch builds a Control Center for your digital operations — a single dashboard where your workflows, AI agents, and infrastructure are mapped, monitored, and governed. When a new automation goes live, it's approved and logged. When an agent acts, you see what it did and what it changed."

- Keep the "Everything Connected" angle, but make it clear it's **infra + workflow + AI orchestration**, not just marketing tools.

---

## 7. Service Packages

**Current packages:** Signal, Blueprint, Relay, Sustain with pricing skewed to small‑business marketing (SEO, 30 social posts/mo, etc.).

**We now have:** Control Center Foundations, Automation Design & Build, Managed Digital Infrastructure & AIOps. [code_file:175]

**Recommendation:**

- **Rename and realign packages**:

  1. **Signal → Assessment & Fit (optional)**  
     - Focus: digital ops + AI readiness assessment.  
     - Deliverables: readiness score, pain map, early Control Center sketch.

  2. **Blueprint → Architecture & Roadmap**  
     - Directly aligned to Sprint 0 / Design. [code_file:175]  
     - Deliverables: architecture diagram, Control Center rollout plan (Builds 1–3), metrics/KPI definitions. [code_file:170]

  3. **Relay → Control Center Foundations (Build)**  
     - Focus: implement the Control Center for one tenant and wire in high‑value workflows + agents.  
     - Deliverables: live dashboard, approvals, seeded metrics, first automations.

  4. **Sustain → Managed Ops & AIOps**  
     - Replace social posting with change budgets, monitoring, and continuous improvement.  
     - Deliverables: monthly change allowance, monitoring and incident handling, quarterly strategy review.

- If you still want to offer pure "marketing website" work, consider a **separate, lighter offering** or a buried "web builds only" page; keep the homepage focused on Control Center + infra.

---

## 8. Proof of Concept / Case Study

**Current POC:**

- Luxury wellness spa case study showing cost savings ($342 → $51), number of workflows, and what was built.

**Updates to align with Control Center story:**

1. Add **before/after metrics** in terms of:
   - Leads captured automatically.  
   - Hours saved per week.  
   - Reduction in manual changes / incidents.
2. Show at least one **Control Center screenshot** for this client (or anonymized, but same structure):
   - Tenant dashboard with metrics.  
   - Approvals/change log for one quarter. [code_file:170]
3. Reframe the case study intro:
   - From "replaced tools and reduced cost" to "gave them a unified control center for bookings, memberships, and campaigns, with infra cost savings as a side benefit."

---

## 9. "Who Builds This" / About Victor

**Current strengths:**

- Very strong credibility section: USMC, cloud engineering, enterprise ops.

**Enhancements:**

- Add a short paragraph explicitly connecting Victor’s background to **running a control center / AIOps‑style practice**:
  - "Designed and maintained systems where hundreds of workflows had to run reliably every day; now brings that discipline to SMBs building with AI and automation."
- Link to a `Service Playbook` or `How We Work` page (based on `rl-service-playbook-v1.md`). [code_file:175]

---

## 10. Comparison table (Web Designer vs RelayLaunch)

**Current contrast:**

- Good, but overly focused on websites, templates, and social content.

**Adjust to Control Center story:**

- Update "Web Designer" column minimally; update "RelayLaunch" column to emphasize:
  - "Builds a Control Center for your digital operations, not just a website."  
  - "Automations and AI agents are first‑class citizens from day one."  
  - "Includes approvals, metrics, and audit trails."  
  - "Monthly briefings from the Control Center, not just handoff and goodbye."

---

## 11. "Ready to Start?" CTA section

**Current text:**

> "Replace your tool stack with one connected system. Whether you need a full build or just want an honest audit of what's slowing you down — start with a conversation."

**Recommended update:**

- Make the CTA explicitly about **Control Center assessment or roadmap**:

> "Get your Control Center assessment. Whether you're testing AI agents, relying on fragile automations, or just tired of logging into ten dashboards, we'll map your digital ops, score your readiness, and show you what 'ops on autopilot' looks like for your business."

- Primary button: `Book a Control Center assessment`.  
- Secondary: `Download the Digital Ops Readiness Checklist` (update existing free PDF to align with metrics/KPIs doc). [code_file:170]

---

## 12. Content & tone consistency

To keep everything coherent as you implement these changes:

1. **Use the new slogan system consistently** (see `rl-slogan-system-v1.md`). [code_file:199]
2. **Tie every bold phrase to a real feature or artifact**:
   - "Every Launch, Accounted For." → approvals, change logs, activity streams. [code_file:170][code_file:175]  
   - "Turn Workflows into Working Revenue." → metrics and case study numbers. [code_file:170]
3. **Avoid over‑promising cost savings** as the main hook.
   - Cost reduction is a result; the core story is "reliable, governed digital operations and AI".
4. **Keep the veteran + infra credibility front and center**, but show it through the lens of **running a control center** instead of "doing marketing for small businesses".

---

## 13. Implementation notes

When you rebuild the site:

- Use this audit plus:
  - `rl-slogan-system-v1.md` (messaging). [code_file:199]  
  - `rl-service-playbook-v1.md` (service structure). [code_file:175]  
  - `cc-metrics-kpis-v1.md` (for any metrics screenshots or copy). [code_file:170]
- Ask Claude (or another agent) to:  
  - Generate updated Astro page templates using these sections.  
  - Propose responsive layout and visual hierarchy around the new hero and Control Center imagery.
- Keep the initial rebuild focused on **homepage + one "How It Works" / Control Center page**; you can rework deep case studies and resources afterward.
