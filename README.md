# Inventory Management System

## Overview

This Inventory Management System allows product managers to manage products and customers to purchase items. The system is built using Python and SQLite for the database, and it is designed to be run on a server accessed via Putty. 

## Features

- Product management (add, update, delete, view)
- Customer purchasing capabilities
- Sales tracking
- Version control using Git and GitHub

## Prerequisites

- Python 3.x installed on your server
- SQLite3 installed
- Git installed on your server
- PuTTY for SSH access (if accessing a remote server)

## Setup Instructions

### Step 1: Clone the Repository

1. Open your terminal or Putty.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command:
```
git clone git@github.com:username/repo.git
```
Replace `username` with your GitHub username and `repo` with your repository name.

### Step 2: Navigate to the Project Directory

Change into the project directory:
```
cd  repo
```

### Step 3: Create the Database

1. Run the `databasemanagement.py` script to create the database and necessary tables:
```
python databasemanagement.py
```

### Step 4: Run the Application

To start the inventory management application, execute:
```
python app.py
```

### Step 5: Using the Application

1. **User Roles**:
   - **Manager**: Can add, update, delete, and view products.
   - **Customer**: Can search for products, view available products, and make purchases.

2. **Commands**:
   - When prompted, enter `manager` or `customer` based on your role.
   - Follow on-screen instructions for performing actions like adding products or making purchases.

## Version Control with Git

### Initializing Git Repository

1. **Navigate to Your Project Directory**:
```
cd /path/to/your/project
```

2. **Initialize Git**:
```
git init
```

3. **Add Remote Repository**:
```
git remote add origin git@github.com:username/repo.git
```

### Committing Changes

1. **Check Status**:
```
git status
```

2. **Stage Changes**:
```
git add .
```

3. **Commit Changes**:
```
git commit -m "Your commit message"
```
4. **Push Changes to GitHub**:
```
git push origin main
```


### Automating Updates (Optional)

You can create a shell script (`update_repo.sh`) to automate staging, committing, and pushing changes:

```
#!/bin/bash
```

**Navigate to project directory**
```
cd /path/to/your/project
```

**Stage all changes**
```
git add .
```

**Commit changes with a timestamp message**
```
git commit -m "Automated commit on $(date +'%Y-%m-%d %H:%M:%S')"
```

**Push changes to GitHub**
```
git push origin main
```

1. *Make it executable:*
```
chmod +x update_repo.sh
```

2. *Run it whenever you want to update your repository:*
```
./update_repo.sh
```


## Conclusion

This Inventory Management System provides a simple yet effective way for managing products and sales. By following these instructions, you can set up the system on your server and use version control with Git and GitHub for efficient code management.

For any issues or questions, please refer to the documentation or contact me or the support .
