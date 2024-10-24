from fastapi import APIRouter, Depends, HTTPException, status
from schemas.allocation_schema import AllocationSchema
from repos.allocation_repo import get_allocations, insert_allocation, get_allocation, update_allocation, delete_allocation
from conf.app import get_app_instance
from utils.response_builder import build_response
router = APIRouter()

@router.get('/allocations')
async def get_allocations_endpoint(app=Depends(get_app_instance)):
    try:
        allocations = await get_allocations(app)
        return build_response(allocations)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.get('/allocations/{allocation_id}')
async def get_allocation_endpoint(allocation_id: int, app=Depends(get_app_instance)):
    try:
        allocation = await get_allocation(app, allocation_id)
        if not allocation:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Allocation with id {allocation_id} not found")
        return build_response(allocation)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.post('/allocations')
async def insert_allocation_endpoint(allocation: AllocationSchema, app=Depends(get_app_instance)):
    try:
        new_allocation = await insert_allocation(app, allocation)
        return build_response(new_allocation, status_code=status.HTTP_201_CREATED)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.put('/allocations/{allocation_id}')
async def update_allocation_endpoint(allocation_id: int, allocation: AllocationSchema, app=Depends(get_app_instance)):
    try:
        updated_allocation = await update_allocation(app, allocation_id, allocation)
        if not updated_allocation:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Allocation with id {allocation_id} not found")
        return build_response(updated_allocation)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@router.delete('/allocations/{allocation_id}')
async def delete_allocation_endpoint(allocation_id: int, app=Depends(get_app_instance)):
    try:
        deleted_allocation = await delete_allocation(app, allocation_id)
        if not deleted_allocation:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Allocation with id {allocation_id} not found")
        return build_response(deleted_allocation)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))