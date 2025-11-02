# Research: Yahoo Finance Data Downloader

## Decision: Use `yfinance` library

**Rationale**:

The `yfinance` library is a popular and well-maintained open-source Python library for accessing financial data from Yahoo Finance. It directly supports downloading historical market data, which is the primary requirement of this feature. The library is easy to use and integrates well with `pandas`, which is already in use in the project.

**Alternatives considered**:

- **Directly calling Yahoo Finance API:** This would require more effort to implement and maintain. `yfinance` abstracts away the complexities of the API.
- **Other financial data APIs:** While other APIs exist, Yahoo Finance is specified in the feature request. `yfinance` is the de-facto standard for accessing Yahoo Finance data with Python.
