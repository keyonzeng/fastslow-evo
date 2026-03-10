# Office and Study Pain Points

This note reframes `spec-evo` for ordinary knowledge workers and students rather than agent builders.

## 1. AI output sounds polished but is not trustworthy

Observed patterns:
- users get fluent summaries, emails, notes, or explanations that sound right but contain wrong details
- people often overestimate how correct AI-assisted work is
- trust tends to rise faster than reliability

Why it hurts:
- rechecking takes time
- sending wrong content damages trust
- students learn the wrong material confidently

Design implication:
Default to verification and faithfulness checks for summaries, drafts, and study explanations.

## 2. Email, meetings, and task follow-up overload

Observed patterns:
- workers want AI most for email drafting, meeting summarization, and organizing action items
- users are overwhelmed not by one hard task but by repeated coordination overhead
- meeting assistants save time only if outputs are accurate and actionable

Why it hurts:
- inbox and meeting sprawl consume attention
- action items get lost
- summaries become another thing to review instead of a relief

Design implication:
Focus on action extraction, follow-up clarity, and low-friction review instead of long generic summaries.

## 3. Context switching and fragmented workflow

Observed patterns:
- users bounce between chat, docs, spreadsheets, calendar, email, and notes
- AI can create more cognitive overhead if outputs are not grounded in current context
- integration, data quality, and privacy remain major blockers in real workplaces

Why it hurts:
- users spend more time stitching outputs together than acting on them
- partial automation creates double work

Design implication:
Prefer small task-bounded workflows with explicit inputs/outputs over broad “personal AI assistant” promises.

## 4. Students use AI to finish work, but learning quality drops

Observed patterns:
- faculty report strong concern that AI use undermines original writing and critical thinking
- students benefit when AI helps with structure, simplification, and practice questions, but not when it replaces reasoning
- note-taking and summarization tools are useful, but cross-checking remains necessary

Why it hurts:
- assignments get completed without deep understanding
- students confuse summary familiarity with mastery
- original voice and reasoning weaken

Design implication:
Design study workflows that force active recall, source grounding, and “explain in your own words” checks.

## 5. AI-generated workplace writing can reduce trust

Observed patterns:
- polished AI emails and messages can feel inauthentic or overprocessed
- heavy invisible AI assistance may reduce trust in managers and colleagues

Why it hurts:
- communication quality is not just grammar; it includes tone, authenticity, and accountability
- the safer the content sounds, the more people may miss subtle misalignment

Design implication:
Use AI to structure and compress writing, but keep a review step for tone, accountability, and intent.

## 6. Users do not want a framework; they want fewer mistakes and less friction

Observed patterns:
- ordinary users care about visible pain reduction, not meta-systems
- when AI creates extra review burden, people abandon the workflow

Why it hurts:
- impressive automation gets dropped if it adds ceremony
- users stay with simple checklists and templates if they save time immediately

Design implication:
For office/study users, `spec-evo` should lead with small starter workflows, not architecture.

## Product Direction

For mainstream users, optimize `spec-evo` around:
- trustworthy summaries
- action-item extraction
- follow-up drafting with review
- study support with active recall
- bounded templates over open-ended autonomy
