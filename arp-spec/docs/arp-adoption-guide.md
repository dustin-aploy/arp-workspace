# ARP Adoption Guide

## Start with governance, not code

Before implementing an ARP-aware runtime, organizations should identify the owners, approvers, escalation contacts, audit retention expectations, and review processes that their declarations will encode.

## Adopt incrementally

A practical adoption path is:

1. define identity, scope, and authority for one bounded agent role;
2. add escalation and audit requirements;
3. define memory, budget, and performance controls;
4. validate declarations against the ARP schemas; and
5. integrate those declarations into runtime and review workflows.

## Keep protocol artifacts central

Treat ARP declarations as organizational control documents. Downstream code should consume them rather than duplicating them.
