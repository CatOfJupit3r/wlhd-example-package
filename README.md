# Building your own WLHD Package!

This is an template repository for building your own WLHD package. It includes all the necessary information and files to get you started.


## Basics

To create your very own WLHD package, you need to follow these steps:
- create **GITHUB** repository from this template with name following this pattern: `wlhd-<package-name>-package`
- clone the repository to your local machine

It is very important to create on **GITHUB** with the name following the pattern any other links will not be recognized by the game server.

## Structure

The repository is structured in a way that you can easily start building your own package. It includes all the necessary files and directories to get you started.

For details of each directory, on its structure and purpose, see README.md file in corresponding directory.

### Directories

- 'assets' - Contains all the assets for your package. This includes images, sounds, and other files.
- 'data' - Contains JSON preset data for your package. Is not included in game logic, but including your components here ensures that frontend application will recognize and use those presets on combat creation and editing.
- 'functions' - Contains all the custom hooks of your package.
- 'translations' - Contains all the translations for your package.
- 'media' - Contains all the media files for **README.md** file. (purged on import)
- 'components' - Contains Python declarations of presets, which will be used to create game components in combats.

## Importing and Exporting

Take into account, that WLHD repositories will automatically purge all files that don't belong to it.

For example, game coordinator will delete `functions` and `components` directories, as they are not used in the game server.

And game server will delete `assets`, `data` and `translations` directories, as they are not used in the game server.


## Manifest

The manifest file is a JSON file that contains all the necessary information about your package. 
It includes the name, version, description, and other information about your package.

If your package does not have a manifest file, it will not be imported into the game server (or deleted if cloned beforehand).

### Example (manifest)

```json
{
    "title": "Example package",
    "description": "Example of possible package, supported by WLHD game servers.",
    "descriptor": "example",
    "author": "CatOfJupit3r",
    "version": "0.0.1",
    "source": "https://github.com/CatOfJupit3r/wlhd-example-package"
}
```

### Fields

- `name` - The name of your package.
- `descriptor` - The descriptor of the package. Very important, as it is used to identify the package in code. (should be unique)
- `version` - The version of your package. (will tell you a little secret, it is not used anywhere, but it is good to have it)
- `description` - A short description of your package.
- `author` - The author of the package.
- `source` - The source of the package. Should always be a GitHub repository. (This will be checked with regex, so be careful with it)
- `dependencies` - An array of dependencies that your package requires. (not implemented yet)


## Troubleshooting

If you have any problems with building your package, then I'm not reading allat 🙏.

<p align="center">
  <img src="media/literally_me.PNG" alt="literally_me" title="How I feel writing this shitpost" />
</p>

[Image credit](https://twitter.com/Juanfe_507/status/1712696420283584871)