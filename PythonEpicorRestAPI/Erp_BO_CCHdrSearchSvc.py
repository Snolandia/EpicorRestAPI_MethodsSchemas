import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CCHdrSearchSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CCHdrSearches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CCHdrSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CCHdrSearches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCHdrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/CCHdrSearches",headers=creds) as resp:
           return await resp.json()

async def post_CCHdrSearches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CCHdrSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CCHdrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CCHdrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/CCHdrSearches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CCHdrSearches_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq(Company, Plant, WarehouseCode, CCYear, CCMonth, FullPhysical, CycleSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CCHdrSearch item
   Description: Calls GetByID to retrieve the CCHdrSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CCHdrSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param CCYear: Desc: CCYear   Required: True
      :param CCMonth: Desc: CCMonth   Required: True
      :param FullPhysical: Desc: FullPhysical   Required: True
      :param CycleSeq: Desc: CycleSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CCHdrRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/CCHdrSearches(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CCHdrSearches_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq(Company, Plant, WarehouseCode, CCYear, CCMonth, FullPhysical, CycleSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CCHdrSearch for the service
   Description: Calls UpdateExt to update CCHdrSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CCHdrSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param CCYear: Desc: CCYear   Required: True
      :param CCMonth: Desc: CCMonth   Required: True
      :param FullPhysical: Desc: FullPhysical   Required: True
      :param CycleSeq: Desc: CycleSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CCHdrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/CCHdrSearches(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CCHdrSearches_Company_Plant_WarehouseCode_CCYear_CCMonth_FullPhysical_CycleSeq(Company, Plant, WarehouseCode, CCYear, CCMonth, FullPhysical, CycleSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CCHdrSearch item
   Description: Call UpdateExt to delete CCHdrSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CCHdrSearch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param WarehouseCode: Desc: WarehouseCode   Required: True   Allow empty value : True
      :param CCYear: Desc: CCYear   Required: True
      :param CCMonth: Desc: CCMonth   Required: True
      :param FullPhysical: Desc: FullPhysical   Required: True
      :param CycleSeq: Desc: CycleSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/CCHdrSearches(" + Company + "," + Plant + "," + WarehouseCode + "," + CCYear + "," + CCMonth + "," + FullPhysical + "," + CycleSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CCHdrListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCCHdr, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseCCHdr=" + whereClauseCCHdr
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(plant, warehouseCode, ccYear, ccMonth, fullPhysical, cycleSeq, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
   Required: True
   Required: True
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
   params += "ccYear=" + ccYear
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ccMonth=" + ccMonth
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "fullPhysical=" + fullPhysical
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "cycleSeq=" + cycleSeq

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCCHdr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCCHdr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCCHdr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCCHdr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCCHdr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CCHdrSearchSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCHdrListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CCHdrListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CCHdrRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CCHdrRow] = obj["value"]
      pass

class Erp_Tablesets_CCHdrListRow:
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
      self.CycleDate:str = obj["CycleDate"]
      """  The date the cycle is scheduled to begin. This data is initialized in the warehouse cycle count scheduling process.  """  
      self.CycleStatus:int = obj["CycleStatus"]
      """   This code will indicate the status of the cycle. When status is zero the cycle is scheduled but not started. Inventory is frozen at sequence start.
Code/Desc:
0 = scheduled 
1 = tags generated
2 = Count started 
3 = counts entered
4 = recount tags generated 5 = (not used) 
6 = completed
7= canceled.  """  
      self.TagGenDate:str = obj["TagGenDate"]
      """  This is the date the tags were generated  """  
      self.SeqStartDate:str = obj["SeqStartDate"]
      """  This is the date the cycle sequence was started. This is when the inventory counts were frozen.  """  
      self.TimeSeqStarted:int = obj["TimeSeqStarted"]
      """  This is the time the cycle sequence was started and inventory counts were frozen.  """  
      self.CompleteDate:str = obj["CompleteDate"]
      """  This is the date the cycle was completed or cancelled.  """  
      self.CompleteTime:int = obj["CompleteTime"]
      """  This is the time the cycle was completed or cancelled.  """  
      self.AdjustPosted:bool = obj["AdjustPosted"]
      """  Indicated whether adjustments have been posted to inventory. True =  the count posting process has been run at least once for this cycle. False = no adjustments have been posted to inventory.  """  
      self.SheetOrTag:int = obj["SheetOrTag"]
      """   Indicates whether sheets or tags were printed for this cycle.
Code/desc:
0 = no tags have been printed for the cycle
1 =  tags
2 = sheets  """  
      self.TotalParts:int = obj["TotalParts"]
      """  This is the total number of parts scheduled for this cycle at the time the count sequence was started.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number of the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TotalPCIDSelected:int = obj["TotalPCIDSelected"]
      """  The total number of top level PCIDs selected for this cycle.  """  
      self.NumOfBlankTags:int = obj["NumOfBlankTags"]
      """  field used by GenerateTags to indicate how many blank tags should be generated  """  
      self.BlankTagsOnly:bool = obj["BlankTagsOnly"]
      """  field used by Generate Tags logic to control when the user is limited to generating blank tags only  """  
      self.TagSortOption:int = obj["TagSortOption"]
      """  field to indicate the sort order for tag generation.  Enter data in the Code/Desc field: 0 = Bin/UOM.Lot 1 = PartClass/Bin/Part/UOM/Lot 2 = Part/Bin/UOM/Lot  """  
      self.PostTransDate:str = obj["PostTransDate"]
      """  External field to be used as the transaction date for the PartTran records created during post adjustments.  """  
      self.LogFileName:str = obj["LogFileName"]
      """  External field used to hold the Post Counts log filename.  """  
      self.EnablePrintTags:bool = obj["EnablePrintTags"]
      self.EnableReprintTags:bool = obj["EnableReprintTags"]
      self.EnableVoidTagsByPart:bool = obj["EnableVoidTagsByPart"]
      self.EnableVoidBlankTags:bool = obj["EnableVoidBlankTags"]
      self.EnableStartCountSeq:bool = obj["EnableStartCountSeq"]
      self.RemoveAllParts:bool = obj["RemoveAllParts"]
      """  Flag to indicate that all CCDtl (parts) should be removed from the CCHdr. Used by Cycle Count part Selection Update  """  
      self.CycleDateString:str = obj["CycleDateString"]
      self.CycleStatusDesc:str = obj["CycleStatusDesc"]
      """  0 = Scheduled, 1=Tags Generated, 2=Count Started,3=Counts Entered,4=Recount Tags Generated,5=Not Used,6=Completed,7=Cancelled  """  
      self.CancelPI:bool = obj["CancelPI"]
      """  Used to indicate to the BL that the physical inventory cycle should be cancelled.  """  
      self.MonthName:str = obj["MonthName"]
      """  Month Name  """  
      self.CCHdrWarehseDescription:str = obj["CCHdrWarehseDescription"]
      """  Description.  """  
      self.CCPeriodDefnPeriodEnd:str = obj["CCPeriodDefnPeriodEnd"]
      """  Defines the end date of the period  """  
      self.CCPeriodDefnPeriodStart:str = obj["CCPeriodDefnPeriodStart"]
      """  Defines the start date of the count period  """  
      self.CCPeriodDefnPeriodDesc:str = obj["CCPeriodDefnPeriodDesc"]
      """  Unique period description assigned by the user.  """  
      self.WhseCodeDescription:str = obj["WhseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CCHdrRow:
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
      self.CycleDate:str = obj["CycleDate"]
      """  The date the cycle is scheduled to begin. This data is initialized in the warehouse cycle count scheduling process.  """  
      self.CycleStatus:int = obj["CycleStatus"]
      """   This code will indicate the status of the cycle. When status is zero the cycle is scheduled but not started. Inventory is frozen at sequence start.
Code/Desc:
0 = scheduled 
1 = tags generated
2 = Count started 
3 = counts entered
4 = recount tags generated 5 = (not used) 
6 = completed
7= canceled.  """  
      self.TagGenDate:str = obj["TagGenDate"]
      """  This is the date the tags were generated  """  
      self.SeqStartDate:str = obj["SeqStartDate"]
      """  This is the date the cycle sequence was started. This is when the inventory counts were frozen.  """  
      self.TimeSeqStarted:int = obj["TimeSeqStarted"]
      """  This is the time the cycle sequence was started and inventory counts were frozen.  """  
      self.CompleteDate:str = obj["CompleteDate"]
      """  This is the date the cycle was completed or cancelled.  """  
      self.CompleteTime:int = obj["CompleteTime"]
      """  This is the time the cycle was completed or cancelled.  """  
      self.AdjustPosted:bool = obj["AdjustPosted"]
      """  Indicated whether adjustments have been posted to inventory. True =  the count posting process has been run at least once for this cycle. False = no adjustments have been posted to inventory.  """  
      self.SheetOrTag:int = obj["SheetOrTag"]
      """   Indicates whether sheets or tags were printed for this cycle.
Code/desc:
0 = no tags have been printed for the cycle
1 =  tags
2 = sheets  """  
      self.TotalParts:int = obj["TotalParts"]
      """  This is the total number of parts scheduled for this cycle at the time the count sequence was started.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number of the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IncludeNonNettable:bool = obj["IncludeNonNettable"]
      """  IncludeNonNettable  """  
      self.TotalPCIDSelected:int = obj["TotalPCIDSelected"]
      """  The total number of top level PCIDs selected for this cycle.  """  
      self.NestedPCID:bool = obj["NestedPCID"]
      """  On the Generate Tags form, True = CCPDICTags are generated for the top level PCIDs already selected for this Cycle and for the related nested PCIDs and ItemPartNum. False = PCID tags will only be generated for the top level PCIDs already selected for this Cycle.  """  
      self.CancelPI:bool = obj["CancelPI"]
      """  Used to indicate to the BL that the physical inventory cycle should be cancelled.  """  
      self.CycleDateString:str = obj["CycleDateString"]
      self.CycleStatusDesc:str = obj["CycleStatusDesc"]
      """  0 = Scheduled, 1=Tags Generated, 2=Count Started,3=Counts Entered,4=Recount Tags Generated,5=Not Used,6=Completed,7=Cancelled  """  
      self.EnablePrintTags:bool = obj["EnablePrintTags"]
      self.EnableReprintTags:bool = obj["EnableReprintTags"]
      self.EnableStartCountSeq:bool = obj["EnableStartCountSeq"]
      self.EnableVoidBlankTags:bool = obj["EnableVoidBlankTags"]
      self.EnableVoidTagsByPart:bool = obj["EnableVoidTagsByPart"]
      self.LogFileName:str = obj["LogFileName"]
      """  External field used to hold the Post Counts log filename.  """  
      self.MonthName:str = obj["MonthName"]
      """  Month Name  """  
      self.NumOfBlankTags:int = obj["NumOfBlankTags"]
      """  field used by GenerateTags to indicate how many blank tags should be generated  """  
      self.PostTransDate:str = obj["PostTransDate"]
      """  External field to be used as the transaction date for the PartTran records created during post adjustments.  """  
      self.RemoveAllParts:bool = obj["RemoveAllParts"]
      """  Flag to indicate that all CCDtl (parts) should be removed from the CCHdr. Used by Cycle Count part Selection Update  """  
      self.TagSortOption:int = obj["TagSortOption"]
      """  field to indicate the sort order for tag generation.  Enter data in the Code/Desc field: 0 = Bin/UOM.Lot 1 = PartClass/Bin/Part/UOM/Lot 2 = Part/Bin/UOM/Lot  """  
      self.BlankTagsOnly:bool = obj["BlankTagsOnly"]
      """  field used by Generate Tags logic to control when the user is limited to generating blank tags only  """  
      self.NumOfBlankPCIDTags:int = obj["NumOfBlankPCIDTags"]
      """  field used by GenerateTags to indicate how many blank PCID tags should be generated  """  
      self.PartPostedExists:bool = obj["PartPostedExists"]
      self.TrackedNumberSerialPart:bool = obj["TrackedNumberSerialPart"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates that any PartNumTrackSerialNum = true exist in details  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CCHdrWarehseDescription:str = obj["CCHdrWarehseDescription"]
      self.CCPeriodDefnPeriodStart:str = obj["CCPeriodDefnPeriodStart"]
      self.CCPeriodDefnPeriodDesc:str = obj["CCPeriodDefnPeriodDesc"]
      self.CCPeriodDefnPeriodEnd:str = obj["CCPeriodDefnPeriodEnd"]
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
   ccYear
   ccMonth
   fullPhysical
   cycleSeq
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.warehouseCode:str = obj["warehouseCode"]
      self.ccYear:int = obj["ccYear"]
      self.ccMonth:int = obj["ccMonth"]
      self.fullPhysical:bool = obj["fullPhysical"]
      self.cycleSeq:int = obj["cycleSeq"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CCHdrListRow:
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
      self.CycleDate:str = obj["CycleDate"]
      """  The date the cycle is scheduled to begin. This data is initialized in the warehouse cycle count scheduling process.  """  
      self.CycleStatus:int = obj["CycleStatus"]
      """   This code will indicate the status of the cycle. When status is zero the cycle is scheduled but not started. Inventory is frozen at sequence start.
Code/Desc:
0 = scheduled 
1 = tags generated
2 = Count started 
3 = counts entered
4 = recount tags generated 5 = (not used) 
6 = completed
7= canceled.  """  
      self.TagGenDate:str = obj["TagGenDate"]
      """  This is the date the tags were generated  """  
      self.SeqStartDate:str = obj["SeqStartDate"]
      """  This is the date the cycle sequence was started. This is when the inventory counts were frozen.  """  
      self.TimeSeqStarted:int = obj["TimeSeqStarted"]
      """  This is the time the cycle sequence was started and inventory counts were frozen.  """  
      self.CompleteDate:str = obj["CompleteDate"]
      """  This is the date the cycle was completed or cancelled.  """  
      self.CompleteTime:int = obj["CompleteTime"]
      """  This is the time the cycle was completed or cancelled.  """  
      self.AdjustPosted:bool = obj["AdjustPosted"]
      """  Indicated whether adjustments have been posted to inventory. True =  the count posting process has been run at least once for this cycle. False = no adjustments have been posted to inventory.  """  
      self.SheetOrTag:int = obj["SheetOrTag"]
      """   Indicates whether sheets or tags were printed for this cycle.
Code/desc:
0 = no tags have been printed for the cycle
1 =  tags
2 = sheets  """  
      self.TotalParts:int = obj["TotalParts"]
      """  This is the total number of parts scheduled for this cycle at the time the count sequence was started.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number of the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TotalPCIDSelected:int = obj["TotalPCIDSelected"]
      """  The total number of top level PCIDs selected for this cycle.  """  
      self.NumOfBlankTags:int = obj["NumOfBlankTags"]
      """  field used by GenerateTags to indicate how many blank tags should be generated  """  
      self.BlankTagsOnly:bool = obj["BlankTagsOnly"]
      """  field used by Generate Tags logic to control when the user is limited to generating blank tags only  """  
      self.TagSortOption:int = obj["TagSortOption"]
      """  field to indicate the sort order for tag generation.  Enter data in the Code/Desc field: 0 = Bin/UOM.Lot 1 = PartClass/Bin/Part/UOM/Lot 2 = Part/Bin/UOM/Lot  """  
      self.PostTransDate:str = obj["PostTransDate"]
      """  External field to be used as the transaction date for the PartTran records created during post adjustments.  """  
      self.LogFileName:str = obj["LogFileName"]
      """  External field used to hold the Post Counts log filename.  """  
      self.EnablePrintTags:bool = obj["EnablePrintTags"]
      self.EnableReprintTags:bool = obj["EnableReprintTags"]
      self.EnableVoidTagsByPart:bool = obj["EnableVoidTagsByPart"]
      self.EnableVoidBlankTags:bool = obj["EnableVoidBlankTags"]
      self.EnableStartCountSeq:bool = obj["EnableStartCountSeq"]
      self.RemoveAllParts:bool = obj["RemoveAllParts"]
      """  Flag to indicate that all CCDtl (parts) should be removed from the CCHdr. Used by Cycle Count part Selection Update  """  
      self.CycleDateString:str = obj["CycleDateString"]
      self.CycleStatusDesc:str = obj["CycleStatusDesc"]
      """  0 = Scheduled, 1=Tags Generated, 2=Count Started,3=Counts Entered,4=Recount Tags Generated,5=Not Used,6=Completed,7=Cancelled  """  
      self.CancelPI:bool = obj["CancelPI"]
      """  Used to indicate to the BL that the physical inventory cycle should be cancelled.  """  
      self.MonthName:str = obj["MonthName"]
      """  Month Name  """  
      self.CCHdrWarehseDescription:str = obj["CCHdrWarehseDescription"]
      """  Description.  """  
      self.CCPeriodDefnPeriodEnd:str = obj["CCPeriodDefnPeriodEnd"]
      """  Defines the end date of the period  """  
      self.CCPeriodDefnPeriodStart:str = obj["CCPeriodDefnPeriodStart"]
      """  Defines the start date of the count period  """  
      self.CCPeriodDefnPeriodDesc:str = obj["CCPeriodDefnPeriodDesc"]
      """  Unique period description assigned by the user.  """  
      self.WhseCodeDescription:str = obj["WhseCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CCHdrListTableset:
   def __init__(self, obj):
      self.CCHdrList:list[Erp_Tablesets_CCHdrListRow] = obj["CCHdrList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CCHdrRow:
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
      self.CycleDate:str = obj["CycleDate"]
      """  The date the cycle is scheduled to begin. This data is initialized in the warehouse cycle count scheduling process.  """  
      self.CycleStatus:int = obj["CycleStatus"]
      """   This code will indicate the status of the cycle. When status is zero the cycle is scheduled but not started. Inventory is frozen at sequence start.
Code/Desc:
0 = scheduled 
1 = tags generated
2 = Count started 
3 = counts entered
4 = recount tags generated 5 = (not used) 
6 = completed
7= canceled.  """  
      self.TagGenDate:str = obj["TagGenDate"]
      """  This is the date the tags were generated  """  
      self.SeqStartDate:str = obj["SeqStartDate"]
      """  This is the date the cycle sequence was started. This is when the inventory counts were frozen.  """  
      self.TimeSeqStarted:int = obj["TimeSeqStarted"]
      """  This is the time the cycle sequence was started and inventory counts were frozen.  """  
      self.CompleteDate:str = obj["CompleteDate"]
      """  This is the date the cycle was completed or cancelled.  """  
      self.CompleteTime:int = obj["CompleteTime"]
      """  This is the time the cycle was completed or cancelled.  """  
      self.AdjustPosted:bool = obj["AdjustPosted"]
      """  Indicated whether adjustments have been posted to inventory. True =  the count posting process has been run at least once for this cycle. False = no adjustments have been posted to inventory.  """  
      self.SheetOrTag:int = obj["SheetOrTag"]
      """   Indicates whether sheets or tags were printed for this cycle.
Code/desc:
0 = no tags have been printed for the cycle
1 =  tags
2 = sheets  """  
      self.TotalParts:int = obj["TotalParts"]
      """  This is the total number of parts scheduled for this cycle at the time the count sequence was started.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction Document Type  """  
      self.LegalNumber:str = obj["LegalNumber"]
      """  The Legal Number of the record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.IncludeNonNettable:bool = obj["IncludeNonNettable"]
      """  IncludeNonNettable  """  
      self.TotalPCIDSelected:int = obj["TotalPCIDSelected"]
      """  The total number of top level PCIDs selected for this cycle.  """  
      self.NestedPCID:bool = obj["NestedPCID"]
      """  On the Generate Tags form, True = CCPDICTags are generated for the top level PCIDs already selected for this Cycle and for the related nested PCIDs and ItemPartNum. False = PCID tags will only be generated for the top level PCIDs already selected for this Cycle.  """  
      self.CancelPI:bool = obj["CancelPI"]
      """  Used to indicate to the BL that the physical inventory cycle should be cancelled.  """  
      self.CycleDateString:str = obj["CycleDateString"]
      self.CycleStatusDesc:str = obj["CycleStatusDesc"]
      """  0 = Scheduled, 1=Tags Generated, 2=Count Started,3=Counts Entered,4=Recount Tags Generated,5=Not Used,6=Completed,7=Cancelled  """  
      self.EnablePrintTags:bool = obj["EnablePrintTags"]
      self.EnableReprintTags:bool = obj["EnableReprintTags"]
      self.EnableStartCountSeq:bool = obj["EnableStartCountSeq"]
      self.EnableVoidBlankTags:bool = obj["EnableVoidBlankTags"]
      self.EnableVoidTagsByPart:bool = obj["EnableVoidTagsByPart"]
      self.LogFileName:str = obj["LogFileName"]
      """  External field used to hold the Post Counts log filename.  """  
      self.MonthName:str = obj["MonthName"]
      """  Month Name  """  
      self.NumOfBlankTags:int = obj["NumOfBlankTags"]
      """  field used by GenerateTags to indicate how many blank tags should be generated  """  
      self.PostTransDate:str = obj["PostTransDate"]
      """  External field to be used as the transaction date for the PartTran records created during post adjustments.  """  
      self.RemoveAllParts:bool = obj["RemoveAllParts"]
      """  Flag to indicate that all CCDtl (parts) should be removed from the CCHdr. Used by Cycle Count part Selection Update  """  
      self.TagSortOption:int = obj["TagSortOption"]
      """  field to indicate the sort order for tag generation.  Enter data in the Code/Desc field: 0 = Bin/UOM.Lot 1 = PartClass/Bin/Part/UOM/Lot 2 = Part/Bin/UOM/Lot  """  
      self.BlankTagsOnly:bool = obj["BlankTagsOnly"]
      """  field used by Generate Tags logic to control when the user is limited to generating blank tags only  """  
      self.NumOfBlankPCIDTags:int = obj["NumOfBlankPCIDTags"]
      """  field used by GenerateTags to indicate how many blank PCID tags should be generated  """  
      self.PartPostedExists:bool = obj["PartPostedExists"]
      self.TrackedNumberSerialPart:bool = obj["TrackedNumberSerialPart"]
      self.PartNumTrackSerialNum:bool = obj["PartNumTrackSerialNum"]
      """  Indicates that any PartNumTrackSerialNum = true exist in details  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CCHdrWarehseDescription:str = obj["CCHdrWarehseDescription"]
      self.CCPeriodDefnPeriodStart:str = obj["CCPeriodDefnPeriodStart"]
      self.CCPeriodDefnPeriodDesc:str = obj["CCPeriodDefnPeriodDesc"]
      self.CCPeriodDefnPeriodEnd:str = obj["CCPeriodDefnPeriodEnd"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CCHdrSearchTableset:
   def __init__(self, obj):
      self.CCHdr:list[Erp_Tablesets_CCHdrRow] = obj["CCHdr"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtCCHdrSearchTableset:
   def __init__(self, obj):
      self.CCHdr:list[Erp_Tablesets_CCHdrRow] = obj["CCHdr"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   plant
   warehouseCode
   ccYear
   ccMonth
   fullPhysical
   cycleSeq
   """  
   def __init__(self, obj):
      self.plant:str = obj["plant"]
      self.warehouseCode:str = obj["warehouseCode"]
      self.ccYear:int = obj["ccYear"]
      self.ccMonth:int = obj["ccMonth"]
      self.fullPhysical:bool = obj["fullPhysical"]
      self.cycleSeq:int = obj["cycleSeq"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CCHdrSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CCHdrSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CCHdrSearchTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CCHdrListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCCHdr_input:
   """ Required : 
   ds
   plant
   warehouseCode
   ccYear
   ccMonth
   fullPhysical
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CCHdrSearchTableset] = obj["ds"]
      self.plant:str = obj["plant"]
      self.warehouseCode:str = obj["warehouseCode"]
      self.ccYear:int = obj["ccYear"]
      self.ccMonth:int = obj["ccMonth"]
      self.fullPhysical:bool = obj["fullPhysical"]
      pass

class GetNewCCHdr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CCHdrSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCCHdr
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCCHdr:str = obj["whereClauseCCHdr"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CCHdrSearchTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_UpdExtCCHdrSearchTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCCHdrSearchTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CCHdrSearchTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CCHdrSearchTableset] = obj["ds"]
      pass

      """  output parameters  """  

