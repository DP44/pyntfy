Write-Host "Uploading wheels to PyPI..." -ForegroundColor Magenta
py -m twine upload -r pypi dist/*
