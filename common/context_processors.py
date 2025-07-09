# common/context_processors.py

def common_context(request):
    return {
        "site_name": "News",
        "year": 2025
    }