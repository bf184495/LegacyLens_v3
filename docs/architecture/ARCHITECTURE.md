# LegacyLens V3 Architecture

> Digital Legacy Operating System

---

## Purpose

LegacyLens V3 is designed as a modular, extensible **Digital Legacy Operating System**.

Its purpose is to help individuals understand, preserve, organize, maintain, and ultimately transfer the digital assets that collectively tell the story of a life.

LegacyLens is not merely:

- A photo manager
- A contact manager
- A document repository

LegacyLens is a unified platform for digital preservation, archive intelligence, and legacy stewardship.

---

# Mission Statement

**To help people preserve, understand, and responsibly pass forward their digital legacy.**

As society becomes increasingly digital, personal history is dispersed across:

- Photos
- Contacts
- Documents
- Email
- Calendars
- Audio
- Video
- Journals
- Notes
- Cloud Storage
- Family Archives

LegacyLens exists to bring those assets together into a cohesive, understandable system.

---

# Vision

The long-term vision of LegacyLens is to become the primary system through which individuals, families, archivists, and estate planners can understand the condition, contents, and significance of a person's digital life.

The platform should ultimately answer two questions:

> What is the current condition of my digital legacy?

and

> What story would my archive tell if I were no longer here to explain it?

---

# Design Goals

LegacyLens shall:

- Support multiple archive types
- Share common platform services
- Operate locally whenever possible
- Minimize dependency on cloud services
- Preserve user ownership of data
- Prevent accidental data loss
- Scale to millions of records
- Support AI-assisted analysis
- Remain explainable and auditable

---

# Architectural Principles

## Platform Before Modules

LegacyLens is a platform.

Modules are consumers of platform services.

Common services shall not be reimplemented inside individual modules.

Examples:

- Archive Health
- Reporting
- Search
- Scoring
- Relationships
- Timelines

should exist once and be shared.

---

## Local First

The system should operate without requiring cloud services.

Cloud services may be integrated in the future, but the platform must remain functional offline.

---

## Human-In-The-Loop

LegacyLens may:

- Recommend
- Suggest
- Flag
- Prepare

But should never:

- Delete
- Destroy
- Overwrite

without explicit user approval.

---

## Explainability

The user should always be able to understand:

- Why something was classified
- Why something was flagged
- Why two items were linked
- Why an item received a score

AI must remain transparent.

---

## Preservation Before Cleanup

Preservation is prioritized over organization.

The archive must remain protected even when imperfect.

---

# High-Level Architecture

```text
LegacyLens V3
│
├── Platform
├── Modules
├── User Interface
├── Data
├── Reports
└── Resources
```

---

# Platform Layer

```text
platform/
```

The platform contains all shared services.

Modules may consume platform functionality but should not duplicate it.

---

## platform/models

Contains common data structures used throughout the system.

Examples:

```text
ArchiveItem
HealthIssue
HealthReport
Relationship
TimelineEvent
ModuleInfo
ScanResult
```

These models become the shared language of LegacyLens.

---

## platform/archive_health

Purpose:

Evaluate archive quality across every module.

Examples:

- Missing metadata
- Corruption
- Duplicates
- Relationship inconsistencies
- Missing required fields

Outputs:

- Health Issues
- Health Scores
- Health Reports

---

## platform/reporting

Responsible for generating:

- HTML
- CSV
- XLSX
- PDF

Modules provide data.

Reporting provides presentation.

---

## platform/search

Provides unified search capability across all modules.

Future examples:

```text
Find every reference to John Smith

Across:

Photos
Contacts
Email
Documents
Calendar
```

---

## platform/relationships

Responsible for connecting information across modules.

Examples:

```text
Photo → Contact

Contact → Email

Email → Event

Document → Person
```

---

## platform/scoring

Provides standardized score calculations.

Examples:

- Archive Health Score
- Contact Quality Score
- Metadata Completeness Score

---

## platform/timelines

Collects events from all modules.

Examples:

- Photo Taken
- Email Sent
- Document Created
- Calendar Event

Unified into chronological views.

---

## platform/validation

Supports:

- Sampling
- Human review
- Quality assurance
- Verification workflows

---

# Module Layer

```text
modules/
```

Each archive type becomes a module.

---

# Photos Module

```text
modules/photos/
```

Responsibilities:

- Scanning
- Classification
- Duplicate Detection
- Near Duplicate Detection
- Metadata Analysis
- Archive Health

Future:

- Event Clustering
- Family Relationships
