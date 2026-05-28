## Overview

This document summarizes the real-world source formats researched for the assignment and how they influenced the prototype design.

The prototype intentionally models realistic enterprise ingestion problems rather than idealized clean datasets.

---

# 1. SAP Fuel and Procurement Data

## Research

Investigated common SAP export approaches including:

* flat-file CSV exports
* IDocs
* BAPIs
* OData services

Observed that sustainability and finance teams commonly exchange operational exports as spreadsheets or CSV files.

Real-world characteristics include:

* plant codes
* inconsistent abbreviations
* mixed units
* localized column names
* inconsistent date formats

Examples encountered during research:

* WERKS
* MATNR
* MEINS
* BUDAT

---

## Prototype Choice

Implemented CSV ingestion because:

* it is realistic for operational reporting workflows
* it allows meaningful normalization logic
* it avoids requiring actual SAP infrastructure

---

## Sample Data Characteristics

The prototype sample data intentionally includes:

* fuel quantities in gallons
* electricity in MWh
* simplified operational activity types

Example:

activity_type,quantity,unit
fuel,500,gal

---

## What Would Break in Production

Potential production issues include:

* localized SAP configurations
* multilingual field names
* inconsistent export schemas
* malformed dates
* duplicate records
* missing lookup tables

---

# 2. Utility Electricity Data

## Research

Investigated how facilities teams commonly retrieve utility data.

Common methods observed:

* utility portal CSV exports
* PDF bills
* utility APIs

Typical challenges:

* billing periods crossing calendar months
* multiple meters
* tariff variations
* mixed units

---

## Prototype Choice

Implemented CSV-based utility ingestion.

Reasoning:

* common operational workflow
* practical within assignment constraints
* allows realistic normalization scenarios

---

## Sample Data Characteristics

Example:

meter_id,start_date,end_date,consumption,unit,tariff
MTR001,2026-03-15,2026-04-14,1200,kWh,industrial

The prototype simplifies utility data into normalized electricity records.

---

## What Would Break in Production

Production systems would need to handle:

* time-of-use tariffs
* meter corrections
* missing billing cycles
* partial usage periods
* utility-specific schemas
* OCR extraction errors

---

# 3. Corporate Travel Data

## Research

Investigated corporate travel platforms such as:

* Concur
* Navan
* travel management APIs

Observed common travel record categories:

* flights
* hotels
* rail
* taxis
* car rentals

Also observed that:

* airport codes are often provided instead of distances
* some records contain incomplete itineraries
* hotel records frequently use nights rather than emissions directly

---

## Prototype Choice

Implemented simplified travel activity ingestion focused on:

* flights
* hotels

This was chosen because it clearly demonstrates Scope 3 handling.

---

## Sample Data Characteristics

Example:

[
{
"type": "flight",
"from": "BLR",
"to": "DEL"
}
]

The prototype simplifies travel ingestion into normalized activity records.

---

## What Would Break in Production

Production systems would likely require:

* airport distance lookup services
* itinerary reconstruction
* cabin-class adjustments
* duplicate booking handling
* cancellation handling
* supplier-specific mappings
* API rate limiting management

---

# Final Notes

The prototype intentionally focuses on:

* realistic ingestion challenges
* normalization workflows
* auditability
* analyst review

instead of attempting to simulate every complexity of a production ESG platform.

The design prioritizes clarity, defensibility, and realistic operational assumptions within the assignment constraints.
