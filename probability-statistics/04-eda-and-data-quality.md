# Checking and looking at data: statistical checks, EDA, missing data, visualization

Before you trust a dataset, test it with numbers, then look at it with pictures.

## Statistical checks: test the data before you trust it

**Statistical checks** are numeric tests run on a dataset to see whether it matches what you expect, before you use it. Each one is a rule that gives a number or a pass/fail, so a script (or an AI agent) can run it.

1. **Shape.** How many rows and columns, and is that the number you expected? Are the keys unique? Any duplicates?
2. **Row reconciliation.** Rows in each source, versus rows after a join or merge; counts per group before and after. *This is the check that catches the "clean dataset" failure: three sources joined, 4% of the rows vanished, all from one group, and nothing later could see rows that were already gone.*
3. **Types and formats.** Does each column parse as what it should be (a number, a date, a category)? Any sentinel values like "N/A"?
4. **Ranges and validity.** Minimum and maximum, impossible values (a negative age), wrong units.
5. **Missingness counts.** How many values are missing, and in which columns. (The reasons come later, under missing data.)
6. **Distributions.** Mean, median, standard deviation, quantiles, skew; compare with what you expect.
7. **Relationships.** Correlations, and cross-field rules (an end date comes after its start date).
8. **By group.** Repeat the checks inside each subgroup, because a problem in one small group disappears in the total.
9. **Over time and across versions.** Compare new data with old, and training data with live data, to catch drift and skew. Production systems automate this: Google's data-validation system for machine-learning pipelines checks incoming data against a schema and flags anomalies, drift and training/serving skew.

**What they cannot do.** They read the data as it was written. They cannot see a row that never arrived, or tell you whether the number you expected was the right number. Deciding what to expect takes knowledge of the domain. A passing check shows only that the property you checked holds.

**In one line:** statistical checks are numbers a rule can test (shape, row counts, types, ranges, missingness, distributions, relationships, by group, over time). A script can run them. They cannot see what is not there.

## Descriptive statistics and EDA

**Descriptive statistics**
- **Center:** mean (pulled by outliers), median (middle value, robust), mode (most frequent).
- **Spread:** range, variance, standard deviation, **IQR** (Q3 − Q1). A common outlier flag: below Q1 − 1.5·IQR or above Q3 + 1.5·IQR.
- **Shape:** skew (lopsided), bimodal (two humps, often two subgroups), spikes (often a sentinel or default value).
- **Relationship:** correlation r runs from −1 to 1 and measures *linear* association; it is not causation, and outliers distort it.

**EDA**
- EDA uses **statistical and graphical techniques** to summarize the main characteristics of data with one variable, two variables, or many.
- **Purpose:** find relationships among variables and which variables matter for the task.
- **Rationale:** EDA helps you understand the data, form and change theories, and decide which techniques are appropriate. After a model is built, EDA can find patterns the original hypothesis tests missed.
- **Why we plot.** A person cannot read 100,000 to 300,000 rows, and the human brain is good at pictures. Anscombe's quartet (1973) and the "Datasaurus" (2017) show datasets with the same summary statistics and very different plots.
- **Usual EDA moves**: classify column types, check shape and row counts, histogram or bar chart for each variable, scatter plots for pairs, record counts over time, box plots and the IQR rule for outliers, and a missingness map.
- **Statistical checks** (rule-based numeric tests) come first; EDA's plots are what a person looks at to see what the numbers hide.
- **Data integration.** Bring data from several sources into one place (ETL: extract, transform, load; ELT loads first). Row counts before and after a join are a check worth running (see the "clean dataset" case in the data-validation chapter).

## Missing data and imputation

- **Missing values** show up as blanks, NA, NaN, NULL, "None", or sentinel numbers such as 0. Causes: corruption, capture failure, people choosing not to answer, system failure.
- **Check for it:** isnull() and notnull() in pandas; the `missingno` library draws bar, matrix and heatmap views.
- **Three types (Rubin):**
  - **MCAR** (missing completely at random): unrelated to anything; random sensor dropout. Safest to delete or impute.
  - **MAR** (missing at random): depends on something you *observed* (younger respondents skip the income question). Predictable from the other columns.
  - **MNAR** (missing not at random): depends on the missing value itself (high earners do not report income; the sickest patients leave a study). Biased in a direction you cannot measure; needs modeling or domain thinking, and records should be flagged, not simply dropped.
- **Deletion:** *listwise* (drop any row with a missing value), *pairwise* (use all available pairs; assumes MCAR; results come from different subsets), and *dropping a variable* (a common rule of thumb is to consider dropping a variable when over about 60% of it is missing and it is unimportant). Deletion loses information and biases results unless data are MCAR.
- **Imputation (filling in):**
  - **Mean / median / mode:** quick; assumes MCAR; shrinks variance and distorts correlations; use the median or mode for skewed data.
  - **Most frequent or constant value:** works for categorical columns; can add bias.
  - **k-nearest-neighbors:** fill from similar rows; more accurate; slow and outlier-sensitive.
  - **MICE (multivariate imputation by chained equations):** fills repeatedly from the other columns and shows the uncertainty.
  - **Regression imputation:** predict from other variables; **stochastic** regression imputation adds a random residual to keep the spread.
  - **Hot-deck:** copy an observed value from a similar row.
  - **Interpolation / extrapolation:** use neighboring values in a sequence.
  - **Deep-learning imputers** exist (for example the Datawig library).
  - **Categorical columns:** do not use the mean or zero; use the most frequent class.
- **The rule that matters:** how you handle missing data depends on *why* it is missing, and imputing under MNAR can bias the result. Keep a record of how much was missing in each column.

## Visualization

- **Data types:** **nominal** (category names), **ordinal** (ordered values), **quantitative** (numbers; ratio data need a zero baseline for proportional comparison), **temporal** (time points or intervals). The types form a hierarchy: ordinal supports "same or different," quantitative supports ranking. A number is not automatically quantitative (an age band can be ordinal).
- **Marks and channels:** a chart is a set of **marks** (points, bars, lines, areas) whose attributes (**position, size, shape, color, opacity**) are **channels** that carry data values.
- **Grammar of graphics (Wilkinson; layered version by Wickham):** describe a chart by its parts: **data, aesthetics (what maps to what), scales, geometric objects (geoms), statistics, facets (small multiples), coordinate system**.
- **The visualization zoo:** families of chart: time series (index charts, stacked graphs, small multiples), statistical distributions (histograms, box plots), multivariate (parallel coordinates), maps, hierarchies, networks.
- **Data humanism** treats data as human stories, not only numbers. **Interaction** and declarative charting libraries such as **Altair** are common tools.
- Perceptual ranking: position on a common scale is read most accurately; area and color intensity less so. This is why a bar chart beats a pie chart for comparing values.
