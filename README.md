# ansible-json-yaml-validator
Ansible module for validating json or yaml files by comparing to a jsonschema file (https://json-schema.org/)

## To use

1. Copy `schema_validator.py` into your ansible module directory (typically this is something like ~/.ansible/plugins/modules/)
2. Make sure you have the dependencies installed on the host machine that will be running this module
    1. `pip3 install jsonschema`
    2. `pip3 install pyyaml` 
3. Verify setup is correct: `ansible-doc schema_validator`

### Playbook examples:

Run the included sample playbook via: `ansible-playbook -v example/test-playbook.yaml -e 'ansible_python_interpreter=/usr/bin/python3'`

```
- name: Test the schema_validator module
  hosts: localhost
  tasks:

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
    ignore_errors: yes

  - name: Test not providing JSON or YAML path
    schema_validator:
      schema_path: "schema.json"
    ignore_errors: yes
```
