# Branch And PR Model

## Purpose

Define how branches and pull requests enforce app, service, library, and event ownership boundaries in a multi-squad banking program.

## Branch Model

Use short-lived branches tied to a single primary slice:

```text
feature/<capability>-<slice>
bugfix/<capability>-<slice>
chore/<target>-<change>
```

Examples:

- `feature/local-payments-slice-1`
- `feature/payment-common-dto-update`
- `bugfix/paymentcompleted-schema-fix`

## PR Rules

Every PR must include:

- primary target type
- primary target path
- owning squad
- impacted secondary targets
- required contract tests
- required regression tests
- cross-squad impact review result when relevant

## Path Boundary Checks

The PR automation or review process must compare changed file paths against the catalog and CODEOWNERS.

Boundary result:

- in-scope: all changed paths belong to the declared primary owner
- shared: changed paths include a shared library, event, or shell component
- cross-squad: changed paths touch more than one owner
- blocked: changed paths do not match the declared owner or slice target

## PR Review Requirements

### In-scope change

- primary squad review
- automated tests for the slice

### Shared asset change

- primary squad review
- shared asset owner review
- consumer review if public contract changes

### Cross-squad change

- all affected squad owners
- contract tests
- regression tests for adjacent capabilities
- explicit impact review summary

## Banking Examples

### Mobile banking app shared by three feature squads

If a PR touches the shared mobile app shell and local payments module together:

- the PR must name the mobile app shell as the primary target or be split
- the PR requires Mobile Banking owner review plus local payments reviewer

If a PR touches only the local payments module inside the shared app:

- the PR can stay within the local payments ownership path if the app catalog grants that module boundary

### Services

- `local-payment-service` changes stay within the Local Payments squad path
- `remittance-service` changes stay within the Remittance squad path
- `card-management-service` changes stay within the Cards squad path

If one PR changes both `local-payment-service` and `remittance-service`, split it unless both squads and the platform owner approve the shared contract change.

### Shared payment-common library

Any public API change in `payment-common` must:

- include library owner review
- include consumer review from local payments, remittance, and cards
- include versioning or compatibility evidence

## Do / Don't Rules

Do:

- keep PRs narrow and owner-aligned
- use path-based checks to detect boundary violations
- split PRs when ownership is mixed

Do not:

- merge a PR that silently crosses squad boundaries
- rely on branch naming alone without path verification
- accept shared library changes without consumer impact review

