import os

def create_project_directory(project_name):
    # 创建项目目录
    os.makedirs(project_name, exist_ok=True)
    
    # 在项目目录中创建 main.py 文件
    with open(f"{project_name}/main.py", "w") as f:
        pass
    
    # 在项目目录中创建 requirements.txt 文件
    with open(f"{project_name}/requirements.txt", "w") as f:
        pass
    
    # 在项目目录中创建 .env 文件
    with open(f"{project_name}/.env", "w") as f:
        pass
    
    # 在项目目录中创建 app 目录
    os.makedirs(f"{project_name}/app", exist_ok=True)
    
    # 在 app 目录中创建 __init__.py 文件
    with open(f"{project_name}/app/__init__.py", "w") as f:
        pass
    
    # 在 app 目录中创建 router.py 文件
    with open(f"{project_name}/app/router.py", "w") as f:
        pass
    
    # 在 app 目录中创建 models.py 文件
    with open(f"{project_name}/app/models.py", "w") as f:
        pass
    
    # 在 app 目录中创建 api 目录
    os.makedirs(f"{project_name}/app/api", exist_ok=True)
    
    # 在 api 目录中创建 __init__.py 文件
    with open(f"{project_name}/app/api/__init__.py", "w") as f:
        pass
    
    # 在 api 目录中创建 api_v1.py 文件
    with open(f"{project_name}/app/api/api_v1.py", "w") as f:
        pass
    
    # 在 app 目录中创建 database 目录
    os.makedirs(f"{project_name}/app/database", exist_ok=True)
    
    # 在 database 目录中创建 __init__.py 文件
    with open(f"{project_name}/app/database/__init__.py", "w") as f:
        pass
    
    # 在 database 目录中创建 database.py 文件
    with open(f"{project_name}/app/database/database.py", "w") as f:
        pass
    
    # 在 app 目录中创建 services 目录
    os.makedirs(f"{project_name}/app/services", exist_ok=True)
    
    # 在 services 目录中创建 __init__.py 文件
    with open(f"{project_name}/app/services/__init__.py", "w") as f:
        pass
    
    # 在 services 目录中创建 example_service.py 文件
    with open(f"{project_name}/app/services/example_service.py", "w") as f:
        pass
    
    # 在 app 目录中创建 utils 目录
    os.makedirs(f"{project_name}/app/utils", exist_ok=True)
    
    # 在 utils 目录中创建 __init__.py 文件
    with open(f"{project_name}/app/utils/__init__.py", "w") as f:
        pass
    
    # 在 utils 目录中创建 example_util.py 文件
    with open(f"{project_name}/app/utils/example_util.py", "w") as f:
        pass
    
    # 在项目目录中创建 tests 目录
    os.makedirs(f"{project_name}/tests", exist_ok=True)
    
    # 在 tests 目录中创建 test_example.py 文件
    with open(f"{project_name}/tests/test_example.py", "w") as f:
        pass

# 示例调用
create_project_directory("my_project")