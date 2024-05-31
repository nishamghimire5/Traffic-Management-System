# 3d-reconstruction-from-2d-image

## Introduction
## Goals
## Contributors
<table>
<tr>
    <td align="center" width="200">
      <pre><a href="https://github.com/dklkushal07" target="_blank" style = "text-decoration: none;"><img src="https://avatars.githubusercontent.com/u/68638711?v=4" width="200" alt="GitHub Profile of Kushal Dhakal" /><br/><sub>Kushal Dhakal</sub></a></pre>
    </td>
        <td align="center" width="200">
      <pre><a href="https://github.com/nishamghimire5" target="_blank style = "text-decoration: none;""><img src="https://avatars.githubusercontent.com/u/77533996?v=4" width="200" alt="GitHub Profile of Kushal Dhakal" /><br/><sub>Nisham Ghimire</sub></a></pre>
    </td>
        <td align="center" width="200">
      <pre><a href="https://github.com/Shubham-karn" target="_blank" style = "text-decoration: none;"><img src="https://avatars.githubusercontent.com/u/147227439?v=4" width="200" alt="GitHub Profile of Kushal Dhakal" /><br/><sub>Shubham Karn</sub></a></pre>
    </td>
        <td align="center" width="200">
      <pre><a href="https://github.com/dklgarima" target="_blank" style = "text-decoration: none;"><img src="https://avatars.githubusercontent.com/u/66936719?v=4" width="200" alt="GitHub Profile of Kushal Dhakal" /><br/><sub>Garima Dhakal</sub></a></pre>
    </td>
</tr>
</table>
## Project Architecture


# Status
## Known Issue
## High Level Next Steps


# Usage
## Installation
To begin this project, use the included `Makefile`

#### Creating Virtual Environment

This package is built using `python-3.8`. 
We recommend creating a virtual environment and using a matching version to ensure compatibility.

#### pre-commit

`pre-commit` will automatically format and lint your code. You can install using this by using
`make use-pre-commit`. It will take effect on your next `git commit`

#### pip-tools

The method of managing dependencies in this package is using `pip-tools`. To begin, run `make use-pip-tools` to install. 

Then when adding a new package requirement, update the `requirements.in` file with 
the package name. You can include a specific version if desired but it is not necessary. 

To install and use the new dependency you can run `make deps-install` or equivalently `make`

If you have other packages installed in the environment that are no longer needed, you can you `make deps-sync` to ensure that your current development environment matches the `requirements` files. 

## Usage Instructions


# Data Source
## Code Structure
## Artifacts Location

# Results
## Metrics Used
## Evaluation Results