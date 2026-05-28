# Breathe ESG Prototype

A prototype ESG data ingestion and analyst review platform built using Django REST Framework and React.

This system ingests heterogeneous enterprise ESG data from multiple sources, normalizes the records into a common schema, calculates emissions, flags suspicious activity, and allows analyst review before audit signoff.

---

# Features

## Multi-Source ESG Ingestion

Supports ingestion from:

* SAP fuel/procurement exports
* Utility electricity data
* Corporate travel data

---

## Normalization Pipeline

The ingestion engine:

* normalizes units
* classifies ESG scopes
* calculates emissions
* stores raw and normalized records separately

Examples:

| Input   | Normalized |
| ------- | ---------- |
| gallons | liters     |
| MWh     | kWh        |

---

## ESG Scope Classification

| Scope   | Examples        |
| ------- | --------------- |
| Scope 1 | Fuel            |
| Scope 2 | Electricity     |
| Scope 3 | Flights, Hotels |

---

## Analyst Review Workflow

Analysts can:

* review normalized records
* approve records
* inspect failed ingestion rows
* identify suspicious activity

---

## Auditability

The platform stores:

* original source payloads
* normalization outputs
* approval actions
* audit logs

This allows traceability from final ESG records back to original ingestion sources.

---

# Tech Stack

## Backend

* Django
* Django REST Framework
* SQLite (prototype)

## Frontend

* React
* Axios

---

# System Architecture

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

# Project Structure

backend/

* core/
* services.py
* models.py
* serializers.py
* views.py

frontend/

* Upload.js
* Dashboard.js
* FailedRecords.js
* App.js

docs/

* MODEL.md
* DECISIONS.md
* TRADEOFFS.md
* SOURCES.md

---

# API Endpoints

## Upload ESG Data

POST /api/upload/

Accepts CSV uploads.

---

## Normalized Records

GET /api/records/

Returns normalized ESG records.

---

## Failed Records

GET /api/failed-records/

Returns malformed ingestion rows and parsing failures.

---

## Approve Record

PATCH /api/approve/<id>/

Example:

{
"status": "APPROVED"
}

---

# Running Locally

## Backend

Install dependencies:

pip install -r requirements.txt

Run migrations:

python manage.py makemigrations
python manage.py migrate

Start server:

python manage.py runserver

---

## Frontend

Install dependencies:

npm install

Start React app:

npm start

---

# Example CSV Upload

activity_type,quantity,unit
fuel,500,gal
electricity,2,mwh
flight,1200,km
hotel,3,nights

---

# Realistic Enterprise Considerations

The prototype intentionally models realistic ingestion problems including:

* inconsistent units
* malformed rows
* source traceability
* analyst review workflows
* suspicious record detection
* multi-source normalization

---

# Known Limitations

This is a prototype and intentionally excludes:

* authentication and RBAC
* async ingestion queues
* OCR PDF parsing
* production-grade API integrations
* advanced emissions factor engines

See TRADEOFFS.md for details.

---

# Future Improvements

Potential future extensions:

* OCR utility bill parsing
* live SAP/API integrations
* configurable emissions factors
* role-based access control
* immutable audit locking
* advanced analyst dashboards
* airport distance lookup APIs

---

# Deployment

Backend and frontend can be deployed independently using:

* Render
* Railway
* Fly.io
* Vercel

---

# Author

Built as part of the Breathe ESG Tech Intern Assignment.
