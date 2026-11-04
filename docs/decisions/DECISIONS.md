LegacyLens V3 Architectural Decision Record (ADR)
Purpose

This document records significant architectural, technical, and organizational decisions made during the development of LegacyLens V3.

The goal is to preserve the reasoning behind decisions so future development remains aligned with the platform vision.

Decision Record Template

Every decision should follow this format.

ADR-XXXX

Date: YYYY-MM-DD

Status: Proposed | Approved | Superseded | Deprecated | Rejected

Context

Why was a decision needed?

Decision

What was decided?

Alternatives Considered
Option A
Option B
Option C
Consequences

Benefits

Benefit 1
Benefit 2

Costs

Cost 1
Cost 2
ADR-0001

Date: 2026-11-03

Status: Approved

Context

LegacyLens currently exists as a working photo-analysis application.

Major architectural changes would significantly alter:

Project structure
Module boundaries
Shared services
User interface
Reporting architecture

Performing those changes directly within the production project increases risk.

Decision

Develop LegacyLens V3 in a separate architecture sandbox.

Production:

LegacyLens

Future Platform:

LegacyLens_v3

Alternatives Considered
Refactor LegacyLens in place
Create feature branches only
Full rewrite from scratch
Consequences
Benefits
Reduced risk
Freedom to redesign architecture
Easier experimentation
Costs
Two codebases temporarily exist
Migration effort later
ADR-0002

Date: 2026-11-03

Status: Approved

Context

LegacyLens began as a photo-management tool.

The long-term vision now includes:

Photos
Contacts
Documents
Email
Calendar
Knowledge
Decision

LegacyLens V3 will become a Digital Legacy Operating System.

Photos become only one module of a larger platform.

Alternatives Considered
Remain photo-centric
Build independent applications
Focus solely on media preservation
Consequences
Benefits
Larger mission
Unified user experience
Cross-module intelligence
Costs
Increased architectural complexity
ADR-0003

Date: 2026-11-03

Status: Approved

Context

Future modules will require common capabilities.

Examples:

Archive Health
Reporting
Search
Validation
Relationships
Scoring

Duplicating those capabilities across modules would create long-term maintenance problems.

Decision

Create:

platform/

as the home for all shared services.

Modules consume platform services.

Modules do not reimplement them.

Consequences
Benefits
Reduced duplication
Consistent behavior
Easier maintenance
Costs
Additional architecture work up front
ADR-0004

Date: 2026-11-03

Status: Approved

Context

Future modules require common data structures.

Without shared models, every module will invent incompatible representations.

Decision

Create:

platform/models

Initial shared models:

ArchiveItem
HealthIssue
HealthReport
Relationship
TimelineEvent
ModuleInfo
ScanResult
Consequences
Benefits
Shared language
Easier interoperability
Simplified reporting
Costs
Upfront model design
ADR-0005

Date: 2026-11-03

Status: Approved

Context

Archive Health originated as a Photos feature.

Future modules need similar capabilities.

Examples:

Duplicate contacts
Missing document metadata
Corrupt files
Missing calendar information
Decision

Archive Health becomes a platform-wide capability.

Transition:

Photo Health

to

Archive Health

Consequences
Benefits
Unified quality reporting
Cross-module health scoring
Better user insight
Costs
Migration effort
ADR-0006

Date: 2026-11-03

Status: Approved

Context

LegacyLens currently launches directly into a photo workflow.

Future versions will contain multiple modules.

Decision

Introduce a Home Screen.

Initial layout:

Photos
Contacts
Documents
Email
Calendar
Knowledge
Archive Health
Settings
Consequences
Benefits
Better scalability
Clear module separation
Improved navigation
Costs
Additional UI development
ADR-0007

Date: 2026-11-03

Status: Approved

Context

Long-term projects fail when architectural decisions are forgotten.

Decision

Maintain the following core documents:

README.md
ARCHITECTURE.md
DECISIONS.md
ROADMAP.md

Session documentation should also be preserved.

Consequences
Benefits
Better continuity
Easier onboarding
Improved planning
Costs
Documentation maintenance
Future Decisions

Additional decisions should continue the sequence:

ADR-0008
ADR-0009
ADR-0010
...
Current Architectural Baseline

Approved:

Separate V3 architecture
Modular platform architecture
Shared services layer
Archive Health framework
Shared models layer
Home screen concept
Documentation-first methodology

Current Project Phase:

Phase 0 - Foundation and Platform Architecture
