# AI as a Code Reader and Physics Sanity-Checker

This exercise uses a short, pre-written trajectory calculation. The code
contains a deliberate unit error: `trajectory_at_distance` expects its
distance in meters, but the caller passes `target_distance_ft` directly.

## Activity

1. Open `projectile.py` in VS Code and run it before changing anything.
2. Ask Copilot Chat: **"Explain what this script calculates line by line."**
3. Ask Copilot Chat: **"Why does this projectile travel an unphysical distance?"**
4. Decide whether Copilot correctly identified the feet-to-meters mismatch.
5. Fix the input conversion, rerun the script, and compare the result.

## Learning goals

- Use AI to digest code that someone else wrote.
- Trace values through a physics calculation instead of trusting a plausible
  output.
- Check units at function boundaries and validate AI explanations against the
  equations.

The engineering judgment remains yours: Copilot can explain the code and point
to a likely problem, but you must verify the units and decide how to correct it.
