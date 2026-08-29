# Security and secrets

## Core rule

Never place database passwords, API keys, access tokens, private keys, or full authenticated connection strings in source code, Git commits, issue text, screenshots, prompts, sample data, or browser-delivered JavaScript.

The application should reference secret **names** such as `DATABASE_URL`; the actual values are injected by the developer or deployment environment.

## Local development

1. Copy `.env.example` to `.env.local`.
2. Put development-only credentials in `.env.local`.
3. Keep `.env.local` out of Git.
4. Prefer a dedicated Neon development branch and a restricted application role rather than the database-owner credential.
5. Rotate credentials immediately if they are accidentally pasted into chat, committed, logged, or otherwise exposed.

## ChatGPT-assisted development

When asking ChatGPT to build or debug code, provide placeholders such as:

```text
DATABASE_URL=<configured locally>
OPENAI_API_KEY=<configured locally>
```

ChatGPT can write code against `process.env.DATABASE_URL` without knowing the value.

If ChatGPT has an authenticated connector to a service such as Neon or GitHub, prefer that connector for service operations. Do not paste credentials merely to make the connector work; connector authentication is separate.

When a secret is required to run code on your own machine, add it locally after pulling the generated code. When a secret is required in a deployment platform, use that platform's encrypted environment-variable or secret-management interface.

## Browser safety

Database credentials must never be shipped to the browser. Do not use `NEXT_PUBLIC_`, `VITE_`, or other client-exposed prefixes for server credentials.

Browser code should call authenticated server/API endpoints. Those server endpoints perform database operations using server-side credentials.

## Database access

For production:

- use least-privilege application roles;
- keep owner/admin credentials for migrations and administration only;
- use separate development and production credentials;
- prefer separate Neon branches/databases for development and production;
- validate and parameterize all database inputs;
- authenticate and authorize write endpoints;
- avoid returning internal database errors or credentials to clients;
- rotate secrets periodically and after any suspected exposure.

## Before committing

Check staged changes for secret-bearing files and credential patterns. At minimum run:

```bash
git status
git diff --cached
```

A secret scanner such as Gitleaks can be added to local hooks and CI as the project becomes a full application.

## Incident response

If a credential is exposed, deleting the text is not sufficient. Treat the credential as compromised: revoke or rotate it, update the legitimate secret store, and verify that the old credential no longer authenticates.
