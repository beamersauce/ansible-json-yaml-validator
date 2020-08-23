#!/usr/bin/python

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'beamersauce'
}

DOCUMENTATION = '''
---
module: schema_validator

short_description: Validates JSON/YAML file formats

version_added: "2.11"

description:
    - "Tests YAML or JSON files against a JSON schema file to validate. If both json_path and yaml_path are provided, will only validate json_path and will ignore the yaml_path"

options:
    schema_path:
        description:
            - Path of the JSON schema file to validate against (https://json-schema.org/)
        required: true
    json_path:
        description:
            - Path of the JSON file to validate (this or yaml_path must be provided)
        required: false
    yaml_path:
        description:
            - Path of the YAML file to validate (this or json_path must be provided)
        required: false

requirements:
    - jsonschema
    - pyyaml

author:
    - Caleb Burch (@beamersauce)
'''

EXAMPLES = '''
  - name: Test valid JSON
    schema_validator:
      json_path: 'test-valid.json'
      schema_path: "schema.json"

  - name: Test invalid JSON
    schema_validator:
      json_path: 'test-invalid.json'
      schema_path: "schema.json"
    ignore_errors: yes

  - name: Test valid YAML
    schema_validator:
      yaml_path: 'test-valid.yaml'
      schema_path: "schema.json"

  - name: Test invalid YAML
    schema_validator:
      yaml_path: 'test-invalid.yaml'
      schema_path: "schema.json"
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from jsonschema import validate
    import jsonschema
    import json
    import yaml
    HAS_DEPS=True
except:
    HAS_DEPS=False    

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        json_path=dict(type='str', required=False),
        yaml_path=dict(type='str', required=False),
        schema_path=dict(type='str', required=True)
    )

    # seed result object
    result = dict(
        changed=False
    )

    # init args and check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Verify deps exist
    if not HAS_DEPS:
        module.fail_json(msg="'jsonschema' and 'pyyaml' dependencies are required on hosts running this module. Use `pip3 install jsonschema pyyaml`", **result)
    
    with open(module.params['schema_path']) as f_schema:
        schema_data = json.load(f_schema)

    # validate json if path was provided
    if module.params['json_path'] is not None:
        # load in json file
        with open(module.params['json_path']) as f_json:
            data = json.load(f_json)
    elif module.params['yaml_path'] is not None:
       # load in yaml file and convert to json
        with open(module.params['yaml_path']) as f_yaml:
            data = yaml.load(f_yaml)
    else:
        module.fail_json(msg="One of 'json_path' or 'yaml_path' are required", **result)

    # validate the json against schema
    try:
        validate(instance=data, schema=schema_data)
    except jsonschema.exceptions.ValidationError as err:
        module.fail_json(msg="Message: '%s', Error: '%s'" % (err.message, str(err)), **result)

    # success, exit out
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()