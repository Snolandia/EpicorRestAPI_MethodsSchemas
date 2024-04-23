import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PartAttributeSetSearchSvc
# Description: Service to Part with Attribute Set
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAttributeSetSearchSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAttributeSetSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartAttributeSetSearchListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAttributeSetSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def post_GetRows(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: This service is currently not implemented.
   OperationID: GetRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAttributeSetSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: This service will return all parts and related attribute sets (if any).
This method will try to mirror the functionality of the base GetList method, but since we are
populating a temp table (PartAttributeSetSearch) we need our own public method.
   OperationID: GetList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAttributeSetSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAttributeSetSearchListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartAttributeSetSearchListRow] = obj["value"]
      pass

class Erp_Tablesets_PartAttributeSetSearchListRow:
   def __init__(self, obj):
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.ClassID:str = obj["ClassID"]
      """  The Inventory class that this Part belongs to.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Description:str = obj["Description"]
      """  The Full Description of the Attribute Set.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group ID for the Part.  """  
      self.QtyBearing:bool = obj["QtyBearing"]
      """  Indicates a Quantity Bearing part.  """  
      self.ShortDescription:str = obj["ShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.TrackInventoryAttributes:bool = obj["TrackInventoryAttributes"]
      """  Indicates if inventory for this part is tracked at the attribute level.  """  
      self.TypeCode:str = obj["TypeCode"]
      """   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part.
K = Sales Kit Part.  """  
      self.IUM:str = obj["IUM"]
      """  Primary Inventory Unit of Measure.  """  
      self.NonStock:bool = obj["NonStock"]
      """  A flag which indicates if this Part is not a stocked inventory item.  """  
      self.InActive:bool = obj["InActive"]
      """  Flag which indicates if the Part Master is considered as "Inactive".  """  
      self.Method:bool = obj["Method"]
      """  An internal flag which indicates that this part contains Method of Manufacture details (PartMtl/PartOpr records).  """  
      self.PhantomBOM:bool = obj["PhantomBOM"]
      """  A flag which indicates if this Part is a "Phantom BOM".  """  
      self.SearchWord:str = obj["SearchWord"]
      """  An abbreviated part description field by which the user can search the Part file.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_PartAttributeSetSearchListRow:
   def __init__(self, obj):
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.ClassID:str = obj["ClassID"]
      """  The Inventory class that this Part belongs to.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Description:str = obj["Description"]
      """  The Full Description of the Attribute Set.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group ID for the Part.  """  
      self.QtyBearing:bool = obj["QtyBearing"]
      """  Indicates a Quantity Bearing part.  """  
      self.ShortDescription:str = obj["ShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.TrackInventoryAttributes:bool = obj["TrackInventoryAttributes"]
      """  Indicates if inventory for this part is tracked at the attribute level.  """  
      self.TypeCode:str = obj["TypeCode"]
      """   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part.
K = Sales Kit Part.  """  
      self.IUM:str = obj["IUM"]
      """  Primary Inventory Unit of Measure.  """  
      self.NonStock:bool = obj["NonStock"]
      """  A flag which indicates if this Part is not a stocked inventory item.  """  
      self.InActive:bool = obj["InActive"]
      """  Flag which indicates if the Part Master is considered as "Inactive".  """  
      self.Method:bool = obj["Method"]
      """  An internal flag which indicates that this part contains Method of Manufacture details (PartMtl/PartOpr records).  """  
      self.PhantomBOM:bool = obj["PhantomBOM"]
      """  A flag which indicates if this Part is a "Phantom BOM".  """  
      self.SearchWord:str = obj["SearchWord"]
      """  An abbreviated part description field by which the user can search the Part file.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartAttributeSetSearchListTableset:
   def __init__(self, obj):
      self.PartAttributeSetSearchList:list[Erp_Tablesets_PartAttributeSetSearchListRow] = obj["PartAttributeSetSearchList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartAttributeSetSearchRow:
   def __init__(self, obj):
      self.AttrClassID:str = obj["AttrClassID"]
      """  ID of related Attribute Class.  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.ClassID:str = obj["ClassID"]
      """  The Inventory class that this Part belongs to.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Description:str = obj["Description"]
      """  The Full Description of the Attribute Set.  """  
      self.PartDescription:str = obj["PartDescription"]
      """  Describes the Part.  """  
      self.PartNum:str = obj["PartNum"]
      """  A unique part number that identifies this part.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  Product Group ID for the Part.  """  
      self.QtyBearing:bool = obj["QtyBearing"]
      """  Indicates a Quantity Bearing part.  """  
      self.ShortDescription:str = obj["ShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.TrackInventoryAttributes:bool = obj["TrackInventoryAttributes"]
      """  Indicates if inventory for this part is tracked at the attribute level.  """  
      self.TypeCode:str = obj["TypeCode"]
      """   Classifies Parts into the following...
M = Manufactured Part.
P = Purchased Part.
K = Sales Kit Part.  """  
      self.NonStock:bool = obj["NonStock"]
      """  A flag which indicates if this Part is not a stocked inventory item.  """  
      self.InActive:bool = obj["InActive"]
      """  Flag which indicates if the Part Master is considered as "Inactive".  """  
      self.Method:bool = obj["Method"]
      """  An internal flag which indicates that this part contains Method of Manufacture details (PartMtl/PartOpr records).  """  
      self.PhantomBOM:bool = obj["PhantomBOM"]
      """  A flag which indicates if this Part is a "Phantom BOM".  """  
      self.IUM:str = obj["IUM"]
      """  Primary Inventory Unit of Measure.  """  
      self.SearchWord:str = obj["SearchWord"]
      """  An abbreviated part description field by which the user can search the Part file.  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartAttributeSetSearchTableset:
   def __init__(self, obj):
      self.PartAttributeSetSearch:list[Erp_Tablesets_PartAttributeSetSearchRow] = obj["PartAttributeSetSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetList_input:
   """ Required : 
   whereClauseDynAttrValueSet
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDynAttrValueSet:str = obj["whereClauseDynAttrValueSet"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartAttributeSetSearchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseDynAttrValueSet
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseDynAttrValueSet:str = obj["whereClauseDynAttrValueSet"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartAttributeSetSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

