from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.session import get_db
from app.models.smtp import SMTPAccount
from app.schemas.smtp import SMTPCreate, SMTPResponse
from app.core.security import encrypt_password

router = APIRouter()

@router.post("/", response_model=SMTPResponse, status_code=status.HTTP_201_CREATED)
async def create_smtp(smtp_in: SMTPCreate, db: AsyncSession = Depends(get_db)):
    """Add a new SMTP account."""
    new_smtp = SMTPAccount(
        name=smtp_in.name,
        host=smtp_in.host,
        port=smtp_in.port,
        username=smtp_in.username,
        encrypted_password=encrypt_password(smtp_in.password),
        security=smtp_in.security,
        is_active=smtp_in.is_active
    )
    db.add(new_smtp)
    await db.commit()
    await db.refresh(new_smtp)
    return new_smtp

@router.get("/", response_model=List[SMTPResponse])
async def list_smtps(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    """List all SMTP accounts."""
    result = await db.execute(select(SMTPAccount).offset(skip).limit(limit))
    return result.scalars().all()

@router.get("/{smtp_id}", response_model=SMTPResponse)
async def get_smtp(smtp_id: UUID, db: AsyncSession = Depends(get_db)):
    """Get specific SMTP details."""
    result = await db.execute(select(SMTPAccount).where(SMTPAccount.id == smtp_id))
    smtp = result.scalar_one_or_none()
    if not smtp:
        raise HTTPException(status_code=404, detail="SMTP Account not found")
    return smtp

@router.delete("/{smtp_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_smtp(smtp_id: UUID, db: AsyncSession = Depends(get_db)):
    """Delete an SMTP account."""
    result = await db.execute(select(SMTPAccount).where(SMTPAccount.id == smtp_id))
    smtp = result.scalar_one_or_none()
    if not smtp:
        raise HTTPException(status_code=404, detail="SMTP Account not found")
    
    await db.delete(smtp)
    await db.commit()
    return None