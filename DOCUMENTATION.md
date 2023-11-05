# Ansible Content Management Script

This script is designed to document Ansible roles and collections within a YAML file, `content.yml`, which can be subsequently used to generate an overview of available Ansible content in markdown format. It facilitates the addition of new roles and collections, and allows for the inclusion of CI badges and status updates.

## Script Usage

The script can be operated in both interactive and command-line argument modes.

### Interactive Mode

To enter interactive mode, simply run the script without any arguments:

```bash
./script_name.py
```

You will be presented with a menu to choose from various options such as adding a new role, a new collection, or adding a role to an existing collection.

### Command-Line Arguments

The script accepts several command-line arguments to perform operations directly.

#### Adding a Role

To add a new role:

```bash
./script_name.py --add-role <role_name> [--ci <true|false>] [--status <status_code_or_custom_status>]
```

- `--add-role`: Specifies the name of the role to be added.
- `--ci`: Optional. Indicates whether the role has CI (Continuous Integration). Accepts `true` or `false`.
- `--status`: Optional. Specifies the status of the role. Accepts `1` (Maintained), `2` (Unmaintained), `3` (Deprecated), or a custom status string.

#### Adding a Collection

To add a new collection:

```bash
./script_name.py --add-collection <collection_name> [--status <status_code_or_custom_status>]
```

- `--add-collection`: Specifies the name of the collection to be added.
- `--status`: Optional. Specifies the status of the collection. Accepts `1` (Maintained), `2` (Unmaintained), `3` (Deprecated), or a custom status string.

#### Adding a Role to a Collection

To add a new role to an existing collection:

```bash
./script_name.py --add-role <role_name> --to-collection <collection_name> [--ci <true|false>] [--status <status_code_or_custom_status>]
```

- `--add-role`: Specifies the name of the role to be added to a collection.
- `--to-collection`: Specifies the name of the collection to which the role should be added.
- `--ci`: Optional. Indicates whether the role has CI. Accepts `true` or `false`.
- `--status`: Optional. Specifies the status of the role within the collection.

#### Sorting Content

To sort the collections and roles alphabetically:

```bash
./script_name.py --sort-content
```

## Status Codes

The script defines three status codes:

- `1`: Maintained
- `2`: Unmaintained
- `3`: Deprecated

A custom status can also be provided as a string.

## Output File

The `content.yml` file is updated with the new roles and collections after each operation. Ensure that you have write permissions to the file before running the script.

## Defaults in `content.yml`

The `defaults` section of the `content.yml` file provides template values that are used throughout the Ansible content overview. These values set common properties for roles and collections to ensure consistency and reduce redundancy. Here's an explanation of each default:

- `author`: The default author name, used in various URLs and names.
- `collection_galaxy_url`: The URL template for the collection's page on Ansible Galaxy, utilizing the author and collection's name.
- `collection_git_url`: The repository URL template for the collection on GitHub.
- `collection_repo_name`: The naming convention for collection repositories, combining the author's name and the collection's name.
- `collection_role_ci_badge_url`: The URL template for the Continuous Integration (CI) badge for roles within a collection.
- `collection_role_ci_url`: The URL template for the CI workflows for roles within a collection.
- `role_ci_badge_url`: The URL template for the CI badge for standalone roles.
- `role_ci_url`: The URL template for the CI workflows for standalone roles.
- `role_galaxy_url`: The URL template for the role's page on Ansible Galaxy.
- `role_git_url`: The repository URL template for the role on GitHub.
- `role_repo_name`: The naming convention for role repositories, indicating it's an Ansible role followed by the role's name.

These templates use placeholders enclosed in curly braces `{}`. When adding new roles or collections, the script replaces these placeholders with actual values based on the input provided. For example, `{author}` will be replaced with the value of `author` defined in `defaults`.

Here's an example of how the defaults are used when adding a new role:

```yaml
roles:
  - name: nginx
    gh_url: https://github.com/diademiemi/ansible_role_nginx
    galaxy_url: https://galaxy.ansible.com/diademiemi/nginx
    ci_badge: https://github.com/diademiemi/ansible_role_nginx/actions/workflows/molecule.yml/badge.svg
    ci_url: https://github.com/diademiemi/ansible_role_nginx/actions/workflows/molecule.yml
    status: "Maintained"
```

In this example, `ansible_role_{name}` in `role_repo_name` is replaced with `ansible_role_nginx`, using `nginx` as the role's name. The script automates these replacements, ensuring that users don't have to manually edit these URLs for each role or collection.

Always verify that the `defaults` are accurate and up-to-date to reflect the current repository and CI configurations.

For more details on the defaults and how to override them, please visit the [GitHub repository](https://github.com/diademiemi/ansible-content-management).

## Dependencies

- Python 3.x
- PyYAML library (usually installed via `pip install pyyaml`)

Ensure these are installed and available in your environment to run the script successfully.

For more details on usage and contributions, please visit the [GitHub repository](https://github.com/diademiemi/ansible-content-management).
