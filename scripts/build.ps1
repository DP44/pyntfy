# Build the project wheels.
# NOTE: I specified the -n flag because virtualenv was freaking out preventing me from building.
py -m build -n

# Publish wheels to pypi
py -m twine upload --repository pypi dist/*