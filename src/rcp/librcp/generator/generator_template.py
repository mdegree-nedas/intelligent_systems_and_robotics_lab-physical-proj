from pathlib import Path
import os


class TemplateGenerator:
    def __init__(self):
        self._cfg_dict = None

        self._gen_name_k = None
        self._gen_sensors_k = None
        self._gen_vector_sensors = []
        self._gen_actuators_k = None
        self._gen_vector_actuators = []
        self._gen_commands_k = None
        self._gen_vector_commands = []

    def _initialize(self, cfg_dict, cfg_parse):
        self._cfg_dict = cfg_dict

        (
            self._gen_name_k,
            self._gen_sensors_k,
            self._gen_vector_sensors,
            self._gen_actuators_k,
            self._gen_vector_actuators,
            self._gen_commands_k,
            self._gen_vector_commands,
            self._gen_vector_topics,
        ) = cfg_parse[:]

        self._sep = "/"
        self._ext = ".py"

        self._tab = "    "
        self._2tab = self._tab * 2
        self._3tab = self._tab * 3
        self._nl = "\n"

    def _initialize_template(self):
        self._prefix = "."
        self._destdir = "out" + self._sep + self._gen_name_k
        Path(self._prefix + self._sep + self._destdir).mkdir(
            parents=True, exist_ok=True
        )

        self._filename = (
            self._prefix
            + self._sep
            + self._destdir
            + self._sep
            + "template"
            + self._ext
        )

        payload = [
            "# rcp: TEMPLATE MODULE" + self._nl,
            "# rcp: auto-generated ros foreign interface file" + self._nl,
            "# rcp: do not edit this file" + self._nl,
            self._nl,
        ]

        f = open(self._filename, "w")
        f.writelines(payload)
        f.close()

    def generate(self, cfg_dict, cfg_parse):
        self._initialize(cfg_dict, cfg_parse)

        self._initialize_template()
        self._gen_template_imports()

        self._gen_template_sensors()

        # for c in self._gen_vector_commands:
        #     print(self._cfg_dict[self._gen_name_k][self._gen_commands_k][c])

        self._finalize()

    # ##################################################
    # GEN EXTRA

    def _gen_template_imports(self):
        payload = [
            self._nl,
        ]

        f = open(self._filename, "a")
        f.writelines(payload)
        f.close()

    def _finalize(self):
        print("finalize: " + self._filename)
        os.system("black -q " + self._filename)

    # ##################################################
    # GEN TEMPLATE SENSORS

    def _gen_template_sensors(self):
        for sensor in self._gen_vector_sensors:
            payload = [
                "def " + sensor + "_read_callback():" + self._nl,
            ]
            payload.append(
                self._tab + 'print("sensor callback: ' + sensor + '")' + self._nl
            )

            f = open(self._filename, "a")
            f.writelines(payload)
            f.close()
