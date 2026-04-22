# Assistant design

The chatbot is composed of a single agent reacting to the user's request. An API is available for it to access and edit the team at all times. Other available APIs for the agent are:

- `type_chart_calc()`: gets as input the current team and returns the full list of weaknesses/resists.
- `damage_calc()`: gets as input a pair of pokemon and their relevant info, to do damage calculation.
- `meta()`: retrieves the info about current meta pokemon: retrieves the info about current meta pokemon..
