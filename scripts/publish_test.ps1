Write-Host "Uploading wheels to TestPyPI..." -ForegroundColor Magenta
py -m twine upload -p $ENV:TWINE_TEST_PASSWORD -r testpypi dist/*
