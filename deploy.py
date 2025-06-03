import os
import shutil
import subprocess
from pathlib import Path

def run_command(command):
    """运行命令并打印输出"""
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True
    )
    output, error = process.communicate()
    
    if output:
        print(output.decode())
    if error:
        print(error.decode())
    
    return process.returncode

def deploy():
    """部署到 GitHub Pages"""
    print("🚀 开始部署...")
    
    # 1. 构建静态文件
    print("📦 构建静态文件...")
    if run_command("npm run docs:build") != 0:
        print("❌ 构建失败")
        return
    
    # 2. 进入构建目录
    dist_path = Path("docs/.vuepress/dist")
    os.chdir(dist_path)
    
    # 3. 初始化 git 并提交
    print("📝 准备提交文件...")
    commands = [
        "git init",
        "git add -A",
        'git commit -m "deploy"',
        "git push -f git@github.com:Vivaldi4Git/tech-beacon.git master:gh-pages"
    ]
    
    for cmd in commands:
        if run_command(cmd) != 0:
            print(f"❌ 命令失败: {cmd}")
            return
    
    # 4. 返回原目录
    os.chdir("../../..")
    print("✅ 部署完成！")
    print("🌐 网站将在几分钟后在 https://Vivaldi4Git.github.io/vuepress 可访问")

if __name__ == "__main__":
    deploy()