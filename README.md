# ansible-json-yaml-validator
Ansible module for validating json or yaml files by comparing to a jsonschema file (https://json-schema.org/)

## To use

1. Copy `schema_validator.py` into your ansible module directory (typically this is something like ~/.ansible/plugins/modules/)
2. Make sure you have the dependencies installed on the host machine that will be running this module: `pip3 isntall jsonschema pyyaml`
3. Verify setup is correct: `ansible-doc schema_validator`

### Playbook examples:

Run the included sample playbook via: `ansible-playbook -v example/test-playbook.yaml -e 'ansible_python_interpreter=/usr/bin/python3'`

Use in your own playbook:

```
  - name: Test valid YAML
    schema_validator:
      yaml_path: 'test-valid.yaml'
      schema_path: "schema.json"
```