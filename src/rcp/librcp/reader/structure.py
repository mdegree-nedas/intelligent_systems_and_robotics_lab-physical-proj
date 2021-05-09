from itertools import chain


class Structure:
    def __init__(self):
        self._initialize()

    def _initialize(self):
        self._cfg_default_classes = ["sensors", "actuators", "commands"]
        self._cfg_default_sensors_fields = ["id", "type", "address", "data"]
        self._cfg_default_actuators_fields = ["id", "address", "commands"]
        self._cfg_default_commands_fields = ["data", "time"]

        self._cfg_vector_name = []
        self._cfg_vector_classes = []
        self._cfg_vector_sensors = []
        self._cfg_vector_sensors_fields = []
        self._cfg_vector_actuators = []
        self._cfg_vector_actuators_commands = []
        self._cfg_vector_actuators_fields = []
        self._cfg_vector_commands = []
        self._cfg_vector_commands_fields = []

    def cfg_validate(self, cfg_dict):
        self._initialize()
        self._cfg_vector_name = list(cfg_dict.keys())
        assert len(self._cfg_vector_name) == 1
        name_k = self._cfg_vector_name[0]

        self._cfg_vector_classes = list(cfg_dict[name_k].keys())
        assert len(self._cfg_vector_classes) == 3
        assert self._cfg_vector_classes == self._cfg_default_classes

        sensors_k, actuators_k, commands_k = self._cfg_vector_classes[:]

        self._cfg_vector_sensors = list(cfg_dict[name_k][sensors_k].keys())
        for sensor in self._cfg_vector_sensors:
            self._cfg_vector_sensors_fields = list(
                cfg_dict[name_k][sensors_k][sensor].keys()
            )
            assert len(self._cfg_vector_sensors_fields) == 4
            assert self._cfg_vector_sensors_fields == self._cfg_default_sensors_fields

        self._cfg_vector_actuators = list(cfg_dict[name_k][actuators_k].keys())
        for actuator in self._cfg_vector_actuators:
            self._cfg_vector_actuators_fields = list(
                cfg_dict[name_k][actuators_k][actuator].keys()
            )
            self._cfg_vector_actuators_commands.append(
                list(cfg_dict[name_k][actuators_k][actuator]["commands"])
            )
            assert len(self._cfg_vector_actuators_fields) == 3
            assert (
                self._cfg_vector_actuators_fields == self._cfg_default_actuators_fields
            )

        self._cfg_vector_actuators_commands = list(
            chain.from_iterable(self._cfg_vector_actuators_commands)
        )
        self._cfg_vector_commands = list(cfg_dict[name_k][commands_k].keys())
        assert self._cfg_vector_commands == self._cfg_vector_actuators_commands

        for command in self._cfg_vector_commands:
            self._cfg_vector_commands_fields = list(
                cfg_dict[name_k][commands_k][command].keys()
            )
            assert len(self._cfg_vector_commands_fields) == 2
            assert self._cfg_vector_commands_fields == self._cfg_default_commands_fields
