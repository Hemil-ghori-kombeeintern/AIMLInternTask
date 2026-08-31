# DVC + Git Commands

## Step 1: Initialize DVC

```bash
dvc init
```

## Step 2: Add and Track Data

```bash
dvc add data.txt
```

## Step 3: Commit DVC Tracking File to Git

```bash
git add data.txt.dvc .gitignore
git commit -m "Add first version of data"
```

## Step 4: Track a New Version

```bash
dvc add data.txt
git add data.txt.dvc
git commit -m "Add modified version of data"
```

## Step 5: Roll Back to a Previous Data Version

```bash
git checkout <commit_hash>
dvc checkout
```

## Step 6: Configure Remote Storage

```bash
dvc remote add local /path/to/dvc_storage
```

## Step 7: Push Data to Remote

```bash
dvc push -r local
```

## Step 8: Pull Data from Remote

```bash
dvc pull
```

## Step 9: Import Data from Another DVC Project

```bash
dvc import <repository_url> <path_to_data>
```
