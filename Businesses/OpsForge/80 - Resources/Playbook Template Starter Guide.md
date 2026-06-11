# Playbook Template Starter Guide

## Purpose
This guide provides a high-level starting point for creating effective OpsForge playbooks. Use it during service engagements, self-serve platform use, or when contributing to the marketplace.

A good playbook is:
- Clear enough for a competent person (or AI agent) to follow with minimal ambiguity.
- Structured for both human readability and machine execution.
- Auditable and improvable over time.
- Grounded in real work, not theory.

## Recommended Playbook Structure
1. **Title & Purpose**
   - Short, descriptive name.
   - One-sentence statement of what this playbook achieves and why it matters.

2. **Triggers & Context**
   - When/how this process starts (event, schedule, manual trigger, upstream playbook).
   - Prerequisites or required inputs (data, approvals, context).

3. **Steps**
   - Numbered or decision-tree format.
   - For each step:
     - Action or decision.
     - Who (or which agent) performs it.
     - Tools/systems involved.
     - Expected output or state change.
     - Success criteria or validation.
     - Evidence to capture (screenshots, logs, notes, approvals).

4. **Decision Points & Branches**
   - Clear if/then logic.
   - Escalation paths for exceptions or judgment calls.

5. **Inputs, Outputs & Data**
   - Defined schemas or examples for data moving through the process.
   - Required vs. optional fields.

6. **Oversight & Assurance**
   - Human review/approval checkpoints (default to conservative for important processes).
   - Metrics to track (time, error rate, completion quality, client impact).
   - Known risks or common failure modes + mitigations.

7. **Versioning & Change Log**
   - Current version.
   - History of changes with rationale and date.
   - Owner / last updated by.

8. **Related Playbooks & Resources**
   - Links to upstream/downstream processes.
   - Supporting templates, examples, or training materials.

## Writing Tips
- Write for the "competent but new" person or agent.
- Use specific language ("Send the welcome email using template X") rather than vague ("communicate with the client").
- Include examples where helpful (sample emails, document templates, data formats).
- Capture edge cases and "what if" scenarios — these are where most operational risk lives.
- Keep it concise but complete. Long playbooks can be broken into sub-playbooks.
- Test by having someone unfamiliar with the process attempt to follow it (or simulate with AI).

## AI Capture Best Practices
- Start with a natural language description from the person who does the work.
- Ask clarifying questions: "What happens if X?", "How do you decide Y?", "What evidence do you keep?"
- Import existing artifacts (docs, emails, runbooks) and have AI help extract/structure.
- Always have a human expert review and edit the AI draft — especially decisions, exceptions, and client-facing steps.
- Iterate: Run a pilot execution, capture feedback, refine the playbook.

## OpsForge Platform Features to Leverage
- Version history and rollback.
- Comments and approval workflows during authoring.
- Execution logging with context (what step, inputs, outputs, human interventions).
- Metrics dashboards tied to the playbook.
- Agent configuration (autonomy level per step, required approvals).
- Export options for review or backup.

## Marketplace Contribution Tips
- Make the playbook as self-contained and reusable as possible.
- Include clear prerequisites and assumptions.
- Add notes on customization points.
- Provide example data or templates where appropriate.
- Tag appropriately (industry, function, complexity) for discoverability.

## Example Starter Playbooks (Ideas)
- New client onboarding.
- Project kickoff checklist + communications.
- Monthly reporting process.
- Proposal review and handoff.
- Quality assurance / peer review workflow.
- Invoice generation and follow-up.
- Knowledge capture / handoff when someone leaves a project.

Start simple. One solid, well-used playbook is more valuable than ten incomplete ones.

This is a living resource — update with lessons from real use.
