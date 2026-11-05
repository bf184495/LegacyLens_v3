# ADR-0007

## Title

Archive Intelligence as a Core Platform Objective

## Status

Accepted

## Context

LegacyLens began as a photo archive analysis platform.

As platform capabilities expanded, it became clear that greater value exists in understanding relationships across all archive types rather than treating each archive independently.

## Decision

LegacyLens V3 will be designed around a future Archive Intelligence layer capable of analyzing information across modules.

## Consequences

Future modules must expose:

- Relationships
- Timeline information
- Ownership information
- Confidence values
- Cross-reference metadata

Archive Intelligence will become a first-class platform service.