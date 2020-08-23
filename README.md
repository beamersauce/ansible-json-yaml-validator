# ansible-json-yaml-validator
Ansible module for validating json or yaml files by comparing to a jsonschema file (https://json-schema.org/)

## To use

1. Copy `schema_validator.py` into your ansible module directory (typically this is something like ~/.ansible/plugins/modules/)
2. Make sure you have the dependencies installed on the host machine that will be running this module
    1. `pip3 install jsonschema`
    2. `pip3 install pyyaml` 
3. Verify setup is correct: `ansible-doc schema_validator`

### Playbook examples:

```
- name: Test the schema_validator module
  hosts: localhost
  tasks:

  - name: Test valid JSON
    schema_validator:
      json_path: 'example/test-valid.json'
      schema_path: "example/schema.json"

  - name: Test invalid JSON
    schema_validator:
      json_path: 'example/test-invalid.json'
      schema_path: "example/schema.json"
    ignore_errors: yes

  - name: Test valid YAML
    schema_validator:
      yaml_path: 'example/test-valid.yaml'
      schema_path: "example/schema.json"

  - name: Test invalid YAML
    schema_validator:
      yaml_path: 'example/test-invalid.yaml'
      schema_path: "example/schema.json"
    ignore_errors: yes

  - name: Test not providing JSON or YAML path
    schema_validator:
      schema_path: "example/schema.json"
    ignore_errors: yes
```
