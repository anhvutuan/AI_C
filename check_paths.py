import sys, site, os
from tiktoken.load import tiktoken_cache_dir

print("🧠 Python executable:", sys.executable)
print("📂 sys.path:")
for p in sys.path:
    print(" -", p)

print("\n📦 site-packages:")
print(site.getsitepackages())

print("\n📦 user site-packages:")
print(site.getusersitepackages())

print("\n💾 Tiktoken cache dir:", tiktoken_cache_dir())


import site
print(site.getsitepackages())
