# Translations!

This directory contains translations of the main README.md file. If you would like to contribute a translation, please follow the instructions below.

## Structure

```
- lang_code/
  - *.json
```

## Usage

To use a translation, you can use i18n library and load the translation file.

If you don't want to use the library (or can't), you will need to write your own code to load the translation file and use it.

However, the translation string should follow i18n format, so it can be easily replaced with the library in the future.

### Example (i18n string)

```javascript
const translatableString = 'Hello, {{name}}!';

console.log(translate(translatableString, { name: 'John' }));
// Output: Hello, John!
```


## Creating a new translation

To add a new translation, create a new directory with the language code (e.g. `en_US`, `pl_PL`, `uk_UA`, etc.) and add a JSON file with the translation. The JSON file should contain the following structure:

```json
{
    "title": "Title of the project",
    "description": "Description of the project",
    "prerequisites": "Prerequisites for the project",
    "installation": "Installation instructions",
    "environment_variables": "Environment variables",
    "usage": "Usage instructions",
    "tree": {
        "name": "Name of the tree",
        "description": "Description of the tree",
        "nodes": [
            {
                "name": "Name of the node",
                "description": "Description of the node",
                "children": [
                    {
                        "name": "Name of the child node",
                        "description": "Description of the child node",
                        "children": []
                    }
                ]
            }
        ]
    }
}

```

