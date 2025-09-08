## Using pip.conf for Internal Package Indexes

If you need to use a private or internal Python package index (for example, a company-internal PyPI mirror), you can configure pip to use it by providing a `pip.conf` file. A template is provided as `pip.conf-template` in this repository.

1. Copy the template to your project root or your home directory:
    ```bash
    cp pip.conf-template pip.conf
    # or to your user config
    cp pip.conf-template ~/.config/pip/pip.conf
    ```
2. Edit the file and set your internal index URL, credentials, and any extra index URLs as needed. Example:
    ```ini
    [global]
    index-url = https://your-internal-pypi/simple
    extra-index-url = https://pypi.org/simple
    trusted-host = your-internal-pypi
    ```
3. Now, all pip/uv install commands will use your internal index automatically.