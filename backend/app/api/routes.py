from fastapi import APIRouter
from app.api import health
# from app.api.smtp import routes as smtp_routes

# Uncomment these lines as you create the routes.py files in those folders:
# from app.api.proxies import routes as proxy_routes
# from app.api.campaigns import routes as campaign_routes
# from app.api.templates import routes as template_routes
# from app.api.analytics import routes as analytics_routes
# from app.api.warmup import routes as warmup_routes
# from app.api.spam import routes as spam_routes

api_router = APIRouter()

# 1. Add System/Health Routes (No prefix, so it stays at /health)
api_router.include_router(health.router, tags=["System"])

# 2. Add SMTP Routes (Prefix /smtp, so endpoints become /api/v1/smtp/...)
# api_router.include_router(
#     smtp_routes.router, 
#     prefix="/smtp", 
#     tags=["SMTP"]
# )

# 3. Future Routes (Uncomment as you build them)
# api_router.include_router(proxy_routes.router, prefix="/proxies", tags=["Proxies"])
# api_router.include_router(campaign_routes.router, prefix="/campaigns", tags=["Campaigns"])
# api_router.include_router(template_routes.router, prefix="/templates", tags=["Templates"])
# api_router.include_router(analytics_routes.router, prefix="/analytics", tags=["Analytics"])
# api_router.include_router(warmup_routes.router, prefix="/warmup", tags=["Warmup"])
# api_router.include_router(spam_routes.router, prefix="/spam", tags=["Spam"])