#! /usr/bin/env bash

# Check if a project name argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <project_name>"
    exit 1
fi

# Extract the project name from the argument and replace spaces with underscores
project_name="${1// /_}"

# Create the main project directory
mkdir -vp "$project_name"

# Function to create a README.md file in a directory
create_readme() {
    local dir="$1"
    echo "# $dir" > "$dir/README.md"
    echo "This directory contains files related to $dir." >> "$dir/README.md"
    echo "You can add your own content to this README." >> "$dir/README.md"
}

# folder for project requirements and configs
## python reuirements file
mkdir -vp "$project_name/config"
create_readme "$project_name/config"
touch "$project_name/config/requirements.txt"
touch "$project_name/config/pyproject.toml"
touch "$project_name/config/Dockerfile"


# Create data directory and subdirectories
mkdir -vp "$project_name/data/raw_data"
create_readme "$project_name/data/raw_data"
mkdir -vp "$project_name/data/processed_data"
create_readme "$project_name/data/processed_data"
mkdir -vp "$project_name/data/processed_data/logs"
create_readme "$project_name/data/processed_data/logs"
mkdir -vp "$project_name/data/annotations"
create_readme "$project_name/data/annotations"

# Uncomment these lines to create module-related directories and files
#mkdir -vp "$project_name/modules/module1/tests"
#create_readme "$project_name/modules/module1/tests"
# mkdir -vp "$project_name/modules/module2/tests"
# create_readme "$project_name/modules/module2/tests"

# Create scripts directory and subdirectories
mkdir -vp "$project_name/scripts/preprocessing"
create_readme "$project_name/scripts/preprocessing"
mkdir -vp "$project_name/scripts/analysis"
create_readme "$project_name/scripts/analysis"
mkdir -vp "$project_name/scripts/visualization"
create_readme "$project_name/scripts/visualization"
mkdir -vp "$project_name/scripts/workflows"
create_readme "$project_name/scripts/workflows"

# Create tests directory and subdirectories
mkdir -vp "$project_name/tests/test_preprocessing"
create_readme "$project_name/tests/test_preprocessing"
mkdir -vp "$project_name/tests/test_analysis"
create_readme "$project_name/tests/test_analysis"
mkdir -vp "$project_name/tests/test_visualization"
create_readme "$project_name/tests/test_visualization"

# Create results directory and subdirectories
mkdir -vp "$project_name/results/figures"
create_readme "$project_name/results/figures"
mkdir -vp "$project_name/results/tables"
create_readme "$project_name/results/tables"
mkdir -vp "$project_name/results/reports"
create_readme "$project_name/results/reports"
mkdir -vp "$project_name/results/reports/logs"
create_readme "$project_name/results/reports/logs"


# Create documentation directory and subdirectories
mkdir -vp "$project_name/documentation/docs"
create_readme "$project_name/documentation/docs"

# Create README and other documentation files
touch "$project_name/documentation/README.md"
echo "# $project_name" > "$project_name/documentation/README.md"
echo "This is the main README for the project." >> "$project_name/documentation/README.md"
echo "You can add an overview of your project here." >> "$project_name/documentation/README.md"
echo "Please refer to individual directory README files for details." >> "$project_name/documentation/README.md"
echo "Created file: $project_name/documentation/README.md"

touch "$project_name/documentation/requirements_prj.txt"
echo "This is where you can specify project requirements." >> "$project_name/documentation/requirements_prj.txt"
echo "Created file: $project_name/documentation/requirements_prj.txt"

touch "$project_name/documentation/notes.txt"
echo "You can keep project-related notes and ideas here." >> "$project_name/documentation/notes.txt"
echo "Created file: $project_name/documentation/notes.txt"

touch "$project_name/documentation/changelog.txt"
echo "You can record changes made to the project in this file." >> "$project_name/documentation/changelog.txt"
echo "Created file: $project_name/documentation/changelog.txt"

# Print a message to indicate completion
echo "Project directory structure for '$project_name' created successfully."


# # Create empty __init__.py files for modules (if you're using Python)
# ouch "$project_name/modules/module1/__init__.py"
# echo "Created file: $project_name/modules/module1/__init__.py"
# touch "$project_name/modules/module2/__init__.py"
# echo "Created file: $project_name/modules/module2/__init__.py"

# # Create example code and test files (you can replace these with your actual files)
# touch "$project_name/modules/module1/module1_code.py"
# echo "Created file: $project_name/modules/module1/module1_code.py"
# touch "$project_name/modules/module1/tests/test_module1.py"
# echo "Created file: $project_name/modules/module1/tests/test_module1.py"
# touch "$project_name/modules/module2/module2_code.py"
# echo "Created file: $project_name/modules/module2/module2_code.py"
# touch "$project_name/modules/module2/tests/test_module2.py"
# echo "Created file: $project_name/modules/module2/tests/test_module2.py"

