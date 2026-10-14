# Security policy

- Keep the repository private.
- Do not store tokens, passwords, personal information, or credentials in git.
- Use GitHub Actions secrets for future scoped integrations.
- Grant the minimum permissions required, and use short-lived credentials where possible.
- Require explicit approval for deployments and changes outside this repository.
- Do not execute code from untrusted issues or pull requests with privileged tokens.
- Keep initial automation manually triggered and non-destructive.
- Review third-party Actions and pin trusted versions before production use.
