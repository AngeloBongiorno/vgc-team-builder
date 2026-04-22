# VGC Archetype Knowledge Base — Document Schema

## Design principles
- Each section is a self-contained retrieval unit. A chunk of any single section should make sense without the others.
- No regulation-specific Pokémon names. Roles only. This keeps documents meta-agnostic.
- Dense, declarative sentences. No narrative, no filler.
- Consistent field names across all archetype documents so the LLM can compare archetypes reliably.

---

## Schema

```
archetype_id: <snake_case_identifier>
archetype_name: <Human readable name>
tags: [<list of keywords for retrieval: e.g. weather, speed_control, setup>]
aliases: [<other names this archetype is known by>]
```

### 1. Core gameplan
*One short paragraph. What is this team trying to do to win? Written as a strategic objective, not a description of mechanics.*

### 2. Roles
*Each role on the team, as a structured list. For each role:*
- **Role name** — Why this role exists on this archetype. What it enables. How many slots it typically occupies (1 or 2).

### 3. Structural requirements
*The non-negotiable building constraints. What must be true for the team to function.*
- Written as rules: "The team requires at least one X that does Y."
- Include redundancy requirements where relevant (e.g. "setter should have a backup").

### 4. Win conditions
*How does this team close out a game? List the primary and secondary win conditions.*

### 5. Common weaknesses
*Structural weaknesses that are intrinsic to the archetype, not fixable by slot choices.*
- Each weakness stated as a threat pattern: "Teams that can [action] will [consequence]."

### 6. Counterplay it struggles against
*Specific strategies and mechanics this archetype is systematically weak to.*

### 7. Flex slots and customization axes
*Which slots have the most variance, and what strategic axes do those choices represent (speed control vs. bulk, offense vs. support, etc.).*

### 8. Synergy notes
*Key internal synergies that define the archetype. Stated as relationships between roles, not Pokémon.*

### 9. Interaction with other archetypes
*How this archetype typically fares against each major archetype. Use: favored / roughly even / unfavored + one sentence of reasoning.*

---

## Example — Trick Room

```
archetype_id: trick_room
archetype_name: Trick Room
tags: [speed_control, setup, bulky, slow_attackers, reversal_terrain]
aliases: [TR, reversed speed]
```

### 1. Core gameplan
Trick Room reverses the speed order for 5 turns, allowing slow, high-power Pokémon to move first. The team wins by setting Trick Room reliably in turn 1, then applying overwhelming offensive pressure from slow attackers before the effect expires. Games are typically decided in the first Trick Room window.

### 2. Roles
- **Trick Room setter** — Sets the terrain. Must be slow (low base speed) to benefit from it once active, and bulky or protected enough to survive the turn it sets. Typically occupies 1-2 slots for redundancy.
- **Primary attacker** — Slow, high base power attacker that abuses the reversed speed. The core offensive threat once TR is up.
- **Backup setter** — A secondary Pokémon capable of setting TR, ensuring the win condition is accessible even if the primary setter is KO'd or Taunted.
- **Speed control disruption** — A Pokémon that handles opposing speed control (Tailwind, opposing TR) to protect the team's win condition.
- **TR extender / support** — Optional slot that can reset TR turns or provide utility (redirection, chip damage, status).

### 3. Structural requirements
- The team requires at least two independent sources of Trick Room to ensure reliability.
- All primary attackers must have base speed low enough to move first under TR against common threats.
- The team must have an answer to Taunt on its setters, either through item (Mental Herb), ability, or a backup setter immune to Taunt.
- At least one setter must be able to set TR under spread move pressure (either via redirection support or natural bulk).

### 4. Win conditions
- **Primary**: Set TR turn 1, KO two opposing Pokémon in the first window, and close with the residual advantage.
- **Secondary**: Bait TR removal or Taunt from the opponent early, then pivot to a second setter when they've exhausted their answer.

### 5. Common weaknesses
- Teams that can consistently prevent TR from being set (Taunt, Imprison) shut down the primary win condition entirely.
- TR has a fixed 5-turn timer. Stall tactics and pivoting can force the team to spend turns re-setting rather than attacking.
- The team's attackers are typically slow and frail outside of TR, making them liabilities if TR is not up.

### 6. Counterplay it struggles against
- **Taunt** on the setter, especially from a fast lead, can deny setup entirely.
- **Imprison + Trick Room** from an opposing TR team neutralizes both setters simultaneously.
- **Prankster Encore** can lock a setter into TR or a non-TR move at a critical moment.
- **High-speed priority moves** bypass speed order entirely and punish slow, bulky setters.

### 7. Flex slots and customization axes
- The backup setter slot is the primary flex decision: a second identical setter increases reliability; a different setter type (e.g. offensive setter) adds unpredictability.
- The 5th and 6th slots typically balance between additional TR support and lead versatility to handle non-TR matchups.
- A key customization axis is **speed creep**: how slow should the attacker be? Lower speed is better under TR but worse in any turn outside it.

### 8. Synergy notes
- Setter + redirection support is the core duo: the redirector protects the setter on the turn TR goes up.
- Slow attacker + setter should share defensive synergy so they can be brought together in multiple matchups safely.
- The backup setter should share as few weaknesses as possible with the primary setter, to prevent both being removed by the same threat.

### 9. Interaction with other archetypes
- **vs. Sun**: roughly even — sun teams are fast and hit hard before TR, but TR attackers can OHKO spread attackers once set.
- **vs. Rain**: unfavored — rain teams typically have priority (Jet Punch) and spread damage that punishes bulky setters.
- **vs. Tailwind**: favored if TR lands first; unfavored if Tailwind is established before TR — the speed gap becomes unmanageable.
- **vs. Hyper Offense**: favored — bulk of TR setters absorbs the initial burst; TR punishes frail fast attackers.
- **vs. Goodstuff/Bulky Offense**: roughly even — matchup depends heavily on slot-by-slot specifics.
