# The TeX Configuration Project

## Configuration
- [Where can I put local latex style files and packages?](https://www.ias.edu/math/computing/faq/local-latex-style-files)
- The location of your local texmf can be found by using the command:
    ```bash
    kpsewhich -var-value TEXMFHOME
    ```
- To set the root directory of this project as TEXMFHOME, first go to the root directory of this project, then:
    ```bash
    export TEXMFHOME=${PWD}
    ```
- To check if the setting is succesfull:
    ```bash
    kpsewhich -var-value TEXMFHOME
    ```
  or to see which `QIColor.sty` is used when compiling the tex file:
    ```bash
    kpsewhich QIColor.sty
    ```

## Installing the style files
The following command can be used:
```bash
./config.sh ~/texmf
```