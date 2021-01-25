# ansible-json-yaml-validator
Ansible module for validating json or yaml files by comparing to a jsonschema file (https://json-schema.org/)

## To use

1. Copy `schema_validator.py` into your ansible module directory (typically this is something like ~/.ansible/plugins/modules/)
2. Make sure you have the dependencies installed on the host machine that will be running this module: `pip3 install jsonschema pyyaml`
3. Verify setup is correct: `ansible-doc schema_validator`

> :warning: Ansible typically installs it's own python interpreter so be certain you have installed the pip dependencies on the same interpreter that Ansible is using (you can see which interpreter ansible is using via `ansible --version` or by forcing it to use one of your choosing by passing `-e 'ansible_python_interpreter=/usr/local/bin/python3'` )

### Playbook examples:

Run the included sample playbook via: `ansible-playbook -v example/test-playbook.yaml -e 'ansible_python_interpreter=/usr/local/bin/python3'`

Use in your own playbook:

```
  - name: Test valid YAML
    schema_validator:
      yaml_path: 'test-valid.yaml'
      schema_path: "schema.json"
```

### Parameters

| Parameter | Type | Required | Description |
|---|---|---|---|
| schema_path | string (file path) | yes | Path to JSON Schema file - used to validate the JSON or YAML file |
| json_path | string (file path) | no* | Path to JSON file to validate |
| yaml_path | string (file path) | no* | Path to YAML file to validate |

\* one of `json_path` or `yaml_path` must exist -- you need something to validate!

## Under the covers

This module uses jsonschema to validate the given file against the given schema (https://python-jsonschema.readthedocs.io/en/stable/).  If you supply a YAML file - then PyYaml is used to read in the contents which are converted to json and then validated against.