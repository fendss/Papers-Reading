#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简化版的论文更新脚本
直接运行，无需参数
"""

import os
import sys
import subprocess

def check_python_version():
    """检查Python版本"""
    if sys.version_info < (3, 6):
        print("❌ 需要Python 3.6或更高版本")
        return False
    return True

def install_requirements():
    """检查并安装必要的包"""
    try:
        import pathlib
        return True
    except ImportError:
        print("❌ 缺少必要模块")
        return False

def run_update():
    """运行更新"""
    print("🚀 论文网站自动更新工具")
    print("=" * 40)
    
    if not check_python_version():
        return
    
    if not install_requirements():
        return
    
    # 获取当前目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    update_script = os.path.join(current_dir, "update_papers.py")
    
    if not os.path.exists(update_script):
        print(f"❌ 找不到文件: {update_script}")
        return
    
    try:
        # 运行主脚本
        subprocess.run([sys.executable, update_script], cwd=current_dir)
    except KeyboardInterrupt:
        print("\n⏹️  用户取消操作")
    except Exception as e:
        print(f"❌ 运行失败: {e}")

if __name__ == "__main__":
    run_update()