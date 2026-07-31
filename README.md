# UFSC Academic Archive

Historical projects developed during my Information Systems degree at the
Federal University of Santa Catarina (UFSC).

This repository consolidates coursework, exercises, and small academic
experiments that were previously maintained as separate repositories. It is
kept as a record of my software development journey rather than as a collection
of actively maintained applications.

## Projects

| Area | Project | What it covers | Technologies |
| --- | --- | --- | --- |
| Compilers | [Compiler implementations](projects/compiladores) | Two compiler construction assignments, grammars, parsers, reports, and sample programs | Python, ANTLR, Java |
| Object-oriented systems | [Seafood restaurant guide](projects/dso2/guia-sushi) | Mobile restaurant guide backed by an HTTP API and database | React Native, Expo, Express, MongoDB |
| Object-oriented systems / IoT | [Arduino ultrasonic sensor](projects/dso2/arduino) | Ultrasonic sensor readings sent to an HTTP service | Arduino, C++, Node.js, Express |
| Data structures | [Data structures exercises](projects/estruturas-de-dados) | Array-based list, queue, and stack implementations | C++ |
| SECCOM | [Python mini-course](projects/seccom/minicurso-python) | Reverse Polish notation calculator used in a Python mini-course | Python |
| Operating systems | [Assignment 1](projects/sistemas-operacionais/t1) | Thread synchronization assignment and supporting report | C, POSIX threads |
| Operating systems | [Assignment 2](projects/sistemas-operacionais/t2) | Memory management and paging assignment | C |

## History preservation

The projects were imported with `git subtree` without squashing. Their original
commits, authors, dates, messages, and commit hashes remain reachable from this
repository's history. The former compiler repository became this archive and
its files were moved into the structure above without changing their contents.

The Arduino project's former `dev` branch is preserved as the
`archive/arduino/dev` tag. Automated Dependabot branches were intentionally not
retained.

| Former repository | Branch | Imported head | Destination |
| --- | --- | --- | --- |
| `ufsc-compiladores` | `main` | [`0ce2845`](../../commit/0ce28457453015dc0402dee0e631eb99c8419488) | `projects/compiladores` |
| `ufsc-dso2-trabalho2-guia-sushi` | `master` | [`780ae7e`](../../commit/780ae7ec4a90c9561a8aee3bec77ae3e4708b462) | `projects/dso2/guia-sushi` |
| `ufsc-dso2-trabalho3-arduino` | `master` | [`8746395`](../../commit/8746395161720381ecaa72309a47f2df0196cf0e) | `projects/dso2/arduino` |
| `ufsc-estruturas-de-dados` | `master` | [`f0eb605`](../../commit/f0eb60593a1bff4046d50bd32f0ab0790fbce923) | `projects/estruturas-de-dados` |
| `ufsc-seccom-minicurso-python` | `master` | [`a39e305`](../../commit/a39e30588007d97e6cbecb64776288d934be5494) | `projects/seccom/minicurso-python` |
| `ufsc-sistemas-operacionais-t1` | `main` | [`1cc1f50`](../../commit/1cc1f5088496539404fab90ca487b535aaf6c77c) | `projects/sistemas-operacionais/t1` |
| `ufsc-sistemas-operacionais-t2` | `main` | [`d37dd35`](../../commit/d37dd35a1719d88beff77181dcdccf7dddcb003f) | `projects/sistemas-operacionais/t2` |

## Related project

[MercadoZetta](https://github.com/viniciuspizettadesouza/mercadozetta)
originated as a UFSC assignment and later evolved into a production-oriented
full-stack engineering study. It remains an independent, actively maintained
project.

## Status

Archived for historical and educational reference. Individual projects may use
outdated dependencies and are not maintained as production software.
