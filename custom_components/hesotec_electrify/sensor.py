"""Sensor platform for hesotec_electrify."""

from __future__ import annotations

from typing import TYPE_CHECKING

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription

from .entity import HesotecElectrifyEntity

if TYPE_CHECKING:
    from homeassistant.core import HomeAssistant
    from homeassistant.helpers.entity_platform import AddEntitiesCallback

    from .coordinator import HesotecElectrifyDataUpdateCoordinator
    from .data import HesotecElectrifyConfigEntry

ENTITY_DESCRIPTIONS = (
    SensorEntityDescription(
        key="hesotec_electrify",
        name="Hesotec Sensor",
        icon="mdi:format-quote-close",
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,  # noqa: ARG001 Unused function argument: `hass`
    entry: HesotecElectrifyConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    async_add_entities(
        HesotecElectrifySensor(
            coordinator=entry.runtime_data.coordinator,
            entity_description=entity_description,
        )
        for entity_description in ENTITY_DESCRIPTIONS
    )


class HesotecElectrifySensor(HesotecElectrifyEntity, SensorEntity):
    """hesotec_electrify Sensor class."""

    def __init__(
        self,
        coordinator: HesotecElectrifyDataUpdateCoordinator,
        entity_description: SensorEntityDescription,
    ) -> None:
        """Initialize the sensor class."""
        super().__init__(coordinator)
        self.entity_description = entity_description

    @property
    def native_value(self) -> str | None:
        """Return the native value of the sensor."""
        return self.coordinator.data.get("body")