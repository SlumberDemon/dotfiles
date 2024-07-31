# Create location

mkdir $1
cd $1

# Add requirements file

touch requirements.txt

# Create venv

python3 -m venv .venv

echo "{
  \"venvPath\": \".\",
  \"venv\": \".venv\"
}" > pyrightconfig.json
