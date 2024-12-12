# 定义资产的zpi的model对象
from datetime import datetime
from typing import Optional, List, Any, Dict

from pydantic import BaseModel, Field


# 资产位置信息
class AssetPositionApiModel(BaseModel):
    asset_id: Optional[str] = Field(None, description="资产设备的id")
    frame_position: Optional[str] = Field(None, description="机架")
    cabinet_position: Optional[str] = Field(None, description="机柜")
    u_position: Optional[str] = Field(None, description="U位")
    description: Optional[str] = Field(None, description="描述信息")


# 资产配件信息
class AssetPartApiModel(BaseModel):
    id: Optional[str] = Field(None, description="配件信息的id")
    name: Optional[str] = Field(None, description="配件的名称")
    asset_id: Optional[str] = Field(None, description="配件关联的资产设备的id")
    part_type: Optional[str] = Field(None, description="配件的类型")
    part_brand: Optional[str] = Field(None, description="配件的品牌")
    part_config: Optional[str] = Field(None, description="配件的配置")
    part_number: Optional[str] = Field(None, description="配件的编号")
    personal_used_flag: Optional[bool] = Field(False, description="配件是否可自用")
    surplus: Optional[str] = Field(None, description="配件的剩余情况")
    description: Optional[str] = Field(None, description="配件的备注描述")


# 资产生产厂商信息
class AssetManufacturerApiModel(BaseModel):
    asset_id: Optional[str] = Field(None, description="厂商关联的资产设备编号信息")
    name: Optional[str] = Field(None, description="厂商的名称")
    description: Optional[str] = Field(None, description="厂商的描述信息")


# 资产购买合同信息
class AssetContractApiModel(BaseModel):
    asset_id: Optional[str] = Field(None, description="合同关联的资产设备的id")
    contract_number: Optional[str] = Field(None, description="采购合同编号")
    purchase_date: Optional[int] = Field(None, description="购买日期")
    batch_number: Optional[str] = Field(None, description="批次")
    description: Optional[str] = Field(None, description="合同的描述信息")


# 资产归属信息
class AssetBelongApiModel(BaseModel):
    asset_id: Optional[str] = Field(None, description="归属关联的资产设备的id")
    department_id: Optional[str] = Field(None, description="资产归属的部门id")
    department_name: Optional[str] = Field(None, description="资产归属的部门名称")
    user_id: Optional[str] = Field(None, description="资产归属的用户id")
    user_name: Optional[str] = Field(None, description="资产归属的用户名称")
    tel_number: Optional[str] = Field(None, description="资产归属的联系电话")
    description: Optional[str] = Field(None, description="资产归属的描述信息")


# 资产租户信息
class AssetCustomerApiModel(BaseModel):
    asset_id: Optional[str] = Field(None, description="租户关联的资产设备的id")
    customer_id: Optional[str] = Field(None, description="客户编号")
    customer_name: Optional[str] = Field(None, description="客户名称")
    rental_duration: Optional[int] = Field(0, description="出租时长")
    start_date: Optional[int] = Field(None, description="开始时间")
    end_date: Optional[int] = Field(None, description="结束时间")
    vlan_id: Optional[str] = Field(None, description="VlanID")
    float_ip: Optional[str] = Field(None, description="浮动IP")
    band_width: Optional[str] = Field(None, description="流量带宽")
    description: Optional[str] = Field(None, description="租户的描述信息")


class AssetCreateApiModel(BaseModel):
    # 资产通用信息
    asset_id: Optional[str] = Field(None, description="资产设备的id")
    asset_name: str = Field(..., description="资产设备的名称")
    asset_type_id: Optional[str] = Field(..., description="资产设备的类型id")
    asset_description: Optional[str] = Field(None, description="资产设备描述信息")
    # 资产基础信息
    equipment_number: Optional[str] = Field(None, description="资产设备型号")
    sn_number: Optional[str] = Field(None, description="资产设备的序列号")
    asset_number: Optional[str] = Field(None, description="资产设备的资产编号")
    asset_status: Optional[str] = Field("0", description="资产设备的状态")
    extra: Optional[Dict[str, Any]] = Field(None, description="资产设备的扩展信息")
    # 配件信息
    asset_part: Optional[List[AssetPartApiModel]] = Field(None, description="资产设备的配件信息")
    # 位置信息
    asset_position: Optional[AssetPositionApiModel] = Field(None, description="资产设备的位置信息")
    # 厂商信息
    asset_manufacturer: Optional[AssetManufacturerApiModel] = Field(None, description="资产设备的厂商信息")
    # 合同信息
    asset_contract: Optional[AssetContractApiModel] = Field(None, description="资产设备的合同信息")
    # 所属用户信息
    asset_belong: Optional[AssetBelongApiModel] = Field(None, description="资产设备的所属用户信息")
    # 租户信息
    asset_customer: Optional[AssetCustomerApiModel] = Field(None, description="资产设备的租户信息")
