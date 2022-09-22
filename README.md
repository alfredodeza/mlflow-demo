# Example MLFlow Projects

This repository is part of the MLOps Coursera Course with practical examples to apply different MLFlow techniques for understanding the components of MLFlow better.


## Create an MLFlow Project

Find more about what it takes to create an MLFlow project with Conda, a packaging solution that can work with Python as well as other system dependencies.

For this project, we'll use a small CSV file with data about wines, called [wine-ratings.csv](wine-ratings.csv).

### Step 1: Start with the dependencies

Before going into the details of the project, you probably have a good idea of what you need to install. I recommend setting up a Conda environment first. Even if you prefer using `pip` for installing dependencies, you can still define that with a Conda environment.

This early in the project's lifecycle you are probably not ready to do some training, so let's only concentrate in exploratory work for the dataset.

```
conda create --name exploratory python=3.8
```

Once the environment is created, activate it so that packages are installed in that activated environment.

```
conda activate exploratory
```

Next, with the _exploratory_ environment activated export the dependencies so a new YAML file named _conda_env.yml_

```
conda env export --name exploratory > conda_env.yml
```

You should end up with a file similar to this:

```yaml
name: exploratory
channels:
  - conda-forge
dependencies:
  - bzip2=1.0.8
  - ca-certificates
  - libffi=3.4.2
  - libsqlite=3.39.3
  - libzlib=1.2.12
  - ncurses=6.3
  - openssl=3.0.5
  - python=3.8.13
  - readline=8.1.2
  - setuptools=65.3.0
  - sqlite=3.39.3
  - tk=8.6.12
  - wheel=0.37.1
  - xz=5.2.6
  - pip
```

Next, append a few lines to use `pip` to install `mlflow` and `pandas`. This is not a hard requirement, but it is useful to know that you can use the conda environment file to add more dependencies using `pip` and not `conda`. The newly appended lines should look like this:

```yaml
  - pip:
    - pandas==1.5.0
    - mlflow==1.29.0
```

The full file should look exactly like [exploratory/conda_env.yml](./exploratory/conda_env.yml)

Since you added the `pip` installs directly to the file, you didn't really install them, so go ahead and run the following command to ensure everything is working:

```
 conda env update --file conda_env.yml --prune
```

The command will look into any new (or different) dependencies and install them. The `--prune` flag will remove anything that is no longer defined in the _conda_env.yml_ file. In this case, you didn't remove anything, but it is still a good idea to keep using it.
