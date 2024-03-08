# configuration.py

import ujson
from logger import logger

class Config:
    def __init__(self):
        self.config = {}
        self.log = logger("config", 1, True)
        # Load the existing configuration from a JSON file (if available)
        try:
            with open("config.json", "r") as config_file:
                saved_config = ujson.load(config_file)
                self.config.update(saved_config)
                self.log.debug('loaded config from filesystem!')
        except OSError:
            self.log.error('Could not load config!')
        
    def generate_form_elements(self, parent_key=""):
        self.log.debug('generate_form_elements')
        data = self.config
        form_elements = ""
        for key, value in data.items():
            field_type = value.get("type", "text")
            field_value = value.get("value", "")

            # Create HTML input element based on field type
            input_element = f'<input type="{field_type}" name="{parent_key}.{key}" value="{field_value}"><br>'

            form_elements += input_element

        return form_elements #html_form = f'<form method="POST" action="/">\n{generate_form_elements(config)}<input type="submit" value="Save"></form>'

    def getInputsForKey(self, obj, key): # {'value': 'ThisIsOnlyAnExample', 'type': 'text'}, userAgent
        print(obj)
        if "type" in obj: # it's a parameter
            self.log.debug(f'build input for config value: {key}')
            input_type = obj["type"]
            input_value = obj["value"]
            return f'''
            <div class="col-sm-6">
            <label class="control-label col-sm-2" for='{key}'>{key}:</label><br>
            <input type='{input_type}' id='{key}' name='{key}' value='{input_value}'><br>
            '''
        else: # its an object
            inputList = ""
            for subkey in obj:
               print(subkey)
               inputList += self.getInputsForKey(obj[subkey], subkey)
            return inputList 

    def getHTMLFormForConfig(self):
        # open config template
        new_file = open('config.html', 'r')
        form_html = new_file.read()
        new_file.close()

        # replace placeholder with generated inputs
        inputs = ""
        for area in self.config:
            inputs += '<div class="form-group">'
            for key in self.config[area]:
                inputs += self.getInputsForKey(self.config[area], key)
            inputs += '</div>'
        
        form_html.replace('@@inputs@@', inputs)
        return form_html
                    
    def getValue(self, key): 
        tempConf = self.config
        keyChain = key.split(".")
        for key in keyChain:
            if key in tempConf:
                tempConf = tempConf[key]
            else:
                self.log.warning(f"{key} is not present in config.json")
                return None
                
        return tempConf["value"]

    def setValue(self, key, value):
        if key in self.config:
            self.config[key]["value"] = value
            __save_config()

    def __save_config(self):
        with open("config.json", "w") as config_file:
            ujson.dump(self.config, config_file)
