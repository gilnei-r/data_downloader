# Data Model: Metastock Data Provider

**Date**: 2025-11-01

## Entities

### HistoricalData

Represents a single data point for a security.

**Fields**:

- `Ticker`: `string` - The ticker symbol of the security.
- `Date`: `datetime` - The date of the data point.
- `Open`: `float` - The opening price.
- `High`: `float` - The highest price.
- `Low`: `float` - The lowest price.
- `Close`: `float` - The closing price.
- `Volume`: `integer` - The trading volume.

**Validation Rules**:

- `Ticker` must not be empty.
- `Date` must be a valid date.
- `Open`, `High`, `Low`, `Close`, and `Volume` must be non-negative.

### MetastockConfig

Represents the configuration for the Metastock data provider.

**Fields**:

- `metastock_data_path`: `string` - The absolute path to the Metastock data folder.

**Validation Rules**:

- `metastock_data_path` must be a valid and existing directory path.
