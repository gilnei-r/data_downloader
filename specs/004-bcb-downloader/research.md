# Research: BCB Time Series Downloader

## Decision: Use the `python-bcb` library

**Rationale**: The `python-bcb` library is a well-documented and actively maintained Python library that provides a simple interface to the Banco Central do Brasil (BCB) API. It allows for easy downloading of time series data from the SGS (Sistema Gerenciador de Séries Temporais) and integrates seamlessly with pandas, which is already a project dependency. This choice aligns with the project's existing technology stack and simplifies the implementation.

**Alternatives considered**:

*   **BacenAPI**: Another Python package for accessing BCB data. While it also seems capable, `python-bcb` appears to be more comprehensive and widely used.
*   **Direct API calls**: Making direct HTTP requests to the BCB API was considered but rejected due to the increased complexity of handling API endpoints, authentication, and data parsing.
