# ARP Split Export Guides

These guides describe how to extract the current grouped workspace into three
standalone repositories without redesigning ownership boundaries:

- [`arp-spec.md`](./arp-spec.md)
- [`arp-devkit.md`](./arp-devkit.md)
- [`arp-registry.md`](./arp-registry.md)

Use these guides when exporting from the validated `arp-workspace` tree. Each
guide includes:

1. source directories in `arp-workspace`
2. exact target directory structure
3. files to copy
4. required standalone fixes
5. validation commands
6. dependency relationships

## Cross-guide rules

- Keep protocol truth in `arp-spec` only.
- Do not invent alternate schema or field names during export.
- Prefer minimal standalone fixes over structural redesign.
- Update README files so they no longer assume sibling folders from the grouped
  workspace unless the target repository intentionally keeps those references.
- Run validation inside the exported standalone repository before publishing it.
