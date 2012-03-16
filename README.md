# Boilerplate Source Code

Templates for boilerplate code in various languages.

For instance, `html/html5...` contains your usual html/head/body song and dance.

## Style

Please keep it restrained. The rules are:

* Fields ( {{foo}} and the like) should not be used if they are only referenced once. Use a triple underscore instead `___` (a triple underscore can be double clicked, and does not require any UI).
* If it's possible to define the template without defining *any* fields, err on the side of that. We don't want to pop up a wizard UI unless we absolutely have to since 1 click is better than 3.
* Users are perfectly capable of typing things, they're just lazy. If something in your template will cost the user more time than it saves them, don't include it!

Files should end with a newline.

## Default Variables

* **filename**: the name of the file, excluding the extension.
* **FILENAME**: the name of the file IN UPPERCASE, excluding the extension.

## License

All code is made available under the [WTFPL](http://sam.zoy.org/wtfpl/). By contributing any code (e.g. via a pull request) you agree to perpetually license your code under that license. Though since this is all boilerplate code used in thousands of files already, not much of it is copyrightable.
