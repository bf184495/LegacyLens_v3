LegacyLens V3 Roadmap
Project Status

Current Phase:

Phase 0 - Foundation and Platform Architecture

LegacyLens V3 is in active architectural development.

The focus is currently on building a scalable platform that will support multiple archive types through a shared set of services and common data models.

Mission

Create a Digital Legacy Operating System capable of helping individuals understand, preserve, organize, manage, and ultimately transfer the digital assets that define a life.

Strategic Objectives
Short-Term Objectives

Establish the architectural foundation.

Create shared platform services
Define shared data models
Establish project governance
Create module architecture
Build Archive Health framework
Medium-Term Objectives

Expand beyond Photos.

Home Screen
Contacts Module
Relationship Engine
Cross-Module Search
Long-Term Objectives

Become a complete Digital Legacy Operating System.

Knowledge Engine
Narrative Generation
Timeline Intelligence
Estate Planning Features
Family Archive Preservation
Phase 0 - Platform Foundation

Status: Active

Target: Stable Architecture

Goals

Create shared infrastructure before new modules are introduced.

Deliverables
Project Governance
 README.md
 ARCHITECTURE.md
 DECISIONS.md
 ROADMAP.md
Project Structure
 platform/
 modules/
 ui/
 data/
 resources/
Platform Models
 ArchiveItem
 HealthIssue
 HealthReport
 Relationship
 TimelineEvent
 ModuleInfo
 ScanResult
Archive Health Platform
 engine.py
 issue_registry.py
 score.py
 severity.py
Phase 1 - Home Workspace

Status: Planned

Goals

Introduce the concept of LegacyLens as a platform rather than a photo application.

Deliverables
Module Selector
 Home Screen
 Module Registry
 Navigation Framework
Initial Workspace Selection
 Photos
 Archive Health
 Contacts (Coming Soon)
 Documents (Coming Soon)
 Email (Coming Soon)
 Calendar (Coming Soon)
 Knowledge (Coming Soon)
Dashboard
 Archive Summary
 Archive Health Summary
 Recent Activity
 Module Status
Phase 2 - Archive Health Platform

Status: Planned

Goals

Convert Archive Health from a Photo feature to a Platform feature.

Deliverables
Shared Health Engine
 Health Issues
 Severity System
 Recommendations
 Score Calculation
Reporting
 HTML
 CSV
 XLSX
 PDF
Scoring
 Archive Health Score
 Module Health Scores
Phase 3 - Photos Migration

Status: Planned

Goals

Migrate photo functionality into V3 architecture.

Deliverables
Photo Services
 Scanner
 Metadata
 Classification
 Duplicate Detection
 Near Duplicate Detection
Archive Health Integration
 Shared HealthIssue objects
 Shared HealthReport objects
Shared Reporting
 Platform Report Engine
Phase 4 - Contacts Module

Status: Planned

Goals

Introduce the second archive type.

Deliverables
Import
 CSV Import
 VCF Import
Health
 Missing Email Detection
 Missing Phone Detection
 Duplicate Contact Detection
Contact Intelligence
 Merge Suggestions
 Relationship Discovery
Phase 5 - Relationship Engine

Status: Planned

Goals

Begin connecting information across modules.

Deliverables
Relationship Objects
 Person ↔ Photo
 Person ↔ Email
 Person ↔ Event
 Person ↔ Document
Graph Analysis
 Relationship Network
 Family Network
 Communication Network
Phase 6 - Documents Module

Status: Planned

Deliverables
 Inventory
 Metadata Analysis
 Duplicate Detection
 Health Reporting
Categories
Financial
Medical
Legal
Personal
Employment
Education
Phase 7 - Email Module

Status: Planned

Deliverables
 Mailbox Inventory
 Correspondence Analysis
 Relationship Mapping
 Health Reporting
Future Enhancements
 Conversation Summaries
 Historical Significance Detection
 Communication Timelines
Phase 8 - Calendar Module

Status: Planned

Deliverables
 Event Inventory
 Timeline Generation
 Historical Review
Future Enhancements
 Life Chapters
 Travel Histories
 Employment Timelines
Phase 9 - Knowledge Engine

Status: Future

Goals

Transform archive data into human understanding.

Deliverables
Timeline Intelligence
 Life Timeline
 Historical Timeline
 Event Clustering
Narrative Intelligence
 Story Generation
 Archive Summaries
 Family History Drafts
Knowledge Graph
 Person Graph
 Event Graph
 Archive Graph
Phase 10 - Estate and Preservation Tools

Status: Future

Deliverables
 Archive Export
 Family Preservation Packages
 Digital Legacy Summaries
 Estate Planning Support
Definition of Success

LegacyLens V3 succeeds when:

Multiple archive types operate on a common platform.
Archive Health spans the entire system.
Relationships connect information across modules.
Users gain meaningful insight into their digital lives.
Future generations can understand the story preserved within an archive.
Current Priority

Phase 0 - Foundation and Platform Architecture

Immediate Next Steps:

Complete platform directory structure.
Create platform models.
Build Archive Health shared services.
Create module registry.
Build Home Workspace.
Architectural Guiding Principle

Build the platform first.

Build the modules second.

Build intelligence third.

LegacyLens V3 is not a collection of features.

LegacyLens V3 is a platform designed to preserve and understand a person's digital legacy.