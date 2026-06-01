import os
import re
import time
import requests
from scholarly import scholarly
from typing import List, Dict

RESEARCH_KEYWORDS_BASE = ["deep hedging", "FunNN", "functional neural network", "empirical Esscher", "Esscher transform", "diffusion model", "interest rate derivative", "CVA", "portfolio optimization"]

DOWNLOAD_DIR = "my_deep_hedging_broadening_papers"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def sanitize_filename(name: str) -> str:
    name = re.sub(r'[\\/*?:"<>|]', "_", name)
    return name.strip()[:180]

def calculate_broadening_score(title: str, abstract: str) -> float:
    """拓宽价值评分（更高 = 越能扩展现有工作）"""
    text = (title + " " + abstract).lower()
    score = 0.0
    broadening_indicators = ["survey", "review", "extension", "future", "beyond", "hybrid", "reinforcement", "multi-asset", "quantum", "graph neural", "stochastic control", "generative ai", "emerging", "new framework"]
    for ind in broadening_indicators:
        if ind in text:
            score += 2.0
    # 基础匹配加分但不主导
    base_matches = sum(1.0 for kw in RESEARCH_KEYWORDS_BASE if kw in text)
    score += min(base_matches * 0.5, 3.0)
    return round(min(score / 8.0, 1.0), 2)

def search_broadening_papers(focus_area: str = "", max_results: int = 6) -> List[Dict]:
    """AI Agent 主调用工具 - 专为拓宽设计"""
    if focus_area:
        query = f'deep hedging OR "interest rate" OR CVA OR "portfolio optimization" {focus_area} (extension OR survey OR review OR hybrid OR future OR emerging OR beyond)'
    else:
        # 内置多方向探索查询（覆盖常见拓宽路径）
        query = 'deep hedging (survey OR review OR extension OR "future directions" OR reinforcement OR "multi-asset" OR quantum OR "graph neural" OR "stochastic control" OR hybrid OR generative)'
    
    print(f"🔍 Agent 正在搜索拓宽文献: {query}")
    results = []
    pubs = scholarly.search_pubs(query)
    
    for _ in range(max_results):
        try:
            pub = next(pubs)
            scholarly.fill(pub)
            bib = pub.get('bib', {})
            
            title = bib.get('title', 'Unknown')
            abstract = bib.get('abstract', 'No abstract available')
            authors = bib.get('author', 'Unknown')
            year = bib.get('pub_year', '')
            scholar_url = pub.get('url', '')
            
            broadening_score = calculate_broadening_score(title, abstract)
            
            results.append({
                "title": title,
                "authors": authors,
                "year": year,
                "abstract": abstract[:650] + "..." if len(abstract) > 650 else abstract,
                "broadening_score": broadening_score,
                "scholar_url": scholar_url,
                "why_broaden": "可提供新理论框架 / 新应用场景 / 跨领域方法 / 未来方向启发" if broadening_score > 0.6 else "潜在扩展点，值得精读"
            })
            time.sleep(1.5)
        except StopIteration:
            break
    
    return results

def download_paper_by_title(title: str) -> str:
    """下载工具（自动以标题命名）"""
    pubs = scholarly.search_pubs(f'"{title}"')
    try:
        pub = next(pubs)
        scholarly.fill(pub)
        
        filename = sanitize_filename(title) + ".pdf"
        filepath = os.path.join(DOWNLOAD_DIR, filename)
        
        for key in ['url_pdf', 'eprint_url', 'pdf_url']:
            pdf_url = pub.get(key)
            if pdf_url and pdf_url.startswith('http'):
                r = requests.get(pdf_url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=20)
                if r.status_code == 200 and b'%PDF' in r.content[:10]:
                    with open(filepath, 'wb') as f:
                        f.write(r.content)
                    return f"✅ 下载成功！\n文件路径：{filepath}\n文件名：{filename}"
        
        return f"⚠️ 自动下载失败，请手动打开 Scholar 链接（已登录学生账号）：{pub.get('url')}"
    except Exception as e:
        return f"❌ 下载失败: {str(e)}"

# LangChain 兼容（可选）
try:
    from langchain_core.tools import tool
    @tool
    def search_broadening_papers_tool(focus_area: str = "", max_results: int = 6):
        return search_broadening_papers(focus_area, max_results)
    @tool
    def download_paper_by_title_tool(title: str):
        return download_paper_by_title(title)
except ImportError:
    pass

print("✅ Deep Hedging Broadening Skill 加载完成！（专为拓宽领域设计）")
