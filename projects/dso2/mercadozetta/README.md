# MercadoZetta

Historical version of MercadoZetta developed for the Object-Oriented Systems
Development II course at UFSC in 2019.

The project is preserved as two applications:

- `backend/`: Express and MongoDB HTTP API. The imported version requires the
  `MONGODB_URI` environment variable.
- `frontend/`: Create React App web client. Its API endpoint is configured with
  `REACT_APP_API_URL`.

## History and security

The default branches of the former `mercadozetta-backend` and
`mercadozetta-frontend` repositories were imported without squashing.
Automated Dependabot branches were intentionally excluded.

The backend originally embedded a MongoDB credential in six historical
commits. Those commits were sanitized before import, so their authors, dates,
and messages are retained but their commit hashes differ from the former
repository. The credential itself is not part of this archive.

## Later evolution

The independent
[MercadoZetta repository](https://github.com/viniciuspizettadesouza/mercadozetta)
contains the later production-oriented full-stack engineering study. It is not
part of this academic archive migration.
