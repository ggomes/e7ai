# Automated Parameter Sweeps

This exercise provides one engineering calculation in
`truss_stress.py`. The `truss_stress(load_kN, beam_diameter_mm)` function
returns axial stress in MPa for a circular beam. Its implementation is
complete; do not replace the solver while doing the activity.

## Activity

1. Open `truss_stress.py` and inspect the function's units and return value.
2. Ask Copilot Chat: **"Write a script that tests `truss_stress` for load
   values from 10 kN to 50 kN in steps of 10 kN and prints a clean summary
   table."**
3. Choose a beam diameter, run the generated script, and inspect every row.
4. Check that the load values are exactly 10, 20, 30, 40, and 50 kN and that
   stress increases with load.
5. Explain which parts of the generated code are repetitive bookkeeping and
   which conclusions require engineering judgment.

## Learning goals

- Use natural language to delegate loop and table-formatting boilerplate.
- Read generated code closely enough to catch range and unit mistakes.
- Focus engineering attention on interpreting the resulting stress data.

Copilot should generate the sweep script, but you remain responsible for
choosing a meaningful diameter, checking units, and deciding whether the
reported stresses are physically acceptable.
