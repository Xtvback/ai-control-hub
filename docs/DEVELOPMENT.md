# Development workflow

## Phase 2: automatic code checks

The Code Quality GitHub Actions workflow validates Python syntax, runs unit tests, and checks project structure on pushes and pull requests affecting the relevant files. It can also be triggered manually.

It uses no API keys, external accounts, deployment credentials, or paid AI model APIs. It does not create commits, merge pull requests, or deploy.

## Future autonomous coding

Before enabling an AI coding agent, separately choose a model provider, set a budget, use a restricted token and isolated runner, and require human review for all pull requests. Do not expose GitHub secrets to untrusted pull request code.

## Local equivalent

Run `python -m unittest discover -s tests -v` and `python scripts/validate_project.py`.
