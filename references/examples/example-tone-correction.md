# Example 2: Tone Too Formal

## Evidence Example

```md
# Correction Record: corr-example-tone

## Summary
The reply sounded too formal and unnatural.

## Source
- user

## Context
Casual chat reply in a collaborative group.

## Full Context
- task: answer naturally in a group chat
- user-intent: keep the tone human and low-friction
- surrounding-dialogue: informal back-and-forth, short replies from others
- prior-agent-behavior: wrote a polished but stiff answer
- correction-signal: user said the tone was too formal

## Raw Signal
- "太官方了，下次自然一点。"

## Notes
- gap: behavior_gap
- recurrence_hint: 1
- created_at: <fill>
```

## Expected Review Result

```md
## Review Result
- What happened: The reply matched the topic but missed the social tone of the conversation.
- Why it matters: Tone mismatch creates friction and makes the assistant feel unnatural in-group.
- Pattern judgment: unclear
- Pattern rationale: This may be an isolated style miss unless more similar corrections appear.
- Convergence action: no-action
- Convergence rationale: There is not enough evidence yet to merge into or create a durable candidate.
- State decision: fast
- State rationale: A small local fix is obvious and easy to validate in the next similar reply.
- Proposed next step: apply a local tone rule for short, natural group-chat replies.
- Validation path: Check the next few group replies for reduced stiffness.
- Regression / rollback trigger: If the new tone becomes too casual or loses clarity, adjust locally instead of promoting.
```
