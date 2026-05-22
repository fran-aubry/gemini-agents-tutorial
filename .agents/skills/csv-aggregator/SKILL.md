---
name: csv-aggregator
description: Use this skill when the user asks to aggregate a CSV by one column (the group) and sum another column (the metric), then plot the top N groups. Triggered by requests like "top 10 genres by viewership", "biggest categories by sales", or "pie chart of regions by revenue".
---

# CSV Aggregation Workflow

Parse the user's request into four parameters, then execute the workflow.

## Parameters to extract from the request

- **group_column**: the column to group by (e.g., "genres" → `Genre` column)
- **metric_column**: the column to sum within each group (e.g., "viewership" → `Viewership` column)
- **top_n**: how many top groups to show. Default to 10 if unspecified.
- **chart_type**: `"bar"` or `"pie"`. Default to `"bar"` if unspecified.

If any of these are ambiguous, inspect the CSV header first and pick the best column match. State your interpretation before running the code.

## Workflow

1. **Inspect**: Read the CSV header and the first few rows. Confirm which columns match `group_column` and `metric_column`.

2. **Clean the metric column**: It may be a string with units (e.g., `"23.0M Streams"`, `"$1.2K"`). Strip non-numeric characters and convert suffixes (`K`, `M`, `B`) to their numeric multipliers. Cast to float.

3. **Handle multi-value group columns**: If the group column contains multiple values per row separated by `/`, `,`, `;`, or `&` (e.g., `"Sci-Fi / Horror"`, `"Comedy Drama"`), split on those separators and `explode()` so each value becomes its own row. Strip whitespace from each value.

4. **Aggregate**: `df.groupby(group_column)[metric_column].sum().sort_values(ascending=False).head(top_n)`.

5. **Plot**: Render `chart_type` using matplotlib. Title the chart with the user's request. Label axes. Save as PNG to the current working directory with a descriptive filename (e.g., `top_10_genres_by_viewership.png`).

6. **Report**: Print the aggregated table and the saved filename.

## Notes

- Always use `pandas` and `matplotlib`.
- If `matplotlib` is not installed, install it first.
- Do not assume the metric column is already numeric — always clean it.
- Do not assume the group column is single-valued — always check for separators.
