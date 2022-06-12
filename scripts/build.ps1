function Get-BuiltWheel {
    Get-ChildItem -Path dist -Filter *.whl | Foreach-Object {
        return $_.FullName
    }
}


if (Test-Path -Path dist) {
    Write-Host "Removing previous builds from the dist/ directory..." -ForegroundColor Magenta
    Remove-Item -Path dist -Recurse
}

Write-Host "Building project wheels..." -ForegroundColor Magenta

# NOTE: The -n flag is here because virtualenv was freaking out preventing me from building.
py -m build -n

Write-Host "Removing previous build from packages..." -ForegroundColor Magenta
py -m pip uninstall pyntfy

Write-Host "Installing built package..." -ForegroundColor Magenta

$whl_file = Get-BuiltWheel
py -m pip install $whl_file