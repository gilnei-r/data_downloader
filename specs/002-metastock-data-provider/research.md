# Research: Python Library for Reading Metastock Files

**Date**: 2025-11-01

## Decision

We will use the `metastock2pd` Python library to read Metastock data files.

## Rationale

- The `metastock2pd` library is specifically designed to convert Metastock data into pandas DataFrames, which aligns with the project's existing use of pandas.
- It can read `master`, `emaster`, and `xmaster` files to get a list of available data, and then read the individual data files.
- It is available via both `pip` and `conda`, making it easy to install.
- The library handles the complexity of the Metastock binary format.

## Alternatives Considered

- **Custom parsing logic**: Building a custom parser would be time-consuming and error-prone due to the complexity of the Metastock binary format.
- **`ms2txt`**: This is a command-line utility that decodes Metastock files into text format. While `metastock2pd` is built upon it, using `metastock2pd` directly is more convenient as it provides a Python API and integrates with pandas.
