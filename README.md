Create a Repositatory
-> Go TO Anaconda Promt /-> THEN TYPE  CD  /->D:/"projectname"  /->D: it will direct to Specific folder  /->Type code .  /-> VS opens

VisualStudio-> New Terminal -> New environment  
conda create -p name(venv)"environment" python==3.10 -y 

conda activate venv/ -> it will activate the environment

pip install -r requirements.txt
pip install -e 

python -m mlproject.pipeline.predict_pipeline ---> RUN a python file
python -m mlproject.utils
python -m mlproject.pipeline.training_pipeline

This tells Python:  ---->> “Treat mlproject as a package”




==============GIT COMMANDS=========================
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com

Commit cleanly to GitHub
git add .
git commit -m "Project setup with src layout and packaging"
git push

…or create a new repository on the command line
echo "# Jupiter" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/chapalamanojreddy-glitch/MachineLearning.git
git push -u origin main

==========⚠️ Never use LFS for venv or logs==========

🧠 ML Industry Rules (Remember forever)

❌ Never push	✅ Push instead
venv/			requirements.txt
logs/			logging config
models			download script
raw data		data pipeline




.000.00.





