import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PartWhseFullSearchSvc
# Description: BO to retrieve the records from PartWhse, unlike PartWhseSearch this BO
           does NOT filter the plants by cur-plant.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PartWhseFullSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PartWhseFullSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartWhseFullSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartWhseSearchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/PartWhseFullSearches",headers=creds) as resp:
           return await resp.json()

async def post_PartWhseFullSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartWhseFullSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartWhseSearchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartWhseSearchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/PartWhseFullSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PartWhseFullSearches_Company_PartNum_WarehouseCode(Company, PartNum, WarehouseCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartWhseFullSearch item
   Description: Calls GetByID to retrieve the PartWhseFullSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartWhseFullSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartWhseSearchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/PartWhseFullSearches(" + Company + "," + PartNum + "," + WarehouseCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PartWhseFullSearches_Company_PartNum_WarehouseCode(Company, PartNum, WarehouseCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PartWhseFullSearch for the service
   Description: Calls UpdateExt to update PartWhseFullSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartWhseFullSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartWhseSearchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/PartWhseFullSearches(" + Company + "," + PartNum + "," + WarehouseCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PartWhseFullSearches_Company_PartNum_WarehouseCode(Company, PartNum, WarehouseCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PartWhseFullSearch item
   Description: Call UpdateExt to delete PartWhseFullSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartWhseFullSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/PartWhseFullSearches(" + Company + "," + PartNum + "," + WarehouseCode + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartWhseSearchListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePartWhseSearch, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePartWhseSearch=" + whereClausePartWhseSearch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(partNum, warehouseCode, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "partNum=" + partNum
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "warehouseCode=" + warehouseCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartWhseSearch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartWhseSearch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartWhseSearch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartWhseSearch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartWhseSearch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartWhseFullSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartWhseSearchListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartWhseSearchListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartWhseSearchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartWhseSearchRow] = obj["value"]
      pass

class Erp_Tablesets_PartWhseSearchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse  """  
      self.CountedDate:str = obj["CountedDate"]
      """  Date last counted.  Updated during the Inventory Posting Process.  Not directly maintainable by user.  """  
      self.OnHandQty:int = obj["OnHandQty"]
      """  A summary of PartBin.OnHandQty for the warehouse where the bin is a nettable bin (WhseBin.NonNettable = NO). Maintained via the PartBin write trigger.  """  
      self.NonNettableQty:int = obj["NonNettableQty"]
      """  A summary of PartBin.OnHandQty for the warehouse where the bin is a non nettable bin (WhseBin.NonNettable = YES). Maintained via the PartBin write trigger.  """  
      self.SalesReservedQty:int = obj["SalesReservedQty"]
      """  A total of inventory quantities that has been reserved  for sales orders.   A summary of PartAlloc.ReservedQty for sales order allocations against stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  """  
      self.SalesPickingQty:int = obj["SalesPickingQty"]
      """   Quantity that is in the picking process for sales orders. A summary of PartAlloc.PickingQty where PartAlloc.OrderNum > 0
A summary of PartAlloc.PickingQty for sales order that are being picked from stock (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  """  
      self.SalesPickedQty:int = obj["SalesPickedQty"]
      """  Stock Quantity picked for sales orders.  A summary of PartAlloc.PickedQty for sales order picked from stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  """  
      self.JobReservedQty:int = obj["JobReservedQty"]
      """  Summary of mfg demands on released jobs. That is, a summary of outstanding JobMtl and JobAsmbl.PullQty where JobHead.JobFirm = Yes and JobReleased = Yes  """  
      self.KBCode:str = obj["KBCode"]
      """  Uniquely indentifies the record.  """  
      self.MinimumQty:int = obj["MinimumQty"]
      """  Indicates the desired minimum on-hand quantity. This is used by the time phase requirements report when user requests to show any parts that will or have fallen below this level. It is also used as a selection parameter for the inventory reorder report. This is an optional field.  """  
      self.MaximumQty:int = obj["MaximumQty"]
      """  Use to set a Maximum quantity limit that is desired to be on-hand. This field is used as a selection option by the inventory reorder report to show all parts that are over this limit. This field is optional.  """  
      self.SafetyQty:int = obj["SafetyQty"]
      """   Safety quantity is a "purchasing cushion" limit. It's the amount you would need to have to cover your requirements until a shipment arrives from the vendor. If your on-hand quantity falls below this limit it means that there is a good chance that you will run out of material before the next shipment arrives. This value is used by the inventory reorder report and the time phase report. It is an optional field.
Note: Safety + Minimum = Reorder Point...  using this formula the  reorder point is the amount at which to reorder to maintain at least the prescribed minimum quantity.  """  
      self.KBPONUM:int = obj["KBPONUM"]
      """  Purchase order number  that the detail line item is linked to.  """  
      self.KBPOLine:int = obj["KBPOLine"]
      """  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.KBWarehouseCode:str = obj["KBWarehouseCode"]
      """  Kanban Warehouse  """  
      self.KBBinNum:str = obj["KBBinNum"]
      """  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  """  
      self.KBPlant:str = obj["KBPlant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.KBQty:int = obj["KBQty"]
      """  Indicates the desired minimum on-hand Kanban quantity.  """  
      self.AllocQty:int = obj["AllocQty"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SalesAllocQty:int = obj["SalesAllocQty"]
      self.JobAllocQty:int = obj["JobAllocQty"]
      self.JobUnfirmAllocQty:int = obj["JobUnfirmAllocQty"]
      self.Plant:str = obj["Plant"]
      """  Filled in by BO, not physically in the database  """  
      self.DefaultWhse:bool = obj["DefaultWhse"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      """  Description.  """  
      self.SharedWarehouse:bool = obj["SharedWarehouse"]
      """  Determine if this Warehouse is a Shared Warehouse  """  
      self.RemotePlant:str = obj["RemotePlant"]
      """  Indicate which is the Shared Site for the Shared Warehouse. If is empty is because is not a Shared Warehouse.  """  
      self.IsUserAllowed:bool = obj["IsUserAllowed"]
      """  Determines if a User has the rights to perform Adjustments on this Warehouse  """  
      self.PlantName:str = obj["PlantName"]
      """  Plant Name  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartWhseSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse  """  
      self.CountedDate:str = obj["CountedDate"]
      """  Date last counted.  Updated during the Inventory Posting Process.  Not directly maintainable by user.  """  
      self.OnHandQty:int = obj["OnHandQty"]
      """  A summary of PartBin.OnHandQty for the warehouse where the bin is a nettable bin (WhseBin.NonNettable = NO). Maintained via the PartBin write trigger.  """  
      self.NonNettableQty:int = obj["NonNettableQty"]
      """  A summary of PartBin.OnHandQty for the warehouse where the bin is a non nettable bin (WhseBin.NonNettable = YES). Maintained via the PartBin write trigger.  """  
      self.SalesReservedQty:int = obj["SalesReservedQty"]
      """  A total of inventory quantities that has been reserved  for sales orders.   A summary of PartAlloc.ReservedQty for sales order allocations against stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  """  
      self.SalesPickingQty:int = obj["SalesPickingQty"]
      """   Quantity that is in the picking process for sales orders. A summary of PartAlloc.PickingQty where PartAlloc.OrderNum > 0
A summary of PartAlloc.PickingQty for sales order that are being picked from stock (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  """  
      self.SalesPickedQty:int = obj["SalesPickedQty"]
      """  Stock Quantity picked for sales orders.  A summary of PartAlloc.PickedQty for sales order picked from stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  """  
      self.JobReservedQty:int = obj["JobReservedQty"]
      """  Summary of mfg demands on released jobs. That is, a summary of outstanding JobMtl and JobAsmbl.PullQty where JobHead.JobFirm = Yes and JobReleased = Yes  """  
      self.KBCode:str = obj["KBCode"]
      """  Uniquely indentifies the record.  """  
      self.MinimumQty:int = obj["MinimumQty"]
      """  Indicates the desired minimum on-hand quantity. This is used by the time phase requirements report when user requests to show any parts that will or have fallen below this level. It is also used as a selection parameter for the inventory reorder report. This is an optional field.  """  
      self.MaximumQty:int = obj["MaximumQty"]
      """  Use to set a Maximum quantity limit that is desired to be on-hand. This field is used as a selection option by the inventory reorder report to show all parts that are over this limit. This field is optional.  """  
      self.SafetyQty:int = obj["SafetyQty"]
      """   Safety quantity is a "purchasing cushion" limit. It's the amount you would need to have to cover your requirements until a shipment arrives from the vendor. If your on-hand quantity falls below this limit it means that there is a good chance that you will run out of material before the next shipment arrives. This value is used by the inventory reorder report and the time phase report. It is an optional field.
Note: Safety + Minimum = Reorder Point...  using this formula the  reorder point is the amount at which to reorder to maintain at least the prescribed minimum quantity.  """  
      self.KBPONUM:int = obj["KBPONUM"]
      """  Purchase order number  that the detail line item is linked to.  """  
      self.KBPOLine:int = obj["KBPOLine"]
      """  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.KBWarehouseCode:str = obj["KBWarehouseCode"]
      """  Kanban Warehouse  """  
      self.KBBinNum:str = obj["KBBinNum"]
      """  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  """  
      self.KBPlant:str = obj["KBPlant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.KBQty:int = obj["KBQty"]
      """  Indicates the desired minimum on-hand Kanban quantity.  """  
      self.AllocQty:int = obj["AllocQty"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SalesAllocQty:int = obj["SalesAllocQty"]
      self.JobAllocQty:int = obj["JobAllocQty"]
      self.JobUnfirmAllocQty:int = obj["JobUnfirmAllocQty"]
      self.Plant:str = obj["Plant"]
      """  Filled in by BO, not physically in the database  """  
      self.DefaultWhse:bool = obj["DefaultWhse"]
      self.IsUserAllowed:bool = obj["IsUserAllowed"]
      """  Determines if a User has the rights to perform Adjustments on this Warehouse  """  
      self.RemotePlant:str = obj["RemotePlant"]
      """  Indicate which is the Shared Site for the Shared Warehouse. If is empty is because is not a Shared Warehouse.  """  
      self.SharedWarehouse:bool = obj["SharedWarehouse"]
      """  Determine if this Warehouse is a Shared Warehouse  """  
      self.BitFlag:int = obj["BitFlag"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   partNum
   warehouseCode
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.warehouseCode:str = obj["warehouseCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_PartWhseFullSearchTableset:
   def __init__(self, obj):
      self.PartWhseSearch:list[Erp_Tablesets_PartWhseSearchRow] = obj["PartWhseSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartWhseSearchListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse  """  
      self.CountedDate:str = obj["CountedDate"]
      """  Date last counted.  Updated during the Inventory Posting Process.  Not directly maintainable by user.  """  
      self.OnHandQty:int = obj["OnHandQty"]
      """  A summary of PartBin.OnHandQty for the warehouse where the bin is a nettable bin (WhseBin.NonNettable = NO). Maintained via the PartBin write trigger.  """  
      self.NonNettableQty:int = obj["NonNettableQty"]
      """  A summary of PartBin.OnHandQty for the warehouse where the bin is a non nettable bin (WhseBin.NonNettable = YES). Maintained via the PartBin write trigger.  """  
      self.SalesReservedQty:int = obj["SalesReservedQty"]
      """  A total of inventory quantities that has been reserved  for sales orders.   A summary of PartAlloc.ReservedQty for sales order allocations against stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  """  
      self.SalesPickingQty:int = obj["SalesPickingQty"]
      """   Quantity that is in the picking process for sales orders. A summary of PartAlloc.PickingQty where PartAlloc.OrderNum > 0
A summary of PartAlloc.PickingQty for sales order that are being picked from stock (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  """  
      self.SalesPickedQty:int = obj["SalesPickedQty"]
      """  Stock Quantity picked for sales orders.  A summary of PartAlloc.PickedQty for sales order picked from stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  """  
      self.JobReservedQty:int = obj["JobReservedQty"]
      """  Summary of mfg demands on released jobs. That is, a summary of outstanding JobMtl and JobAsmbl.PullQty where JobHead.JobFirm = Yes and JobReleased = Yes  """  
      self.KBCode:str = obj["KBCode"]
      """  Uniquely indentifies the record.  """  
      self.MinimumQty:int = obj["MinimumQty"]
      """  Indicates the desired minimum on-hand quantity. This is used by the time phase requirements report when user requests to show any parts that will or have fallen below this level. It is also used as a selection parameter for the inventory reorder report. This is an optional field.  """  
      self.MaximumQty:int = obj["MaximumQty"]
      """  Use to set a Maximum quantity limit that is desired to be on-hand. This field is used as a selection option by the inventory reorder report to show all parts that are over this limit. This field is optional.  """  
      self.SafetyQty:int = obj["SafetyQty"]
      """   Safety quantity is a "purchasing cushion" limit. It's the amount you would need to have to cover your requirements until a shipment arrives from the vendor. If your on-hand quantity falls below this limit it means that there is a good chance that you will run out of material before the next shipment arrives. This value is used by the inventory reorder report and the time phase report. It is an optional field.
Note: Safety + Minimum = Reorder Point...  using this formula the  reorder point is the amount at which to reorder to maintain at least the prescribed minimum quantity.  """  
      self.KBPONUM:int = obj["KBPONUM"]
      """  Purchase order number  that the detail line item is linked to.  """  
      self.KBPOLine:int = obj["KBPOLine"]
      """  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.KBWarehouseCode:str = obj["KBWarehouseCode"]
      """  Kanban Warehouse  """  
      self.KBBinNum:str = obj["KBBinNum"]
      """  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  """  
      self.KBPlant:str = obj["KBPlant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.KBQty:int = obj["KBQty"]
      """  Indicates the desired minimum on-hand Kanban quantity.  """  
      self.AllocQty:int = obj["AllocQty"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SalesAllocQty:int = obj["SalesAllocQty"]
      self.JobAllocQty:int = obj["JobAllocQty"]
      self.JobUnfirmAllocQty:int = obj["JobUnfirmAllocQty"]
      self.Plant:str = obj["Plant"]
      """  Filled in by BO, not physically in the database  """  
      self.DefaultWhse:bool = obj["DefaultWhse"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      """  Description.  """  
      self.SharedWarehouse:bool = obj["SharedWarehouse"]
      """  Determine if this Warehouse is a Shared Warehouse  """  
      self.RemotePlant:str = obj["RemotePlant"]
      """  Indicate which is the Shared Site for the Shared Warehouse. If is empty is because is not a Shared Warehouse.  """  
      self.IsUserAllowed:bool = obj["IsUserAllowed"]
      """  Determines if a User has the rights to perform Adjustments on this Warehouse  """  
      self.PlantName:str = obj["PlantName"]
      """  Plant Name  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartWhseSearchListTableset:
   def __init__(self, obj):
      self.PartWhseSearchList:list[Erp_Tablesets_PartWhseSearchListRow] = obj["PartWhseSearchList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartWhseSearchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse  """  
      self.CountedDate:str = obj["CountedDate"]
      """  Date last counted.  Updated during the Inventory Posting Process.  Not directly maintainable by user.  """  
      self.OnHandQty:int = obj["OnHandQty"]
      """  A summary of PartBin.OnHandQty for the warehouse where the bin is a nettable bin (WhseBin.NonNettable = NO). Maintained via the PartBin write trigger.  """  
      self.NonNettableQty:int = obj["NonNettableQty"]
      """  A summary of PartBin.OnHandQty for the warehouse where the bin is a non nettable bin (WhseBin.NonNettable = YES). Maintained via the PartBin write trigger.  """  
      self.SalesReservedQty:int = obj["SalesReservedQty"]
      """  A total of inventory quantities that has been reserved  for sales orders.   A summary of PartAlloc.ReservedQty for sales order allocations against stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  """  
      self.SalesPickingQty:int = obj["SalesPickingQty"]
      """   Quantity that is in the picking process for sales orders. A summary of PartAlloc.PickingQty where PartAlloc.OrderNum > 0
A summary of PartAlloc.PickingQty for sales order that are being picked from stock (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  """  
      self.SalesPickedQty:int = obj["SalesPickedQty"]
      """  Stock Quantity picked for sales orders.  A summary of PartAlloc.PickedQty for sales order picked from stock  (PartAlloc.OrderNum > 0 & SupplyJobNum = blank).  """  
      self.JobReservedQty:int = obj["JobReservedQty"]
      """  Summary of mfg demands on released jobs. That is, a summary of outstanding JobMtl and JobAsmbl.PullQty where JobHead.JobFirm = Yes and JobReleased = Yes  """  
      self.KBCode:str = obj["KBCode"]
      """  Uniquely indentifies the record.  """  
      self.MinimumQty:int = obj["MinimumQty"]
      """  Indicates the desired minimum on-hand quantity. This is used by the time phase requirements report when user requests to show any parts that will or have fallen below this level. It is also used as a selection parameter for the inventory reorder report. This is an optional field.  """  
      self.MaximumQty:int = obj["MaximumQty"]
      """  Use to set a Maximum quantity limit that is desired to be on-hand. This field is used as a selection option by the inventory reorder report to show all parts that are over this limit. This field is optional.  """  
      self.SafetyQty:int = obj["SafetyQty"]
      """   Safety quantity is a "purchasing cushion" limit. It's the amount you would need to have to cover your requirements until a shipment arrives from the vendor. If your on-hand quantity falls below this limit it means that there is a good chance that you will run out of material before the next shipment arrives. This value is used by the inventory reorder report and the time phase report. It is an optional field.
Note: Safety + Minimum = Reorder Point...  using this formula the  reorder point is the amount at which to reorder to maintain at least the prescribed minimum quantity.  """  
      self.KBPONUM:int = obj["KBPONUM"]
      """  Purchase order number  that the detail line item is linked to.  """  
      self.KBPOLine:int = obj["KBPOLine"]
      """  The line number of the detail record on the purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  """  
      self.KBWarehouseCode:str = obj["KBWarehouseCode"]
      """  Kanban Warehouse  """  
      self.KBBinNum:str = obj["KBBinNum"]
      """  Identifies the Bin location that contains an Onhand quantity for this Part within a warehouse. The PartBin.BinNum can be blank (indicating bin tracking is not used for this part) or it  must be valid in the WhseBin table.  """  
      self.KBPlant:str = obj["KBPlant"]
      """  Site Identifier. This field cannot be blank.  """  
      self.KBQty:int = obj["KBQty"]
      """  Indicates the desired minimum on-hand Kanban quantity.  """  
      self.AllocQty:int = obj["AllocQty"]
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SalesAllocQty:int = obj["SalesAllocQty"]
      self.JobAllocQty:int = obj["JobAllocQty"]
      self.JobUnfirmAllocQty:int = obj["JobUnfirmAllocQty"]
      self.Plant:str = obj["Plant"]
      """  Filled in by BO, not physically in the database  """  
      self.DefaultWhse:bool = obj["DefaultWhse"]
      self.IsUserAllowed:bool = obj["IsUserAllowed"]
      """  Determines if a User has the rights to perform Adjustments on this Warehouse  """  
      self.RemotePlant:str = obj["RemotePlant"]
      """  Indicate which is the Shared Site for the Shared Warehouse. If is empty is because is not a Shared Warehouse.  """  
      self.SharedWarehouse:bool = obj["SharedWarehouse"]
      """  Determine if this Warehouse is a Shared Warehouse  """  
      self.BitFlag:int = obj["BitFlag"]
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtPartWhseFullSearchTableset:
   def __init__(self, obj):
      self.PartWhseSearch:list[Erp_Tablesets_PartWhseSearchRow] = obj["PartWhseSearch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   partNum
   warehouseCode
   """  
   def __init__(self, obj):
      self.partNum:str = obj["partNum"]
      self.warehouseCode:str = obj["warehouseCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartWhseFullSearchTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartWhseFullSearchTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartWhseFullSearchTableset] = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartWhseSearchListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPartWhseSearch_input:
   """ Required : 
   ds
   partNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PartWhseFullSearchTableset] = obj["ds"]
      self.partNum:str = obj["partNum"]
      pass

class GetNewPartWhseSearch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartWhseFullSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePartWhseSearch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePartWhseSearch:str = obj["whereClausePartWhseSearch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartWhseFullSearchTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

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

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPartWhseFullSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPartWhseFullSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PartWhseFullSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartWhseFullSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

