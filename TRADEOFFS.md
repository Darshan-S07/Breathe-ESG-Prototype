# Overview

This prototype intentionally prioritizes:

* realistic ingestion behavior
* normalization quality
* auditability
* analyst workflows
* data traceability

over feature completeness.

Several capabilities were deliberately excluded to keep the implementation focused and defensible within the assignment timeline.

---

# 1. Live External Integrations

## Not Implemented

Direct integrations with:

* SAP APIs
* Concur APIs
* Navan APIs
* utility provider APIs

## Why

Production-grade integrations would require:

* authentication systems
* OAuth flows
* credentials management
* retry infrastructure
* webhook handling
* API sandbox access

This complexity would significantly reduce focus on the ingestion architecture and analyst workflows being evaluated.

## Tradeoff

The prototype uses realistic exported datasets instead of live API connections.

---

# 2. OCR-Based Utility Bill Parsing

## Not Implemented

Automatic extraction from PDF utility bills.

## Why

OCR pipelines introduce substantial complexity:

* provider-specific templates
* layout detection
* parsing inconsistencies
* image preprocessing
* extraction reliability problems

Given the assignment constraints, structured CSV ingestion provided a more reliable demonstration of normalization logic.

## Tradeoff

The system supports utility exports but not scanned document ingestion.

---

# 3. Advanced Emissions Factor Engine

## Not Implemented

A configurable emissions engine supporting:

* regional factors
* methodology versioning
* supplier-specific factors
* regulatory datasets

## Why

The assignment primarily evaluates:

* ingestion design
* normalization logic
* review workflows
* auditability

A simplified emissions engine allowed more focus on realistic ingestion handling.

## Tradeoff

Emission calculations are simplified but architecturally extensible.

---

# 4. Authentication and RBAC

## Not Implemented

* user accounts
* role permissions
* tenant-level authorization

## Why

The prototype focuses on ingestion architecture and analyst workflow design.

Implementing full authentication would significantly increase backend complexity without materially improving the core assignment objectives.

## Tradeoff

The current prototype assumes trusted internal analyst access.

---

# 5. Asynchronous Processing

## Not Implemented

Background ingestion queues using:

* Celery
* Redis
* Kafka

## Why

The ingestion volume in the prototype is intentionally small.

Synchronous processing keeps the system simpler and easier to explain during evaluation.

## Tradeoff

Large enterprise uploads would eventually require asynchronous ingestion and retry mechanisms.

---

# Deferred Future Enhancements

Additional intentionally deferred features include:

* immutable audit locking
* advanced filtering/search
* bulk analyst actions
* websocket ingestion updates
* dashboard analytics
* tenant-specific validation rules
* emissions factor versioning
* airport distance lookup services

These would likely be prioritized in a production implementation.

---

# Final Note

The prototype intentionally focuses on:

* realistic ingestion challenges
* normalization quality
* source traceability
* analyst review workflows
* auditability

rather than attempting to simulate every capability of a production ESG platform.
