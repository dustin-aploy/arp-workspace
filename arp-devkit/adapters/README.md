# ARP Adapters

`arp-devkit/adapters` contains thin integration guidance for mapping external frameworks and environments onto ARP concepts.

Adapters must:
- depend on normative concepts from `../../arp-spec`
- align with reference behavior from `../runtime` when useful
- avoid redefining ARP semantics or turning the workspace into a framework monolith
