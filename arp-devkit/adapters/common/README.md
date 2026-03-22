# Common Adapter Guidance

The `common/` directory explains the shared integration shape across frameworks.

ARP adapters should not try to normalize every framework into one runtime abstraction. Instead, they should answer a simpler question:

**Where can ARP responsibility checks be inserted before and after meaningful actions?**

Use the documents here to keep framework-specific adapters consistent:

- `interfaces.md` explains the thin adapter surface area.
- `lifecycle-hooks.md` explains the main lifecycle moments where ARP hooks belong.
