if (Test-Path -Path dist) {
    Remove-Item -Path dist -Recurse
}

Write-Host "Building project wheels..." -ForegroundColor Magenta
# NOTE: The -n flag is here because virtualenv was freaking out preventing me from building.
py -m build -n