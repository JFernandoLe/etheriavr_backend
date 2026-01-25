class UserConfiguration:
    def __init__(
        self,
        user_id: int = None,
        midi_device_name: str = None,
        audience_intensity: str = "Medio",
    ):
        self.user_id = user_id
        self.midi_device_name = midi_device_name
        self.audience_intensity = audience_intensity
