# LegacyLens Architecture

## Overview

LegacyLens is a modular Digital Legacy Operating System.

The architecture separates user-facing modules from shared platform services.

## Layers

### User Interface

Location:

ui/

Responsibilities:

- Navigation
- Dashboards
- Workspace Views

### Modules

Location:

modules/

Responsibilities:

Archive-specific capabilities.

Current Modules:

- Photos
- Contacts
- Documents
- Email
- Calendar
- Knowledge

### Core Platform

Location:

core/

Responsibilities:

Shared services used by all modules.

Services:

- Archive Health
- Relationships
- Search
- Timelines
- Validation
- Reporting
- Models

### Data Layer

Location:

data/

Responsibilities:

- Cache
- Databases
- Imports
- Exports

## Design Principles

- Modular
- Local-First
- Human-In-The-Loop
- Explainable
- Privacy Respecting