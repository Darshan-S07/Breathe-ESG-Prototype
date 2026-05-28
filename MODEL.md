

## Overview

This system is designed to ingest heterogeneous ESG data from multiple enterprise sources, normalize it into a consistent schema, and provide an auditable analyst review workflow before records are finalized for audit reporting.

The application was intentionally designed around realistic enterprise ingestion problems rather than idealized clean datasets.

The prototype currently supports:

* SAP fuel and procurement exports
* Utility electricity consumption data
* Corporate travel activity data
* Analyst approval workflow
* Failed ingestion handling
* Audit trail generation
* Scope 1 / 2 / 3 classification
* Unit normalization

---

# Core Design Principles

## 1. Separation of Raw and Normalized Data

The system separates ingestion into two stages:

### RawRecord

Stores the exact original payload received from the source.

Purpose:

* Preserve source-of-truth data
* Allow reprocessing if normalization logic changes
* Support auditability
* Prevent data loss during parsing failures
* Allow analysts to inspect malformed rows

### NormalizedRecord

Stores standardized ESG-ready records derived from raw ingestion.

Purpose:

* Enable consistent emissions calculations
* Normalize units and classifications
* Simplify analyst review workflows
* Support downstream reporting

This separation mirrors how enterprise ETL pipelines commonly operate.

---

## 2. Multi-Tenancy

All records are scoped by Organization.

This ensures:

* Isolation between enterprise clients
* Tenant-specific ingestion tracking
* Future extensibility for permissions and RBAC
* Cleaner audit separation

Current implementation uses a simple foreign key relationship.

---

## 3. Source Tracking

Each ingestion operation creates a DataSource object.

Tracked metadata includes:

* source type
* ingestion method
* organization
* ingestion timestamp

Supported source types:

* SAP
* Utility
* Travel

Supported ingestion methods:

* File upload
* API (future extension)

This design allows analysts to trace every normalized record back to its originating source.

---

## 4. ESG Scope Classification

The prototype classifies records into:

### Scope 1

Direct emissions.

Examples:

* Fuel combustion
* Diesel
* Petrol

### Scope 2

Indirect purchased energy.

Examples:

* Electricity consumption

### Scope 3

Indirect value-chain emissions.

Examples:

* Flights
* Hotels
* Corporate travel

Classification is currently rule-based but designed to be extensible.

---

## 5. Unit Normalization

Enterprise source systems often contain inconsistent units.

Examples:

* gallons
* liters
* MWh
* kWh

The ingestion pipeline normalizes quantities into standard units before emissions calculation.

Examples:

| Input | Normalized |
| ----- | ---------- |
| gal   | liters     |
| MWh   | kWh        |

This prevents inconsistent emissions calculations across datasets.

---

## 6. Emissions Calculation

The prototype applies simplified emission factors based on activity type.

Examples:

| Activity    | Example Factor    |
| ----------- | ----------------- |
| fuel        | 2.31 kg CO2/liter |
| electricity | 0.82 kg CO2/kWh   |
| flight      | 0.15 kg CO2/km    |
| hotel       | 10 kg CO2/night   |

The architecture intentionally separates emissions logic into services.py for future extensibility.

---

## 7. Suspicious Record Detection

The system flags anomalous records using threshold-based heuristics.

Examples:

* unusually large fuel usage
* excessive hotel nights
* abnormal electricity consumption

Flagged records remain reviewable by analysts before approval.

This feature simulates enterprise data quality workflows.

---

## 8. Analyst Review Workflow

Records move through the following lifecycle:

PENDING → APPROVED → REJECTED

Analysts review normalized records before finalization.

The workflow intentionally uses partial updates for status changes rather than replacing full records.

---

## 9. Audit Logging

Every approval workflow update creates an AuditLog entry.

Tracked information:

* previous values
* updated values
* action type
* timestamp

This provides basic traceability required for ESG reporting and future auditor review.

---

# Entity Relationships

Organization
↓
DataSource
↓
RawRecord
↓
NormalizedRecord
↓
AuditLog

---

# Why This Model Was Chosen

The design prioritizes:

* traceability
* auditability
* extensibility
* realistic ingestion behavior
* imperfect real-world datasets

instead of optimizing purely for CRUD simplicity.

The architecture intentionally mirrors how enterprise ESG ingestion systems separate:

* ingestion
* normalization
* analyst review
* audit tracking

into distinct layers.

---

# Future Extensions

Potential future improvements include:

* role-based access control
* asynchronous ingestion queues
* OCR-based utility bill parsing
* airport distance lookup APIs
* emissions factor versioning
* immutable audit locking
* tenant-specific emission factors
* API-based ingestion connectors
