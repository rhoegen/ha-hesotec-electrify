"""Custom types for hesotec_electrify."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import HesotecElectrifyApiClient
    from .coordinator import HesotecElectrifyDataUpdateCoordinator


type HesotecElectrifyConfigEntry = ConfigEntry[HesotecElectrifyData]


@dataclass
class HesotecElectrifyData:
    """Data for the HesotecElectrify integration."""

    client: HesotecElectrifyApiClient
    coordinator: HesotecElectrifyDataUpdateCoordinator
    integration: Integration