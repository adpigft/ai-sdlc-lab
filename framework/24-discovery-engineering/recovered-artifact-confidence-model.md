# Recovered Artifact Confidence Model

## Purpose

The confidence model makes brownfield extraction transparent so teams can tell which recovered artifacts are well evidenced and which still need validation.

## Confidence Levels

- High: strong direct evidence from source files, runtime behavior, or authoritative documentation.
- Medium: mixed evidence with limited inference.
- Low: weak evidence or broad inference.

## Decision Rule

- High-confidence artifacts may be used as the basis for the next modernization stage.
- Medium-confidence artifacts should be reviewed and validated before downstream use.
- Low-confidence artifacts should be treated as provisional and revisited.

## Required Labels

Every recovered artifact should indicate:

- evidence used
- inference used
- confidence level
- unresolved questions
- discovery limitations when the evidence set is incomplete
