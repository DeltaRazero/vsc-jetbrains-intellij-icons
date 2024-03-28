
# vsc-jetbrains-intellij-icons

<!-- BADGES -->
<div align="left">
    <!--
        Library tag version
    --->
    <a href="https://github.com/deltarazero/vsc-jetbrains-intellij-icons/tags">
        <img src="https://img.shields.io/github/v/tag/deltarazero/vsc-jetbrains-intellij-icons?labelColor=363d45&logo=github&logoColor=white"
        alt="Latest release tag version"/></a>
    <!--
        License
    --->
    <a href="https://choosealicense.com/licenses/apache-2.0/">
        <img src="https://img.shields.io/github/license/DeltaRazero/vsc-jetbrains-intellij-icons?labelColor=363d45&color=informational"
        alt="Apache License 2.0"/></a>
</div>

JetBrains IntelliJ file/product icon themes for Visual Studio Code.

> [!NOTE]
> The theme is currently not yet finished; some icons are missing.
> If you'd like to try it out, you'll have to build it yourself at the moment.


## Generating VSIX

Since the theme is not finished, it's not published yet on the VSCode extension marketplace. You'll have to install the extension by using a VSIX package.

There currently is not a way yet to only run container image as a standalone means to generate the VSIX package. You'll have to use the following procedure:

* Build container image.
* Run image (e.g. `podman-compose up -d`) and SSH into the running container.
* Run `/usr/src/myapp/bin/make_dist.py` to start the icon theme build process, or alternatively run with `--validate-only` to check if the icon definitions are valid.
* Resulting VSIX file will be in `/dist`.


## License

© DeltaRazero. All rights reserved. <br/>
© JetBrains s.r.o. and contributors for all branding icons, and icons used as base for custom icons.

All included files, scripts, modules, etc. are licensed under the terms of the  [Apache License 2.0](https://github.com/deltarazero/vsc-jetbrains-intellij-icons/LICENSE), unless stated otherwise in the respective files.
