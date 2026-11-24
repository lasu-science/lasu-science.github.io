# Graph Report - lasu-science.github.io  (2026-11-19)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 177 nodes · 333 edges · 8 communities
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 29 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `5c9b2c95`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- optimizer.py
- thermodynamics.py
- permissions
- numpy
- main.py
- get-pip.py
- injector_model.py
- steps

## God Nodes (most connected - your core abstractions)
1. `PropellantCombination` - 25 edges
2. `evaluate_design()` - 21 edges
3. `compute_nozzle_state()` - 15 edges
4. `EngineCycle` - 14 edges
5. `objective_score()` - 14 edges
6. `score_breakdown()` - 14 edges
7. `design_engine()` - 9 edges
8. `optimise_for_cycle()` - 8 edges
9. `run_optimisation()` - 8 edges
10. `design_injectors()` - 7 edges

## Surprising Connections (you probably didn't know these)
- `hard_constraint_penalty()` --uses--> `EngineCycle`  [INFERRED]
  archivos/LRL/RED/objective_function.py → archivos/LRL/RED/cycle_selector.py
- `objective_score()` --uses--> `EngineCycle`  [INFERRED]
  archivos/LRL/RED/objective_function.py → archivos/LRL/RED/cycle_selector.py
- `score_breakdown()` --uses--> `EngineCycle`  [INFERRED]
  archivos/LRL/RED/objective_function.py → archivos/LRL/RED/cycle_selector.py
- `score_complexity()` --uses--> `EngineCycle`  [INFERRED]
  archivos/LRL/RED/objective_function.py → archivos/LRL/RED/cycle_selector.py
- `design_injectors()` --uses--> `PropellantCombination`  [INFERRED]
  archivos/LRL/RED/injector_model.py → archivos/LRL/RED/propellants.py

## Import Cycles
- None detected.

## Communities (8 total, 0 thin omitted)

### Community 0 - "optimizer.py"
Cohesion: 0.12
Nodes (15): cycle_Isp_efficiency(), EngineCycle, get_all_feasible_cycles(), is_cycle_feasible(), score_cycle(), select_cycle(), evaluate_design(), optimise_for_cycle() (+7 more)

### Community 1 - "thermodynamics.py"
Cohesion: 0.08
Nodes (13): area_mach_ratio(), characteristic_velocity(), compute_nozzle_state(), exit_diameter(), exit_pressure(), gamma_function(), isentropic_pressure_ratio(), mach_from_area_ratio_supersonic() (+5 more)

### Community 2 - "permissions"
Cohesion: 0.08
Nodes (24): name, permissions, runs-on, strategy, build-mode, language, jobs, analyze (+16 more)

### Community 3 - "numpy"
Cohesion: 0.16
Nodes (10): hard_constraint_penalty(), objective_score(), score_breakdown(), score_chamber_pressure(), score_complexity(), score_dP_fraction(), score_expansion_ratio(), score_injector_count() (+2 more)

### Community 4 - "main.py"
Cohesion: 0.14
Nodes (6): design_engine(), print_report(), run_demo(), _validate_inputs(), get_propellant(), _quadratic_peak()

### Community 5 - "get-pip.py"
Cohesion: 0.16
Nodes (6): bootstrap(), determine_pip_install_arguments(), include_setuptools(), include_wheel(), main(), monkeypatch_for_cert()

### Community 6 - "injector_model.py"
Cohesion: 0.20
Nodes (5): best_injector_type_for_propellant(), design_injectors(), injector_pressure_drop_penalty(), InjectorDesign, InjectorType

### Community 7 - "steps"
Cohesion: 0.20
Nodes (10): steps, if, name, run, shell, uses, with, build-mode (+2 more)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `PropellantCombination` connect `optimizer.py` to `thermodynamics.py`, `numpy`, `main.py`, `injector_model.py`?**
  _High betweenness centrality (0.110) - this node is a cross-community bridge._
- **Are the 13 inferred relationships involving `PropellantCombination` (e.g. with `get_all_feasible_cycles()` and `is_cycle_feasible()`) actually correct?**
  _`PropellantCombination` has 13 INFERRED edges - model-reasoned connections that need verification._
- **Should `optimizer.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12121212121212122 - nodes in this community are weakly interconnected._
- **Why does `compute_nozzle_state()` connect `thermodynamics.py` to `optimizer.py`, `numpy`?**
  _High betweenness centrality (0.054) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `evaluate_design()` (e.g. with `EngineCycle` and `PropellantCombination`) actually correct?**
  _`evaluate_design()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Should `thermodynamics.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08377896613190731 - nodes in this community are weakly interconnected._
- **Why does `evaluate_design()` connect `optimizer.py` to `thermodynamics.py`, `numpy`, `injector_model.py`?**
  _High betweenness centrality (0.044) - this node is a cross-community bridge._