# Agency Agents Reference Guide for Claude Code

A practical reference for using [The Agency](https://github.com/msitarzewski/agency-agents) AI agents with Claude Code. 120+ specialized agents organized across 12 divisions, each with distinct personality, workflows, and deliverables.

## Installation

```bash
# Clone the repo
git clone https://github.com/msitarzewski/agency-agents.git
cd agency-agents

# Run the install script (auto-detects Claude Code)
bash scripts/install.sh

# Or install for Claude Code only
bash scripts/install.sh --tool claude-code
```

Agents install to `~/.claude/agents/` as markdown files with YAML frontmatter.

---

## Quick Reference: When to Use What

| Scenario | Agent(s) | Division |
|----------|----------|----------|
| Build a web app from scratch | Frontend Developer + Backend Architect | Engineering |
| Design a UI component library | UI Designer + UX Architect | Design |
| Run a full multi-agent project | Agents Orchestrator | Specialized |
| Optimize site performance | Frontend Developer + Performance Benchmarker | Engineering + Testing |
| Launch a marketing campaign | Growth Hacker + Content Creators | Marketing |
| Audit code quality | Evidence Collector + Reality Checker | Testing |
| Build a mobile app | Mobile App Builder | Engineering |
| Set up CI/CD pipelines | DevOps Automator | Engineering |
| Security review | Security Engineer + Threat Detection Engineer | Engineering |
| Write API documentation | Technical Writer + API Tester | Engineering + Testing |

---

## Division Breakdown

### Engineering Division (16 agents)

| Agent | Specialty | Best For |
|-------|-----------|----------|
| Frontend Developer | React/Vue/Angular, responsive design, Core Web Vitals | Building web apps, component libraries, PWAs |
| Backend Architect | API design, databases, scalability | Server-side systems, microservices |
| Mobile App Builder | iOS/Android, React Native, Flutter | Native and cross-platform mobile apps |
| AI Engineer | ML models, deployment, AI pipelines | Machine learning features, AI integrations |
| DevOps Automator | CI/CD, infrastructure as code, automation | Pipeline development, cloud deployment |
| Rapid Prototyper | Fast POC development, MVPs | Quick proof-of-concepts, hackathons |
| Senior Developer | Laravel/Livewire, advanced patterns | Complex implementations, architecture decisions |
| Security Engineer | Threat modeling, secure code review | Application security, vulnerability assessment |
| Data Engineer | LLM routing, cost optimization, shadow testing | Autonomous routing, intelligent API selection |
| Embedded Firmware Engineer | Bare-metal, RTOS, ESP32/STM32 | Production-grade embedded systems and IoT |
| Incident Response Commander | Incident management, post-mortems | Managing production incidents, on-call |
| Smart Contract Engineer | EVM contracts, gas optimization, DeFi | Secure, gas-optimized blockchain development |
| Technical Writer | Developer docs, API references | Clear, accurate technical documentation |
| Threat Detection Engineer | SIEM rules, threat hunting, ATTACK mapping | Building detection layers, threat hunting |
| Autonomous Optimization Architect | LLM routing, cost optimization | Automated model selection and cost reduction |
| WeChat Mini Program Developer | WeChat ecosystem, applets | Building performant WeChat apps |

**Example prompts:**

```
# Frontend Developer
"As the Frontend Developer agent, build a responsive dashboard component
using React and Tailwind CSS. Optimize for Core Web Vitals and ensure
WCAG 2.1 AA accessibility compliance."

# Backend Architect
"As the Backend Architect agent, design a REST API for a user
authentication system with JWT tokens, rate limiting, and PostgreSQL
storage. Include the database schema and endpoint specifications."

# DevOps Automator
"As the DevOps Automator agent, create a GitHub Actions CI/CD pipeline
that builds, tests, and deploys an Astro site to Cloudflare Workers."

# Security Engineer
"As the Security Engineer agent, review this codebase for OWASP Top 10
vulnerabilities. Focus on authentication flows and data validation."
```

---

### Design Division (8 agents)

| Agent | Specialty | Best For |
|-------|-----------|----------|
| UI Designer | Visual design, component libraries, design systems | Interface creation, brand-aligned component design |
| UX Researcher | User testing, behavior analysis, research | Understanding users, testing insights |
| UX Architect | Technical architecture, CSS systems, implementations | Developer-friendly foundations, implementation |
| Brand Guardian | Brand identity, consistency, positioning | Brand strategy, identity development, guidelines |
| Visual Storyteller | Visual narratives, multimedia content | Compelling visual stories, brand storytelling |
| Whimsy Injector | Personality design, playful interactions | Adding joy, micro-interactions, Easter eggs |
| Image Prompt Engineer | AI image generation, prompt crafting | Photography prompts for Midjourney, DALL-E, Stable Diffusion |
| Inclusive Visuals Specialist | WCAG auditing, assistive technology | Accessibility compliance, screen reader testing |

**Example prompts:**

```
# Brand Guardian
"As the Brand Guardian agent, audit this website for brand consistency.
Check color usage, typography, voice/tone, and visual hierarchy against
our brand guidelines."

# UX Researcher
"As the UX Researcher agent, design a usability test plan for our
checkout flow. Include test scenarios, participant criteria, and
metrics to measure."
```

---

### Product Division (4 agents)

| Agent | Specialty | Best For |
|-------|-----------|----------|
| Sprint Prioritizer | Agile planning, feature scoring | Sprint planning, resource allocation, backlog triage |
| Trend Researcher | Market intelligence, competitive analysis | Market research, opportunity assessment |
| Feedback Synthesizer | User feedback analysis, insights | Feedback analysis, product insights |
| Behavioral Nudge Engine | Behavioral psychology, nudge design | Maximizing user motivation through behavioral science |

**Example prompts:**

```
# Sprint Prioritizer
"As the Sprint Prioritizer agent, evaluate these 12 feature requests
and rank them by impact vs. effort. Consider our Q2 goals of improving
retention and reducing churn."

# Trend Researcher
"As the Trend Researcher agent, analyze the current landscape of
AI-powered website builders. Identify gaps and opportunities for a
veteran-owned digital consultancy."
```

---

### Project Management Division (6 agents)

| Agent | Specialty | Best For |
|-------|-----------|----------|
| Studio Producer | High-level orchestration, multi-project oversight | Multi-project oversight, resource allocation |
| Project Shepherd | Cross-functional coordination, timeline management | End-to-end project coordination |
| Studio Operations | Day-to-day efficiency, process optimization | Operational excellence, team productivity |
| Experiment Tracker | A/B tests, hypothesis validation | Experiment management, data-driven decisions |
| Senior Project Manager | Realistic scoping, task conversion | Converting specs to tasks, sprint planning |
| Jira Workflow Steward | Git workflow, branch strategy, traceability | Enforcing Jira-linked discipline and delivery |

**Example prompts:**

```
# Senior Project Manager
"As the Senior Project Manager agent, break down this feature request
into development tasks with estimates, dependencies, and acceptance
criteria. Organize into a 2-week sprint."

# Agents Orchestrator (Specialized Division)
"As the Agents Orchestrator, coordinate a full build: PM scopes tasks,
Frontend Developer builds the UI, Backend Architect designs the API,
Evidence Collector validates each component."
```

---

### Testing Division (8 agents)

| Agent | Specialty | Best For |
|-------|-----------|----------|
| Evidence Collector | Screenshot-based QA, visual proof | UI testing, visual verification, catching bugs |
| Reality Checker | Production readiness, quality verification | Pre-launch audits, specification compliance |
| Test Results Analyzer | Test output analysis, quality metrics | Test output analysis, coverage reporting |
| Performance Benchmarker | Performance testing, load analysis | Speed testing, performance profiling |
| API Tester | API validation, endpoint verification | API testing, endpoint verification |
| Tool Evaluator | Technology evaluation, tech decisions | Evaluating tools, software recommendations |
| Workflow Optimizer | Process analysis, efficiency mapping | Process optimization, efficiency improvements |
| Accessibility Auditor | WCAG auditing, assistive technology | Accessibility compliance, inclusive design testing |

**Example prompts:**

```
# Evidence Collector
"As the Evidence Collector agent, perform a visual QA audit of this
website. Take screenshots of every page, test all interactive elements
(forms, accordions, navigation), and document every issue found."

# Performance Benchmarker
"As the Performance Benchmarker agent, audit this Astro site for
performance. Run Lighthouse, measure Core Web Vitals, and provide
specific optimization recommendations."

# Accessibility Auditor
"As the Accessibility Auditor agent, test this website for WCAG 2.1 AA
compliance. Check heading hierarchy, color contrast, keyboard
navigation, and screen reader compatibility."
```

---

### Marketing Division (18 agents)

| Agent | Specialty | Best For |
|-------|-----------|----------|
| Growth Hacker | Rapid user acquisition, viral loops, experiments | Explosive growth, user acquisition, conversion optimization |
| Social Media Strategist | Multi-platform content, brand calendars | Content planning, brand campaigns |
| Twitter Engager | Real-time engagement, thought leadership | Twitter strategy, LinkedIn campaigns |
| TikTok Viral Architect | Viral content, algorithm optimization | TikTok growth, viral content, Gen Z/Millennial reach |
| Instagram Curator | Visual storytelling, community building | Instagram strategy, community building |
| Reddit Community Builder | Authentic engagement, value-driven content | Reddit strategy, community trust building |
| App Store Optimizer | ASO, conversion optimization | App marketing, store optimization |
| E-Commerce Operator | Cross-platform strategy, growth-driven | Ecommerce social strategy, multi-platform campaigns |
| SEO Specialist | Technical SEO, content strategy | Driving sustainable organic growth |
| Content creators for: Bilibili, Kuaishou, WeChat, Xiaohongshu, Zhihu, Baidu, LinkedIn, Taobao | Regional platform expertise | Market-specific content and growth in China/Asia |

**Example prompts:**

```
# Growth Hacker
"As the Growth Hacker agent, design a 30-day growth experiment plan
for a B2B digital consultancy website. Focus on organic channels
and content-led acquisition."

# SEO Specialist
"As the SEO Specialist agent, audit this website's technical SEO.
Check meta tags, structured data, sitemap, robots.txt, Core Web
Vitals, and provide an action plan ranked by impact."
```

---

### Sales Division (8 agents)

| Agent | Specialty | Best For |
|-------|-----------|----------|
| Outbound Strategist | Signal-based prospecting, multi-channel sequences | Building pipeline through research-driven outreach |
| Discovery Coach | SPIN, Cap Selling, Sandler questioning | Preparing for discovery calls, qualifying opportunities |
| Deal Strategist | MEDDPICC qualification, competitive positioning | Scoring deals, pipeline building, win strategies |
| Sales Engineer | Technical demos, POC engineering, competitive analysis | Pre-sales technical work, demos, proof-of-concepts |
| Proposal Strategist | RFP response, win themes | Writing proposals that win |
| Pipeline Analyst | Forecasting, pipeline health, deal velocity | Pipeline reviews, revenue operations |
| Account Strategist | Land-and-expand, QBRs, stakeholder mapping | Enterprise account planning, NBR growth |
| Sales Coach | Rep development, call coaching, pipeline review | Making every rep and deal better through coaching |

**Example prompts:**

```
# Proposal Strategist
"As the Proposal Strategist agent, help me write a proposal for a
$15K website rebuild engagement. The client is a mid-size law firm
wanting to modernize their online presence."
```

---

### Paid Media Division (7 agents)

| Agent | Specialty | Best For |
|-------|-----------|----------|
| PPC Campaign Strategist | Google/Microsoft/Amazon Ads, account architecture | Budget allocation, scaling, performance campaigns |
| Search Query Analyst | Search term analysis, negative keywords | Query audits, wasted spend cleanup |
| Paid Media Auditor | 200+ point account audits, competitive analysis | Account takeovers, competitive pitches |
| Tracking & Measurement Specialist | GTM, GA4, conversion tracking | Conversion tracking, attribution, platform integration |
| Ad Creative Strategist | SOA copy, Meta Creative, Performance Max assets | Creative launches, testing programs, ad fatigue mitigation |
| Programmatic & Display Buyer | CDN, DSPs, partner media, ABM display | Display planning, partner outreach, ABM programs |
| Paid Social Strategist | Meta, LinkedIn, TikTok, cross-platform | Ad programs, cross-platform audience strategy |

---

### Support Division (6 agents)

| Agent | Specialty | Best For |
|-------|-----------|----------|
| Support Responder | Customer service, issue resolution | Customer support, user-facing operations |
| Analytics Reporter | Data analysis, dashboards, insights | Business intelligence, KPI tracking |
| Finance Tracker | Financial planning, budget management | Financial analysis, cash flow, budgeting |
| Infrastructure Maintainer | Systems monitoring, maintenance | Infrastructure management, system monitoring |
| Legal Compliance Checker | Compliance, regulations, legal review | Legal compliance, regulatory checklists |
| Executive Summary Generator | C-suite communication, board reporting | Executive reporting, strategic decision support |

---

### Spatial Computing Division (6 agents)

| Agent | Specialty | Best For |
|-------|-----------|----------|
| XR Interface Architect | Spatial interaction design, immersive UX | AR/VR/XR interface design, spatial computing UX |
| macOS Spatial/Metal Engineer | WebXR, browser-based 3D | Browser-based immersive experiences, WebXR |
| XR Immersive Developer | High-performance Vulkan/Metal, cross-platform XR | VisionPro/Meta/SteamVR, cross-platform XR apps |
| XR Cockpit Specialist | Cockpit-based controls, immersive systems | Cockpit control systems, immersive control |
| visionOS Spatial Engineer | Apple Vision Pro apps, spatial experiences | Vision Pro apps, spatial UI development |
| Terminal Integration Specialist | Terminal integration, command-line tools | CLI tools, terminal workflows, developer tools |

---

### Specialized Division (14 agents)

| Agent | Specialty | Best For |
|-------|-----------|----------|
| Agents Orchestrator | Multi-agent coordination, workflow management | Complex projects requiring multiple agent coordination |
| LSP/Index Engineer | Language Server Protocol, code intelligence | Code intelligence systems, IDE integrations |
| Sales Data Extraction | Event monitoring, sales metric extraction | Sales data ingestion, MQTT/CSV/Time-Series |
| Data Consolidation | Data aggregation, dashboard reports | Territory summaries, rep performance reports |
| Report Distribution | Automated report delivery, scheduled sends | Targeted report delivery, scheduled sends |
| Identity & Trust Architect | Agent identity systems, credential management | Multi-agent identity systems, trust frameworks |
| Blockchain Security Auditor | Smart contract audits, DeFi security | Finding vulnerabilities in smart contracts |
| Compliance Auditor | SOC 2, ISO 27001, HIPAA, PCI DSS | Guiding organizations through compliance certification |
| Cultural Intelligence Strategist | Cross-cultural communication, localization | Ensuring software resonates across cultures |
| Developer Advocate | Community building, DX, documentation | Building product and developer community |
| Model QA Specialist | ML audits, model evaluation, analysis | End-to-end QA for machine learning models |
| ZK Steward | Zero-knowledge proofs, privacy technology | Building connected, validated privacy solutions |

---

### Game Development Division

**Cross-Engine Agents:**

| Agent | Specialty | Best For |
|-------|-----------|----------|
| Game Designer | Systems design, GDD authoring, game mechanics | Designing game mechanics, writing design documents |
| Level Designer | Layout theory, encounter design | Building levels, designing environments |
| Technical Artist | Shaders, VFX, LOD pipelines | Bridging art and engineering, shader authoring |
| Game Audio Engineer | FMOD/Wwise, adaptive audio, spatial audio | Interactive audio systems, spatial audio |
| Narrative Designer | Story systems, branching dialogue, lore architecture | Branching narratives, world lore, dialogue |

**Engine-Specific Agents:**

| Engine | Agents Available |
|--------|-----------------|
| Unity | Architect, Shader Graph Artist, Multiplayer Engineer, Editor Tool Developer |
| Unreal Engine | C++ Blueprint hybrid, GAS, Material Editor, Niagara, PCG |
| Godot | GDScript, scene architecture |
| Roblox Studio | Luau scripting, experience development |

---

## Multi-Agent Workflow Patterns

### Pattern 1: Full Project Build (Startup MVP)
```
1. Senior Project Manager → Scope and create task breakdown
2. Frontend Developer → Build the UI components
3. Backend Architect → Design and build the API
4. Evidence Collector → QA each deliverable
5. Reality Checker → Final production readiness check
```

### Pattern 2: Website Audit & Improvement
```
1. Brand Guardian → Brand consistency audit
2. Accessibility Auditor → WCAG compliance check
3. Performance Benchmarker → Speed and performance audit
4. SEO Specialist → Technical SEO audit
5. Senior Developer → Implement fixes from all audits
```

### Pattern 3: Marketing Campaign Launch
```
1. Growth Hacker → Strategy and channel selection
2. Social Media Strategist → Content calendar
3. Twitter Engager → Twitter-specific execution
4. Instagram Curator → Visual content and stories
5. Analytics Reporter → Track and optimize performance
```

### Pattern 4: Security Hardening
```
1. Security Engineer → Threat modeling, code review
2. Threat Detection Engineer → Detection rules, monitoring
3. API Tester → Endpoint security validation
4. Compliance Auditor → Regulatory compliance check
```

### Pattern 5: Multi-Agent Orchestration
```
# Use the Agents Orchestrator to coordinate automatically
"As the Agents Orchestrator, run a full development cycle:
PM scopes → Architect designs → Developer builds → QA validates.
Maximum 3 retries per task before escalation."
```

---

## NEXUS Strategy: Deployment Modes

The repo includes a **NEXUS Strategy** layer (`strategy/nexus-strategy.md`) for orchestrating agents as coordinated teams. Three deployment modes:

| Mode | Scope | Duration | Example |
|------|-------|----------|---------|
| **NEXUS-Full** | Enterprise launches, full product builds | Weeks-months | New SaaS product from discovery to deployment |
| **NEXUS-Sprint** | Feature development, focused deliverables | 2-6 weeks | Add authentication system, redesign checkout flow |
| **NEXUS-Micro** | Targeted tasks, bug fixes, quick wins | Hours-days | Fix deployment pipeline, audit a single page |

Additional strategy resources in `strategy/`:
- `coordination/` — Team coordination playbooks
- `playbooks/` — Scenario-specific playbooks
- `runbooks/` — Operational runbooks

---

## Tips for Using Agents with Claude Code

1. **Invoke by role**: Start prompts with "As the [Agent Name] agent..." to activate the personality and workflows.

2. **Chain agents**: Complete one agent's work, then hand off to the next. Each agent's output becomes the next agent's input.

3. **Use the Orchestrator for complex projects**: When coordinating 3+ agents, let the Agents Orchestrator manage the pipeline.

4. **Match agent to task scope**: Use specialized agents for focused work (e.g., API Tester for endpoints only) and generalist agents for broader tasks (e.g., Senior Developer for full-stack work).

5. **Combine divisions**: The best results come from cross-division collaboration (e.g., Engineering + Testing + Design).

6. **Trust the agent's personality**: Each agent has a distinct voice and approach. The Evidence Collector will be skeptical. The Brand Guardian will be protective. This is by design.

---

*Source: [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) — 120+ specialized AI agent personalities*
