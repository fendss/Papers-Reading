#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
论文网站自动更新脚本
作者: AI Assistant
功能: 自动重命名PDF文件、更新网站索引、同步到GitHub
使用方法: python update_papers.py
"""

import os
import re
import subprocess
import sys
from pathlib import Path
from datetime import datetime

class PaperUpdater:
    def __init__(self):
        self.root_path = Path(__file__).parent.absolute()
        self.categories = {
            'AutoML': 'AutoML',
            'AI4Science': 'AI4Science', 
            'LLM4CO': 'LLM4CO',
            'Security': 'Security',
            'Surveys': 'Surveys',
            'benchmark': 'benchmark',
            'embodied': 'embodied'
        }
        
    def convert_to_title_case(self, filename):
        """将文件名转换为This Kind Of Style格式"""
        name = filename.replace('.pdf', '')
        name = name.replace('_', ' ').replace('-', ' ')
        name = name.lower()
        
        # 特殊词汇处理
        special_words = {
            'auto': 'Auto', 'ml': 'ML', 'ai': 'AI', 
            'pdf': 'PDF', 'llm': 'LLM', 'pinn': 'PINN',
            'soh': 'SOH', 'kaggle': 'Kaggle'
        }
        
        for key, value in special_words.items():
            name = re.sub(rf'\b{key}\b', value, name, flags=re.IGNORECASE)
        
        # 标题大小写
        words = name.split()
        title_words = []
        for word in words:
            if word:
                title_words.append(word[0].upper() + word[1:].lower())
        
        return ' '.join(title_words) + '.pdf'
    
    def rename_papers(self, category):
        """重命名指定目录的PDF文件"""
        dir_path = self.root_path / category
        if not dir_path.exists():
            return 0
            
        renamed_count = 0
        pdf_files = list(dir_path.glob('*.pdf'))
        
        for file_path in pdf_files:
            new_name = self.convert_to_title_case(file_path.name)
            new_path = dir_path / new_name
            
            if file_path.name != new_name:
                if new_path.exists():
                    print(f"  ⚠️  Skipped (exists): {new_name}")
                    continue
                    
                try:
                    file_path.rename(new_path)
                    print(f"  ✅ Renamed: {file_path.name} -> {new_name}")
                    renamed_count += 1
                except Exception as e:
                    print(f"  ❌ Failed: {file_path.name} - {e}")
        
        return renamed_count
    
    def get_paper_list(self, category):
        """获取目录下的PDF文件列表"""
        dir_path = self.root_path / category
        if not dir_path.exists():
            return ""
        
        files = sorted([f.name for f in dir_path.glob('*.pdf')])
        if not files:
            return ""
        
        formatted_files = [f"    '{filename}'" for filename in files]
        return ",\n                    ".join(formatted_files)
    
    def update_index_html(self):
        """更新index.html中的文件列表"""
        index_path = self.root_path / "index.html"
        
        if not index_path.exists():
            print("❌ index.html not found")
            return False
        
        try:
            with open(index_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 构建新的papers对象
            new_papers = f"""            const papers = {{
                'AutoML': [
                    {self.get_paper_list('AutoML')},
                ],
                'AI4Science': [
                    {self.get_paper_list('AI4Science')},
                ],
                'LLM4CO': [
                    {self.get_paper_list('LLM4CO')},
                ],
                'Security': [
                    {self.get_paper_list('Security')},
                ],
                'Surveys': [
                    {self.get_paper_list('Surveys')},
                ],
                'benchmark': [
                    {self.get_paper_list('benchmark')},
                ],
                'embodied': [
                    {self.get_paper_list('embodied')},
                ]
            }};"""
            
            # 使用正则表达式替换
            pattern = r'const papers = \{.*?\};'
            new_content = re.sub(pattern, new_papers, content, flags=re.DOTALL)
            
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print("✅ index.html updated successfully")
            return True
            
        except Exception as e:
            print(f"❌ Failed to update index.html: {e}")
            return False
    
    def show_statistics(self):
        """显示统计信息"""
        print("\n📊 Statistics:")
        print("-" * 30)
        
        total_papers = 0
        for category in self.categories.keys():
            dir_path = self.root_path / category
            if dir_path.exists():
                count = len(list(dir_path.glob('*.pdf')))
                total_papers += count
                print(f"  {category}: {count} papers")
        
        print(f"  Total: {total_papers} papers")
        print("-" * 30)
    
    def run_git_commands(self):
        """执行Git命令"""
        try:
            os.chdir(self.root_path)
            
            # 检查是否有更改
            result = subprocess.run(['git', 'status', '--porcelain'], 
                                  capture_output=True, text=True)
            if not result.stdout.strip():
                print("✅ No changes to commit")
                return
            
            # 添加所有更改
            subprocess.run(['git', 'add', '.'], check=True)
            
            # 提交更改
            commit_msg = f"Auto update papers - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            subprocess.run(['git', 'commit', '-m', commit_msg], check=True)
            
            # 推送到GitHub
            subprocess.run(['git', 'push', 'origin', 'main'], check=True)
            
            print("✅ Successfully pushed to GitHub")
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Git operation failed: {e}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def run_update(self):
        """运行完整更新流程"""
        print("🚀 Starting paper website update...")
        print("=" * 50)
        
        try:
            # 1. 重命名PDF文件
            print("\n📁 Step 1: Renaming PDF files...")
            total_renamed = 0
            for category in self.categories.keys():
                renamed = self.rename_papers(category)
                total_renamed += renamed
            
            if total_renamed > 0:
                print(f"✅ Renamed {total_renamed} files")
            
            # 2. 更新网站索引
            print("\n📝 Step 2: Updating website index...")
            success = self.update_index_html()
            if not success:
                return False
            
            # 3. 显示统计信息
            self.show_statistics()
            
            # 4. GitHub同步
            print("\n🔄 Step 3: Syncing to GitHub...")
            response = input("  Push to GitHub? (y/n) [y]: ").strip().lower()
            if response in ['', 'y', 'yes']:
                self.run_git_commands()
            
            print("\n🎉 Update completed!")
            print("Website will update in 2-5 minutes")
            print("URL: https://fendss.github.io/Papers-Reading")
            
            return True
            
        except Exception as e:
            print(f"\n❌ Update failed: {e}")
            return False

def main():
    """主函数"""
    if len(sys.argv) > 1 and sys.argv[1] == '--no-git':
        updater = PaperUpdater()
        updater.run_git_commands = lambda: print("Git sync skipped")
        updater.run_update()
    else:
        updater = PaperUpdater()
        updater.run_update()

if __name__ == "__main__":
    main()