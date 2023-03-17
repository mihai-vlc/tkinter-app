$buildFolder = '_dist'

# generate spec file
if (-not (Test-Path -Path $buildFolder)) {
    mkdir -p $buildFolder
    pushd $buildFolder
    python -m PyInstaller --onefile --windowed --log-level ERROR --name myapp ../main.py
    popd
}

pushd $buildFolder
python -m PyInstaller --log-level ERROR myapp.spec 
popd
