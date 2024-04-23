import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CCTagSearchSvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCTagSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCTagSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CCTagSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CCTagSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CCTagSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCTagRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCTagSearchSvc/CCTagSearches",headers=creds) as resp:
           return await resp.json()

async def post_CCTagSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CCTagSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CCTagRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CCTagRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCTagSearchSvc/CCTagSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CCTagSearches_Company_Plant_WarehouseCode_TagNum(Company, Plant, WarehouseCode, TagNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CCTagSearch item
   Description: Calls GetByID to retrieve the CCTagSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CCTagSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param TagNum: Desc: TagNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CCTagRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCTagSearchSvc/CCTagSearches(" + Company + "," + Plant + "," + WarehouseCode + "," + TagNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CCTagSearches_Company_Plant_WarehouseCode_TagNum(Company, Plant, WarehouseCode, TagNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CCTagSearch for the service
   Description: Calls UpdateExt to update CCTagSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CCTagSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param TagNum: Desc: TagNum   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CCTagRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CCTagSearchSvc/CCTagSearches(" + Company + "," + Plant + "," + WarehouseCode + "," + TagNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CCTagSearches_Company_Plant_WarehouseCode_TagNum(Company, Plant, WarehouseCode, TagNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CCTagSearch item
   Description: Call UpdateExt to delete CCTagSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CCTagSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param TagNum: Desc: TagNum   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CCTagSearchSvc/CCTagSearches(" + Company + "," + Plant + "," + WarehouseCode + "," + TagNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCTagListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCTagSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCCTag, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCCTag=" + whereClauseCCTag
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCTagSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(plant, warehouseCode, tagNum, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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
   params += "plant=" + plant
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "warehouseCode=" + warehouseCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "tagNum=" + tagNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCTagSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCTagSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCCTag(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCCTag
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCCTag
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCCTag_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCCTag_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCTagSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCTagSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCTagSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCTagSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCTagSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCTagSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCTagListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CCTagListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCTagRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CCTagRow] = obj["value"]
      pass

class Erp_Tablesets_CCTagListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Bindesc:str = obj["Bindesc"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Unique identifier for this warehouse assigned by the user.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number selected for counting.  """  
      self.TagNum:str = obj["TagNum"]
      """  Tag number. This will be generated from Warehse and will be in the format of tagNum.countseq where countSeq is the count/recount sequence. First count for example would be tag 000000001.1 recount generate tag 000000001.2 from tag 000000001.1, second recount would generate tag 000000001.3  the same part, etc.  """  
      self.TagSelForVoid:bool = obj["TagSelForVoid"]
      self.BinNum:str = obj["BinNum"]
      """  Bin number for the tag  """  
      self.CountedBy:str = obj["CountedBy"]
      """  Person that counted the parts on the Count Tag.  """  
      self.WrehouseCode:str = obj["WrehouseCode"]
      self.CountedQty:int = obj["CountedQty"]
      """  Quantity counted for the tag. Like PartBin.OnHandQty except no negative allowed. This is expressed in the qty per the CCTag.UOM unit of measure, which may not be the Part base UOM.  """  
      self.WarehseDesc:str = obj["WarehseDesc"]
      self.CountedTime:str = obj["CountedTime"]
      """  Optional field that Indicates when the count took place to aid in determining what activity took place before the actual count.  """  
      self.TagReturned:bool = obj["TagReturned"]
      """  Indicates the Count Tag has been returned and the results entered into the count.  This is set when during Tag Entry when the user keys in a counted amount (or voids the tag).  System Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TopLevelPCID:str = obj["TopLevelPCID"]
      """  The outermost PCID that contains this CCPDICTag.PCID  """  
      self.PCID:str = obj["PCID"]
      """  Parent PCID that this tag is associated with. Equates similar to the way PkgControlItem.PCID relates to PkgControlHeader.PCID  """  
      self.ItemPCID:str = obj["ItemPCID"]
      """  Child PCID, equates to a PkgControlItem.ItemPCID. Either ItemPCID or ItemPartNum will be populated but never both, as is done in PkgControlItem table.  """  
      self.TagStatusDesc:str = obj["TagStatusDesc"]
      """  Tag Status Description  """  
      self.CCTagCharacter02:str = obj["CCTagCharacter02"]
      """  Tag Type for PCID tag  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetIDDescription:str = obj["AttributeSetIDDescription"]
      self.AttributeSetIDShortDescription:str = obj["AttributeSetIDShortDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CCTagRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Unique identifier for this warehouse assigned by the user.  """  
      self.Plant:str = obj["Plant"]
      """  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  """  
      self.CCYear:int = obj["CCYear"]
      """  Calendar year that this cycle count control record is for.  """  
      self.CCMonth:int = obj["CCMonth"]
      """  CCPeriodDefn.CycleSeq that this cycle count control record is for.  """  
      self.FullPhysical:bool = obj["FullPhysical"]
      """  Indicates that the count cycle is either a cycle count cycle or a full physical inventory count cycle.  Full Physical Inventory cycles are for the entire set of parts in the warehouse(s) and this record was created by Initialize Physical Inventory process.  Cycle Counts are only for a limited number of parts at one time and this record was created by the Cycle Count Schedule Maintenance process. Required as part of the primary key because full physical and cycle count cycles can be set for the same whs/monthy/year  """  
      self.CycleSeq:int = obj["CycleSeq"]
      """  Cycle sequence number, used to keep the primary index unique since there can be multiple cycles set up for the same date.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number selected for counting.  """  
      self.TagNum:str = obj["TagNum"]
      """  Tag number. This will be generated from Warehse and will be in the format of tagNum.countseq where countSeq is the count/recount sequence. First count for example would be tag 000000001.1 recount generate tag 000000001.2 from tag 000000001.1, second recount would generate tag 000000001.3  the same part, etc.  """  
      self.BinNum:str = obj["BinNum"]
      """  Bin number for the tag  """  
      self.CountedBy:str = obj["CountedBy"]
      """  Person that counted the parts on the Count Tag.  """  
      self.CountedQty:int = obj["CountedQty"]
      """  Quantity counted for the tag. Like PartBin.OnHandQty except no negative allowed. This is expressed in the qty per the CCTag.UOM unit of measure, which may not be the Part base UOM.  """  
      self.CountedTime:str = obj["CountedTime"]
      """  Optional field that Indicates when the count took place to aid in determining what activity took place before the actual count.  """  
      self.TagNote:str = obj["TagNote"]
      """  Tag Note  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  This field is set equal to the Login ID variable.  System Set when a user enters a counted amount for the tag or voids the tag.  """  
      self.TagPrinted:bool = obj["TagPrinted"]
      """  Indicates that the Count Tag has been printed.  Manually entered tags are set to "Printed" when they are entered.  System Set.  """  
      self.TagReturned:bool = obj["TagReturned"]
      """  Indicates the Count Tag has been returned and the results entered into the count.  This is set when during Tag Entry when the user keys in a counted amount (or voids the tag).  System Set.  """  
      self.CountedDate:str = obj["CountedDate"]
      """  Date the count was performed.  """  
      self.TagStatus:int = obj["TagStatus"]
      """   Tag status.
Code/Desc:
0 = open
1 = posted
2 = voided 3=Closed/Recount.  """  
      self.BlankTag:bool = obj["BlankTag"]
      """  True = this tag was generated as a blank tag. This will control whether bin/lot/serial data can be changed on the tag and whether the tag can be voided independent of other tags generated for an part.  """  
      self.LotNum:str = obj["LotNum"]
      """  LotNum for the tag  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number.  """  
      self.UOM:str = obj["UOM"]
      """  The PartBin Unit of measure for this tag.  """  
      self.FrozenQOH:int = obj["FrozenQOH"]
      """  QOH in PartBin at the time the inventory was frozen. This is expressed in the qty per the CCTag.UOM unit of measure, which may not be the Part base UOM. For blank tags this will be zero.  """  
      self.FrozenCost:int = obj["FrozenCost"]
      """  The per unit part cost at the time the quantity was frozen, based on the costing method for the part/Site. This is the unit cost based on the part base UOM, which might not be the CCTag.UOM so to get total frozen cost for this tag, the CCTag quantities wi  """  
      self.EntryDate:str = obj["EntryDate"]
      """  The date the count was entered or tag was voided  """  
      self.EntryTime:int = obj["EntryTime"]
      """  The time the count was entered or tag was voided  """  
      self.SheetNum:int = obj["SheetNum"]
      """  The sheet number the tag is assigned to. If the sheet is being accessed by enter count by sheet, tags tied to that sheet cannot be accessed individually until the sheet record is unlocked.  """  
      self.FrozenTranDate:str = obj["FrozenTranDate"]
      """  The PartTran.SysDate for the last PartTran for this part when  the quantity was frozen, used with FrozentTranNum and FrozenTranTime to determine what activity has taken place after the freeze.  """  
      self.FrozenTranTime:int = obj["FrozenTranTime"]
      """  The PartTran.SysTime for the last PartTran for this part when  the quantity was frozen, used with FrozentTranDate and FrozenTranNum to determine what activity has taken place after the freeze.  """  
      self.ActivityBeforeCount:int = obj["ActivityBeforeCount"]
      """  Manually entered by the user to account for ongoing activity that took place during the count.  Inventory activity that took place AFTER the start of the count FrozenQOH), but BEFORE the actual count.  This number is used to adjust the "FrozenQOH" when determining the variance between the Frozen Quantity and the Actual Counted Quantity.  Example:  At 1:00 the count is started and the computer has 250 units on hand for part XYZ.  At 1:30 75 units are issued to a job.  At 2:30 John counts 175 units.  The variance report would report a variance of 75 units and show the issue as activity.  The user could then decide that the issue took place before the count took place and enter 75 units into the Activity Before Count field in Tag Maintenance.  The variance report would then "expect" 175 units and have a count of 175 units for a variance of zero(0).  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCIDTag:bool = obj["PCIDTag"]
      """  True indicates this tag is associated with a PCID, false indicates this tag is associated to loose inventory (non-PCID)  """  
      self.TopLevelPCID:str = obj["TopLevelPCID"]
      """  The outermost PCID that contains this CCPDICTag.PCID  """  
      self.PCID:str = obj["PCID"]
      """  Parent PCID that this tag is associated with. Equates similar to the way PkgControlItem.PCID relates to PkgControlHeader.PCID  """  
      self.ItemPCID:str = obj["ItemPCID"]
      """  Child PCID, equates to a PkgControlItem.ItemPCID. Either ItemPCID or ItemPartNum will be populated but never both, as is done in PkgControlItem table.  """  
      self.ReturnNestedPCID:bool = obj["ReturnNestedPCID"]
      """  Only applies if ItemPCID has data. True = indicates in Count Entry that all of the related CCPCIDTag records for this CCPCIDTag.ItemPCID and all lower level nested child PCIDs/Parts should be set to TagReturned = true and  for ItemPartNum records set CountedQty = FrozenQty as if the user had accessed each of the tags and manually entered.  """  
      self.CCTagBoolean01:bool = obj["CCTagBoolean01"]
      """  CCTagBoolean01  """  
      self.CCTagBoolean02:bool = obj["CCTagBoolean02"]
      """  CCTagBoolean02  """  
      self.CCTagCharacter01:str = obj["CCTagCharacter01"]
      """  Move To Bin for the tag  """  
      self.CCTagCharacter02:str = obj["CCTagCharacter02"]
      """  Tag Type for PCID tag  """  
      self.CCTagCharacter03:str = obj["CCTagCharacter03"]
      """  CCTagCharacter03  """  
      self.CCTagCharacter04:str = obj["CCTagCharacter04"]
      """  CCTagCharacter04  """  
      self.CCTagCharacter05:str = obj["CCTagCharacter05"]
      """  Source data used to generate the default serial tag when no standard tag is generated from SerialNo, PartBinQOH or  PrimaryBin  """  
      self.CCTagDate01:str = obj["CCTagDate01"]
      """  CCTagDate01  """  
      self.CCTagDate02:str = obj["CCTagDate02"]
      """  CCTagDate02  """  
      self.CCTagDecimal01:int = obj["CCTagDecimal01"]
      """  CCTagDecimal01  """  
      self.CCTagDecimal02:int = obj["CCTagDecimal02"]
      """  CCTagDecimal02  """  
      self.CCTagInteger01:int = obj["CCTagInteger01"]
      """  CCTagInteger01  """  
      self.CCTagInteger02:int = obj["CCTagInteger02"]
      """  CCTagInteger02  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.CountedQtyWarn:str = obj["CountedQtyWarn"]
      self.EnableLotNo:bool = obj["EnableLotNo"]
      self.EnableSerialNo:bool = obj["EnableSerialNo"]
      self.EnableUOMWorksheet:bool = obj["EnableUOMWorksheet"]
      """  True when UOM Worksheet must be enabled  """  
      self.HasActivity:str = obj["HasActivity"]
      """  This field is to indicate there is data in the activity grid to cue the user to consult the detail sheet before entering counts.  """  
      self.SavedBlankTag:bool = obj["SavedBlankTag"]
      self.SelectedForVoid:bool = obj["SelectedForVoid"]
      """  External field. Used by the Void Blank Tags processing to indicate the tag was selected for void.  """  
      self.TagStatusDesc:str = obj["TagStatusDesc"]
      """  Tag Status Description  """  
      self.UOMDO:str = obj["UOMDO"]
      """  Display Only Unit Of Measure.  """  
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.EnablePCID:bool = obj["EnablePCID"]
      self.EnableItemPCID:bool = obj["EnableItemPCID"]
      self.IsNestedPCID:bool = obj["IsNestedPCID"]
      self.IsItemQty:bool = obj["IsItemQty"]
      self.MoveToBinDescription:str = obj["MoveToBinDescription"]
      self.TagTypeDescList:str = obj["TagTypeDescList"]
      """  Used for Code Desc list to allow changing this list by manually setting in code logic.  """  
      self.TagTypeDescription:str = obj["TagTypeDescription"]
      """  Tag Type Description  """  
      self.EnableTagType:bool = obj["EnableTagType"]
      self.EnableGenLowerNestedPCID:bool = obj["EnableGenLowerNestedPCID"]
      self.HHNumOfBlankPCIDTags:int = obj["HHNumOfBlankPCIDTags"]
      """  This field used by GenerateTags to indicate how many blank PCID tags should be generated in the HH Count Entry. Field was added because cycle header is not used in HH Count Entry so cannot use similar field from CCHdr table  """  
      self.HHNumOfBlankTags:int = obj["HHNumOfBlankTags"]
      """  This field used by GenerateTags to indicate how many blank tags should be generated in the HH Count Entry. Field was added because cycle header is not used in HH Count Entry so cannot use similar field from CCHdr table  """  
      self.EnableBinNum:bool = obj["EnableBinNum"]
      """  Flag to set row rule to know if CCTag.BinNum should be enabled in UI  """  
      self.EnableReturnNestedPCID:bool = obj["EnableReturnNestedPCID"]
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.DisableRevisionNum:bool = obj["DisableRevisionNum"]
      self.BitFlag:int = obj["BitFlag"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.CCPeriodDefnPeriodEnd:str = obj["CCPeriodDefnPeriodEnd"]
      self.CCPeriodDefnPeriodDesc:str = obj["CCPeriodDefnPeriodDesc"]
      self.CCPeriodDefnPeriodStart:str = obj["CCPeriodDefnPeriodStart"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.WarehseDescription:str = obj["WarehseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   plant
   warehouseCode
   tagNum
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.warehouseCode:str = obj["warehouseCode"]
      self.tagNum:str = obj["tagNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CCTagListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Bindesc:str = obj["Bindesc"]
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Unique identifier for this warehouse assigned by the user.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number selected for counting.  """  
      self.TagNum:str = obj["TagNum"]
      """  Tag number. This will be generated from Warehse and will be in the format of tagNum.countseq where countSeq is the count/recount sequence. First count for example would be tag 000000001.1 recount generate tag 000000001.2 from tag 000000001.1, second recount would generate tag 000000001.3  the same part, etc.  """  
      self.TagSelForVoid:bool = obj["TagSelForVoid"]
      self.BinNum:str = obj["BinNum"]
      """  Bin number for the tag  """  
      self.CountedBy:str = obj["CountedBy"]
      """  Person that counted the parts on the Count Tag.  """  
      self.WrehouseCode:str = obj["WrehouseCode"]
      self.CountedQty:int = obj["CountedQty"]
      """  Quantity counted for the tag. Like PartBin.OnHandQty except no negative allowed. This is expressed in the qty per the CCTag.UOM unit of measure, which may not be the Part base UOM.  """  
      self.WarehseDesc:str = obj["WarehseDesc"]
      self.CountedTime:str = obj["CountedTime"]
      """  Optional field that Indicates when the count took place to aid in determining what activity took place before the actual count.  """  
      self.TagReturned:bool = obj["TagReturned"]
      """  Indicates the Count Tag has been returned and the results entered into the count.  This is set when during Tag Entry when the user keys in a counted amount (or voids the tag).  System Set.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TopLevelPCID:str = obj["TopLevelPCID"]
      """  The outermost PCID that contains this CCPDICTag.PCID  """  
      self.PCID:str = obj["PCID"]
      """  Parent PCID that this tag is associated with. Equates similar to the way PkgControlItem.PCID relates to PkgControlHeader.PCID  """  
      self.ItemPCID:str = obj["ItemPCID"]
      """  Child PCID, equates to a PkgControlItem.ItemPCID. Either ItemPCID or ItemPartNum will be populated but never both, as is done in PkgControlItem table.  """  
      self.TagStatusDesc:str = obj["TagStatusDesc"]
      """  Tag Status Description  """  
      self.CCTagCharacter02:str = obj["CCTagCharacter02"]
      """  Tag Type for PCID tag  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.AttributeSetIDDescription:str = obj["AttributeSetIDDescription"]
      self.AttributeSetIDShortDescription:str = obj["AttributeSetIDShortDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CCTagListTableset:
   def __init__(self, obj):
      self.CCTagList:list[Erp_Tablesets_CCTagListRow] = obj["CCTagList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CCTagRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Unique identifier for this warehouse assigned by the user.  """  
      self.Plant:str = obj["Plant"]
      """  The Site (Site.Site) that the warehouse is associated with. If a warehouse is shared between multiple Sites, the SiteShared table will be utilized to associate additional Sites with this warehouse.  """  
      self.CCYear:int = obj["CCYear"]
      """  Calendar year that this cycle count control record is for.  """  
      self.CCMonth:int = obj["CCMonth"]
      """  CCPeriodDefn.CycleSeq that this cycle count control record is for.  """  
      self.FullPhysical:bool = obj["FullPhysical"]
      """  Indicates that the count cycle is either a cycle count cycle or a full physical inventory count cycle.  Full Physical Inventory cycles are for the entire set of parts in the warehouse(s) and this record was created by Initialize Physical Inventory process.  Cycle Counts are only for a limited number of parts at one time and this record was created by the Cycle Count Schedule Maintenance process. Required as part of the primary key because full physical and cycle count cycles can be set for the same whs/monthy/year  """  
      self.CycleSeq:int = obj["CycleSeq"]
      """  Cycle sequence number, used to keep the primary index unique since there can be multiple cycles set up for the same date.  """  
      self.PartNum:str = obj["PartNum"]
      """  Part Number selected for counting.  """  
      self.TagNum:str = obj["TagNum"]
      """  Tag number. This will be generated from Warehse and will be in the format of tagNum.countseq where countSeq is the count/recount sequence. First count for example would be tag 000000001.1 recount generate tag 000000001.2 from tag 000000001.1, second recount would generate tag 000000001.3  the same part, etc.  """  
      self.BinNum:str = obj["BinNum"]
      """  Bin number for the tag  """  
      self.CountedBy:str = obj["CountedBy"]
      """  Person that counted the parts on the Count Tag.  """  
      self.CountedQty:int = obj["CountedQty"]
      """  Quantity counted for the tag. Like PartBin.OnHandQty except no negative allowed. This is expressed in the qty per the CCTag.UOM unit of measure, which may not be the Part base UOM.  """  
      self.CountedTime:str = obj["CountedTime"]
      """  Optional field that Indicates when the count took place to aid in determining what activity took place before the actual count.  """  
      self.TagNote:str = obj["TagNote"]
      """  Tag Note  """  
      self.EntryPerson:str = obj["EntryPerson"]
      """  This field is set equal to the Login ID variable.  System Set when a user enters a counted amount for the tag or voids the tag.  """  
      self.TagPrinted:bool = obj["TagPrinted"]
      """  Indicates that the Count Tag has been printed.  Manually entered tags are set to "Printed" when they are entered.  System Set.  """  
      self.TagReturned:bool = obj["TagReturned"]
      """  Indicates the Count Tag has been returned and the results entered into the count.  This is set when during Tag Entry when the user keys in a counted amount (or voids the tag).  System Set.  """  
      self.CountedDate:str = obj["CountedDate"]
      """  Date the count was performed.  """  
      self.TagStatus:int = obj["TagStatus"]
      """   Tag status.
Code/Desc:
0 = open
1 = posted
2 = voided 3=Closed/Recount.  """  
      self.BlankTag:bool = obj["BlankTag"]
      """  True = this tag was generated as a blank tag. This will control whether bin/lot/serial data can be changed on the tag and whether the tag can be voided independent of other tags generated for an part.  """  
      self.LotNum:str = obj["LotNum"]
      """  LotNum for the tag  """  
      self.SerialNumber:str = obj["SerialNumber"]
      """  Serial number.  """  
      self.UOM:str = obj["UOM"]
      """  The PartBin Unit of measure for this tag.  """  
      self.FrozenQOH:int = obj["FrozenQOH"]
      """  QOH in PartBin at the time the inventory was frozen. This is expressed in the qty per the CCTag.UOM unit of measure, which may not be the Part base UOM. For blank tags this will be zero.  """  
      self.FrozenCost:int = obj["FrozenCost"]
      """  The per unit part cost at the time the quantity was frozen, based on the costing method for the part/Site. This is the unit cost based on the part base UOM, which might not be the CCTag.UOM so to get total frozen cost for this tag, the CCTag quantities wi  """  
      self.EntryDate:str = obj["EntryDate"]
      """  The date the count was entered or tag was voided  """  
      self.EntryTime:int = obj["EntryTime"]
      """  The time the count was entered or tag was voided  """  
      self.SheetNum:int = obj["SheetNum"]
      """  The sheet number the tag is assigned to. If the sheet is being accessed by enter count by sheet, tags tied to that sheet cannot be accessed individually until the sheet record is unlocked.  """  
      self.FrozenTranDate:str = obj["FrozenTranDate"]
      """  The PartTran.SysDate for the last PartTran for this part when  the quantity was frozen, used with FrozentTranNum and FrozenTranTime to determine what activity has taken place after the freeze.  """  
      self.FrozenTranTime:int = obj["FrozenTranTime"]
      """  The PartTran.SysTime for the last PartTran for this part when  the quantity was frozen, used with FrozentTranDate and FrozenTranNum to determine what activity has taken place after the freeze.  """  
      self.ActivityBeforeCount:int = obj["ActivityBeforeCount"]
      """  Manually entered by the user to account for ongoing activity that took place during the count.  Inventory activity that took place AFTER the start of the count FrozenQOH), but BEFORE the actual count.  This number is used to adjust the "FrozenQOH" when determining the variance between the Frozen Quantity and the Actual Counted Quantity.  Example:  At 1:00 the count is started and the computer has 250 units on hand for part XYZ.  At 1:30 75 units are issued to a job.  At 2:30 John counts 175 units.  The variance report would report a variance of 75 units and show the issue as activity.  The user could then decide that the issue took place before the count took place and enter 75 units into the Activity Before Count field in Tag Maintenance.  The variance report would then "expect" 175 units and have a count of 175 units for a variance of zero(0).  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PCIDTag:bool = obj["PCIDTag"]
      """  True indicates this tag is associated with a PCID, false indicates this tag is associated to loose inventory (non-PCID)  """  
      self.TopLevelPCID:str = obj["TopLevelPCID"]
      """  The outermost PCID that contains this CCPDICTag.PCID  """  
      self.PCID:str = obj["PCID"]
      """  Parent PCID that this tag is associated with. Equates similar to the way PkgControlItem.PCID relates to PkgControlHeader.PCID  """  
      self.ItemPCID:str = obj["ItemPCID"]
      """  Child PCID, equates to a PkgControlItem.ItemPCID. Either ItemPCID or ItemPartNum will be populated but never both, as is done in PkgControlItem table.  """  
      self.ReturnNestedPCID:bool = obj["ReturnNestedPCID"]
      """  Only applies if ItemPCID has data. True = indicates in Count Entry that all of the related CCPCIDTag records for this CCPCIDTag.ItemPCID and all lower level nested child PCIDs/Parts should be set to TagReturned = true and  for ItemPartNum records set CountedQty = FrozenQty as if the user had accessed each of the tags and manually entered.  """  
      self.CCTagBoolean01:bool = obj["CCTagBoolean01"]
      """  CCTagBoolean01  """  
      self.CCTagBoolean02:bool = obj["CCTagBoolean02"]
      """  CCTagBoolean02  """  
      self.CCTagCharacter01:str = obj["CCTagCharacter01"]
      """  Move To Bin for the tag  """  
      self.CCTagCharacter02:str = obj["CCTagCharacter02"]
      """  Tag Type for PCID tag  """  
      self.CCTagCharacter03:str = obj["CCTagCharacter03"]
      """  CCTagCharacter03  """  
      self.CCTagCharacter04:str = obj["CCTagCharacter04"]
      """  CCTagCharacter04  """  
      self.CCTagCharacter05:str = obj["CCTagCharacter05"]
      """  Source data used to generate the default serial tag when no standard tag is generated from SerialNo, PartBinQOH or  PrimaryBin  """  
      self.CCTagDate01:str = obj["CCTagDate01"]
      """  CCTagDate01  """  
      self.CCTagDate02:str = obj["CCTagDate02"]
      """  CCTagDate02  """  
      self.CCTagDecimal01:int = obj["CCTagDecimal01"]
      """  CCTagDecimal01  """  
      self.CCTagDecimal02:int = obj["CCTagDecimal02"]
      """  CCTagDecimal02  """  
      self.CCTagInteger01:int = obj["CCTagInteger01"]
      """  CCTagInteger01  """  
      self.CCTagInteger02:int = obj["CCTagInteger02"]
      """  CCTagInteger02  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set.  """  
      self.NumberOfPieces:int = obj["NumberOfPieces"]
      """  Number of pieces for this attribute set.  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  Revision number which is used to uniquely identify the revision of the part.  """  
      self.CountedQtyWarn:str = obj["CountedQtyWarn"]
      self.EnableLotNo:bool = obj["EnableLotNo"]
      self.EnableSerialNo:bool = obj["EnableSerialNo"]
      self.EnableUOMWorksheet:bool = obj["EnableUOMWorksheet"]
      """  True when UOM Worksheet must be enabled  """  
      self.HasActivity:str = obj["HasActivity"]
      """  This field is to indicate there is data in the activity grid to cue the user to consult the detail sheet before entering counts.  """  
      self.SavedBlankTag:bool = obj["SavedBlankTag"]
      self.SelectedForVoid:bool = obj["SelectedForVoid"]
      """  External field. Used by the Void Blank Tags processing to indicate the tag was selected for void.  """  
      self.TagStatusDesc:str = obj["TagStatusDesc"]
      """  Tag Status Description  """  
      self.UOMDO:str = obj["UOMDO"]
      """  Display Only Unit Of Measure.  """  
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      self.EnablePCID:bool = obj["EnablePCID"]
      self.EnableItemPCID:bool = obj["EnableItemPCID"]
      self.IsNestedPCID:bool = obj["IsNestedPCID"]
      self.IsItemQty:bool = obj["IsItemQty"]
      self.MoveToBinDescription:str = obj["MoveToBinDescription"]
      self.TagTypeDescList:str = obj["TagTypeDescList"]
      """  Used for Code Desc list to allow changing this list by manually setting in code logic.  """  
      self.TagTypeDescription:str = obj["TagTypeDescription"]
      """  Tag Type Description  """  
      self.EnableTagType:bool = obj["EnableTagType"]
      self.EnableGenLowerNestedPCID:bool = obj["EnableGenLowerNestedPCID"]
      self.HHNumOfBlankPCIDTags:int = obj["HHNumOfBlankPCIDTags"]
      """  This field used by GenerateTags to indicate how many blank PCID tags should be generated in the HH Count Entry. Field was added because cycle header is not used in HH Count Entry so cannot use similar field from CCHdr table  """  
      self.HHNumOfBlankTags:int = obj["HHNumOfBlankTags"]
      """  This field used by GenerateTags to indicate how many blank tags should be generated in the HH Count Entry. Field was added because cycle header is not used in HH Count Entry so cannot use similar field from CCHdr table  """  
      self.EnableBinNum:bool = obj["EnableBinNum"]
      """  Flag to set row rule to know if CCTag.BinNum should be enabled in UI  """  
      self.EnableReturnNestedPCID:bool = obj["EnableReturnNestedPCID"]
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  The Short Description of the Attribute Set.  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  The Full Description of the Attribute Set.  """  
      self.EnableAttributeSetSearch:bool = obj["EnableAttributeSetSearch"]
      self.DispNumberOfPieces:int = obj["DispNumberOfPieces"]
      """  Number of pieces for inventory attribute tracked parts.  """  
      self.DisableRevisionNum:bool = obj["DisableRevisionNum"]
      self.BitFlag:int = obj["BitFlag"]
      self.BinNumDescription:str = obj["BinNumDescription"]
      self.CCPeriodDefnPeriodEnd:str = obj["CCPeriodDefnPeriodEnd"]
      self.CCPeriodDefnPeriodDesc:str = obj["CCPeriodDefnPeriodDesc"]
      self.CCPeriodDefnPeriodStart:str = obj["CCPeriodDefnPeriodStart"]
      self.PartNumTrackInventoryByRevision:bool = obj["PartNumTrackInventoryByRevision"]
      self.PartNumAttrClassID:str = obj["PartNumAttrClassID"]
      self.PartNumSalesUM:str = obj["PartNumSalesUM"]
      self.PartNumTrackDimension:bool = obj["PartNumTrackDimension"]
      self.PartNumIUM:str = obj["PartNumIUM"]
      self.PartNumPartDescription:str = obj["PartNumPartDescription"]
      self.PartNumTrackLots:bool = obj["PartNumTrackLots"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      self.PartNumSellingFactor:int = obj["PartNumSellingFactor"]
      self.PartNumPricePerCode:str = obj["PartNumPricePerCode"]
      self.PartNumTrackInventoryAttributes:bool = obj["PartNumTrackInventoryAttributes"]
      self.WarehseDescription:str = obj["WarehseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CCTagSearchTableset:
   def __init__(self, obj):
      self.CCTag:list[Erp_Tablesets_CCTagRow] = obj["CCTag"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtCCTagSearchTableset:
   def __init__(self, obj):
      self.CCTag:list[Erp_Tablesets_CCTagRow] = obj["CCTag"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   plant
   warehouseCode
   tagNum
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.warehouseCode:str = obj["warehouseCode"]
      self.tagNum:str = obj["tagNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CCTagSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CCTagSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CCTagSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CCTagListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCCTag_input:
   """ Required : 
   ds
   plant
   warehouseCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CCTagSearchTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      self.warehouseCode:str = obj["warehouseCode"]
      pass

class GetNewCCTag_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CCTagSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCCTag
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCCTag:str = obj["whereClauseCCTag"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CCTagSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtCCTagSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCCTagSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CCTagSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CCTagSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

