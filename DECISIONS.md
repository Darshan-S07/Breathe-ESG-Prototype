## Overview

This document captures architectural and implementation decisions made during development, including assumptions, ambiguities, and tradeoffs.

The assignment intentionally left multiple areas undefined. This prototype focuses on a realistic and defensible subset rather than attempting to simulate all enterprise complexity.

---

# 1. SAP Ingestion Design

## Decision

Used CSV-based SAP export ingestion.

## Why

Real SAP integrations can involve:

* IDocs
* BAPIs
* OData services
* flat file exports

For a 4-day prototype, CSV export ingestion was chosen because:

* enterprise teams frequently export operational reports manually
* sustainability teams commonly work from flat-file extracts
* CSV allows realistic normalization challenges without requiring SAP infrastructure

The prototype intentionally simulates:

* mixed units
* inconsistent date formats
* abbreviated plant codes
* inconsistent naming

---

# 2. Utility Data Design

## Decision

Used utility CSV portal export ingestion.

## Why

Many facilities teams still retrieve electricity data manually from utility portals.

This approach was selected because it is:

* common in enterprise operations
* realistic for sustainability reporting teams
* simple enough for prototype implementation

The prototype accounts for:

* billing periods
* unit normalization
* tariff metadata

but does not fully implement tariff-specific emissions calculations.

---

# 3. Travel Data Design

## Decision

Used simplified travel-platform-style JSON/CSV activity ingestion.

## Why

Corporate travel systems such as Concur or Navan often expose:

* flights
* hotels
* ground transport

through APIs or exports.

The prototype focuses primarily on:

* flights
* hotels

because they demonstrate Scope 3 handling clearly.

---

# 4. File Upload vs API Pull

## Decision

Primary ingestion mechanism is file upload.

## Why

API integrations would require:

* authentication flows
* external credentials
* sandbox environments
* significantly more infrastructure

File uploads were chosen because:

* they are realistic for ESG onboarding workflows
* enterprise sustainability teams frequently exchange CSV extracts
* they allow demonstration of normalization and review logic within assignment scope

---

# 5. Separation of Raw and Normalized Records

## Decision

Raw ingestion data is stored separately from normalized ESG records.

## Why

This design improves:

* auditability
* reprocessing capability
* debugging
* analyst transparency

It also prevents accidental destruction of source-of-truth data.

---

# 6. Scope Classification Logic

## Decision

Used rule-based scope classification.

## Why

A rule-based system is:

* easy to explain
* deterministic
* sufficient for a prototype

More advanced systems could use:

* configurable mappings
* category taxonomies
* ML-assisted classification

---

# 7. Emission Factor Design

## Decision

Used simplified hardcoded emission factors.

## Why

The assignment primarily evaluates ingestion and normalization quality.

The prototype intentionally keeps emission factors simple while preserving architectural extensibility.

Future systems would likely use:

* factor databases
* region-specific factors
* time-versioned factors
* EPA or DEFRA datasets

---

# 8. Approval Workflow Design

## Decision

Implemented analyst approval using PATCH-based partial updates.

## Why

Analysts typically modify only review state, not entire normalized records.

PATCH semantics more accurately reflect real review workflows.

---

# 9. Failed Record Handling

## Decision

Malformed rows are stored rather than discarded.

## Why

Enterprise ingestion pipelines commonly encounter:

* invalid units
* malformed quantities
* incomplete rows
* inconsistent formatting

The prototype exposes failed rows to analysts for investigation.

---

# 10. Ambiguities and Assumptions

## Assumptions Made

* One organization can own multiple ingestion sources
* Analysts review normalized data before final approval
* Uploaded files are trusted internal enterprise exports
* Scope classification can initially be rule-based
* Utility data is electricity-only for this prototype

---

# Questions I Would Ask the PM

If more product clarification time were available, key questions would include:

1. Should emission factors be region-specific?
2. Are records immutable after approval?
3. Should analysts be able to edit normalized values?
4. What scale of ingestion volume is expected?
5. Are there regulatory requirements for audit retention?
6. Will API integrations eventually replace manual uploads?
7. Should ingestion be asynchronous?
8. Are there tenant-specific validation rules?

# TRADEOFFS.md

## Overview

This prototype intentionally prioritizes:

* realistic ingestion behavior
* clear data modeling
* auditability
* analyst workflow

over feature completeness.

The following capabilities were deliberately not implemented.

---

# 1. Real-Time External API Integrations

## Not Built

Direct integrations with:

* SAP APIs
* Concur APIs
* Navan APIs
* utility provider APIs

## Why

Building production-grade integrations would require:

* authentication systems
* credentials management
* OAuth flows
* sandbox environments
* asynchronous retries

This complexity would significantly reduce focus on the ingestion and normalization architecture being evaluated.

## Tradeoff

The prototype uses realistic exported datasets instead of live integrations.

---

# 2. OCR-Based PDF Utility Parsing

## Not Built

Automated PDF extraction for utility bills.

## Why

OCR introduces substantial complexity:

* layout detection
* provider-specific templates
* parsing reliability issues
* image preprocessing

Given the assignment timeline, structured CSV exports were chosen as a more reliable demonstration of ingestion logic.

## Tradeoff

The prototype handles utility exports but not scanned documents.

---

# 3. Advanced Emissions Methodology Engine

## Not Built

A configurable emissions-factor engine with:

* regional datasets
* versioning
* methodology updates
* supplier-specific calculations

## Why

The assignment focuses more heavily on:

* ingestion
* normalization
* review workflows
* auditability

A simplified factor engine allowed more time to build realistic ingestion handling.

## Tradeoff

Emission calculations are simplified but architecturally extensible.

---

# Additional Deferred Features

The following were also intentionally deferred:

* authentication and RBAC
* async processing queues
* file versioning
* bulk analyst actions
* advanced filtering/search
* immutable record locking
* dashboard analytics
* websocket ingestion status updates

These features would likely be prioritized in a production implementation.
