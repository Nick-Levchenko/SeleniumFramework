import json


class ConfigReader:
    CONFIG_PATH = 'config.json'

    def read_driver_config(self, parameter: str):
        with open(self.CONFIG_PATH) as json_file:
            config = json.load(json_file)
        return config["driver_options"][parameter]

    def get_url_by_test_case(self, test_case_name: str):
        with open(self.CONFIG_PATH) as json_file:
            config = json.load(json_file)
            return config["test_cases"][test_case_name]["url"]

    def get_param_by_test_case(self, test_case_name: str, param_name: str):
        with open(self.CONFIG_PATH) as json_file:
            config = json.load(json_file)
            return config["test_cases"][test_case_name][param_name]

    def get_autoit_script(self):
        with open(self.CONFIG_PATH) as json_file:
            config = json.load(json_file)
            return config["autoit_script"]
