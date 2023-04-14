## References

- https://tkdocs.com/
- API reference: https://tkdocs.com/pyref/index.html
- https://pillow.readthedocs.io/en/stable/reference/ImageTk.html

## Build notes

In the spec file add

```
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          Tree("../resources/", prefix="resources"),
```

Reference: https://stackoverflow.com/questions/20602727/pyinstaller-generate-exe-file-folder-in-onefile-mode/20677118#20677118

https://github.com/RobertJN64/TKinterModernThemes
