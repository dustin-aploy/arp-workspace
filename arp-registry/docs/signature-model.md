# Signature Model

## Why signatures exist

Registry entries point to public compliance evidence. Detached signatures help a consumer verify that the published compliance report has not been altered after issuance or mirroring.

## Scope of signing

The recommended artifact to sign is the exact JSON byte stream of the published `ARPComplianceReport` file after canonical serialization for distribution. The registry entry itself may also be signed in future deployments, but the report is the minimum trust artifact.

## Detached signature approach

This repository models a detached-signature workflow:

- `reports/compliance-report.example.json` contains the report payload; and
- `reports/compliance-report.example.sig` contains detached signature metadata and signature bytes.

A practical deployment may use Ed25519, Sigstore, Minisign, or another verifiable public-key signature system, but the registry should always publish:

- the signing algorithm;
- the signer identity or issuer;
- the key identifier or certificate chain reference;
- the digest of the signed artifact; and
- the detached signature value.

## Verification expectations

A registry reviewer should verify that:

1. the digest in the signature metadata matches the report file;
2. the signature verifies against the declared key material;
3. the signer identity is appropriate for the listing level; and
4. the report being signed is the same report referenced from the registry entry.

## Limits

A valid signature proves integrity and provenance of the signed artifact. It does **not** prove that the underlying project remains secure, unchanged, or still compliant after the signed report was issued.
